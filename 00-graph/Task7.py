# поиск листьев

import sys
from typing import List

def read_input() -> List[List[int]]:
    with open('input.txt') as in_file:
        n = int(in_file.readline())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, in_file.readline().split(sep=' '))))

    return matrix

def analyze(matrix: List[List[int]]) -> List[int] | str | None:
    vertices: List[int] = []
    for i in range(len(matrix)):
        if matrix[i].count(1) == 1:
            vertices.append(i)

    if vertices:
        return vertices
    else:
        return "NO LEAVES"

def write_answer(answer: List[int] | str):
    with open('output.txt', 'w') as out_file:
        if type(answer) is str:
            out_file.write(answer)
        else:
            out_file.write('\n'.join(map(str, answer)))

def main():
    matrix = read_input()
    answer = analyze(matrix)
    write_answer(answer)
    pass


if __name__ == '__main__':
    main()
