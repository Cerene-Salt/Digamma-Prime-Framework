from epe_maria import curvature
from sympy import symbols

x = symbols('x')
f = x**2 + 3*x + 2

print("Average curvature:", curvature(f))
