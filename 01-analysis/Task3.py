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