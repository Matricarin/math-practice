# нахождение экстремумов на заданном интервале

import sympy as sp

(a, b, c, d) = list(map(float, input().split(sep=' ')))
(p, q) = list(map(float, input().split(sep=' ')))

x = sp.symbols('x')

f = a * x ** 3 + b * x ** 2 + c * x + d
f_prime = sp.diff(f, x)
f_double = sp.diff(f_prime, x)

criticals = sp.solveset(f_prime, x, domain=sp.Interval(p, q))

for r in criticals:
    ans = round(r, 5)
    val = f_double.subs(x, ans)
    f_val = round(f.subs(x, r))
    if val > 0:
        print(f"Local minimum at x = {ans}")
        print(f"f(x) = {f_val}")
    if val < 0:
        print(f"Local maximum at x = {ans}")
        print(f"f(x) = {f_val}")
        