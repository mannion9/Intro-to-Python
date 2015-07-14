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



def Choice(cdf,x):
    ''' Returns the the chosen value (corresponding to the CDF) that are closest to the choice random value (ranging from 0 to 1)'''
    choice = r.random()
    pos = bisect_left(cdf,choice)
    if pos == 0:
        pos_next = 1
    if pos == len(cdf) or pos == len(cdf)-1:
        pos = len(cdf)-1
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


    
    
