''' Guassian elimination for the system Ax=b where
    A is a NxN matrix, x is a length N vector to be
    solved for and b is the lenght N vector'''

A = [[1,0,0],[0,1,0],[0,0,1]]
b = [4,5,6]


def Solve(A,b):
    for row in range(len(A)):
        A[row].append(b[row])
    #eliminate columns
    for col in range(len(A[0])):
        for row in range(col+1, len(A)):
            r = [(rowValue * (-(A[row][col] / A[col][col]))) for rowValue in A[col]]
            A[row] = [sum(pair) for pair in zip(A[row], r)]
    #now backsolve by substitution
    x = []
    A.reverse() #makes it easier to backsolve
    for sol in range(len(A)):
        if sol == 0:
            x.append(A[sol][-1] / A[sol][-2])
        else:
            inner = 0
            #substitute in all known coefficients
            for i in range(sol):
                inner += (x[i]*A[sol][-2-i])
            #the equation is now reduced to ax + b = c form
            #solve with (c - b) / a
            x.append((A[sol][-1]-inner)/A[sol][-sol-2])
    x.reverse()
    return x

sol = Solve(A,b)
print(sol)
