

#Symbolic Documentation — Lady Epe

## Introduction
Lady Epe is a symbolic system for model auditing, capable of detecting structural divergence, curvature, and functional instability.

## Metrics

| Symbol | Technical Name       | Symbolic Interpretation                     |
|--------|----------------------|---------------------------------------------|
| ϝ      | Structural Variation | Difference in the overall shape of the function |
| δϝ     | Rate Variation       | Difference in the speed of change           |
| δ²ϝ    | Curvature Variation  | Difference in the acceleration of change    |

## Applications

-  Curvature: Detects shape changes even when values are similar  
-  Fairness: Reveals instabilities that affect fairness  
- Stability: Monitors structural consistency over time  
-  Education: Translates functional algebra into visual language  

## Pedagogical Interpretation

- ϝ → distance between functions  
- δϝ → difference in velocities  
- δ²ϝ → difference in accelerations  

## Visual Example

Functions: `f(x) = x`, `g(x) = x²`  
ϝ is small, δ²ϝ is large → g(x) accelerates, f(x) does not.

## Pipeline

- `metrics.py`: defines ϝ and δϝ  
- `temporal.py`: defines δ²ϝ  
- `monitor.py`: applies alerts  
- `benchmark.py`: compares with KS-test  
- `run_monitor.py`: runs audit with real data  
- `test_visual_benchmark.py`: generates comparative graphs  

---

#  Full Summary — Lady Epe

## Introduction

Lady Epe is a symbolic system for model auditing, capable of detecting structural changes, rate variations, and curvature in time series. It goes beyond classical statistical tests, offering a functional, visual, and pedagogical approach.

---

## Core Metrics

| Symbol | Technical Name       | Meaning                                      |
|--------|----------------------|----------------------------------------------|
| ϝ      | Structural Variation | Difference between series values             |
| δϝ     | Rate Variation       | Difference in velocities (1st derivative)    |
| δ²ϝ    | Curvature Variation  | Difference in accelerations (2nd derivative) |

---

## Computational Formulas

```python
def phi(f, g):
    return np.linalg.norm(f - g)

def delta_phi(f, g):
    df = np.diff(f)
    dg = np.diff(g)
    return np.linalg.norm(df[:min(len(df), len(dg))] - dg[:min(len(df), len(dg))])

def second_order_divergence(f, g):
    d2f = np.diff(np.diff(f))
    d2g = np.diff(np.diff(g))
    return np.linalg.norm(d2f[:min(len(d2f), len(d2g))] - d2g[:min(len(d2f), len(d2g))])
```
