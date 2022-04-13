

def ZeroMatrix(n):
    mat = [([0] * n) for i in range(n)]  # initialize the matrix with zeros
    return mat


def printMatrix(matrix):
    for line in matrix:
        print('  '.join(map(str, line)))
    print("\n")


def strongU(matrix):
    mat = ZeroMatrix(len(matrix))
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if c > r:
                mat[r][c] = matrix[r][c]
    return mat


def strongD(matrix):
    mat = ZeroMatrix(len(matrix))
    for r in range(len(matrix)):
        mat[r][r] = matrix[r][r]
    return mat


def strongL(matrix):
    mat = ZeroMatrix(len(matrix))
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if c < r:
                mat[r][c] = matrix[r][c]
    return mat

matrix = [[1,2,3],[4,5,6],[7,8,9]]

printMatrix(matrix)
print("U: ")
printMatrix(strongU(matrix))
print("D: ")
printMatrix(strongD(matrix))
print("L: ")
printMatrix(strongL(matrix))