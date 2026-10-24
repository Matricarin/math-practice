import math
import sys

LIP = "LIPSCHITZ"
NOT_LIP = "NOT LIPSCHITZ"
EPSILON = 1e-6

def read_input(path: str) -> tuple[str, float, float, float]:
    with open(path) as in_file:
        sys.stdin = in_file
        f_expr = input()
        a, b = map(float, input().split())
        l = float(input())
    return f_expr, a, b, l

def find_answer(f_expr: str, a: float, b: float, l: float) -> str:
    if abs(a - b) <= EPSILON:
        return LIP
    
    safe_dict = {
        "sin": math.sin, "cos": math.cos, "exp": math.exp,
        "log": math.log, "sqrt": math.sqrt, "pi": math.pi, "e": math.e
    }
    
    try:
        f = eval(f'lambda x, e=e: {f_expr}', {"__builtins__": {}}, safe_dict)
    except Exception:
        f = eval(f'lambda x, e=math.e: {f_expr}', {"__builtins__": {}}, safe_dict)

    h = 1e-7
    def f_prime(x):
        return (f(x + h) - f(x - h)) / (2 * h)

    steps = 200_000
    step_size = (b - a) / steps
    
    max_abs_prime = 0.0
    
    for i in range(steps + 1):
        x_val = a + i * step_size
        try:
            val = abs(f_prime(x_val))
            if val > max_abs_prime:
                max_abs_prime = val
        except Exception:
            continue

    if max_abs_prime <= l + EPSILON:
        return LIP
    else:
        return NOT_LIP

def write_answer(path: str, answer: str):
    with open(path, 'w') as out_file:
        sys.stdout = out_file
        print(answer)

def main():
    f_expr, a, b, l = read_input('input.txt')
    answer = find_answer(f_expr, a, b, l)
    write_answer("output.txt", answer)
        
if __name__ == "__main__":
    main()