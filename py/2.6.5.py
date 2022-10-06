# Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, 
# как показано в примере (здесь n=5):

# Sample Input:

# 5

# Sample Output:

# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

def sperl(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    dir_index = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    stride = directions[dir_index]
    i, j = 0, 0
    for count in range(1, (n**2) + 1):
        matrix[i][j] = count
        if not (0 <= i + stride[0] < n and 0 <= j + stride[1] < n):
            dir_index += 1
            if dir_index >= len(directions):
                dir_index = 0
            stride = directions[dir_index]
        else:
            if matrix[i+stride[0]][j + stride[1]] != 0:
                dir_index += 1
                if dir_index >= len(directions):
                    dir_index = 0
                stride = directions[dir_index]
        i += stride[0]
        j += stride[1]
    for line in matrix:
        print(*line)
n = int(input())
sperl(n)