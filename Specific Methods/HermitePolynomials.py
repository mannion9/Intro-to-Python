''' Creates hermite Polynomial coefficants for the probabilistic defininition and the physics definintion '''
''' Note that my indexing is one off from the standard, that is to say that H_0 in the standard = 1 but for me H_1 = 1
    I will work on this later I am just lazy and did everything like this '''
################################################
################## Inputs ######################
################################################
order = 6         # What order polynomial do you need up to
PType = 'Prob'   # Set to "Phy" for the physicist definition and "Prob" for the probabilitistic defintion


################################################
############# Create Polynomials ###############
################################################

####### Create an empty array to put coefficants in
coef = [(order+1)*[0] for i in range(order)]

####### Initialize the first two coefficants
if PType == 'Phy':
    coef[1][0] , coef[2][1] = 1 , 2
    #
    # Goes through and applies the first rule in the recursion, that being
    # multiply the highest order coeficant of order say A in the previous
    # polynomial by 2 and put that value as the coefficant for the next
    # polynomial's highest order which is order A+1
    #
    for n in range(order-1):
        for counter in reversed(range(1,order-1)):
            coef[n+1][counter+1] += 2*(coef[n][counter])
    #
    # Goes through and applies the second rule in the recursion, that being
    # multiply every order term in the polynomial two n values down by two
    # and the n value you would like to create, and add that to the value to the
    # coefficant in the previous polynomial multiplied by two
    #
    for n in range(order-1):
        for sort in reversed(range(1,order)):
            if coef[n][sort] != 0:
                break
        for counter in range(order):
            if counter < sort:
                coef[n+1][counter] += (n-1)*(-2)*coef[n-1][counter]+2*coef[n][counter-1]
            else:
                break
        

if PType == 'Prob':
    coef[1][0] , coef[2][1] = 1 , 1
    for n in range(order-1):
        for counter in reversed(range(1,order-1)):
            coef[n+1][counter+1] += (coef[n][counter])

    for n in range(order-1):
        for sort in reversed(range(1,order)):
            if coef[n][sort] != 0:
                break
        for counter in range(order):
            if counter < sort:
                coef[n+1][counter] += coef[n][counter-1]-(n-1)*coef[n-1][counter]
            else:
                break
        


def Hermite(n,x):
    H = 0  
    n+=1      
    for m in range(n):
        H += coef[n][m]*x**m
    return H
        
################################################
####### Check ##################################
################################################
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,6,100)
if PType == 'Phy':
    y_0_me = Hermite(0,x)
    y_1_me = Hermite(1,x)
    y_2_me = Hermite(2,x)
    y_3_me = Hermite(3,x)
    y_4_me = Hermite(4,x)
    y_0_k = 1
    y_1_k = 2*x
    y_2_k = 4*x**2 - 2
    y_3_k = 8*x**3 - 12*x
    y_4_k = 16*x**4 - 48*x**2 + 12
    print('Known minus mine',max(y_0_k-y_0_me))
    print('Known minus mine',max(y_1_k-y_1_me))
    print('Known minus mine',max(y_2_k-y_2_me))
    print('Known minus mine',max(y_3_k-y_3_me))
    print('Known minus mine',max(y_4_k-y_4_me))
    plt.figure(1)
    plt.plot(x,y_1_me)
    plt.plot(x,y_2_me)
    plt.plot(x,y_3_me)
    plt.plot(x,y_4_me)
    plt.show()
if PType == 'Prob':
    y_0_me = Hermite(0,x)
    y_1_me = Hermite(1,x)
    y_2_me = Hermite(2,x)
    y_3_me = Hermite(3,x)
    y_4_me = Hermite(4,x)
    y_0_k = 1
    y_1_k = x
    y_2_k = x**2 - 1
    y_3_k = x**3 - 3*x
    y_4_k = x**4 - 6*x**2 + 3
    print('Known minus mine',max(y_0_k-y_0_me))    
    print('Known minus mine',max(y_1_k-y_1_me))
    print('Known minus mine',max(y_2_k-y_2_me))
    print('Known minus mine',max(y_3_k-y_3_me))
    print('Known minus mine',max(y_4_k-y_4_me))
    plt.figure(2)
    plt.plot(x,y_1_me)
    plt.plot(x,y_2_me)
    plt.plot(x,y_3_me)
    plt.plot(x,y_4_me)
    plt.show()
