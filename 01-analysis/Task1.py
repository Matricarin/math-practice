# вычисление предела последовательности

import sys

def read_input(path:str) -> int:
    with open(path, 'r') as f:
        sys.stdin = f
        return int(input())

def calculate_lim(n: int) -> float:
    return round(float(n / (n + 1)), 6)

def write_answer(path:str, answer:float) -> None:
    with open(path, 'w') as f:
        sys.stdout = f
        print(answer)

def main():
    n = read_input("input.txt")
    answer = calculate_lim(n)
    write_answer(path="output.txt", answer=answer)


if __name__ == '__main__':
    main()
