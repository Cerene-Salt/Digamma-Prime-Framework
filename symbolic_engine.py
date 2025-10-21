from symbolic_extensions import scaffold, mollify, jacobian, implicit_diff, symbolic_kernel

def audit_extensions(f, g=None):
    print("Scaffolded:", scaffold([f, g] if g else [f]))
    print("Mollified:", mollify(f))
    if g:
        print("Kernel (dot):", symbolic_kernel(f, g))
        print("Kernel (cosine):", symbolic_kernel(f, g, norm='cosine'))

def audit_implicit(F):
    print("Implicit derivative dy/dx:", implicit_diff(F))
