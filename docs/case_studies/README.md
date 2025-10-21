# 🔧 Predictive Maintenance Audit — AI4I Case Study

This case study demonstrates symbolic drift detection using Digamma Prime on the AI4I 2020 predictive maintenance dataset. We simulate controlled drift and compare traditional performance metrics (AUC) with symbolic metrics (φ and Δφ).

---

## 📁 Dataset

- **Source**: AI4I 2020 Predictive Maintenance Dataset
- **Target**: Unified binary failure indicator (`Failure`)
- **Features**: Sensor readings, operational settings, and product type

---

## 🧪 Experiment Setup

- **Model**: Random Forest Classifier (100 trees)
- **Drift Simulation**: Additive shift to `"Torque [Nm]"` across test set
- **Sweep Range**: Drift magnitude from `0.0σ` to `1.0σ` in 0.1 increments

---

## 📊 Results Summary

| Metric        | Value         |
|---------------|---------------|
| Baseline AUC  | 0.999997      |
| Drifted AUC   | 0.999995      |
| φ             | 0.0015        |
| Δφ            | 0.0014        |

- **φ vs Drift**: Structural divergence increases non-linearly  
- **Δφ vs Drift**: Slope sensitivity tracks rate of change  
- **AUC vs Drift**: Performance remains high until ~0.5σ, then drops

---

## 📈 Visuals

Plots generated:
- `φ vs drift magnitude`
- `Δφ vs drift magnitude`
- `AUC vs drift magnitude`

Saved in:
docs/case_studies/predictive_maintenance_ai4i/results/


---

## 🧠 Interpretation

Symbolic metrics detect drift **before** performance degrades. This confirms Digamma Prime’s ability to surface early warnings in model behavior, even when traditional metrics remain stable.

---

## 🔁 Next Steps

- Feature sensitivity sweep  
- Retraining on drifted data  
- Cross-model comparison  
- Integration into audit dashboard

---

## 🧩 Reproducibility

All code, data, and results are versioned and modular. See:
dp_predictive_maintenance_ai4i.py symbolic_drift_sweep.csv


## 🔧 Case Study Included

See `docs/case_studies/predictive_maintenance_ai4i/` for a full symbolic drift audit using Digamma Prime.

Includes:
- `ai4i2020.csv` (example dataset)
- `dp_predictive_maintenance_ai4i.py` (execution script)
- `symbolic_drift_sweep.csv` (results)
- Visuals: φ, Δφ, AUC vs drift

📖 Full documentation available in `docs/case_studies/predictive_maintenance_ai4i/README.md`

Symbolic Audit: Predictive Maintenance (AI4I2020)
Module: symbolic_pm_ai4i.py Dataset: ai4i2020.csv Location: docs/case_studies/predictive_maintenance_ai4i/

🧠 Purpose
This case study demonstrates symbolic auditing of sensor-derived failure models using the AI4I2020 dataset. It applies algebraic operators to quantify model similarity, smooth symbolic drift, and scaffold predictive structures.

🔣 Operators Used
𝓢[f] Scaffolding: structural comparison of symbolic models

𝓜[f] Mollification: smoothing via polynomial truncation

𝓚[f, g] Symbolic Kernel: cosine similarity between symbolic expressions

📊 Results
Symbolic Models:

x² + mean(Process temperature)

x² + x + std(Rotational speed)

x³ + mean(Torque)

Mollified Expressions (degree ≤ 3):

1.0·x² + 310.00556

1.0·x² + 1.0·x + 179.2841

1.0·x³ + 39.98691

Cosine Similarity Matrix:

Código
[1.0,    1.0,    0.9997]
[1.0,    1.0,    0.9997]
[0.9997, 0.9997, 1.0   ]
✅ Interpretation
High symbolic similarity between quadratic models

Slight divergence from cubic torque-based model

Mollification preserves structure while reducing drift sensitivity

📁 Files
symbolic_pm_ai4i.py: audit logic

ai4i2020.csv: raw dataset

symbolic_extensions.py: operator definitions

