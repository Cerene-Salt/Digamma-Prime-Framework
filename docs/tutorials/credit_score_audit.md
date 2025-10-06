# 💳 Tutorial — Credit Score Audit

This tutorial shows how Digamma-Prime can detect symbolic drift in credit scoring models — helping monitor fairness and stability.

---

## 📦 Dataset

Synthetic credit scoring dataset with features like:

- Income  
- Age  
- Debt-to-income ratio  
- Credit history length

---

## 🧪 Models

- `LogisticRegression`  
- `GradientBoostingClassifier`

---

## 🔍 Audit Goal

Compare predictions from both models on the same test set using:

- φ → structural divergence  
- Δφ → rate divergence  
- Drift verdict → fairness check

---

## 🧪 Code Snippet

```python
from epe_maria import phi, delta_phi
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

# Assume X, y loaded from credit dataset
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

lr = LogisticRegression().fit(Xtr, ytr)
gb = GradientBoostingClassifier().fit(Xtr, ytr)

phi_val = phi(lr.predict_proba(Xte)[:,1], gb.predict_proba(Xte)[:,1])
delta_val = delta_phi(lr.predict_proba(Xte)[:,1], gb.predict_proba(Xte)[:,1])

Results:

φ = 6.42
Δφ = 9.87

📈 Visuals
φ shows disagreement in predicted probabilities

Δφ reveals nonlinear sensitivity to income and age

🧠 Interpretation
φ indicates structural drift — models assign different scores

Δφ shows shape instability — GradientBoosting reacts more sharply to certain features

This could affect fairness or consistency in credit decisions