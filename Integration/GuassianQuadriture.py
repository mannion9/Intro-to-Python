roots = [[0],[0.577350269189626,-0.577350269189626],[0.000000000000000,0.774596669241483,-0.774596669241483],[0.339981043584856,-.339981043584856,.86113631159405,-.86113631159405],[0.000000000000000,0.538469310105683,-0.538469310105683,.90617984593866,-.90617984593866]]
coef = [[2],[1,1],[0.888888888888889,0.555555555555556,0.555555555555556],[0.652145154862546,0.652145154862546,0.347854845137454,0.347854845137454],[0.568888888888889,.478628670499366,.478628670499366,0.23692688505618,0.23692688505618]]


def GuassQuad(function,n,a,b):
    x_i , a_i = roots[n] , coef[n]
    t_j = [(.5*(b-a)*x_j+.5*(b+a)) for x_j in x_i]
    b_j  = [.5*(b-a)*a_j for a_j in a_i]
    I = 0
    for i in range(n+1):
        I += b_j[i]*function(t_j[i])
    return I
def Trapazoid(function,x):
    y = function(x)
    del_x = (x[-1]-x[0])/(2*(len(x)-1))
    A = 2*np.identity(len(x))
    A[0][0] , A[-1][-1] = 1 , 1
    I = sum(A.dot(y))*del_x
    return (I)

import math
import numpy as np
from time import time as tic
def func(t):
    return t**2
    #return math.exp(-t**2)
x = np.linspace(0,1,10)
I_1 = Trapazoid(func,x)
I_2 = GuassQuad(func,2,0,1)

start = tic()
for i in range(10000):           
    GuassQuad(func,3,0,1)
print('Time to run guassian quad:',tic()-start)
start = tic()
for i in range(10000):
    Trapazoid(func,x)
print('Time to run trapazoid:',tic()-start)
