# Filename: dp_predictive_maintenance_ai4i.py

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.interpolate import interp1d
from epe_maria import phi, delta_phi

# ---- 1. Load Data ----
df = pd.read_csv("docs/case_studies/predictive_maintenance_ai4i/ai4i2020.csv")

# Create unified failure target
df["Failure"] = df[["TWF", "HDF", "PWF", "OSF", "RNF"]].max(axis=1)
target = "Failure"

# Drop identifiers and target
drop_cols = ["UDI", "Product ID", target]
X = df.drop(columns=drop_cols)
y = df[target]

# Encode categorical columns
X = pd.get_dummies(X, drop_first=True)

# Scale numeric features
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# ---- 2. Train/Test Split ----
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)

# ---- 3. Train Baseline Model ----
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
pred_base = clf.predict_proba(X_test)[:, 1]

# Compute baseline AUC
auc_base = roc_auc_score(y_test, pred_base)
print("Baseline AUC:", auc_base)

# ---- 4. Simulate Drift ----
drift_feature = "Torque [Nm]" if "Torque [Nm]" in X_test.columns else X_test.columns[0]
std = X_test[drift_feature].std()
X_test_drift = X_test.copy()
X_test_drift[drift_feature] += 0.5 * std

pred_drift = clf.predict_proba(X_test_drift)[:, 1]
auc_drift = roc_auc_score(y_test, pred_drift)
print("AUC under drift:", auc_drift)

# ---- 5. Compute DP Metrics ----
domain = np.arange(len(pred_base))
f = interp1d(domain, pred_base, kind="linear", fill_value="extrapolate")
g = interp1d(domain, pred_drift, kind="linear", fill_value="extrapolate")

phi_val = phi(f, g, domain)
delta_val = delta_phi(f, g, domain)
print(f"φ (base vs drift): {phi_val:.4f}")
print(f"Δφ (base vs drift): {delta_val:.4f}")

# ---- 6. Drift magnitude sweep experiment ----
drift_amounts = np.linspace(0.0, 1.0, 11)
phi_vals = []
delta_vals = []
auc_vals = []
for amt in drift_amounts:
    Xt = X_test.copy()
    Xt[drift_feature] += amt * std
    p = clf.predict_proba(Xt)[:, 1]
    f = interp1d(domain, pred_base, kind="linear", fill_value="extrapolate")
    g = interp1d(domain, p, kind="linear", fill_value="extrapolate")
    phi_vals.append(phi(f, g, domain))
    delta_vals.append(delta_phi(f, g, domain))
    auc_vals.append(roc_auc_score(y_test, p))

# ---- 7. Plot results ----
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(drift_amounts, phi_vals, marker="o")
plt.xlabel("Drift magnitude (σ multiples)")
plt.ylabel("φ")
plt.title("φ vs drift")

plt.subplot(1, 3, 2)
plt.plot(drift_amounts, delta_vals, marker="o", color="orange")
plt.xlabel("Drift magnitude (σ multiples)")
plt.ylabel("Δφ")
plt.title("Δφ vs drift")

plt.subplot(1, 3, 3)
plt.plot(drift_amounts, auc_vals, marker="o", color="green")
plt.xlabel("Drift magnitude (σ multiples)")
plt.ylabel("AUC")
plt.title("AUC vs drift")

plt.tight_layout()
plt.show()

# ---- 8. Interpretation ----
print("\nInterpretation notes:")
print(f"- φ shows structural divergence as drift increases.")
print(f"- Δφ shows rate/slope sensitivity under drift.")
print(f"- AUC shows performance degradation — symbolic metrics often detect drift earlier.")

# ---- 9. Export results to CSV ----
results_df = pd.DataFrame({
    "drift_magnitude": drift_amounts,
    "phi": phi_vals,
    "delta_phi": delta_vals,
    "auc": auc_vals
})
results_df.to_csv("docs/case_studies/predictive_maintenance_ai4i/results/symbolic_drift_sweep.csv", index=False)
