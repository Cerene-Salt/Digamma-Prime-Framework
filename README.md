
# 📘 Digamma Prime Framework  
### *Symbolic Audit System for Structural Divergence and Functional Variation*

---

## 🎓 Module Title:  
**Symbolic Divergence Metrics and Algebraic Audit Systems in Polynomial Function Spaces**

---

## 🧭 Module Overview

This module introduces the Digamma Prime Framework — a symbolic system for comparing functions, models, and distributions using algebraic structure rather than pointwise behavior. It is designed for:

- Mathematicians interested in algebraic metrics and symbolic geometry  
- Computer scientists working in ML, DS, or symbolic AI  
- Researchers in control theory, fairness auditing, and interpretability

The framework replaces statistical similarity with **structural divergence**, using vectorized representations of functions and their derivatives.

---

## 🧠 Learning Objectives

By the end of this module, students will be able to:

- Define and compute symbolic divergence metrics between functions  
- Represent polynomials and rational functions as coefficient vectors  
- Apply vector norms to quantify structural and rate differences  
- Analyze algebraic operations (sum, product, division) via symbolic residuals  
- Integrate Digamma metrics into ML pipelines and interpretability workflows  
- Understand the philosophical and computational implications of symbolic auditing

---

## 📐 Section 1: Mathematical Foundations

### 1.1 Function Space

Let \( f(x), g(x) \in \mathbb{R}[x] \) be real polynomials or rational functions.

We define a mapping:

\[
\Omega: \mathbb{R}[x] \rightarrow \mathbb{R}^n
\]

Where \( \Omega(f) \) is the **coefficient vector** of \( f(x) \), padded with zeros to match the highest degree involved.

---

### 1.2 Norms and Divergence

Let \( \|\cdot\|_p \) be a vector norm (typically \( p = 1 \) or \( p = 2 \)).

We define:

- **Structural Divergence**  
  \[
  \varphi(f, g) = \|\Omega(f) - \Omega(g)\|_p
  \]

- **Rate Divergence**  
  \[
  \delta\varphi(f, g) = \|\Omega(f') - \Omega(g')\|_p
  \]

- **Fusion Metric**  
  \[
  \varphi^*(f, g) = \alpha \cdot \varphi(f, g) + \beta \cdot \delta\varphi(f, g)
  \]

Where \( \alpha, \beta > 0 \) are tunable weights.

---

## 🔧 Section 2: Algebraic Operations and Residuals

Let \( h = f \text{ op } g \). We define **operation residuals**:

| Operation      | Symbol        | Residual Metric                                      |
|----------------|---------------|------------------------------------------------------|
| Addition       | \( f \oplus g \) | \( \varphi_{\oplus}(f, g, h) = \|\Omega(f) + \Omega(g) - \Omega(h)\|_p \) |
| Subtraction    | \( f \ominus g \) | \( \varphi_{\ominus}(f, g, h) = \|\Omega(f) - \Omega(g) - \Omega(h)\|_p \) |
| Multiplication | \( f \otimes g \) | \( \varphi_{\otimes}(f, g, h) = \|\Omega(f \cdot g) - \Omega(h)\|_p \) |
| Division       | \( f \oslash g \) | Approximate via truncated series: \( \|\Omega(f/g) - \Omega(h)\|_p \) |

These metrics quantify how far the result \( h \) deviates from the expected algebraic output.

---

## 🧪 Section 3: Worked Example

Let:

\[
f(x) = x^3 + 2x + 1,\quad g(x) = x^3 - x + 1
\]

Then:

