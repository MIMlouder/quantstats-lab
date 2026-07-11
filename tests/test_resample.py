import numpy as np
from quantstats.resample import bootstrap, percentile_ci


def test_bootstrap_mean_recovers_truth():
    rng = np.random.default_rng(42)
    data = rng.normal(loc=10, scale=2, size=200)
    reps = bootstrap(data, np.mean, n_boot=2000, seed=1)
    lo, hi = percentile_ci(reps)
    assert lo < 10 < hi
    assert hi - lo < 1.5  # CI width sane for n=200, sd=2


def test_reproducible_with_seed():
    data = np.arange(50, dtype=float)
    a = bootstrap(data, np.mean, n_boot=100, seed=7)
    b = bootstrap(data, np.mean, n_boot=100, seed=7)
    assert np.array_equal(a, b)