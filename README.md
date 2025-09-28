

## ✅ Updated `README.md` for Digamma Prime Framework (with Lady Epe on PyPI)

```markdown
# 🌌 Digamma Prime Framework

**Digamma Prime** is a symbolic audit system for model comparison, divergence analysis, and structural integrity monitoring. Built for data science, machine learning, and AI interpretability, it offers metrics that go beyond statistical tests — revealing how models behave, change, and destabilize.

Now installable via PyPI as **Lady Epe**:

```bash
pip install lady-epe
```

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

### ✅ Recommended (PyPI)

```bash
pip install lady-epe
```

### 🛠️ Development (GitHub)

```bash
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

Compare Lady Epe’s symbolic metrics with traditional statistical tests:

```python
from epe_maria.benchmark import benchmark_epe_vs_ks

result = benchmark_epe_vs_ks(reference, current)
print(result)
```

---

## 📚 Documentation

Full symbolic interpretation, pedagogical examples, and pipeline overview available in:

```
docs/epe_documentacao_simbolica.md
```

Includes:
- Metric definitions and formulas
- Visual examples
- Use cases in fairness, stability, and teaching
- Pipeline overview: metrics → temporal → monitor → benchmark

---

## 🧠 Author

**Cerene Rúbio**  
Symbolic systems architect | Model integrity researcher  
Creator of Lady Epe and the Digamma Prime Framework

---

## 🏷️ PyPI Badge

![PyPI version](https://img.shields.io/pypi/v/lady-epe)  
[View on PyPI →](https://pypi.org/project/lady-epe)
```
