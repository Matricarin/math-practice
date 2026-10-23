# липшицева непрерывность

import ast
import math
import sys


def read_input(path:str) -> tuple[str, float, float, float]:
    with open(path) as in_file:
        sys.stdin = in_file
        f = input()
        (a, b) = list(map(float, input().split(sep=" ")))
        l = float(input())
    return f, a, b, l

# **План решения**

# 1. Считать входные данные: функцию `f` (строку), концы отрезка `a` и `b`, константу `L`.
# 2. Если `a == b`, отрезок вырожден в точку → функция автоматически удовлетворяет условию Липшица → ответ `LIPSCHITZ`.
# 3. Проверить выражение `f` на безопасность (запретить атрибуты, импорты, индексы), чтобы выполнение `eval` не было опасным.
# 4. Построить символьное представление функции с помощью `sympy` и вычислить её первую производную `f'(x)`.
# 5. Найти максимальное значение `|f'(x)|` на отрезке `[a, b]`:
#    - вычислить значения в концах отрезка `a` и `b`;
#    - найти вторую производную `f''(x)`, решить уравнение `f''(x) = 0` и оставить только действительные корни, лежащие внутри `(a, b)`;
#    - вычислить `|f'|` во всех найденных точках;
#    - дополнительно пройтись плотной выборкой точек по отрезку как страховка, чтобы не пропустить острый пик или неограниченный рост производной (например, у `√x` около `0`);
#    - взять максимум среди всех вычисленных значений.
# 6. Если `max |f'(x)| <= L` (с небольшим допуском на погрешность вычислений), то по теореме Лагранжа функция удовлетворяет условию Липшица с константой `L` → ответ `LIPSCHITZ`, иначе → `NOT LIPSCHITZ`.
# 7. Записать ответ в выходной файл.
    
def find_answer(f:str, a:float, b:float, l:float) -> str:
    """
        Определение предела по Липшецу
        |f(x1) - f(x2)| <= L|x1 - x2|
    """    
    
    tree = ast.parse(f, mode="eval")
    
    for node in ast.walk(tree):
        t = type(node)
        if t in [ast.Attribute, ast.Import, ast.Subscript]:
                    raise Exception("Необычная функция")
    code = compile(tree, "<string>", "eval")
    e = math.e
    a_value = eval(code, {"x" : a, "e": e})
    b_value = eval(code, {"x" : b, "e" : e})
    
    if abs(a_value - b_value) <= l * abs(a - b):
        return "LIPSCHITZ"   
    else:
        return " NOT LIPSCHITZ" 
    
def write_answer(path:str, answer:str):
    with open(path, 'w') as out_file:
        sys.stdout = out_file
        print(answer)


def main():
    (f, a, b, l) = read_input('input.txt')
    answer = find_answer(f, a, b, l)
    write_answer("output.txt", answer)
        
if __name__ == "__main__":
    main()