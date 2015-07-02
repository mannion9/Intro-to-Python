class Matrix:
    def __init__(self,X):
        self.X = X
    def __str__(self):
        for i in range(len(self.X)):
            print(str(self.X[i]))
        return ''
    def __mul__(self,other):
        result = self.X
        for i in range(len(self.X)):
           # iterate through columns of Y
           for j in range(len(other[0])):
               # iterate through rows of Y
               for k in range(len(other)):
                   result[i][j] += X[i][k] * other[k][j]

x = [[1,2,3],[1,2,3],[1,2,3]]
Y = Matrix(x)
Z = Y*Y
print(Z)

