# направление шага и лучшее уменьшение по линейной апроксимации

import sys

def read_input(in_path:str) -> tuple[list[float], list[list[float]], float]:
    with open(in_path) as f:
        sys.stdin = f
        line = input().split(sep=' ')
        (n, k , epsilon) = (int(line[0]), int(line[1]), float(line[2]))
        v = list(map(float, input().split(sep=" ")))
        dest = []
        for i in range(n):
            d = list(map(float, input().split(sep=" ")))
            dest.append(d)
        
    return v, dest, epsilon 

def evaluate(v:list[float], dest:list[list[float]], epsilon:float) -> tuple[int, float]:
    
    return 0, 0.0

def write_anser(out_path:str, idx:int, delta_l:float):
    with open(out_path, 'w') as f:
        sys.stdout = f
        print(f"{idx} {round(delta_l, 4):4}")


def main():
    (v, dest, epsilon) = read_input('input.txt')
    (idx, delta_l) = evaluate(v, dest, epsilon)
    write_anser("output.txt", idx, delta_l)

if __name__ == "__main__":
    main()