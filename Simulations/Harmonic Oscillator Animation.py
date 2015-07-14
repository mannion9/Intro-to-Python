# Animation of a quantum harmonic oscillator
#
# Units are such that m_e=1=h_bar=w
#
# When setting the range on n to be larger than roughly 50 there is crazy numbers
# we have discussed this and it appears to be due to the fact that hermite
# polynomials are so large that there is large errors as you go to higher orders
#
# This is was a very tricky code to write. I calucluates hermit polynomials
# up to any order. Takes seconds to run. Sorry if this it is hard to understand
# the algorithm although I try to explain in comments. It was helpuful to draw
# a grid with no gridlines that had all the coefficants in it. Then if you look
# down the diagnoal you see you multiply by two from the one up and to the
# left. Then for all other terms you do some funny business that I explain above.
#

# Inputs

nmin=40
nmax=50

si_squared=0    # Set to 1 if you would like to see si squared amination
si_real=0       # Set to 1 if you would like to see read part of si animation
si_imaginary=0  # Set to 1 if you would like to see the imaginary part of si animation


from collections import defaultdict
import cmath as c
import math as m
import matplotlib.pyplot as plt
import matplotlib.animation as animation

pi=m.pi

xmin=-3*pi
xmax=3*pi

tmin=0
tmax=2*pi

nstep=1

x_number=1000   # The larger the smoother the curve
t_number=100

x_step=(xmax-xmin)/x_number
t_step=(tmax-tmin)/t_number

t=0

coef=defaultdict(list)

order=101

#
# Create an empty matrix with n=order and m=order
#

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

def H_n(n,x):
    N=n
    m=0
    H=0
    while m < N:
        H=H+coef[n][m]*x**m
        m=m+1
    return H

# Calculates Si for a particular x and n value

def Si(x,n,t):
    import math as m
    E=E_n(n,t)
    si=(m.cos(E)+1j*m.sin(E))*(1/pi)**(1/4)*(1/m.sqrt(((2**n)*(m.factorial(n)))))*H_n(n,x)*(m.exp(-.5*(x**2)))
    return si

def E_n(n,t):
    E_n=-1*(t*(n-.5))
    return E_n

#
# si_combo creates a super position of differnet states
#
# x = position
# nmin = minimum state number
# nmax= maximum state number
# nstep = step number between states
# t = time
#

def si_combo(x,t):
    si_combo=0
    n=nmin
    while n <= nmax:
        si_combo=si_combo+Si(x,n,t)
        n=n+nstep
    return si_combo

# Animation loop

def animate_si_squared(i):
    global t
    x=xmin
    si_squared=[]
    x_list=[]
    while x <= xmax:
        si_squared.append((si_combo(x,t)*si_combo(x,t).conjugate()).real)
        x_list.append(x)
        x=x+x_step
    t=t+t_step
    ax1.clear()
    ax1.scatter(x_list,si_squared)
    ax1.axis([xmin,xmax,0,max(si_squared)])
    plt.xlabel('X position')
    plt.ylabel('Si Squared (Probability)')
    plt.title(' Si Squared vs. X position ')

def animate_si_real(i):
    global t
    x=xmin
    si_real=[]
    x_list=[]
    while x<= xmax:
        si_real.append(si_combo(x,t).real)
        x_list.append(x)
        x=x+x_step
    t=t+t_step
    ax1.clear()
    ax1.scatter(x_list,si_real)
    ax1.axis([xmin,xmax,min(si_real),max(si_real)])
    plt.xlabel('X position')
    plt.ylabel('Re(Si)')
    plt.title('Re(Si) vs. X position ')

def animate_si_imaginary(i):
    global t
    x=xmin
    si_imag=[]
    x_list=[]
    while x<= xmax:
        si_imag.append(si_combo(x,t).imag)
        x_list.append(x)
        x=x+x_step
    t=t+t_step
    ax1.clear()
    ax1.scatter(x_list,si_imag)
    ax1.axis([xmin,xmax,min(si_imag),max(si_imag)])
    plt.xlabel('X position')
    plt.ylabel('Im(Si)')
    plt.title('Im(Si) vs. X position ')

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

if si_squared == 1:
    ani=animation.FuncAnimation(fig,animate_si_squared,interval=1)
if si_real == 1:
    ani=animation.FuncAnimation(fig,animate_si_real,interval=10)
if si_imaginary == 1:
    ani=animation.FuncAnimation(fig,animate_si_imaginary,interval=10)
    
plt.show()
