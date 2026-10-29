# нахождение корня функции методом Ньютона

NOT_FOUND = 'Solution not found'

def main():
    (a, b, c) = tuple(map(float, input().split(sep=" ")))
    x = float(input())
    epsilon = float(input())
    
    is_found = False
    for n in range(1, 1001):
        f_value = find_f_value(x, a, b, c)
        f_prime_value = find_f_prime_value(x, a, b)
        if abs(f_value) < epsilon:
            print(f'Root found: x = {x:.5}')
            print(f'Number of iterations: {n - 1}')
            is_found = True
            break
        if abs(f_prime_value) < 1e-6:
            break
        x = x - f_value / f_prime_value

    
    if not is_found:
        print(NOT_FOUND)
    
def find_f_value(x: float, A:float, B:float, C:float) -> float:
    return A * x ** 2 + B * x + C

def find_f_prime_value(x:float, A:float, B:float) -> float:
    return 2 * A * x + B

if __name__ == "__main__":
    main()