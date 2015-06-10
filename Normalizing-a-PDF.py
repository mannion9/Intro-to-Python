# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:55:05 2015

@author: mannion2
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt 

a = 0
b = 1
N = 100
x = np.linspace(a,b,N)

''' Generalized PDF normalization '''

def PDF(x):
    return x**2
    
def Normalize(PDF):
    y = PDF(x)
    I = sp.integrate.simps(y,x)
    return 1/I

cont = Normalize(PDF)

def NormPDF(x):
    return cont * PDF(x)

''' Generalized CDF Creation from Normalized PDF'''

def CDF(x):
    return np.cumsum(NormPDF(x))/N
    
CDF = CDF(x)




''' Check '''
plt.scatter(x,CDF,c='r')
def check(x):
    return x**3
plt.plot(x,check(x),c='b')
plt.xlabel('Variable x ')
plt.ylabel('Cumulative density')
plt.title('Cumulative densty function')
plt.legend()
plt.axis([0,1,0,1])