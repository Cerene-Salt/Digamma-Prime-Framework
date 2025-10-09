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