- \( \Omega(f) = (1, 0, 2, 1) \)  
- \( \Omega(g) = (1, 0, -1, 1) \)  
- \( \Omega(f') = (3, 0, 2) \)  
- \( \Omega(g') = (3, 0, -1) \)

Compute:

- \( \varphi(f, g) = \|(0, 0, 3, 0)\|_2 = 3 \)  
- \( \delta\varphi(f, g) = \|(0, 0, 3)\|_2 = 3 \)  
- \( \varphi^*(f, g) = 3(\alpha + \beta) \)

---

## 📊 Section 4: Partial Fraction Metrics

Given:

\[
\frac{5x + 3}{(x + 1)(x + 2)} = \frac{-2}{x + 1} + \frac{7}{x + 2}
\]

Expand each term as a power series around \( x = 0 \), truncate to degree 2:

- \( \Omega\left(\frac{-2}{x + 1}\right) \approx (-2, 2, -2) \)  
- \( \Omega\left(\frac{7}{x + 2}\right) \approx (3.5, -1.75, 0.875) \)

Sum:

\[
\Omega_{\text{partial}} = (1.5, 0.25, -1.125)
\]

Compare with:

\[
\Omega\left(\frac{5x + 3}{(x + 1)(x + 2)}\right) \approx (1.5, 0.25, -1.125)
\]

Then:

\[
\varphi^{\text{partial}} \approx 0
\]

---

## 🧭 Section 5: Applications in ML and DS

| Domain              | Use Case                                           |
|---------------------|----------------------------------------------------|
| ML fairness         | Compare model outputs across demographic groups    |
| Concept drift       | Monitor symbolic divergence over time              |
| Model comparison    | Audit classifiers by functional behavior           |
| Pedagogical modeling| Teach symbolic variation and structure             |
| Control systems     | Compare controller forms and derivatives           |
| Symbolic AI         | Learn structure-sensitive kernels and embeddings   |

---

## 📚 Section 6: Integration into Python

Install:

```bash
pip install digamma-ep
```

Use:

```python
import numpy as np
from epe_maria.metrics import phi, delta_phi
from epe_maria.temporal import second_order_divergence

x = np.linspace(-2, 2, 100)
reference = x**4
current = x**4 - 1

print("ϝ =", phi(reference, current))
print("δϝ =", delta_phi(reference, current))
print("δ²ϝ =", second_order_divergence(reference, current))
```

---

## 🧠 Section 7: Philosophical Context

Digamma Prime is not a statistical package. It is a **symbolic grammar** for auditing structure, variation, and divergence. It treats functions as algebraic objects, not sampled behaviors. This shift enables:

- Interpretability without domain assumptions  
- Auditing without statistical thresholds  
- Modeling without empirical bias

It is designed for **clarity, rigor, and teachability** — a system that explains itself.

---

## 🧩 Section 8: Expansion Modules

| Module | Description                                      |
|--------|--------------------------------------------------|
| \( \varphi^{(2)} \) | Second derivative divergence (curvature) |
| \( \varphi^{I} \)   | Integral-based divergence (area)         |
| \( \varphi^{M} \)   | Moment-based divergence                  |
| \( \varphi^{N} \)   | Normalized divergence                    |
| \( \varphi^{OR} \)  | Orthogonal basis projection (e.g. Chebyshev) |

---

## 🧠 Section 9: Exercises

1. Compute \( \varphi(f, g) \) for \( f(x) = x^2 + 3x + 2 \), \( g(x) = x^2 + x + 1 \)  
2. Derive \( \delta\varphi(f, g) \) for the same pair  
3. Use symbolic metrics to compare logistic regression vs decision tree outputs  
4. Visualize divergence over time for a drifting model  
5. Implement a symbolic fairness audit across age groups

---

FOR CURIOUS, DEEPER LEARNERS:

Absolutely, Kiki. Here's a full academic syllabus and a publishable guide for the **Digamma Prime Framework**, designed for mathematicians, computer scientists, and ML/DS practitioners. This is structured like a graduate-level course module and can be adapted for workshops, university curricula, or technical documentation.

---

## 🎓 Academic Syllabus: *Symbolic Audit Systems with Digamma Prime*

### 📘 Course Title:
**Symbolic Divergence and Algebraic Auditing in Computational Models**

### 🧠 Course Description:
This course introduces the Digamma Prime Framework — a symbolic system for comparing models, functions, and distributions using algebraic metrics. Students will learn how to quantify divergence in structure, rate, and curvature using coefficient-based representations, and apply these metrics to real-world problems in machine learning, data science, and symbolic computation.

---

### 📚 Weekly Breakdown

#### **Week 1: Foundations of Symbolic Modeling**
- Polynomial spaces and coefficient vectors
- Introduction to symbolic divergence
- Motivation: Why symbolic metrics over statistical ones?

#### **Week 2: Structural Divergence (ϝ)**
- Definition of \( \varphi(f, g) = \|\Omega(f) - \Omega(g)\|_p \)
- Properties: symmetry, zero divergence, norm behavior
- Examples with polynomials and sampled functions

#### **Week 3: Rate Divergence (δϝ)**
- Derivatives and their coefficient vectors
- \( \delta\varphi(f, g) = \|\Omega(f') - \Omega(g')\|_p \)
- Applications in model drift and temporal analysis

#### **Week 4: Fusion Metric (ϝ*)**
- Weighted combination: \( \varphi^* = \alpha \cdot \varphi + \beta \cdot \delta\varphi \)
- Tuning α and β for interpretability
- Use cases in fairness and stability audits

#### **Week 5: Algebraic Operations and Residuals**
- Symbolic metrics for addition, subtraction, multiplication, division
- Residual divergence: \( \varphi_{\oplus}, \varphi_{\otimes}, \varphi_{\oslash} \)
- Partial fraction analysis and rational functions

#### **Week 6: Benchmarking and Comparison**
- Comparing symbolic metrics with KS test and other statistical tools
- `benchmark_epe_vs_ks()` in practice
- Visualization and interpretation of divergence curves

#### **Week 7: Applications in ML and DS**
- Symbolic fairness auditing across features
- Concept drift detection in streaming data
- Model comparison: logistic regression vs decision tree

#### **Week 8: Advanced Modules and Extensions**
- Curvature divergence: second-order metrics
- Integral-based and moment-based divergence
- Orthogonal basis projections (Chebyshev, Legendre)

#### **Week 9: Teaching and Documentation**
- Building teachable symbolic systems
- Writing `teach()` and `help()` functions
- Creating notebooks and visual guides

#### **Week 10: Final Project**
- Students apply Digamma metrics to a real-world dataset
- Audit a model pipeline symbolically
- Present findings with visualizations and metric analysis

---

### 🧪 Assessment

- Weekly exercises (ϝ, δϝ, ϝ*, residuals)
- Midterm: symbolic audit of two ML models
- Final project: full symbolic audit pipeline with documentation

