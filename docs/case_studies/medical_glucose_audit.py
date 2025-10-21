import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "digamma_lite")))
from digamma_lite import lite_rate
from sympy import symbols

def run_medical_audit():
    x = symbols('x')
    model_A = x**2 + 0.5*x + 1
    model_B = x**2 + 0.8*x + 1

    rate = lite_rate(model_A, model_B)
    print("Medical glucose rate divergence:", rate)

    if rate > 1.0:
        print("⚠️ Retrain recommended: rate instability detected.")
    else:
        print("✅ Model behavior stable across glucose range.")
