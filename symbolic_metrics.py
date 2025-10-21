import numpy as np
from sympy import Poly, symbols, diff

x = symbols('x')

def omega(func):
    """Extracts coefficient vector from a polynomial."""
    poly = Poly(func, x)
    coeffs = poly.all_coeffs()
    return np.array(coeffs, dtype=float)

def pad_vectors(v1, v2):
    """Pads vectors to equal length."""
    max_len = max(len(v1), len(v2))
    v1 = np.pad(v1, (0, max_len - len(v1)))
    v2 = np.pad(v2, (0, max_len - len(v2)))
    return v1, v2

def phi_symbolic(f, g, norm='l2'):
    """Structural divergence between f and g using coefficient vectors."""
    v1, v2 = omega(f), omega(g)
    v1, v2 = pad_vectors(v1, v2)
    if norm == 'l1':
        return np.sum(np.abs(v1 - v2))
    elif norm == 'l2':
        return np.linalg.norm(v1 - v2)
    else:
        raise ValueError("Unsupported norm type.")

def delta_phi_symbolic(f, g, norm='l2'):
    """Rate divergence between f and g using symbolic derivatives."""
    f_prime = diff(f, x)
    g_prime = diff(g, x)
    v1, v2 = omega(f_prime), omega(g_prime)
    v1, v2 = pad_vectors(v1, v2)
    if norm == 'l1':
        return np.sum(np.abs(v1 - v2))
    elif norm == 'l2':
        return np.linalg.norm(v1 - v2)
    else:
        raise ValueError("Unsupported norm type.")

def phi_star_symbolic(f, g, alpha=0.5, beta=0.5, norm='l2'):
    """Fusion metric combining structural and rate divergence."""
    phi_val = phi_symbolic(f, g, norm)
    delta_val = delta_phi_symbolic(f, g, norm)
    return alpha * phi_val + beta * delta_val

def symbolic_group_audit(groups, metric='phi', norm='l2'):
    """
    Computes average symbolic divergence between groups.
    groups: dict of group_name -> list of sympy functions
    metric: 'phi' or 'delta'
    norm: 'l1' or 'l2'
    """
    from itertools import product

    group_names = list(groups.keys())
    if len(group_names) != 2:
        raise ValueError("Only two groups supported for now.")

    g1, g2 = groups[group_names[0]], groups[group_names[1]]
    divergences = []

    for f, g in product(g1, g2):
        if metric == 'phi':
            divergences.append(phi_symbolic(f, g, norm))
        elif metric == 'delta':
            divergences.append(delta_phi_symbolic(f, g, norm))
        else:
            raise ValueError("Unsupported metric type.")

    return np.mean(divergences)

from sympy import integrate

def phi_curvature(f, g, norm='l2'):
    """Compares second derivatives (curvature) of f and g."""
    f_double = diff(f, x, 2)
    g_double = diff(g, x, 2)
    v1, v2 = omega(f_double), omega(g_double)
    v1, v2 = pad_vectors(v1, v2)
    if norm == 'l1':
        return np.sum(np.abs(v1 - v2))
    elif norm == 'l2':
        return np.linalg.norm(v1 - v2)
    else:
        raise ValueError("Unsupported norm type.")

def phi_integral(f, g, norm='l2'):
    """Compares symbolic integrals of f and g."""
    f_int = integrate(f, x)
    g_int = integrate(g, x)
    v1, v2 = omega(f_int), omega(g_int)
    v1, v2 = pad_vectors(v1, v2)
    if norm == 'l1':
        return np.sum(np.abs(v1 - v2))
    elif norm == 'l2':
        return np.linalg.norm(v1 - v2)
    else:
        raise ValueError("Unsupported norm type.")

def phi_normalized(f, g, norm='l2'):
    """Scale-invariant φ using normalized coefficient vectors."""
    v1, v2 = omega(f), omega(g)
    v1, v2 = pad_vectors(v1, v2)
    v1 = v1 / np.linalg.norm(v1) if np.linalg.norm(v1) != 0 else v1
    v2 = v2 / np.linalg.norm(v2) if np.linalg.norm(v2) != 0 else v2
    if norm == 'l1':
        return np.sum(np.abs(v1 - v2))
    elif norm == 'l2':
        return np.linalg.norm(v1 - v2)
    else:
        raise ValueError("Unsupported norm type.")

