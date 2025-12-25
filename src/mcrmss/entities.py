from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional


class DroneStatus(str, Enum):
    AVAILABLE = "available"
    IN_REPAIR_QUEUE = "in_repair_queue"
    UNDER_REPAIR = "under_repair"


@dataclass
class Drone:
    drone_id: int
    status: DroneStatus = DroneStatus.AVAILABLE
    # If failed, which component caused it (for attribution)
    failed_component: Optional[str] = None
    # If under repair, days remaining (can be fractional)
    repair_time_remaining: float = 0.0


@dataclass
class InventoryItem:
    on_hand: int
    on_order: int = 0


@dataclass
class Inventory:
    items: Dict[str, InventoryItem] = field(default_factory=dict)

    def has_spare(self, component: str) -> bool:
        return self.items[component].on_hand > 0

    def consume(self, component: str, qty: int = 1) -> None:
        self.items[component].on_hand -= qty

    def receive(self, component: str, qty: int) -> None:
        self.items[component].on_hand += qty

    def place_order(self, component: str, qty: int) -> None:
        self.items[component].on_order += qty

    def fulfill_order(self, component: str, qty: int) -> None:
        self.items[component].on_order -= qty
        self.items[component].on_hand += qty