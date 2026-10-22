# проверка непрерывности функции

import ast
import sys

K: int = 5


def read_input(path: str) -> tuple[str, float, float]:
    with open(path) as in_file:
        sys.stdin = in_file
        f = input()
        x = float(input())
        delta = float(input())
        return f, x, delta


def analyze_continuos(f: str, x: float, delta: float) -> str:
    epsilon = K * delta
    tree = ast.parse(f, mode="eval")
    for n in ast.walk(tree):
        t = type(n)
        if t in [ast.Attribute, ast.Import, ast.Subscript]:
            raise Exception("Необычная функция")

    code = compile(tree, "<string>", "eval")
    value = eval(code, {}, {"x": x})
    left_value = eval(code, {}, {"x": x - delta})
    right_value = eval(code, {}, {"x": x + delta})

    left_lim = abs(left_value - value)
    right_lim = abs(right_value - value)


    if left_lim < epsilon and right_lim < epsilon:
        return "CONTINUOUS"

    return "DISCONTINUOUS"


def write_answer(path: str, answer: str):
    with open(path, "w") as out_file:
        sys.stdout = out_file
        print(answer)


def main():
    (f, x, delta) = read_input("input.txt")
    answer = analyze_continuos(f, x, delta)
    write_answer(path="output.txt", answer=answer)


if __name__ == "__main__":
    main()
