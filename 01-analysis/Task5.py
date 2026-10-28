# нахождение экстремумов на заданном интервале

def main():
    
    (a, b, c, d) = list(map(float, input().split(sep=' ')))
    (p, q) = list(map(float, input().split(sep=' ')))

    x = sp.symbols('x')

    f = a * x ** 3 + b * x ** 2 + c * x + d
    f_prime = sp.diff(f, x)
    f_double = sp.diff(f_prime, x)

    criticals = sp.solveset(f_prime, x, domain=sp.Interval(p, q))
    
    if not criticals or criticals is sp.EmptySet:
        print("No critical points found.")
        return

    critical_points = sorted([float(r) for r in criticals])
        
    for r in critical_points:
        f_double_val = float(f_double.subs(x, r))
        
        f_val = float(f.subs(x, r))
        
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