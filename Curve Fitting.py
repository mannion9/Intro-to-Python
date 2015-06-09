from scipy.optimize import curve_fit
import numpy as np
### Fits functions to a user defined form ###
def func(x,a,b):
    return a*x+b

x_data = [1,2,3,4]
y_data = [1,2,3,4]

sol , var = curve_fit(func,x_data,y_data)
### STD of errors
perr = np.sqrt(np.diag(var))

print('The optimum value for a is:',sol[0],'with an uncertainity of',perr[0])
print('The optimum value for b is:',sol[1],'with an uncertainity of',perr[1])
