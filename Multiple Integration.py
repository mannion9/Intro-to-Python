from scipy.integrate import nquad
import numpy as np

def function(x,t):
    return x+t    
    #return np.exp(-x)*np.sin(t) 
I = nquad(function,[[0,1],[0,1]])
print(I)


def linspace(start, stop, n):
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i

n = 100
m = 100
x_lim = [0,1]
y_lim = [0,1]

def trapazoid_2_d(func,xlim,ylim,n,m):
    h , k = (xlim[1]-xlim[0])/n , (ylim[1]-ylim[0])/n
    x_grid = list(linspace(xlim[0],xlim[1],n))
    y_grid = list(linspace(ylim[0],ylim[1],m))
    i = 1
    I = 0
    while i < n-1:
        j = 1
        while j < m-1:
            I += func(x_grid[i-1],y_grid[j-1])+func(x_grid[i-1],y_grid[j])+func(x_grid[i],y_grid[j-1])+func(x_grid[i],y_grid[j])
            j += 1
        i += 1
    I *= h*k*(1/4)
    return(I)
    
print(trapazoid_2_d(function,x_lim,y_lim,100,100))