# кратчайший путь в неориентированном графе
import sys

def main():
    # считать
    matrix = []
    with open('input.txt') as in_file:
        lines = in_file.readlines()
        n = int(lines[0])
        for i in range(1, n + 1):
            line = list(map(int, str.split(lines[i], sep=" ")))
            matrix.append(line)
        l = lines[-1].split(sep=' ')
        (start, end) = (int(l[0]), int(l[1]))
    
    # найти
    paths = [float('inf')] * n
    paths[start] = 0
    
    visited_vertices = []
    
    # достаточно положить только первую вершину
    vertices_queue = [start]
    
    while len(vertices_queue) > 0:
        vertice = vertices_queue.pop(0)
        if vertice not in visited_vertices:
            visited_vertices.append(vertice)
        else:
            continue
        
        # неучтенный случай проверки уже достигнутой вершины
        if vertice == end:
            break
            
        for i in range(len(matrix[vertice])):
            if matrix[vertice][i] == 1 and paths[i] == float('inf'):
                vertices_queue.append(i)
                paths[i] = paths[vertice] + 1


    # отправить в файл
    with open('output.txt', 'w') as out_file:
        answer = paths[end]
        if answer == float('inf'):
            answer = -1
        out_file.write(f'{answer}')

if __name__ == '__main__':
    main()
        
