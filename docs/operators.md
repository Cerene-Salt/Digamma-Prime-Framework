### Operator: mollify_series

**Module**: `epe_maria.metrics`

**Purpose**: Smooths noisy symbolic input using kernel-based mollification.

**Signature**:
```python
mollify_series(signal, kernel='gaussian', bandwidth=0.5)

Parameters:

#signal: 1D array-like input

kernel: 'gaussian' or 'laplacian'

bandwidth: smoothing intensity (σ for Gaussian)

Returns: Smoothed signal array

#Example:
smoothed = mollify_series(signal, kernel='gaussian', bandwidth=0.5)


### ✅ Ficha: `KernelAudit.compare`

```markdown
### Operator: KernelAudit.compare

**Module**: `epe_maria.core`

**Purpose**: Computes symbolic divergence between two structures using kernel logic.

**Signature**:
```python
compare(structure_A, structure_B)

#Parameters:

structure_A, structure_B: array-like symbolic structures

kernel: 'laplacian' or 'gaussian' (set in constructor)

threshold: divergence sensitivity (set in constructor)

Returns: Divergence array

#Example:
audit = KernelAudit(kernel='laplacian', threshold=0.05)
divergence = audit.compare(A, B)


---

### ✅ Ficha: `plot_divergence_map`

```markdown
### Operator: plot_divergence_map

**Module**: `epe_maria.visuals`

**Purpose**: Visualizes divergence magnitude across indices.

**Signature**:
```python
plot_divergence_map(divergence, title="...")

#Parameters:

divergence: 1D array of divergence values

title: plot title

Returns: Displays plot
#Example:
plot_divergence_map(divergence, title="Kernel-Based Structural Drift")


---

## 📦 Milestone 4: Final PyPI Expansion

### ✅ 1. Version Bump

Update `setup.py`:

```python
version='0.2.0'

include README.md
include docs/*
include examples/*

