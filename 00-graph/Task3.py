# преобразование списка смежности в матрицу смежности

# тестовый случай. 
# вход: 
# 3
# 1  
# 
# 0
# выход: 
# 0 1 0
# 0 0 0
# 1 0 0

def main():

    matrix = []

    with open('input.txt') as f:
        
        n = int(f.readline())

        for i in range(n):
            matrix.append([])
            l = f.readline()
            contains_sym = l.strip('\n')
            if not contains_sym:
                matrix[i] = [0] * n
            else:
                nums = list(map(int, str.split(l, sep=" ")))
                for j in range(n):
                    if(j in nums):
                        matrix[i].append(1) 
                    else:
                        matrix[i].append(0)

    with open('output.txt', 'w') as out_file:
        for line in matrix:
            out_file.write(str.join(" ",map(str, line)) + '\n')

if __name__ == "__main__":
    main()