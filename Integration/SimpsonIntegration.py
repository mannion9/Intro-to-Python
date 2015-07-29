import numpy as np

''' Function '''
''' Not Done '''
def simpson(function,a,b,N):
    h = (b-a)/N
    x = np.linspace(a,b,N)
    x[0] , x[-1] = a , b
    y = function(x)
    A = 4*np.identity(len(x))
    A[0][0] , A[-1][-1] = 1 , 1
    for i in range(int((len(x)-1)/2)-2):
        i += 0
        A[2*i][2*i] -= 4
    I = sum(A.dot(y))*h/3
    return(A,I)

def func(x):
    return x**2

print(simpson(func,0,1,40))
        
