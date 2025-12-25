# Problem Statement

## Operational Context
Small ISR drone detachments are increasingly relied upon to provide persistent
situational awareness under sustained operational tempo. While deployment and
allocation decisions determine where assets are placed, **mission success over
time is governed by reliability, maintenance capacity, and logistics constraints**.

Operational planners must answer not only *where* to deploy ISR assets, but also:

- How many missions can a detachment realistically sustain?
- What failure and maintenance dynamics most constrain availability?
- How sensitive mission success is to sortie tempo and spare part availability?

These questions are inherently stochastic and cannot be answered using
deterministic averages alone.

---

## Problem Definition
This project models the **mission reliability and sustainment performance** of a
small ISR drone detachment using a Monte Carlo simulation.

The system of interest consists of:
- A fixed fleet of ISR drones
- Multiple critical components subject to random failure
- A maintenance process with stochastic repair times
- A limited spare parts inventory with replenishment lead times
- A daily mission (sortie) demand

At each simulated timestep, the system evolves based on:
- Component failures during operations
- Maintenance and repair outcomes
- Logistics constraints affecting part availability
- Mission demand requirements

A mission is considered successful if a drone is available and completes the
assigned sortie without experiencing a mission-ending failure.

---

## Objectives
The primary objectives of the simulation are to:

1. Estimate **mission success probability over time** under sustained operations
2. Quantify **aircraft availability (Ao)** as a function of reliability and logistics
3. Identify **primary drivers of downtime**, including:
   - Component failures
   - Maintenance capacity constraints
   - Spare part stockouts
4. Evaluate sensitivity to key operational parameters such as:
   - Sortie rate
   - Repair time distributions
   - Spare part reorder policies

---

## Scope and Assumptions
To maintain clarity and interpretability, the baseline model makes the following
simplifying assumptions:

- A single ISR drone type is modeled
- Component failures are statistically independent
- Maintenance resources are centralized within the detachment
- Supply replenishment follows fixed lead times
- Environmental and adversarial effects are excluded

These assumptions are intentional and serve to isolate the impact of sustainment
and reliability dynamics on mission outcomes.

---

## Key Outputs
The simulation produces the following metrics for analysis:

- Mission success rate over time
- Fleet availability (Ao)
- Mean time between mission failures
- Downtime attribution by cause
- Distribution of unmet mission demand

---

## Intended Use
This model is intended as a **decision-support tool** for exploring how reliability,
maintenance, and logistics policies influence sustained ISR mission performance.

The framework is designed to support rapid experimentation and extension, enabling
planners and analysts to test alternative sustainment strategies under uncertainty.