Perfect, Cesar — your `index.md` is already crisp and inviting. Let’s now **complete it** by adding the missing sections: the intuitive definitions, visual overview, and navigation table. This will make the homepage fully informative and visually engaging.

---

## ✅ Updated `index.md` (complete version)

```markdown
# 🧠 Digamma-Prime

> **The symbolic engine for comparing, monitoring, and auditing functions.**  
> Measure how models change — not just their scores.

[Get Started ➜](quickstart.md) [Read the Theory ➜](theory.md)

---

## What Is Digamma-Prime?

Digamma-Prime (DP) quantifies **how two functions differ** — in value, slope, and shape.  
It turns comparisons between models, datasets, or systems into clear algebraic measures.

```python
from epe_maria import phi, delta_phi
phi(model_A, model_B)
```

---

### 🔍 Intuition

- **φ (phi)** — *structural divergence*: average output difference between two functions.  
- **Δφ (delta-phi)** — *rate divergence*: difference in slopes or curvature.

These metrics help you detect model drift, audit retrains, and compare functional behavior — symbolically and visually.

---

## 📊 Visual Overview

![surface_comparison](images/surface_comparison.png)

```
        f(x)
         /\
        /  \
       /    \      g(x)
      /      \    /
-----/--------\--/------> x
     ↑φ        ↑Δφ
```

- φ → vertical gap between prediction curves  
- Δφ → difference in curvature or slope

---

## 📚 Learn More

| Section                                            | Description          |
| -------------------------------------------------- | -------------------- |
| [Quickstart](quickstart.md)                        | 5-minute runthrough  |
| [Concepts](concepts.md)                            | Meaning of φ, Δφ, φ* |
| [Automation](automation.md)                        | CLI & pipeline use   |
| [Theory](theory.md)                                | Mathematical core    |
| [API Reference](api.md)                            | Full function docs   |
| [Case Studies](case_studies/retail_forecasting.md) | Real-world examples  |
| [Glossary](glossary.md)                            | Unified terminology  |
| [Roadmap](roadmap.md)                              | Future plans         |

---

## ✳️ Why Symbolic?

Digamma-Prime treats models as functions — and compares them symbolically.  
It doesn’t just measure accuracy; it reveals **how models behave**.

Whether you’re a data scientist monitoring drift, a researcher proving stability, or a student learning how models change — Digamma-Prime gives you one universal language: **φ and Δφ**.
