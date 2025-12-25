# Model Assumptions

## Overview
This document defines the baseline assumptions used in the Monte Carlo mission
reliability and sustainment simulation. Assumptions are intentionally scoped to
balance operational realism with model interpretability and computational
tractability.

All assumptions documented here apply to the **baseline ISR drone detachment
scenario** and serve as the foundation for subsequent sensitivity analyses and
extensions.

---

## Fleet and Mission Assumptions
- The detachment consists of a fixed number of identical ISR drones
- Each drone can execute at most one sortie per timestep
- Mission demand is specified as a fixed number of sorties per day
- Missions are homogeneous in duration and operational profile
- A mission is successful if:
  - A drone is available at mission start
  - No mission-ending failure occurs during the sortie

---

## Time Representation
- The simulation advances in discrete daily timesteps
- All failures, repairs, and logistics events are evaluated at the timestep level
- Partial-day effects are not explicitly modeled
- Simulation horizon is user-defined and long enough to observe steady-state behavior

---

## Failure Modeling Assumptions
- Each drone consists of multiple critical components
- Component failures are statistically independent
- Failure events follow memoryless stochastic processes
- Baseline failure model uses exponential time-to-failure distributions
- A failure of any critical component renders the drone non-mission-capable
- Mission-ending failures occur during sorties and immediately remove the drone
  from availability

---

## Maintenance Assumptions
- All maintenance is performed at a centralized detachment-level facility
- Maintenance resources are finite and modeled as a limited repair capacity
- Repairs require both:
  - Available maintenance capacity
  - Availability of required spare parts
- Repair times are stochastic and drawn from predefined distributions
- Upon completion of repair, drones immediately return to the available pool

---

## Spare Parts and Logistics Assumptions
- Each critical component has a corresponding spare part inventory
- Spare parts are consumed when repairs are initiated
- Replenishment follows a fixed reorder policy with deterministic lead times
- No expedited shipping or priority resupply is modeled
- Stockouts prevent repair initiation and contribute to downtime

---

## Availability and Downtime Assumptions
- Drone availability is binary (available or unavailable)
- Downtime is attributed to one of the following causes:
  - Awaiting maintenance capacity
  - Awaiting spare parts
  - Actively undergoing repair
- Cannibalization between drones is not permitted in the baseline model

---

## Statistical Assumptions
- Monte Carlo trials are independent
- Random number seeds are controlled to ensure reproducibility
- Summary statistics are computed across a large number of simulation runs
- Output metrics are reported using means and empirical distributions

---

## Excluded Effects
The following effects are intentionally excluded from the baseline model:

- Environmental degradation and weather impacts
- Adversarial damage or combat attrition
- Learning effects or adaptive maintenance policies
- Variability in mission criticality or priority
- Multi-echelon logistics networks

These effects are considered candidates for future model extensions.

---

## Rationale
The baseline assumptions prioritize clarity and interpretability while capturing
the primary stochastic drivers of mission sustainment performance. By constraining
model complexity, the framework enables transparent analysis of reliability,
maintenance, and logistics tradeoffs before introducing additional realism.