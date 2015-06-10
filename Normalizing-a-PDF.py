# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:55:05 2015

@author: mannion2
"""

import scipy as sp
import numpy as np
import random as r
import matplotlib.pyplot as plt 
from bisect import bisect_left 

check = 1

''' Generalized PDF normalization '''

def CreateCDF(pdf,a,b,N):
    ''' Generalized CDF Creation from Normalized PDF'''
    x = np.linspace(a,b,N)
    def Normalize(pdf):
        y = pdf(x)
        I = sp.integrate.simps(y,x)
        return 1/I
    
    cont = Normalize(pdf)
    
    def NormPDF(x):
        return cont * pdf(x)
        
    def CDF(x):
        return np.cumsum(NormPDF(x))/N
        
    return CDF(x) , x

def Choice(cdf,x):
    ''' Returns the the chosen value (corresponding to the CDF) that are closest to the choice random value (ranging from 0 to 1)'''
    choice = r.random()
    pos = bisect_left(cdf,choice)
    if pos == 0:
        pos_next = 1
    if pos == len(cdf)-1:
        pos_next = len(cdf)-2
    else:
        if abs(choice-cdf[pos-1]) < abs(choice-cdf[pos+1]):
            pos_next = pos-1
        else:
            pos_next = pos+1     
    ''' linear interpolation between these points to esitmate the result '''
    m = abs(cdf[pos]-cdf[pos_next])/abs(x[pos]-x[pos_next])
    value = ((choice - cdf[pos])/m) + x[pos]
    return value


''' Check '''
if check == 1:
    a = 0
    b = 1
    N = 1000
    def Test_1(x):
        return x**2
    CDF_test_1, x_1 = CreateCDF(Test_1,a,b,N)
    
    plt.figure(1)
    plt.scatter(x_1,CDF_test_1,c='r')
    def check(x):
        return x**3
    plt.plot(x_1,check(x_1),c='b')
    plt.xlabel('Variable x ')
    plt.ylabel('Cumulative density')
    plt.title('Cumulative densty function')
    plt.axis([0,1,0,1])
    
    choices = []    
    for i in range(10000):
        choices.append(Choice(CDF_test_1,x_1))
    plt.figure(2)
    plt.hist(choices)
    plt.xlabel('Chosen random variable')
    plt.ylabel('Counts')
    plt.title('Histogram of chosen variable with a given PDF 10,000 runs')
    
    
    
