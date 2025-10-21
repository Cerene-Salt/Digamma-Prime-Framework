# 📐 Mathematical Appendix

Digamma-Prime is built on symbolic operators that compare functions over a domain.  
These metrics are interpretable, stable, and grounded in functional analysis.

---

## 🔣 Formal Definitions

Let \( \mathcal{F}(\mathbb{R}^n, \mathbb{R}^m) \) be the space of functions from inputs to outputs.

### Structural Divergence



\[
\phi(f, g) = \frac{1}{|D|} \int_D |f(x) - g(x)| \, dx
\]



Measures average output difference across domain \( D \).

---

### Rate Divergence



\[
\Delta\phi(f, g) = \frac{1}{|D|} \int_D |f'(x) - g'(x)| \, dx
\]



Measures difference in local slopes or curvature.

---

### Fusion Metric



\[
\phi^*(f, g, \alpha, \beta) = \alpha \cdot \phi(f, g) + \beta \cdot \Delta\phi(f, g)
\]



Weighted blend of structure and rate divergence.

---

## ✅ Properties

| Property             | Description                                  |
|----------------------|----------------------------------------------|
| Non-negativity       | \( \phi \geq 0 \), \( \Delta\phi \geq 0 \)   |
| Symmetry             | \( \phi(f, g) = \phi(g, f) \)                |
| Identity             | \( \phi(f, f) = 0 \), \( \Delta\phi(f, f) = 0 \) |
| Triangle inequality  | Approximate under norm assumptions           |
| Norm relation        | φ ≈ L₁ norm, Δφ ≈ Sobolev semi-norm          |

---

## 🧮 Linear Algebra View

If \( f(x) = A_f x + b_f \), \( g(x) = A_g x + b_g \):



\[
\phi(f, g) = \| (A_f - A_g)x + (b_f - b_g) \|_1
\]



So φ measures the norm of the difference between affine mappings.

---

## 🎨 Visual Interpretation

![theory_diagram](images/surface_comparison.png)

- φ → vertical gap between functions  
- Δφ → difference in curvature or slope  
- φ* → symbolic blend of both

---

## 🧠 Why Symbolic?

Symbolic metrics are:

- **Scale-invariant**  
- **Interpretable**  
- **Composable**  
- **Mathematically stable**

They allow model comparison without relying on arbitrary thresholds or statistical heuristics.

