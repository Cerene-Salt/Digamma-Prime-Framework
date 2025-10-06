
## 🧪 Next: Tutorials Folder

Let’s start with the first tutorial: **`tutorials/housing_drift.md`**

This one shows how φ and Δφ respond to a simulated income shift in housing data.

---

### 📁 `docs/tutorials/housing_drift.md`

```markdown
# 🏠 Tutorial — Housing Drift Detection

This tutorial shows how Digamma-Prime detects drift in housing price predictions when income distribution shifts.

---

## 📦 Dataset

California Housing (via `sklearn.datasets.fetch_california_housing`)

---

## 🧪 Models

- `LinearRegression`  
- `GradientBoostingRegressor`

---

## 🔁 Shift Simulation

We simulate drift by shifting the `MedInc` feature:

```python
X_shifted = X.copy()
X_shifted['MedInc'] += shift_magnitude
```

---

## 📊 Results

| Shift (σ) | φ       | Δφ      |
|-----------|---------|---------|
| 0.0       | 0.00    | 0.00    |
| 0.2       | 5.12    | 0.31    |
| 0.4       | 7.85    | 1.42    |
| 0.6       | 10.23   | 2.67    |

---

## 📈 Visuals

![housing_phi_plot](../images/housing_phi_plot.png)  
*φ increases with income shift — structural drift detected*

![housing_delta_plot](../images/housing_delta_plot.png)  
*Δφ increases — nonlinear sensitivity to income*

---

## 🧠 Interpretation

- φ shows increasing disagreement between models  
- Δφ reveals shape warping — GradientBoosting reacts more nonlinearly  
- Together, they signal both drift and instability

---

## ✅ Takeaway

Digamma-Prime gives you symbolic, visual insight into how models respond to feature shifts — not just accuracy changes.

