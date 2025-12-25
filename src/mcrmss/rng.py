from __future__ import annotations

import numpy as np


def make_rng(seed: int) -> np.random.Generator:
    """Create a reproducible RNG."""
    return np.random.default_rng(seed)