# нахождение точек экстремума функции

import sympy

x = sympy.symbols('x')
f = x ** 3 - 6 * x ** 2 + 9 * x + 15
f_prime = sympy.diff(f, x)
f_double = sympy.diff(f_prime, x)
ans = sympy.solveset(f_prime, x, domain=sympy.Reals)
for r in ans:
    if f_double.subs(x, r) > 0:
        print(f"Минимум: {r}")
    if f_double.subs(x, r) < 0:
        print(f"Максимум: {r}")
