import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "digamma_lite")))
from digamma_lite import lite_drift
from sympy import symbols

def run_credit_audit():
    x = symbols('x')
    model_A = x**2 + 3*x + 1
    model_B = x**2 + 5*x + 1

    drift = lite_drift(model_A, model_B)
    print("Credit scoring structural drift:", drift)

    if drift > 2.5:
        print("⚠️ Retrain recommended: drift exceeds fairness threshold.")
    else:
        print("✅ Model structure within acceptable bounds.")
