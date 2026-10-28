# нахождение экстремумов на заданном интервале

import math

def main():
    
    EPSILON = 1e-6
    
    (a, b, c, d) = list(map(float, input().split(sep=' ')))
    (p, q) = list(map(float, input().split(sep=' ')))

    # начальная функция: a * x ** 3 + b * x ** 2 + c * x + d
    
    # ее производная: A * x ** 2 + B * x + C
    
    A = 3 * a
    B = 2 * b
    C = c
    
    roots = []
    
    if abs(A) < EPSILON and abs(B) > EPSILON:
        root = - C / B
        if p - EPSILON <= root <= q + EPSILON:
            roots.append(root)
    elif abs(A) > EPSILON and abs(B) > EPSILON:
        D = B ** 2 - 4 * A * C
        if abs(D) < EPSILON:
            root = - B / 2 * A
            if p - EPSILON <= root <= q + EPSILON:
                roots.append(root)
        elif D >= EPSILON:
            r_1 = (- B + math.sqrt(D)) / (2 * A)
            r_2 = (-B - math.sqrt(D)) / (2 * A)
            if p - EPSILON <= r_1 <= q + EPSILON:
                roots.append(r_1)
            if p - EPSILON <= r_2 <= q + EPSILON:
                roots.append(r_2)

    
    if not roots or len(roots) == 0:
        print("No critical points found.")
        return
    
    roots.sort()
        
    for r in roots:
        f_double_val = 6 * a * r + 2 * b
        
        f_val = a * r ** 3 + b * r ** 2 + c * r + d
        
        if abs(f_double_val) < 1e-7:
            nature = "Saddle point"
        elif f_double_val > 0:
            nature = "Local minimum"
        else:
            nature = "Local maximum"
        
        print(f"{nature} at x = {r:.5f}")
        print(f"f(x) = {f_val:.5f}") 


if __name__ == '__main__':
    main()