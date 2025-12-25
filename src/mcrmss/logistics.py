from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from .config import SimulationConfig
from .entities import Inventory


@dataclass
class InboundOrder:
    component: str
    qty: int
    days_until_arrival: int


def init_inventory(cfg: SimulationConfig) -> Inventory:
    inv = Inventory()
    for c in cfg.components:
        inv.items[c.name] = inv.items.get(c.name) or type(inv.items.setdefault(c.name, None))  # noqa: E701
    # The above line is messy; keep it simple below:
    inv.items = {c.name: __import__("mcrmss").mcrmss.entities.InventoryItem(on_hand=c.initial_spares) for c in cfg.components}  # type: ignore
    return inv


def init_inventory_clean(cfg: SimulationConfig) -> Inventory:
    from .entities import InventoryItem

    return Inventory(items={c.name: InventoryItem(on_hand=c.initial_spares) for c in cfg.components})


def maybe_reorder(cfg: SimulationConfig, inventory: Inventory, inbound: List[InboundOrder]) -> None:
    """Simple (s, Q) reorder policy per component."""
    for c in cfg.components:
        on_hand = inventory.items[c.name].on_hand
        if on_hand <= c.reorder_point:
            inventory.place_order(c.name, c.reorder_quantity)
            inbound.append(InboundOrder(component=c.name, qty=c.reorder_quantity, days_until_arrival=cfg.logistics.lead_time_days))


def advance_inbound(inventory: Inventory, inbound: List[InboundOrder]) -> None:
    """Advance inbound pipeline by one day; receive anything that arrives."""
    arrived: List[InboundOrder] = []
    for order in inbound:
        order.days_until_arrival -= 1
        if order.days_until_arrival <= 0:
            arrived.append(order)

    # Remove arrived then receive
    for order in arrived:
        inbound.remove(order)
        inventory.fulfill_order(order.component, order.qty)