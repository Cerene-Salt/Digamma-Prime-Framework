from sympy import symbols
from symbolic_metrics import phi_symbolic, delta_phi_symbolic
import matplotlib.pyplot as plt

x = symbols('x')

def simulate_temporal_drift(base_func, steps=5, drift_type='linear'):
    """
    Generates a sequence of functions with symbolic drift over time.
    base_func: starting sympy function
    steps: number of time steps
    drift_type: 'linear' or 'quadratic'
    """
    drifted_funcs = []
    for t in range(steps):
        if drift_type == 'linear':
            drift = t * x
        elif drift_type == 'quadratic':
            drift = t * x**2
        else:
            raise ValueError("Unsupported drift type.")
        drifted_funcs.append(base_func + drift)
    return drifted_funcs

def plot_temporal_phi(funcs, norm='l2'):
    """
    Plots φ over time between consecutive functions.
    """
    phi_vals = []
    for i in range(len(funcs) - 1):
        phi = phi_symbolic(funcs[i], funcs[i+1], norm)
        phi_vals.append(phi)

    plt.plot(range(1, len(phi_vals)+1), phi_vals, marker='o', color='darkorange')
    plt.title('Symbolic Drift Over Time (φ)')
    plt.xlabel('Time Step')
    plt.ylabel('φ Value')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
