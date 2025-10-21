import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../symbolic_extensions")))

import pandas as pd
from sympy import symbols, sympify
from symbolic_extensions import symbolic_kernel, mollify, scaffold


x = symbols('x')

def load_ai4i_data(path):
    df = pd.read_csv(path)
    return df

def generate_symbolic_models(df):
    # Example symbolic expressions from sensor readings
    f1 = x**2 + df['Process temperature [K]'].mean()
    f2 = x**2 + x + df['Rotational speed [rpm]'].std()
    f3 = x**3 + df['Torque [Nm]'].mean()
    return [sympify(f1), sympify(f2), sympify(f3)]

def run_symbolic_audit(models):
    print("🔣 Scaffolding:")
    print(scaffold(models))

    print("\n🌊 Mollification:")
    for f in models:
        print(mollify(f, degree=3))

    print("\n🧠 Symbolic Kernel Matrix:")
    for i in range(len(models)):
        row = []
        for j in range(len(models)):
            k = symbolic_kernel(models[i], models[j], norm='cosine')
            row.append(round(float(k), 4))
        print(row)

if __name__ == "__main__":
    df = load_ai4i_data("docs/case_studies/predictive_maintenance_ai4i/ai4i2020.csv")
    models = generate_symbolic_models(df)
    run_symbolic_audit(models)
