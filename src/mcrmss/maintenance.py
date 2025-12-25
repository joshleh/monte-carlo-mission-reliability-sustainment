from __future__ import annotations

from dataclasses import dataclass, field
from typing import Deque, List, Optional
from collections import deque

from .entities import Drone, DroneStatus, Inventory
from .failure_models import sample_repair_time_days
import numpy as np


@dataclass
class MaintenanceSystem:
    repair_bays: int
    queue: Deque[int] = field(default_factory=deque)  # drone_ids waiting
    active_repairs: List[int] = field(default_factory=list)  # drone_ids in repair

    def enqueue(self, drone: Drone) -> None:
        if drone.status != DroneStatus.IN_REPAIR_QUEUE:
            drone.status = DroneStatus.IN_REPAIR_QUEUE
            self.queue.append(drone.drone_id)

    def available_bays(self) -> int:
        return max(0, self.repair_bays - len(self.active_repairs))

    def start_repairs(
        self,
        rng: np.random.Generator,
        drones: List[Drone],
        inventory: Inventory,
        mean_repair_days_by_component: dict,
        spares_required: bool = True,
    ) -> None:
        """Start as many repairs as capacity and spares allow."""
        while self.queue and self.available_bays() > 0:
            drone_id = self.queue[0]
            d = drones[drone_id]
            comp = d.failed_component
            if comp is None:
                # Shouldn't happen; drop it safely
                self.queue.popleft()
                d.status = DroneStatus.AVAILABLE
                continue

            if spares_required and not inventory.has_spare(comp):
                # Stockout blocks starting repair
                break

            # Consume spare to begin repair
            if spares_required:
                inventory.consume(comp, 1)

            # Sample repair time and activate
            d.repair_time_remaining = sample_repair_time_days(rng, mean_repair_days_by_component[comp])
            d.status = DroneStatus.UNDER_REPAIR
            self.active_repairs.append(drone_id)
            self.queue.popleft()

    def progress_repairs(self, drones: List[Drone], dt_days: float = 1.0) -> None:
        """Progress active repairs; complete any that finish."""
        completed: List[int] = []
        for drone_id in self.active_repairs:
            d = drones[drone_id]
            d.repair_time_remaining = max(0.0, d.repair_time_remaining - dt_days)
            if d.repair_time_remaining <= 0.0:
                completed.append(drone_id)

        for drone_id in completed:
            self.active_repairs.remove(drone_id)
            d = drones[drone_id]
            d.failed_component = None
            d.status = DroneStatus.AVAILABLE