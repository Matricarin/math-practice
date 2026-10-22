from sympy import *

x, y, z = symbols("x,y,z")

f_ans = solve([x - y - 50, 10 * x - 5 * y - 15], [x, y])
s_ans = solve([4 * x + 6 * y + 10 * z - 20, 2 * x + 2 * y + 4 * z - 6, 6 * x + 14 * y + 8 * z - 6], [x, y, z])

print("Решение для системы 'a':")
print(f"{f_ans}")
print("")   
print("Решение для системы 'b':")
print(f"{s_ans}")