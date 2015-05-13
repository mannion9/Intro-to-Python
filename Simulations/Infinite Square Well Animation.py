# Animation of a quantum particle in a infitie square well
#
# Units are such that m_e=h_bar=1
# There are three main things shown in this simulation
#
# 1) When there is only one state it does not move, and thats why we call
#    these states stationary states
#
# 2) When there is the supperposition of two low states we get some movements
#    that slightly resembes a classical particle moving in a box
#    (choose nmin = 1 and nmax = 2)
#
# 3) When there is the supperposition of high energy states we get very
#    classical behavior
#    (choose nmin = 100 nmax = 110)

# Inputs

nmin=100
nmax=110

si_squared=1 # Set to 1 if you would like to see si squared animation
si_real=0    # Set to 1 if you would like to see real part of si animation
si_imaginary=0 # Set to 1 if you would like to see the imaginary part of si aniamtion

three_D =1    # Set to 1 if you would like a 3D plot of the above value you selected
        # one of the above must be set to 1
        # Beware you cannot let the first animation run too long (more than one
        # oscillation or else your computer will slow down because there will
        # be so many datapoints)
        #
        # 3D=0 for none
        # 3D=1 for si_squared
        
# Imports plotting tools and math and complex math functions

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import cmath as c
import math as m

x_global=[]
t_global=[]
si_squared_global=[]
si_real_global=[]
si_imag_global=[]

pi=m.pi

L=2*pi

xmin=0
xmax=L

tmin=0
tmax=2*pi  # Found using classical I think (I forgot I initally wrote this code a few weeks ago)

nstep=1

x_number=1000   # The larger the smoother the curve (This value is most efficant)
t_number=1000   # The larger the smoother the change in frames

x_step=(xmax-xmin)/x_number
t_step=(tmax-tmin)/t_number

t=0

# This is stationary state * the time dependence for the infinite square well

def Si(x,n,t):
    E=E_n(n,t)
    si=m.sqrt(2/L)*m.sin(n*pi*x/L)*(m.cos(E)+1j*m.sin(E))    
    return si

# Standard time dependence for infitine square well

def E_n(n,t):
    E_n=-1*(t*n**2*pi**2/(2*L**2))
    return E_n

# Supperposition of states

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
        x_global.append(x)
        t_global.append(t)
        si_squared_global.append((si_combo(x,t)*si_combo(x,t).conjugate()).real)
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
        x_global.append(x)
        t_global.append(t)
        si_real_global.append(si_combo(x,t).real)
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
        x_global.append(x)
        t_global.append(t)
        si_imag_global.append(si_combo(x,t).imag)
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
    ani=animation.FuncAnimation(fig,animate_si_squared,interval=10)
if si_real == 1:
    ani=animation.FuncAnimation(fig,animate_si_real,interval=10)
if si_imaginary == 1:
    ani=animation.FuncAnimation(fig,animate_si_imaginary,interval=10)
    
plt.show()

if three_D == 1:
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.scatter(x_global,t_global,si_squared_global)
    ax.set_xlabel('x position')
    ax.set_ylabel('time')
    ax.set_zlabel('si squared')
    plt.show()
    
