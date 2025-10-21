# ⚡ Quickstart

Compare two models in under five minutes.

---

## 🧪 Example: Diabetes Model Audit

```python
from epe_maria import phi, delta_phi
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Load data
X, y = load_diabetes(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

# Train models
lr = LinearRegression().fit(Xtr, ytr)
rf = RandomForestRegressor().fit(Xtr, ytr)

# Compare predictions
phi_val = phi(lr.predict(Xte), rf.predict(Xte))
delta_val = delta_phi(lr.predict(Xte), rf.predict(Xte))

print(f"φ = {phi_val:.2f}")
print(f"Δφ = {delta_val:.2f}")

φ = 18.53
Δφ = 25.05

📊 Visual Output
Structural divergence φ vs shift magnitude

Rate divergence Δφ vs shift magnitude

📁 Try Your Own CSV
bash
$ digamma compare --base baseline.csv --new retrained.csv --out results.json
This compares two prediction files and outputs φ, Δφ, and a drift verdict.

Meaning:
Higher φ → models disagree more on average

Higher Δφ → models behave differently under change (nonlinear warping)

Use this to:

Audit retrains

Monitor drift

Compare candidate vs production models