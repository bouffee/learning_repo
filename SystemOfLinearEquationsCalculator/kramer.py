# рекурсивный код Python для нахождения определителя матрицы.
def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

M = [[4,1,1,2,1],
     [1,2,-1,1,1],
     [3,1,1,1,1],
     [2,1,1,4,1],
     [2,-1,1,1,5]]
print(getMatrixDeternminant(M))
