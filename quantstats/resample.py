import numpy as np

def bootstrap(data, stat_fn=np.mean, n_boot=10_000, seed=None):
    """Bootstrap replicates of a statistic.

    Resamples `data` with replacement n_boot times, applying stat_fn
    to each resample. Returns array of n_boot replicate statistics.

    Assumes observations are independent — NOT valid for
    autocorrelated series without blocking (see block_bootstrap).
    """
    data = np.asarray(data)
    rng = np.random.default_rng(seed)
    n = len(data)
    idx = rng.integers(0, n, size=(n_boot, n))
    return np.array([stat_fn(data[row]) for row in idx])

def percentile_ci(replicates, level=0.95):
    """Percentile confidence interval from bootstrap replicates."""
    alpha = (1 - level) / 2
    return tuple(np.quantile(replicates, [alpha, 1 - alpha]))