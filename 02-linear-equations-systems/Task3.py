from sympy import *

f_matrix = Matrix(([8, 10, 5, 7, 0], [2, 0, 6, 5, 1], [1, 8, 10, 2, 0], [10, 0, 0, 3, 1],[4, 1, 3, 5, 7]))
s_matrix = Matrix(([2, 1, 3, 6], [5, 10, 18, 0], [40, 7, 25, 2]))
f_res = f_matrix.rref()
s_res = s_matrix.rref()
print("Приведенная ступенчатая форма для матрицы 'A':")
print(f_res[0])
print("")
print("Приведенная ступенчатая форма для матрицы 'B':")
print(s_res[0])