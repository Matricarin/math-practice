# преобразования матрицы смежности в список смежности

import sys


def main():

    matrix = []

    with open('input.txt') as in_file:
        matrix = [ list(map(int, str.split(s, sep=' '))) for s in in_file]

    adj_list = []
    for i in range(len(matrix)):
        v = []
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 1):
                v.append(j)
        adj_list.append(v)

    with open('output.txt', 'w') as out_file:
        for row in adj_list:
            out_file.write(str.join(' ', map(str, row)) + '\n')

if __name__ == '__main__':
    main()