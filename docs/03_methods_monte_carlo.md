# Monte Carlo Simulation Methodology

## Overview
This project employs a Monte Carlo simulation to evaluate the mission reliability
and sustainment performance of an ISR drone detachment under stochastic failures,
maintenance processes, and logistics constraints.

Rather than relying on deterministic averages, the model captures uncertainty by
simulating many independent realizations of system behavior over time and
aggregating the resulting performance metrics.

---

## Simulation Structure
The simulation is executed as a discrete-time, event-driven process operating over
a fixed planning horizon.

Each Monte Carlo trial represents one possible realization of detachment operations
given the same input parameters but different random outcomes.

---

## Initialization
At the start of each trial:
- All drones are initialized as mission-capable
- Component ages are reset
- Spare part inventories are initialized to baseline levels
- Maintenance queues are empty
- Random number generator seeds are set for reproducibility

---

## Daily Event Loop
For each simulated day, the model executes the following sequence of events:

1. **Mission Demand Evaluation**
   - Daily sortie demand is assessed
   - Available drones are assigned to missions up to demand limits

2. **Mission Execution**
   - Assigned drones attempt to complete sorties
   - Mission-ending failures are sampled for each sortie
   - Drones experiencing failures are immediately removed from availability

3. **Failure Accumulation**
   - Failed components are recorded
   - Maintenance requirements are generated

4. **Maintenance Processing**
   - Drones awaiting repair enter the maintenance queue
   - Repairs are initiated subject to:
     - Available maintenance capacity
     - Spare part availability
   - Repair durations are sampled from stochastic distributions

5. **Repair Completion**
   - Completed repairs return drones to mission-capable status
   - Maintenance capacity is released

6. **Logistics Updates**
   - Spare part reorder pipelines advance
   - Deliveries arriving after lead times replenish inventory

7. **Metric Collection**
   - Mission outcomes, availability, and downtime states are recorded

---

## Monte Carlo Sampling
Uncertainty is represented through random sampling of:
- Component failures
- Repair durations
- Maintenance and logistics delays

Each trial uses independent random draws while holding input parameters constant.
A large number of trials are executed to ensure statistical stability of outputs.

---

## Output Aggregation
After all trials are completed:
- Time-series metrics are averaged across trials
- Empirical distributions are constructed for key outputs
- Confidence intervals may be estimated using percentile-based methods

Primary metrics include:
- Mission success rate
- Fleet availability (Ao)
- Mean downtime by cause
- Unmet mission demand

---

## Scenario Analysis
The simulation framework supports parametric scenario analysis by varying:
- Fleet size
- Sortie tempo
- Failure rates
- Repair capacity
- Spare part reorder policies

Each scenario is evaluated using identical Monte Carlo procedures to enable
consistent comparison across alternatives.

---

## Reproducibility
All simulations:
- Use controlled random seeds
- Store configuration parameters with results
- Support deterministic re-execution of prior experiments

This ensures transparency and traceability of analytical conclusions.

---

## Limitations
The Monte Carlo approach captures stochastic variability but does not optimize
decisions within the simulation. Policy optimization and adaptive control are
considered future extensions beyond the baseline methodology.