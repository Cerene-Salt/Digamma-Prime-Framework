import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from epe_maria.monitor import EpeMonitor

def load_series_from_csv(path):
    """
    Lê um CSV onde cada linha é uma série temporal.
    A primeira linha será usada como referência.
    """
    df = pd.read_csv(path)
    series = df.values
    return series

def run_epe_monitor(path, visualize=False):
    series = load_series_from_csv(path)
    baseline = series[0]
    monitor = EpeMonitor(baseline)

    print(f"\n🔍 Baseline carregado com {len(baseline)} pontos.\n")

    for i, current in enumerate(series[1:], start=1):
        status = monitor.check_anomaly(current)
        print(f"Modelo {i}: {status}")

    if visualize:
        history = monitor.get_history()
        phi_vals = [h["ϝ"] for h in history]
        delta_vals = [h["δϝ"] for h in history]
        delta2_vals = [h["δ²ϝ"] for h in history]

        plt.plot(phi_vals, label="ϝ")
        plt.plot(delta_vals, label="δϝ")
        plt.plot(delta2_vals, label="δ²ϝ")
        plt.title("Histórico de métricas Epe")
        plt.xlabel("Modelo")
        plt.ylabel("Score")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Exemplo de uso: substitui pelo teu caminho real
    run_epe_monitor("data/series.csv", visualize=True)
