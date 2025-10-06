# 🛍️ Case Study — Retail Forecasting Drift

This case study shows how Digamma-Prime detects symbolic drift in weekly retail demand predictions — revealing model decay over time.

---

## 📦 Dataset

Synthetic retail sales data across 52 weeks, with features like:

- Week number  
- Promotion flag  
- Store type  
- Holiday indicator

---

## 🧪 Models

- `Model_A`: trained on weeks 1–26  
- `Model_B`: retrained on weeks 27–52

---

## 🔍 Drift Analysis

We compare predictions from both models on the full year using:

- φ → structural divergence  
- Δφ → rate divergence  
- Time series of φ to detect decay

---

## 📊 Results

| Week Range | φ     | Δφ    |
|------------|-------|-------|
| 1–13       | 2.1   | 0.4   |
| 14–26      | 4.5   | 1.2   |
| 27–39      | 7.8   | 2.3   |
| 40–52      | 10.2  | 3.1   |

---

## 📈 Visuals

![retail_phi_trend](../images/retail_phi_trend.png)  
*φ increases over time — model decay detected*

![retail_delta_trend](../images/retail_delta_trend.png)  
*Δφ reveals nonlinear sensitivity to promotions and holidays*

---

## 🧠 Interpretation

- φ shows growing disagreement — Model_A becomes outdated  
- Δφ shows shape instability — Model_B reacts differently to seasonal features  
- Together, they signal the need for retraining and feature re-evaluation

---

## ✅ Takeaway

Digamma-Prime helps monitor model health over time — revealing symbolic drift before performance drops.  
It’s a powerful tool for retail forecasting, demand planning, and seasonal modeling.

