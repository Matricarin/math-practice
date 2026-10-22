# теорема о висячих вершинах в дереве

import sys
from typing import Dict, List, Tuple

def read_input() -> Tuple[List[Tuple[str, str]],Dict[str, List[str]], int, int]:
    with open('input.txt') as in_file:
        vertices_amount = int(in_file.readline())
        adj_list = dict((v, []) for v in in_file.readline().replace("\n", "").split(sep=' '))
        edges_amount = int(in_file.readline())
        edges_list: List[Tuple[str, str]] = []
        for _ in range(edges_amount):
            vertices = in_file.readline().replace("\n", "").split(sep=' ')
            edges_list.append((vertices[0], vertices[1]))
            adj_list[vertices[0]].append(vertices[1])
            adj_list[vertices[1]].append(vertices[0])
    return edges_list, adj_list, vertices_amount, edges_amount

def check_is_adj(adj_list: Dict[str, List[str]]) -> bool:
    visited: Dict[str, bool] = dict((v, False) for v in adj_list)
    vertices: List[str] = list(adj_list.keys())
    vertices_queue: List[str] = [vertices[0]]
    while vertices_queue:
        v = vertices_queue.pop(0)
        if visited[v]:
            continue
        visited[v] = True
        for neighbor in adj_list[v]:
            vertices_queue.append(neighbor)
    is_adj = True
    for v in visited:
        if not visited[v]:
            is_adj = False
    return is_adj

def check_vertices_edges_relation(v_amount: int, e_amount:int) -> bool:
    if v_amount - 1 == e_amount:
        return True
    else:
        return False

def check_has_loops(edges_list: List[Tuple[str, str]]) -> bool:
    parent = {}
    rank = {}

    def find(i):
        if i not in parent:
            parent[i] = i
            rank[i] = 0
            return i

        if parent[i] == i:
            return i

        # Сжатие пути
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            # Ранговая эвристика
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True

        return False

    for u, v in edges_list:
        if not union(u, v):
            return True

    return False


def analyze(adj_list: Dict[str, List[str]], is_adj:bool, is_ve:bool, has_loops:bool) -> str:
    if is_adj and is_ve and not has_loops:
        for vertice in adj_list:
            if len(adj_list[vertice]) == 1:
                return "YES"
    return "NO"

def write_answer(answer: str):
    with open('output.txt', 'w') as out_file:
        out_file.write(answer)

def main():
    (edges_list, adj_list, vertices_amount, edges_amount) = read_input()
    is_adj = check_is_adj(adj_list)
    is_ve = check_vertices_edges_relation(vertices_amount, edges_amount)
    has_loops = check_has_loops(edges_list)
    write_answer(analyze(adj_list, is_adj, is_ve, has_loops))

if __name__ == '__main__':
    main()