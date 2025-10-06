

## 🧮 `docs/api.md`

```markdown
# 🧮 API Reference

This section documents all core functions in Digamma-Prime.  
Each function is symbolic, interpretable, and automatable.

---

## `phi(f, g, domain=None)`

**Structural divergence** — average absolute difference between two functions.

```python
phi(f: Callable, g: Callable, domain: Sequence[float] = None) -> float
```

- `f`, `g`: prediction functions or NumPy arrays  
- `domain`: optional array of input values  
- Returns: float (φ value)

---

## `delta_phi(f, g, domain=None)`

**Rate divergence** — difference in slopes or curvature.

```python
delta_phi(f: Callable, g: Callable, domain: Sequence[float] = None) -> float
```

- Computes mean absolute difference of first derivatives  
- Returns: float (Δφ value)

---

## `phi_star(f, g, alpha=0.5, beta=0.5, domain=None)`

**Fusion metric** — weighted blend of φ and Δφ.

```python
phi_star(f: Callable, g: Callable, alpha: float = 0.5, beta: float = 0.5, domain: Sequence[float] = None) -> float
```

- `alpha`, `beta`: weights for φ and Δφ  
- Returns: float (φ* value)

---

## `drift(f, g, domain=None)`

**Directional bias** — signed mean difference.

```python
drift(f: Callable, g: Callable, domain: Sequence[float] = None) -> float
```

- Positive if `f(x)` > `g(x)` on average  
- Returns: float

---

## `curvature(f, domain=None)`

**Average curvature** — mean of second derivative magnitude.

```python
curvature(f: Callable, domain: Sequence[float] = None) -> float
```

- Approximates mean |f''(x)|  
- Returns: float

---

## Notes

- All functions support NumPy arrays or callables  
- If `domain` is omitted, assumes aligned arrays  
- Bootstrap CI wrappers available in CLI and `dp.compare()`

