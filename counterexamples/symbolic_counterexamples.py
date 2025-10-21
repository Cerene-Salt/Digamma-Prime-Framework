from sympy import symbols, Poly
from sympy.matrices import Matrix

x = symbols('x')

def omega(f, degree=None):
    poly = Poly(f, x)
    deg = degree or poly.degree()
    return Matrix([[poly.coeff_monomial(x**i)] for i in range(deg + 1)])

def find_rate_divergence(f, g, tol_static=3.0, tol_dynamic=1.0):
    static_diff = (omega(f) - omega(g)).norm()
    dynamic_diff = (omega(f.diff()) - omega(g.diff())).norm()
    print(f"Static norm difference: {static_diff}")
    print(f"Dynamic norm difference: {dynamic_diff}")
    return static_diff <= tol_static and dynamic_diff >= tol_dynamic

if __name__ == "__main__":
    f = x**2 + 3*x + 1
    g = x**2 + 5*x + 1

    print("Ω(f) =", omega(f).T)
    print("Ω(g) =", omega(g).T)
    print("Ω(f') =", omega(f.diff()).T)
    print("Ω(g') =", omega(g.diff()).T)

    print("Counterexample found:", find_rate_divergence(f, g))
