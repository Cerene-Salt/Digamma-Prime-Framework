#Digamma Prime (`digamma-ep`)

Sistema simbólico para auditoria de modelos com métricas de divergência estrutural, temporal e algébrica.  
Symbolic audit framework for comparing models, tracking divergence, and teaching algebraic structure.

---

##  Installation

```bash
pip install digamma_prime

#A Quickstart
from epe_maria.metrics import phi, delta_phi, phi_star

f = lambda x: x**2 + 2*x + 1
g = lambda x: x**2 + x + 1

print(phi(f, g))        # Structural divergence
print(delta_phi(f, g))  # Rate divergence
print(phi_star(f, g))   # Fusion metric


#Documentation
Operator fichas: docs/operators.md

Symbolic manifesto: docs/epe_maria_manifesto.md

#Examples in:
python examples/symbolic_mollification_demo.py
python examples/kernel_divergence_trace.py

#Features
Symbolic comparison of models

CLI-ready modules for drift detection

Visualizations for φ and Δφ

Curriculum-ready structure

PyPI + GitHub CI/CD integration

Vision
Digamma Prime aims to become a universal symbolic standard for model auditing, drift detection, and interpretability — rooted in the algebraic legacy of Epe Piancé Maria II.

🤝 Contributing
We welcome contributions in tutorials, metrics, automation, and visualizations. See docs/roadmap.md and docs/style_guide.md to get started.

Tests:;
pytest test_benchmark.py
pytest test_monitor.py

bout
Created by Cerene Rúbio License: MIT Namespace: epe_maria/ — honoring the symbolic grammar of Epe Piancé Maria II

Release History
v0.2.0 – Symbolic Expansion
Added operator fichas and visual demos

Published examples/ and docs/ to PyPI

Preserved epe_maria/ namespace

Synced GitHub and PyPI

v0.1.7 – Initial PyPI Release
Core symbolic audit engine

Modules: benchmark, metrics, monitor, visuals

Python 3.11+ compatible
