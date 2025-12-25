# Monte Carlo Mission Reliability & Sustainment Simulation

## Status
🚧 **In Progress**  
This project is actively under development. Core documentation, model assumptions,
and baseline simulation scaffolding are complete. Ongoing work includes automated
testing, scenario experiments, and results analysis.

---

## Overview
This project implements a **Monte Carlo simulation** to evaluate the **mission
reliability and sustainment performance** of a small ISR drone detachment operating
under stochastic failures, maintenance capacity constraints, and spare-parts
logistics.

The model is designed as a **decision-support tool** for operations analysis,
focusing on how uncertainty in reliability and sustainment processes impacts
mission success and fleet availability over time.

---

## Operational Problem
Deployment decisions determine where ISR assets are placed, but **sustainment
dynamics determine whether missions can be completed consistently over time**.

This simulation addresses questions such as:
- How reliably can a drone detachment meet daily sortie demand?
- What sustainment factors most constrain mission success?
- How sensitive performance is to sortie tempo, repair capacity, and logistics?

---

## Modeling Approach
- Discrete-time Monte Carlo simulation
- Daily timestep with stochastic event sampling
- Explicit modeling of:
  - Component failures
  - Maintenance queues and repair capacity
  - Spare parts inventory and resupply lead times
- Reproducible runs using controlled random seeds

---

## Current Capabilities
- Baseline ISR drone detachment model
- Mission success and availability metrics
- Downtime attribution (active repair vs repair queue)
- CLI runner for reproducible experiments
- Structured documentation covering:
  - Problem formulation
  - Model assumptions
  - Simulation methodology
  - Results framework

---

## Repository Structure
