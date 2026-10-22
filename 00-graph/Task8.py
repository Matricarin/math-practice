# кратчайший путь в дереве
import copy
from typing import List, Tuple

def read_input() -> [List[List[int]], int, int]:
    with open('input.txt', 'r') as in_file:
        n = int(in_file.readline())
        matrix = []
        for i in range(n):
            row = list(map(int, in_file.readline().split(sep=' ')))
            matrix.append(row)
        vertices = list(map(int, in_file.readline().split(sep=' ')))
        (start, end) = (vertices[0], vertices[1])
    return [matrix, start,end]


def find_shortest_path(matrix: List[List[int]], start: int, end: int) -> List[int] | str:
    n = len(matrix)
    visited = [False] * n
    parent = [-1] * n

    vertices_queue = [start]
    visited[start] = True

    found = False
    while vertices_queue:
        vertex = vertices_queue.pop(0)
        if vertex == end:
            found = True
            break

        # Находим всех соседей
        neighbors = [x for x in range(n) if matrix[vertex][x] == 1]
        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = vertex
                vertices_queue.append(neighbor)

    if not found:
        return "NO PATH"

    # Восстанавливаем путь от end к start по массиву parent
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


def write_answer(answer: List[int] | str):
    with open('output.txt', 'w') as out_file:
        if type(answer) is str:
            out_file.write(answer)
        else :
            out_file.write(' '.join(map(str, answer)))


def  main():
    (matrix, start, end) = read_input()
    answer = find_shortest_path(matrix, start, end)
    write_answer(answer)


if __name__ == "__main__":
    main()