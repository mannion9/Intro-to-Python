''' Guassian elimination for the system Ax=b where
    A is a NxN matrix, x is a length N vector to be
    solved for and b is the lenght N vector'''
import PypyNumpy as np

A = np.matrix([[1,0],[0,1]])
b = np.vector([[5],[3]])
x = [[0],[0]]

def BackwardSub(A,b,x):
    for i in range(0,A.dimension()[0]):
        x[i][0] = (b[i][0] / A[i,i])
    for k in range(A.dimension()[0],0,-1):
        count = 0
        for j in range(k,A.dimension()[0]-1):
            count += A[k,j]*x[j][0]
        x[k][0] = (b[k][0]-count)/A[k,k]
sol = BackwardSub(A,b,x)
print(sol)
