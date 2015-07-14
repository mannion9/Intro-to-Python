''' Creates hermite Polynomial coefficants for the probabilistic defininition and the physics definintion '''
from collections import defaultdict
coef=defaultdict(list)
order=101
####### Create an empty array to put coefficants in
m=0
while m <= order-1:
    n=0
    while n <= order:
        coef[m].append(0)
        n=n+1
    m=m+1
#
# Initialize the first two coefficants
#

coef[1][0] = 1
coef[2][1] = 2

n=2
counter=order-1

#
# Goes through and applies the first rule in the recursion, the being
# multiply the highest order coeficant of order say A in the previous
# polynomial by 2 and put that value as the coefficant for the next
# polynomial's highest order which is order A+1
#

while n < order-1:
    while counter > 0:
        x=coef[n][counter]
        y=2*x
        coef[n+1][counter+1]=coef[n+1][counter+1]+y
        counter=counter-1
    counter=order-1
    n=n+1

n=2
counter=0

#
# Goes through and applies the second rule in the recursion, that being
# multiply every order term in the polynomial two n values down by two
# and the n value you would like to create, and add that to the value to the
# coefficant in the previous polynomial multiplied by two
#


while n < order-1:
    sort=len(coef[n])-1
    while sort >0:
        if coef[n][sort] != 0:
            break
        else:
            sort=sort-1
        
    while counter < order:
        if counter < sort:
            w=(n-1)*(-2)*coef[n-1][counter]+2*coef[n][counter-1]
            coef[n+1][counter]=coef[n+1][counter]+w
            counter=counter+1
        else:
            break
    counter=0
    n=n+1

# Calculates the value of the hermite polynomial for a particular order and a particular
# x location

def H_n_phy(n,x):
    N=n
    m=0
    H=0
    while m < N:
        H=H+coef[n][m]*x**m
        m=m+1
    return H
def H_n_prob(n,x):
    N=n
    m=0
    H=0
    while m < N:
        H+= 2**(-n/2)*coef[n][m]*(x*2**(-1/2))**m
        m += 1
    if type(x) == int or type(x) == float:
        return H
    else:
        if type(H) == int or type(H) == float:
            return len(x)*[H]
        else: return H
        
        
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,6,100)

y_1_me = H_n_phy(1,x)
y_2_me = H_n_phy(2,x)
y_3_me = H_n_phy(3,x)
y_4_me = H_n_phy(4,x)
y_1_k = 1
y_2_k = 2*x
y_3_k = 4*x**2 - 2
y_4_k = 8*x**3 - 12*x
print(max(y_1_k-y_1_me))
print(max(y_2_k-y_2_me))
print(max(y_3_k-y_3_me))
print(max(y_4_k-y_4_me))
plt.figure(1)
plt.plot(x,y_1_me)
plt.plot(x,y_2_me)
plt.plot(x,y_3_me)
plt.plot(x,y_4_me)
plt.show()

y_1_me = H_n_prob(1,x)
y_2_me = H_n_prob(2,x)
y_3_me = H_n_prob(3,x)
y_4_me = H_n_prob(4,x)
y_1_k = 1
y_2_k = x
y_3_k = x**2 - 1
y_4_k = x**3 - 3*x
print(max(y_1_k-y_1_me))
print(max(y_2_k-y_2_me))
print(max(y_3_k-y_3_me))
print(max(y_4_k-y_4_me))
plt.figure(2)
plt.plot(x,y_1_me)
plt.plot(x,y_2_me)
plt.plot(x,y_3_me)
plt.plot(x,y_4_me)
plt.show()
