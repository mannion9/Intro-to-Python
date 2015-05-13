#####################################
# Tuturiol to fit data to function  #
#####################################

## WARNING: I have found this fitting is not great with error analysis beware

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#### Function you would like to fit with ####
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

#### Sample data ####
# X values
xdata = np.linspace(0, 4, 50)
# Y values
y = func(xdata, 2.5, 1.3, 0.5)
# Give Y values some randomness
ydata = y + 0.2 * np.random.normal(size=len(xdata))


#### Fitting ####
popt, pcov = curve_fit(func, xdata, ydata)

# popt is an array of the fit parameters
# pcov is the fit covarience (the diagonals are the varriance in each fit)

# Create data from estimated fits
y_fit=func(xdata,popt[0],popt[1],popt[2])

# Plot real data
plt.scatter(xdata,ydata)
# Plot fit data
plt.plot(xdata,y_fit)

plt.show()
