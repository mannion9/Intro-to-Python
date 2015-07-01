# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:59:06 2015

@author: mannion2
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,11)
def fit(x,a,b,c):
    return a*x**2+b*x+c
y=fit(x,1,0,0)

x_new = []
y_new = []

N = 100

def interpolate(x_data,y_data,N):
    delta_x_new = (max(x_data)-min(x_data))/N
    x = min(x_data)
    i = 1 
    while i < len(x_data)-1:
        x0,x1,x2 = x_data[i],x_data[i-1],x_data[i+1]
        y0,y1,y2 = y_data[i],y_data[i-1],y_data[i+1]
        first = (x0-x1)*(x0-x2)
        second = (x1-x0)*(x1-x2)
        third = (x2-x0)*(x2-x1)
        coef_1 = (y0/first) + (y1/second) + (y2/third)
        coef_2 = (-y0*(x2+x1)/first)+(-y1*(x2+x0)/second)+(-y2*(x1+x0)/third)
        coef_3 = (y0*x1*x2/first)+(y1*x0*x2/second)+(y2*x0*x1/third)
        while x < x2:
            y_new.append(fit(x,coef_1,coef_2,coef_3))
            x_new.append(x)
            x += delta_x_new
        i += 1
    return x_new,y_new
    
x_plot , y_plot = interpolate(x,y,N)

plt.scatter(x,y)
plt.plot(x_plot,y_plot)
