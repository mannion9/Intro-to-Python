import numpy as np
from scipy.integrate import dblquad 
from time import time as tic

def func_1_d(x):
    return x-x+1
def func_2_d(x,t):
    return x**2 + t**2

N = 10
start = tic()
for i in range(N):
    I = dblquad(func_2_d,0,1,lambda t: 0,lambda t: 1)
print('Numpy function:',tic()-start)



def trapazoid(function,x):
    y = function(x)
    del_x = (x[-1]-x[0])/(2*(len(x)-1))
    A = 2*np.identity(len(x))
    A[0][0] , A[-1][-1] = 1 , 1
    I = sum(A.dot(y))*del_x
    return (I)
    

def trapazoid_2_d(function,x_1,x_2):
    I = 0
    del_x = (x_1[-1]-x_2[0])/(2*(len(x_1)-1))
    A = 4*np.identity(len(x_1))
    A[0][0] , A[-1][-1] = 1 , 1  
    for t in x_2:
        y = function(x_1,t)
        I += sum(A.dot(y))*del_x
    return I*((x_2[-1]-x_2[0])/len(x_2))

x_1 = np.linspace(0,1,10)
x_2 = np.linspace(0,1,10)
start = tic()
for i in range(N):
    I = trapazoid_2_d(func_2_d,x_1,x_2)
print("Me:",tic()-start)

def simpson(function,x):
    y = function(x)
    del_x = (x[-1]-x[0])/(len(x)-1)
    A = 4*np.identity(len(x))
    A[0][0] , A[-1][-1] = 1 , 1
    for i in range(int((len(x)-1)/2)-2):
        i += 1        
        A[2*i][2*i] -= 2
    I = sum(A.dot(y))*del_x/3
    return(I)
    
print(simpson(func_1_d,x_1))
        