from __future__ import annotations

from dataclasses import asdict
from typing import Dict, List, Tuple
import numpy as np

from .config import SimulationConfig
from .rng import make_rng
from .entities import Drone, DroneStatus
from .failure_models import sample_exponential_failure
from .maintenance import MaintenanceSystem
from .logistics import init_inventory_clean, maybe_reorder, advance_inbound, InboundOrder
from .metrics import DailyMetrics, compute_availability, downtime_counts


def run_one_trial(cfg: SimulationConfig, rng: np.random.Generator) -> List[DailyMetrics]:
    # Initialize drones
    drones = [Drone(drone_id=i) for i in range(cfg.fleet.num_drones)]

    # Inventory + inbound pipeline
    inventory = init_inventory_clean(cfg)
    inbound: List[InboundOrder] = []

    # Maintenance
    maint = MaintenanceSystem(repair_bays=cfg.maintenance.repair_bays)

    mean_repair_days_by_component = {c.name: c.mean_repair_days for c in cfg.components}
    failure_rate_by_component = {c.name: c.failure_rate_per_day for c in cfg.components}

    history: List[DailyMetrics] = []

    for day in range(cfg.horizon_days):
        demand = cfg.fleet.daily_sortie_demand

        # 1) Assign missions to available drones
        available_ids = [d.drone_id for d in drones if d.status == DroneStatus.AVAILABLE]
        sorties_flown = min(demand, len(available_ids))  # baseline: 1 sortie per available drone
        assigned_ids = available_ids[:sorties_flown]

        # 2) Mission execution: sample mission-ending failures
        missions_successful = 0
        for drone_id in assigned_ids:
            d = drones[drone_id]

            # For baseline simplicity: if any critical component fails during sortie -> mission-ending
            failed_comp = None
            for comp_name, lam in failure_rate_by_component.items():
                if sample_exponential_failure(rng, lam):
                    failed_comp = comp_name
                    break

            if failed_comp is None:
                missions_successful += 1
            else:
                d.failed_component = failed_comp
                maint.enqueue(d)

        unmet_demand = max(0, demand - sorties_flown)

        # 3) Progress repairs already underway
        maint.progress_repairs(drones, dt_days=1.0)

        # 4) Start new repairs as allowed
        maint.start_repairs(
            rng=rng,
            drones=drones,
            inventory=inventory,
            mean_repair_days_by_component=mean_repair_days_by_component,
            spares_required=cfg.maintenance.spares_required_to_start,
        )

        # 5) Logistics: inbound arrivals + reorder check
        advance_inbound(inventory, inbound)
        maybe_reorder(cfg, inventory, inbound)

        # 6) Metrics
        avail = compute_availability(drones)
        dcounts = downtime_counts(drones)
        history.append(
            DailyMetrics(
                day=day,
                demand=demand,
                sorties_flown=sorties_flown,
                missions_successful=missions_successful,
                availability=avail,
                unmet_demand=unmet_demand,
                downtime_active_repair=dcounts["active_repair"],
                downtime_in_queue=dcounts["in_queue"],
            )
        )

    return history


def run_simulation(cfg: SimulationConfig) -> Dict[str, object]:
    """
    Run Monte Carlo simulation for the given config.
    Returns raw per-trial daily metrics plus simple aggregates.
    """
    all_trials: List[List[DailyMetrics]] = []

    for t in range(cfg.trials):
        rng = make_rng(cfg.seed + t)
        all_trials.append(run_one_trial(cfg, rng))

    # Simple aggregates (you can expand later)
    # Mean mission success rate over all days and trials:
    total_success = sum(dm.missions_successful for trial in all_trials for dm in trial)
    total_demand = sum(dm.demand for trial in all_trials for dm in trial)
    mean_success_rate = (total_success / total_demand) if total_demand > 0 else 0.0

    mean_availability = sum(dm.availability for trial in all_trials for dm in trial) / (cfg.trials * cfg.horizon_days)

    return {
        "config": asdict(cfg),
        "trials": all_trials,
        "summary": {
            "mean_success_rate": mean_success_rate,
            "mean_availability": mean_availability,
        },
    }