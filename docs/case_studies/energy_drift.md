# ⚡ Case Study — Energy Consumption Drift

This case study shows how Digamma-Prime detects symbolic drift in energy usage predictions — especially during seasonal regime changes.

---

## 📦 Dataset

Hourly energy consumption data across multiple months, with features like:

- Temperature  
- Humidity  
- Day of week  
- Hour of day

---

## 🧪 Models

- `Model_A`: trained on spring data  
- `Model_B`: retrained on summer data

---

## 🔍 Drift Analysis

We compare predictions from both models on a transitional month using:

- φ → structural divergence  
- Δφ → rate divergence  
- Curvature → sensitivity to temperature

---

## 📊 Results

| Period      | φ     | Δφ    | Curvature |
|-------------|-------|-------|-----------|
| Week 1      | 3.2   | 0.8   | 1.1       |
| Week 2      | 5.7   | 1.9   | 2.4       |
| Week 3      | 8.4   | 3.1   | 3.8       |
| Week 4      | 11.0  | 4.6   | 5.2       |

---

## 📈 Visuals

![energy_phi_trend](../images/energy_phi_trend.png)  
*φ increases — structural drift across seasonal boundary*

![energy_delta_trend](../images/energy_delta_trend.png)  
*Δφ reveals nonlinear response to temperature and humidity*

---

## 🧠 Interpretation

- φ shows growing disagreement — spring model fails in summer  
- Δφ shows shape instability — summer model reacts more sharply to heat  
- Curvature confirms increased sensitivity to environmental features

---

## ✅ Takeaway

Digamma-Prime helps detect **regime shifts** in time-series models — before performance drops.  
It’s ideal for energy, climate, and infrastructure forecasting.

