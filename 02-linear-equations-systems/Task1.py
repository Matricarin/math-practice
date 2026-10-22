from sympy import *

x, y = symbols("x,y")

ans1 = solve(3 * x - 28 - 2, x)
ans2 = solve(4 * y + 12, y)

print("Решение для уравнения 'a':")
print(f"{ans1}")
print("")
print("Решение для уравнения 'b':")
print(f"{ans2}")
