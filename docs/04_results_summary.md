# Results Summary

## Overview
This document summarizes the results produced by the Monte Carlo mission reliability
and sustainment simulation. At the current stage of development, this section
establishes the **intended analytical outputs, evaluation structure, and reporting
format**.

As simulation experiments are executed, this document will be updated with
quantitative results, figures, and scenario comparisons.

---

## Baseline Scenario Description
The baseline scenario models a small ISR drone detachment operating under sustained
daily sortie demand with stochastic failures, finite maintenance capacity, and
limited spare part inventories.

All results referenced below correspond to this baseline unless otherwise noted.

---

## Primary Performance Metrics

### Mission Success Rate
Mission success rate is defined as the proportion of demanded sorties that are
successfully completed without mission-ending failures.

Planned reporting includes:
- Time-series mission success rate
- Steady-state average mission success
- Variability across Monte Carlo trials

---

### Fleet Availability (Ao)
Fleet availability (Ao) represents the fraction of drones that are mission-capable
at a given time.

Planned reporting includes:
- Average availability over time
- Transient vs steady-state availability behavior
- Sensitivity to maintenance and logistics parameters

---

### Downtime Attribution
Downtime is attributed to the following causes:
- Awaiting maintenance capacity
- Awaiting spare parts
- Actively undergoing repair

Planned reporting includes:
- Fractional downtime by cause
- Identification of dominant sustainment bottlenecks
- Changes in downtime composition across scenarios

---

### Unmet Mission Demand
Unmet mission demand captures instances where sortie requirements cannot be fulfilled
due to insufficient available drones.

Planned reporting includes:
- Frequency of unmet demand events
- Cumulative unmet sorties over time
- Relationship between demand intensity and sustainment shortfalls

---

## Scenario Comparisons
The simulation framework supports structured comparison across scenarios, including
variations in:
- Sortie tempo
- Fleet size
- Failure rates
- Maintenance capacity
- Spare part reorder policies

Scenario results will be presented using consistent metrics to enable direct
operational tradeoff analysis.

---

## Sensitivity Analysis
Sensitivity analyses will assess how uncertainty in key parameters influences
mission outcomes.

Planned sensitivity dimensions include:
- Failure rate assumptions
- Repair time distributions
- Spare part lead times

Results will be used to identify parameters with the greatest impact on mission
success and availability.

---

## Validation and Sanity Checks
All results will be accompanied by validation checks, including:
- Zero-failure edge cases
- Infinite-maintenance-capacity scenarios
- Consistency between availability and downtime accounting

These checks ensure model behavior aligns with analytical expectations.

---

## Key Insights (To Be Updated)
This section will summarize the primary operational insights derived from simulation
results, including:
- Primary drivers of mission failure
- Sustainment constraints limiting operational tempo
- Tradeoffs between logistics investment and mission performance

Insights will be updated as experiments are completed.

---

## Current Status
At present, this document serves as a structured placeholder outlining the intended
analytical outputs and reporting format. Quantitative results and figures will be
added incrementally as simulation experiments are executed.