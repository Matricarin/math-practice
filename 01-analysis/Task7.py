# направление шага и лучшее уменьшение по линейной апроксимации

import sys

def read_input(in_path:str) -> tuple[list[float], list[list[float]], float]:
    return [0.0], [[0.0]], 0.0 

def evaluate(v:list[float], dest:list[list[float]], epsilon:float) -> tuple[int, float]:
    return 0, 0.0

def write_anser(out_path:str, idx:int, delta_l:float):
    pass


def main():
    (v, dest, epsilon) = read_input('input.txt')
    (idx, delta_l) = evaluate(v, dest, epsilon)
    write_anser("output.txt", idx, delta_l)

if __name__ == "__main__":
    main()