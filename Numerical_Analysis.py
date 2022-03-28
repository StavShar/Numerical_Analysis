def initMatrix():
    rows = int(input('Enter the number of rows: '))
    cols = int(input('Enter the number of columns: '))
    mat = []
    print('Enter variables: ')
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(float(input()))
        mat.append(row)
    return mat

def initB(n):
    b = []
    for r in range(n):
        b.append(float(input()))



def printMatrix(matrix):
    for line in matrix:
        print('  '.join(map(str, line)))
    print("\n")


def Identity(n):
    mat = [([0] * n) for i in range(n)]  # initialize the matrix with zeros
    for i in range(0, n):
        mat[i][i] = 1  # the identity matrix includes 1 all over its diagonal, starts at [0][0]
    return mat


def Matrix_multiplication(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        raise Exception("Illegal multiplication between matrix's ")
    result_mat = [([0] * len(mat2[0])) for i in range(len(mat1))]  # initialize the result matrix with zeros
    # iterate through the first matrix rows
    for row1 in range(0, len(mat1)):
        # iterate through the second matrix columns
        for col2 in range(0, len(mat2[0])):
            # iterate through the second matrix rows
            for row2 in range(0, len(mat2)):
                result_mat[row1][col2] += mat1[row1][row2] * mat2[row2][col2]
    return result_mat


def ResetMember(row, col, n, pivot, a):
    elementary_matrix = Identity(n)
    elementary_matrix[row][col] = -(a / pivot)
    return elementary_matrix


def MultiplyRow(row, a, n):
    elementary_matrix = Identity(n)
    elementary_matrix[row][row] = a
    return elementary_matrix


def ExchangeRows(row1, row2, n):
    elementary_matrix = Identity(n)
    elementary_matrix[row1][row1] = 0
    elementary_matrix[row1][row2] = 1
    elementary_matrix[row2][row2] = 0
    elementary_matrix[row2][row1] = 1
    return elementary_matrix


def FinalVector(matrix, b):
    n = len(matrix)
    for j in range(0, n):
        for i in range(0, n):
            if i == j:
                pivot = matrix[i][j]
                for k in range(i + 1, n):
                    if abs(matrix[k][j]) > abs(pivot):  # pivoting
                        print("~~~Old Matrix~~~")
                        printMatrix(matrix)
                        print("~~~Elementary Matrix~~~")
                        elementary_matrix = ExchangeRows(k, i, n)
                        printMatrix(elementary_matrix)
                        matrix = Matrix_multiplication(elementary_matrix, matrix)
                        pivot = matrix[i][j]
                        print("~~~Updated Matrix~~~")
                        printMatrix(matrix)
                        b = Matrix_multiplication(elementary_matrix, b)


        for i in range(0, n):
            if i > j:
                if matrix[i][j] != 0:
                    print("~~~Old Matrix~~~")
                    printMatrix(matrix)
                    print("~~~Elementary Matrix~~~")
                    elementary_matrix = ResetMember(i, j, n, pivot, matrix[i][j])
                    printMatrix(elementary_matrix)
                    matrix = Matrix_multiplication(elementary_matrix, matrix)
                    print("~~~Updated Matrix~~~")
                    printMatrix(matrix)
                    b = Matrix_multiplication(elementary_matrix, b)


        for i in range(0, n):
            if i < j:
                if matrix[i][j] != 0:
                    print("~~~Old Matrix~~~")
                    printMatrix(matrix)
                    print("~~~Elementary Matrix~~~")
                    elementary_matrix = ResetMember(i, j, n, pivot, matrix[i][j])
                    printMatrix(elementary_matrix)
                    matrix = Matrix_multiplication(elementary_matrix, matrix)
                    print("~~~Updated Matrix~~~")
                    printMatrix(matrix)
                    b = Matrix_multiplication(elementary_matrix, b)

    for i in range(0, n):
        if matrix[i][i] != 1:
            if matrix[i][i] < 0:
                print("~~~Old Matrix~~~")
                printMatrix(matrix)
                print("~~~Elementary Matrix~~~")
                elementary_matrix = MultiplyRow(i, -1, n)
                printMatrix(elementary_matrix)
                matrix = Matrix_multiplication(elementary_matrix, matrix)
                print("~~~Updated Matrix~~~")
                printMatrix(matrix)
                b = Matrix_multiplication(elementary_matrix, b)

            print("~~~Old Matrix~~~")
            printMatrix(matrix)
            print("~~~Elementary Matrix~~~")
            elementary_matrix = MultiplyRow(i, 1 / matrix[i][i], n)
            printMatrix(elementary_matrix)
            matrix = Matrix_multiplication(elementary_matrix, matrix)
            print("~~~Updated Matrix~~~")
            printMatrix(matrix)
            print("~~~Result Vector~~~")
            b=Matrix_multiplication(elementary_matrix, b)
            printMatrix(b)
    return b

#Main
mat1 = [[-1.41, 2, 0],
        [0, 2, -1.41],
        [1, -1.41, 1]]

mat2 = [[1, 17, 12,-1/3],
        [92/11, 15, 17.12,9],
        [103/2, 84.62, 0,-11],
        [0, 2, 7,0.2]]

b1 = [[1], [1], [1]]
b2 = [[1], [2], [3], [4]]
#FinalVector(mat1, b1)
# FinalVector(mat2, b2)

def print_mul_format(lmat, rmat, sol):
    assert len(lmat) == len(rmat) and len(lmat) == len(sol), 'Error'
    l = []
    r = []
    s = []
    for row in range(len(lmat)):
        rl = []
        rr = []
        sr = []
        for col in range(len(lmat)):
            rl.append(float(round(lmat[row][col], 2)))  # for nice print
            rr.append(float(round(rmat[row][col], 2)))  # for nice print
            sr.append(float(round(sol[row][col], 2)))  # for nice print
        l.append(rl)
        r.append(rr)
        s.append(sr)
    for line in range(len(lmat)):
        if line == len(lmat)//2:
            print(f'{l[line]} \t*\t {r[line]} \t=\t {s[line]}')
        else:
            print(f'{l[line]}  \t\t {r[line]} \t\t  {s[line]}')

print_mul_format(mat1,mat1,mat1)
print('\n\n')
print_mul_format(mat2,mat2,mat2)