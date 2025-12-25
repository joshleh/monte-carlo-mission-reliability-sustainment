from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class ComponentConfig:
    """Defines a critical component type and its baseline failure/repair parameters."""
    name: str
    # Baseline exponential TTF: daily failure rate lambda (events/day)
    failure_rate_per_day: float
    # Repair time model (baseline): mean repair time in days (can be fractional)
    mean_repair_days: float
    # Spares policy
    initial_spares: int
    reorder_point: int
    reorder_quantity: int


@dataclass(frozen=True)
class FleetConfig:
    """Defines the fleet and mission demand."""
    num_drones: int
    daily_sortie_demand: int
    # If True, each drone can fly at most one sortie/day (baseline True)
    one_sortie_per_drone_per_day: bool = True


@dataclass(frozen=True)
class MaintenanceConfig:
    """Defines maintenance capacity assumptions."""
    # Number of repairs that can be actively worked on in parallel
    repair_bays: int
    # If True, repairs require spares to start (baseline True)
    spares_required_to_start: bool = True


@dataclass(frozen=True)
class LogisticsConfig:
    """Defines supply chain timing assumptions."""
    # Deterministic lead time in days for all components (baseline)
    lead_time_days: int


@dataclass(frozen=True)
class SimulationConfig:
    """Top-level configuration for one scenario."""
    horizon_days: int
    trials: int
    seed: int = 42

    fleet: FleetConfig = field(default_factory=lambda: FleetConfig(num_drones=6, daily_sortie_demand=4))
    maintenance: MaintenanceConfig = field(default_factory=lambda: MaintenanceConfig(repair_bays=2))
    logistics: LogisticsConfig = field(default_factory=lambda: LogisticsConfig(lead_time_days=7))

    # Critical components in the drone (baseline: a few)
    components: List[ComponentConfig] = field(
        default_factory=lambda: [
            ComponentConfig(
                name="motor",
                failure_rate_per_day=0.01,
                mean_repair_days=2.0,
                initial_spares=2,
                reorder_point=1,
                reorder_quantity=2,
            ),
            ComponentConfig(
                name="battery",
                failure_rate_per_day=0.015,
                mean_repair_days=1.0,
                initial_spares=3,
                reorder_point=1,
                reorder_quantity=3,
            ),
            ComponentConfig(
                name="comms",
                failure_rate_per_day=0.007,
                mean_repair_days=3.0,
                initial_spares=1,
                reorder_point=1,
                reorder_quantity=1,
            ),
        ]
    )