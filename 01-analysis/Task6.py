# нахождение корня функции методом Ньютона

from collections.abc import Callable


def evaluate_next(x:float, f:Callable[[float], float], f_prime:Callable[[float], float]) -> float:
    return x - f(x)/f_prime(x)


def main():
    pass

if __name__ == "__main__":
    main()