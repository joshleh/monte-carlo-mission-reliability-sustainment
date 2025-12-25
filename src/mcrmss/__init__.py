"""
Monte Carlo Mission Reliability & Sustainment Simulation (mcrmss).

Baseline: ISR drone detachment sustainment under stochastic failures,
maintenance capacity constraints, and spare parts logistics.
"""

from .config import SimulationConfig, FleetConfig, ComponentConfig, MaintenanceConfig, LogisticsConfig
from .simulation import run_simulation

__all__ = [
    "SimulationConfig",
    "FleetConfig",
    "ComponentConfig",
    "MaintenanceConfig",
    "LogisticsConfig",
    "run_simulation",
]