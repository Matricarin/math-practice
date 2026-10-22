# липшицева непрерывность

import sys

def read_input(path:str) -> tuple[str, float, float, float]:
    with open(path) as in_file:
        sys.stdin = in_file
        f = input()
        (a, b) = list(map(float, input().split(sep=" ")))
        l = float(input())
    return f, a, b, l
    
def find_answer(f:str, a:float, b:float, l:float) -> str:
    return ""
    
def write_answer(path:str, answer:str):
    with open(path, 'w') as out_file:
        sys.stdout = out_file
        print(answer)


def main():
    (f, a, b, l) = read_input('input.txt')
    answer = find_answer(f, a, b, l)
    write_answer("output.txt", answer)
        
if __name__ == "__main__":
    main()