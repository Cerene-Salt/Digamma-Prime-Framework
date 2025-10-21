# Digamma Prime: Symbolic Audit Demo
# Welcome to Digamma Prime — a framework for interpretable algebraic auditing.
# This script demonstrates symbolic metrics (ϝ, δϝ, ϝ*, ϝ²ᴰ, ϝᴵ, ϝᴺ), group audits, and temporal drift detection.
%pip install sympy
from sympy import symbols
from symbolic_metrics import (
    phi_symbolic, delta_phi_symbolic, phi_star_symbolic,
    phi_curvature, phi_integral, phi_normalized,
    symbolic_group_audit
)
from symbolic_visuals import plot_group_divergence
from symbolic_temporal import simulate_temporal_drift, plot_temporal_phi

# Setup
x = symbols('x')

# 1. Symbolic metrics between two functions
f = x**3 + 2*x + 1
g = x**3 - x + 1

print("ϝ =", phi_symbolic(f, g))               # Structural difference
print("δϝ =", delta_phi_symbolic(f, g))        # Difference in rates of change
print("ϝ* =", phi_star_symbolic(f, g))         # Fusion metric
print("ϝ²ᴰ =", phi_curvature(f, g))            # Curvature difference (second derivative)
print("ϝᴵ =", phi_integral(f, g))              # Accumulated behavior difference
print("ϝᴺ =", phi_normalized(f, g))            # Normalized structural difference

# 2. Group audit
group_a = [x**2 + x, x**2 - 1]
group_b = [x**2 + 2*x + 1, x**2 - x]
groups = {'Group A': group_a, 'Group B': group_b}

phi_val = symbolic_group_audit(groups, metric='phi')
delta_val = symbolic_group_audit(groups, metric='delta')

print("Group φ audit:", phi_val)
print("Group δφ audit:", delta_val)

# 3. Visualization of group audit
plot_group_divergence(['Group A', 'Group B'], [phi_val, delta_val], metric_name='φ and δφ')

# 4. Temporal drift simulation
base = x**2 + 1
drifted = simulate_temporal_drift(base, steps=6, drift_type='linear')
plot_temporal_phi(drifted)

# 5. Final reflection
print("\n--- Reflection: What does symbolic justice mean? ---")
print("Digamma Prime uses algebraic logic to audit models and systems.")
print("Instead of statistical metrics, we use symbolic structure to reveal divergence, instability, and bias.")
print("Everything is transparent, reproducible, and interpretable — no data, just algebra.")
