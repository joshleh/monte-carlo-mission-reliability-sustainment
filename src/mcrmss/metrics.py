from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List
from .entities import Drone, DroneStatus


@dataclass
class DailyMetrics:
    day: int
    demand: int
    sorties_flown: int
    missions_successful: int
    availability: float
    unmet_demand: int
    downtime_active_repair: int
    downtime_in_queue: int


def compute_availability(drones: List[Drone]) -> float:
    if not drones:
        return 0.0
    available = sum(1 for d in drones if d.status == DroneStatus.AVAILABLE)
    return available / len(drones)


def downtime_counts(drones: List[Drone]) -> Dict[str, int]:
    return {
        "active_repair": sum(1 for d in drones if d.status == DroneStatus.UNDER_REPAIR),
        "in_queue": sum(1 for d in drones if d.status == DroneStatus.IN_REPAIR_QUEUE),
    }
