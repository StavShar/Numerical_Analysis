import Gaussian_Elimination
import GaussianZydel

def getG(matrix):
    return Gaussian_Elimination.Matrix_multiplication(GaussianZydel.negativeMatrix(Gaussian_Elimination.getInverseMatrix(GaussianZydel.strongD(matrix))), Gaussian_Elimination.getInverseMatrix(GaussianZydel.sumMatrix(GaussianZydel.strongL(matrix), GaussianZydel.strongU(matrix))))

def getH(matrix):
    return Gaussian_Elimination.getInverseMatrix(GaussianZydel.strongD(matrix))

mat = [[9,2,4],[3,9,1],[1,2,9]]

print("G:")
matG = getG(mat)
GaussianZydel.printMatrix(matG)

print("H:")
matH = getH(mat)
GaussianZydel.printMatrix(matH)
