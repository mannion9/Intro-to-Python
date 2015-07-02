# Program to multiply two matrices using nested loops
import time
# 3x3 matrix
X = [[12,7,3,0],
    [4 ,5,6,0],
    [7 ,8,9,0],
    [12,7,3,0]]
# 3x4 matrix
Y = [[12,7,3,0],
    [4 ,5,6,0],
    [7 ,8,9,0],
    [12,7,3,0]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
start = time.time()
for i in range(100000):
    # iterate through rows of X
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
stop = time.time()
print(stop-start)

start_=time.time()
for i in range(100000):
    result_ = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
stop_=time.time()
print(stop_-start_)
