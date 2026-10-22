# число ребер в полном графе

import sys


def main():
    with open('input.txt') as in_file:
        n = int(in_file.readline())
        
        s = n * (n - 1) / 2
                    
    with open('output.txt', 'w') as out_file:
        out_file.write(f"{int(s)}")


if __name__ == '__main__':
    main()
