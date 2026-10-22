# Петли в графе

from os import write
import sys


def main():
    matrix = list()

    with open('input.txt') as input_file:
        matrix = [list(map(int, str.split(line, sep=' '))) for line in input_file]

    loop = list()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(i == j):
                if(matrix[i][j] == 1):
                    loop.append(i)

    with open('output.txt', 'w') as output_file:
        if(len(loop) == 0):
            output_file.write("NO LOOPS")
        else:
            for i in loop:
                output_file.write(f'{i}\n')
    
if __name__ == "__main__":
    main()