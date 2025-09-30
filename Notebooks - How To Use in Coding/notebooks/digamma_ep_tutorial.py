

[![PyPI version](https://badge.fury.io/py/digamma-ep.svg)](https://pypi.org/project/digamma-ep/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<your-username>/<your-repo>/blob/main/notebooks/digamma_ep_tutorial.ipynb)

**Digamma‑ep** is a symbolic audit framework for model divergence and integrity.  
It provides a set of mathematical metrics to compare functions, monitor drift, and measure curvature — useful for data science, machine learning, and symbolic computation.

---

## 🚀 Installation

```bash
pip install digamma-ep==0.1.6
```

---

## 📖 Quickstart

```python
from epe_maria import phi, delta_phi, phi_star, drift, curvature
import math

f = lambda x: x**2
g = lambda x: x + 1
h = lambda x: math.sin(x)

print("phi:", phi(f, g))                 # Structural divergence
print("delta_phi:", delta_phi(f, g))     # Rate divergence
print("phi_star:", phi_star(f, g))       # Fusion metric
print("drift:", drift(f, g))             # Directional bias
print("curvature(f):", curvature(f))     # Curvature of x^2
print("curvature(sin):", curvature(h))   # Curvature of sin(x)
```

---

## 📊 Function Reference

| Function | Math Definition | Description |
|----------|-----------------|-------------|
| **phi(f,g)** | $$\phi(f,g) = \frac{1}{|D|}\sum_{x\in D} |f(x)-g(x)|$$ | Structural divergence between two functions |
| **delta_phi(f,g)** | $$\Delta\phi(f,g) = \frac{1}{|D|}\sum_{x\in D} |f'(x)-g'(x)|$$ | Rate divergence (derivative differences) |
| **phi_star(f,g,α,β)** | $$\phi^*(f,g) = \alpha \cdot \phi(f,g) + \beta \cdot \Delta\phi(f,g)$$ | Fusion metric (weighted blend) |
| **drift(f,g)** | $$\text{drift}(f,g) = \frac{1}{|D|}\sum_{x\in D} \text{sign}(f(x)-g(x))$$ | Directional bias (does f exceed g?) |
| **curvature(f)** | $$\kappa(f) = \frac{1}{|D|}\sum_{x\in D} |f''(x)|$$ | Average curvature (bendiness of f) |

---

## 🧮 Mathematical Walkthrough

- **phi**: Measures average output difference.  
- **delta_phi**: Measures slope differences.  
- **phi_star**: Blends structure + slope into one score.  
- **drift**: Detects directional dominance (bias).  
- **curvature**: Captures smoothness/complexity via second derivative.  

---

## 📓 Tutorial (Colab‑style)

```python
!pip install digamma-ep==0.1.6

from epe_maria import phi, delta_phi, phi_star, drift, curvature
import numpy as np, matplotlib.pyplot as plt, math

f = lambda x: x**2
g = lambda x: x + 1

# Compute metrics
print("phi:", phi(f, g))
print("delta_phi:", delta_phi(f, g))
print("phi_star:", phi_star(f, g))
print("drift:", drift(f, g))
print("curvature(f):", curvature(f))
print("curvature(sin):", curvature(math.sin))

# Visualize
X = np.linspace(-5, 5, 200)
F, G = [f(x) for x in X], [g(x) for x in X]

plt.plot(X, F, label="f(x)=x^2")
plt.plot(X, G, label="g(x)=x+1")
plt.legend()
plt.title("Structural Divergence Example")
plt.show()
```

---

## 📜 Release Notes (v0.1.6)

- Added `drift` and `curvature` functions  
- Improved packaging (`setup.cfg`, `setup.py`, `pyproject.toml`)  
- Confirmed compatibility with Colab, Jupyter, VS Code, PyCharm  
- Updated README with Quickstart and Function Reference  

