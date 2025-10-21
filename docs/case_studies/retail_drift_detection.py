import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "digamma_lite")))
from digamma_lite import lite_drift
from sympy import symbols

def run_retail_audit():
    x = symbols('x')
    model_A = x**2 + 2*x + 1
    model_B = x**2 + 2.5*x + 1

    drift = lite_drift(model_A, model_B)
    print("Retail model drift:", drift)

    if drift > 2.0:
        print("⚠️ Retrain recommended: structural shift detected.")
    else:
        print("✅ Retail model structure is consistent.")
