
# 🌌 Digamma Prime Framework

**Digamma Prime** is a symbolic audit system for model comparison, divergence analysis, and structural integrity monitoring. Built for data science, machine learning, and AI interpretability, it offers metrics that go beyond statistical tests — revealing how models behave, change, and destabilize.

Now installable via PyPI as **digamma-ep**:

```
pip install digamma-ep
```

---

## 🔣 Core Metrics

| Symbol | Name                  | Description                          |
|--------|-----------------------|--------------------------------------|
| ϝ      | Structural divergence | Difference in functional shape       |
| δϝ     | Rate divergence       | Difference in change velocity        |
| δ²ϝ    | Curvature divergence  | Difference in acceleration/instability |

These metrics form the backbone of Digamma Prime — a symbolic system for functional auditing and pedagogical modeling.

---

## 📦 Installation

### ✅ Recommended (PyPI)

```
pip install digamma-ep
```

### 🛠️ Development (GitHub)

```
git clone https://github.com/Cerene-Salt/Digamma-Prime-Framework.git
cd Digamma-Prime-Framework
pip install .
```

---

## 🚀 Quickstart

```python
from epe_maria.metrics import phi, delta_phi
from epe_maria.temporal import second_order_divergence

ϝ = phi(reference, current)
δϝ = delta_phi(reference, current)
δ²ϝ = second_order_divergence(reference, current)
```

---

## 📊 Benchmarking

Compare Digamma Prime’s symbolic metrics with traditional statistical tests:

```python
from epe_maria.benchmark import benchmark_epe_vs_ks

result = benchmark_epe_vs_ks(reference, current)
print(result)
```

---

## 📚 Documentation

Full symbolic interpretation, pedagogical examples, and pipeline overview available in:

docs/epe_documentacao_simbolica.md

Includes:
- Metric definitions and formulas
- Visual examples
- Use cases in fairness, stability, and teaching
- Pipeline overview: metrics → temporal → monitor → benchmark

---

## 🧠 Author

**Cerene Rúbio**  
Symbolic systems architect | Model integrity researcher  
Creator of Digamma Prime and the `digamma-ep` package

---

## 🏷️ PyPI Badge

![PyPI version](https://img.shields.io/pypi/v/digamma-ep)  
View on PyPI → https://pypi.org/project/digamma-ep
```
