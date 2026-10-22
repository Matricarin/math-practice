# проверка полного двудольного графа пользователей и фильмов

import sys
from typing import List

def read_input() -> List[List[int]]:
    with open('input.txt') as in_file:
        users_set = set(in_file.readline().replace("\n", "").split(sep=' '))
        movies_set = list(in_file.readline().replace("\n", "").split(sep=' '))
        matrix = [] * len(users_set)
        for user in users_set:
            user_info = list(in_file.readline().replace("\n", "").split(sep=' '))
            user_movies = [0] * len(movies_set)
            for i in range(2, 2 + int(user_info[1])):
                if user_info[i] in movies_set:
                    user_movies[movies_set.index(user_info[i])] = 1
            matrix.append(user_movies)

    return matrix

def analyze(matrix : List[List[int]]) -> bool:
    for row in matrix:
        for i in range(len(row) - 1):
            if row[i] == 0:
                return False
    return True

def write_output(answer: bool):
    with open('output.txt', 'w') as out_file:
        out_file.write('YES' if answer else 'NO')

def main():
    
    matrix = read_input()
    answer = analyze(matrix=matrix)
    write_output(answer=answer)
    


if __name__ == '__main__':
    main()
