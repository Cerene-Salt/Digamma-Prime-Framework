# 🌌 Digamma Prime Framework

**Digamma Prime** is a symbolic audit system for model comparison, divergence analysis, and structural integrity monitoring. Built for data science, machine learning, and AI interpretability, it offers metrics that go beyond statistical tests — revealing how models behave, change, and destabilize.

---

## 🔣 Core Metrics

| Symbol | Name                  | Description                          |
|--------|-----------------------|--------------------------------------|
| ϝ      | Structural divergence | Difference in functional shape       |
| δϝ     | Rate divergence       | Difference in change velocity        |
| δ²ϝ    | Curvature divergence  | Difference in acceleration/instability |

These metrics form the backbone of Lady Epe — a symbolic system for functional auditing and pedagogical modeling.

---

## 📦 Installation

```bash
git clone https://github.com/Cerene-Salt/Digamma-Prime-Framework.git
cd Digamma-Prime-Framework
pip install .

QUICKSTART:
from epe_maria.metrics import phi, delta_phi
from epe_maria.temporal import second_order_divergence

ϝ = phi(reference, current)
δϝ = delta_phi(reference, current)
δ²ϝ = second_order_divergence(reference, current)


Comparison with K-Test
from epe_maria.benchmark import benchmark_epe_vs_ks

result = benchmark_epe_vs_ks(reference, current)
print(result)

For full symbolic interpretation, pedagogical examples, and pipeline overview available in:
docs/epe_documentacao_simbolica.md
Includes:

Metric definitions and formulas

Visual examples

Use cases in fairness, stability, and teaching

Pipeline overview: metrics → temporal → monitor → benchmark
Author
Cerene Rúbio Symbolic systems architect | Model integrity researcher Creator of Lady Epe and the Digamma Prime Framework
