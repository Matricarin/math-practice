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
        Определение предела по Липшицу
        |f(x1) - f(x2)| <= L|x1 - x2|
    """    
    
    if abs(a - b) <= EPSILON:
        return LIP
    
    x = sympy.symbols('x')
    
    expr = sympy.sympify(f, locals={"sin": sympy.sin, "cos": sympy.cos,
                                    "exp": sympy.exp, "log": sympy.log,
                                    "sqrt": sympy.sqrt, "pi": sympy.pi,
                                    "e": sympy.E})
    
    f_prime = sympy.diff(expr, x)
    
    fa = expr.subs(x, a).evalf()
    fb = expr.subs(x, b).evalf()
    
    f_double = sympy.diff(f_prime, x)
    roots = sympy.solveset(f_double, x, domain=sympy.Reals)
    validated_roots = [r for r in roots if r > a and r < b]
    prime_values = [f_prime.subs(x, v).evalf() for v in validated_roots]
    
    prime_values.append(fa)
    prime_values.append(fb)
    
    max_value = float(max(prime_values))

    
    if abs(max_value - l) <= EPSILON:
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