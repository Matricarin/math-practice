# липшицева непрерывность

import sys

import sympy  # type: ignore[import-untyped]

LIP = "LIPSCHITZ"
NOT_LIP = "NOT LIPSCHITZ" 
EPSILON = 1e-6

def read_input(path:str) -> tuple[str, float, float, float]:
    with open(path) as in_file:
        sys.stdin = in_file
        f = input()
        (a, b) = list(map(float, input().split(sep=" ")))
        l = float(input())
    return f, a, b, l
    
def find_answer(f:str, a:float, b:float, l:float) -> str:
    """
    Определение выполнения условия Липшица: |f(x1) - f(x2)| <= L * |x1 - x2|
    Эквивалентно требованию: max |f'(x)| <= L на отрезке [a, b].
    """ 
    
    if abs(a - b) <= EPSILON:
        return LIP
    
    x = sympy.symbols('x')
    
    expr = sympy.sympify(f, locals={"sin": sympy.sin, "cos": sympy.cos,
                                    "exp": sympy.exp, "log": sympy.log,
                                    "sqrt": sympy.sqrt, "pi": sympy.pi,
                                    "e": sympy.E})
    
    f_prime = sympy.diff(expr, x)
    f_double = sympy.diff(f_prime, x)
    
    candidate_points = [a, b]
    
    roots_prime = sympy.solveset(f_prime, x, domain=sympy.Reals)
    for r in roots_prime:
        if r.is_real and a < r < b:
            candidate_points.append(r)
            
    roots_double = sympy.solveset(f_double, x, domain=sympy.Reals)
    for r in roots_double:
        if r.is_real and a < r < b:
            candidate_points.append(r)
            
    abs_prime_values = [abs(f_prime.subs(x, v).evalf()) for v in candidate_points]
    
    max_abs_value = float(max(abs_prime_values))
    
    if max_abs_value <= l + EPSILON:
        return LIP   
    else:
        return NOT_LIP
    
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