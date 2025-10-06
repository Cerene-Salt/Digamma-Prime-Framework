import numpy as np
from epe_maria.monitor import EpeMonitor

# Modelo de referência (guideline ou versão anterior)
baseline = np.array([1, 2, 3, 4, 5, 6])

# Modelo atual com aceleração divergente
model_v1 = np.array([1, 2, 3, 4, 7, 11])  # aceleração crescente
model_v2 = np.array([1, 2, 3, 4, 5, 5])   # aceleração constante

monitor = EpeMonitor(baseline)

status1 = monitor.check_anomaly(model_v1)
status2 = monitor.check_anomaly(model_v2)

print("Modelo v1:", status1)
print("Modelo v2:", status2)
print("Histórico:", monitor.get_history())
