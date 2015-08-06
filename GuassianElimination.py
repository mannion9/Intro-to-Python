''' Guassian elimination for the system Ax=b where
    A is a NxN matrix, x is a length N vector to be
    solved for and b is the lenght N vector'''
import PypyNumpy as np

A = [ [1,1,1],[0,1,0],[0,0,1]]
b = [4,5,6]

n = len(A[0])
for k in range(1,n-1):
    for i in range(k+1,n):
        l = A[i][k]/A[k][k]
        for j in range(k+1,n):
            A[i][j] -= l*A[k][j]
        b[i] -= l*b[k]
for k in range(
        
