# quantstats-lab

A small library of statistical methods for quantamental analysis,
built as a learning project. Each method is implemented from scratch
first, demonstrated on public dry bulk shipping data, and documented
with an honest note: what it does, when it lies, what it cannot
tell you.

**This is a learning repo, not a trading system.** Nothing here is
a signal, a strategy, or an alpha claim. All data is public
(Pilbara Ports, Comex Stat, USDA, public index histories).

## Modules

| Module | Method | Status |
|---|---|---|
| M1 | Resampling & small-n inference | in progress |
| M3 | Path statistics / event census | planned |
| M2 | Bayesian hierarchical models | planned |
| M4 | Bayesian structural time series | planned |
| M5 | HMM regime labeling (descriptive) | planned |

## Setup

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Data pulls: see `data/` for scripts. Raw data is not committed.# quantstats-lab