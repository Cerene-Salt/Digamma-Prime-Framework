# 🩺 Tutorial — Diabetes Model Audit

This tutorial shows how Digamma-Prime compares two models on health data — revealing symbolic differences beyond accuracy.

---

## 📦 Dataset

Diabetes dataset (`sklearn.datasets.load_diabetes`)

---

## 🧪 Models

- `LinearRegression`  
- `RandomForestRegressor`

---

## 🔍 Audit Goal

Compare predictions from both models on the same test set using:

- φ → structural divergence  
- Δφ → rate divergence  
- Bootstrap CI → confidence in drift

---

## 🧪 Code Snippet

```python
from epe_maria import phi, delta_phi
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

lr = LinearRegression().fit(Xtr, ytr)
rf = RandomForestRegressor().fit(Xtr, ytr)

phi_val = phi(lr.predict(Xte), rf.predict(Xte))
delta_val = delta_phi(lr.predict(Xte), rf.predict(Xte))

φ = 18.53
Δφ = 25.05

📈 Visuals
φ shows average disagreement between models

Δφ reveals nonlinear behavior in RandomForest

🧠 Interpretation
φ is high → models disagree structurally

Δφ is higher → RandomForest bends differently across feature space

Accuracy alone wouldn’t reveal this — symbolic audit does
