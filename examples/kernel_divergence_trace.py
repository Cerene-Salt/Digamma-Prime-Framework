import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from epe_maria.core import KernelAudit
from epe_maria.visuals import plot_divergence_map
import numpy as np

# Generate symbolic structures
structure_A = np.random.rand(50)
structure_B = structure_A + np.random.normal(0, 0.1, size=50)

# Initialize kernel audit
audit = KernelAudit(kernel='laplacian', threshold=0.05)
divergence = audit.compare(structure_A, structure_B)

# Visualize divergence
plot_divergence_map(divergence, title="Kernel-Based Structural Drift")
