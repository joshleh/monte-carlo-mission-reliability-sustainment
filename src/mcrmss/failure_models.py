from __future__ import annotations

import numpy as np


def sample_exponential_failure(rng: np.random.Generator, failure_rate_per_day: float) -> bool:
    """
    Baseline: discrete daily timestep approximation.
    Given rate lambda (events/day), approximate daily failure probability:
        p = 1 - exp(-lambda * 1 day)
    Returns True if failure occurs within the day.
    """
    if failure_rate_per_day <= 0:
        return False
    p = 1.0 - np.exp(-failure_rate_per_day)
    return rng.random() < p


def sample_repair_time_days(rng: np.random.Generator, mean_days: float) -> float:
    """
    Baseline: repair time is sampled from an exponential distribution with given mean.
    (Simple, memoryless; easy to swap later to lognormal/triangular.)
    """
    if mean_days <= 0:
        return 0.0
    return float(rng.exponential(scale=mean_days))