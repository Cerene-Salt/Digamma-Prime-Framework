import numpy as np
from epe_maria.benchmark import benchmark_epe_vs_ks

# Simulação: referência vs modelo com leve drift
reference = np.random.normal(0, 1, 1000)
model_drift = np.random.normal(0.3, 1, 1000)

# Simulação: referência vs modelo com curvatura alterada
model_curved = np.array([np.sin(x/10) for x in range(1000)]) + np.random.normal(0, 0.1, 1000)

# Testes
result_drift = benchmark_epe_vs_ks(reference, model_drift)
result_curved = benchmark_epe_vs_ks(reference, model_curved)

print("Drift simples:")
for k, v in result_drift.items():
    print(f"  {k}: {v}")

print("\nCurvatura alterada:")
for k, v in result_curved.items():
    print(f"  {k}: {v}")
