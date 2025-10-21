# Digamma Prime

Digamma Prime is a symbolic audit engine for divergence detection, structural drift, and kernel-based analysis.

## Installation

```bash
pip install digamma_prime


Modules
digamma_prime.benchmark: Reference metrics and symbolic baselines

digamma_prime.monitor: Drift detection and audit triggers

digamma_prime.visuals: Symbolic plots and divergence maps

License
MIT © Cesar Rubio


---

## 🧭 Optional Enhancements

- Add `mkdocs.yml` for live documentation site
- Add `docs/operators.md` with fichas for mollification, Liouville, implicit drift
- Add CLI examples in `docs/cli.md` like:
  ```bash
  python run_audit.py --mode temporal --threshold 0.05
