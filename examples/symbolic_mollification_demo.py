import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from epe_maria.visuals import plot_symbolic_series
from epe_maria.metrics import mollify_series
import numpy as np

# Simulate noisy symbolic input
x = np.linspace(0, 10, 100)
noise = np.random.normal(0, 0.3, size=x.shape)
signal = np.sin(x) + noise

# Apply mollification
smoothed = mollify_series(signal, kernel='gaussian', bandwidth=0.5)

# Visualize
plot_symbolic_series(x, [signal, smoothed], labels=["Noisy", "Mollified"])
