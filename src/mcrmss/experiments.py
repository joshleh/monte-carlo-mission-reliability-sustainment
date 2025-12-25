from __future__ import annotations

from typing import Dict, List
from .config import SimulationConfig
from .simulation import run_simulation


def run_baseline(cfg: SimulationConfig) -> Dict[str, object]:
    return run_simulation(cfg)


def run_tempo_sweep(cfg: SimulationConfig, tempos: List[int]) -> Dict[int, Dict[str, object]]:
    results = {}
    for tempo in tempos:
        new_cfg = SimulationConfig(
            horizon_days=cfg.horizon_days,
            trials=cfg.trials,
            seed=cfg.seed,
            fleet=type(cfg.fleet)(num_drones=cfg.fleet.num_drones, daily_sortie_demand=tempo, one_sortie_per_drone_per_day=cfg.fleet.one_sortie_per_drone_per_day),
            maintenance=cfg.maintenance,
            logistics=cfg.logistics,
            components=cfg.components,
        )
        results[tempo] = run_simulation(new_cfg)
    return results