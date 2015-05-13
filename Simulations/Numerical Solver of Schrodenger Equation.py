import math as m
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cmath
pi=m.pi

#
# Numerical integration of Schrodenger Equation using the leap from method.
#
# In this program you can simulate three different situations with a free particle
# wave packet. 1) No potential 2) SHO Potential 3) Infintie Step Potential and
# 4) Finite Step Potential.
#
# Required input:
#
# v_harmonic == 0 ==> Free Particle
# v_harmonic == 1 ==> Harmonic Oscillator
# v_harmonic == 2 ==> Infinite Step (choose your heigh h below)
# v_harmonic == 3 ==> Finite Step 
# v_harmonic -- 4 ==> Potential Well

v_harmonic = 1

# Optional input:

a=1        # Width of wave packet
k_0=10     # Momentum of wave packet
j=5        # Spring Constant (only neccessary if v_harmonic == 1)

xmin=-2*m.pi  # Left end of box
xmax= 2*m.pi  # Right end of box
tmin=0        # Initial Time
tmax=5*pi     # Maximum Time

w=xmax/3  # Width of well or step

# Program

h=50 # Heigh of infinite step potential (computers dont do infinite but 100 is sufficant)

x_number=100     # Number of x points  (x_number = 100) 
t_number=10000    # Number of t points  (t_number = 1000)

integrate_forward='no'

x_step=(xmax-xmin)/x_number
t_step=(tmax-tmin)/t_number

x_list=[]

V=[]

t=0
t_i=t_step

x=xmin

counter=xmin

while counter <= xmax:
    x_list.append(counter)
    counter=counter+x_step

def si(a,x):
    si_x_t=(1/2/a)**(1/4)*(1+2j*a*t)**(-1/2)*cmath.exp(1j*k_0*(x+2)-1j*k_0**2*t/2+(-a*((x+2)-k_0*t)**2/(1+2j*a*t)))
    si=(1/2/a)**(1/4)*cmath.exp(-a*x**2+1j*k_0*x)
    return si_x_t

# Creates x list and intial si list
def initial_conditions(a,x,t):
    si_initial=[]
    while x<=xmax:
        si_initial.append(si(a,x))
        if v_harmonic == 0:
            V.append(0)
        if v_harmonic == 1:
            V.append(j*x**2)
        if v_harmonic == 2:
            if x <= 0:
                V.append(0)
            else:
                V.append(h)
        if v_harmonic == 3:
            if x>=0:
                if x <= w:
                    V.append(30)
            else:
                V.append(0)
        if v_harmonic == 4:
            if x>=0:
                if x<=w:
                    V.append(-h)
            else:
                V.append(0)
        x=x+x_step
    return si_initial

real_n=[]
imag_n=[]

def animate_leapfrog(i):

    global t
    global w
    global t_r
    global t_i
    global real_n
    global imag_n
    global integrate_forward
    global x_list
    

    # Anylitical Solution Si Squared
    if v_harmonic == 0:
        si_a=[]
        si_a_squared=[]
        
        for i in x_list:
            si_a.append(si(a,i))
        for i in si_a:
            si_a_squared.append((i*i.conjugate()).real)
            
        ax1.clear()
        ax1.plot(x_list,si_a_squared)
        ax1.axis([xmin,xmax,-.1,1])
        ax1.set_xlabel('X position')
        ax1.set_ylabel('Si Squared')
        ax1.set_title('Magnitude Squared vs. X (Analitical Solutio)n')

    # Numerical Solution

    si_n=[0]*x_number
    si_n_squared=[]
    if t != tmin:        
        if integrate_forward == 'real': # t_r=t_r+t_step
            real_new=[0]*x_number
            for i in x_list:
                x_loc=x_list.index(i) # What x coord in list
                # Make end points always zero
                if x_loc != 0:
                    if x_loc != len(x_list)-1:
                        
                        real_new[x_loc]=real_n[x_loc]+t_step*(((-1/(2*x_step**2))*(imag_n[x_loc+1]+imag_n[x_loc-1]-2*imag_n[x_loc]))+(V[x_loc]*imag_n[x_loc]))
                else:
                    real_new[x_loc]=0
                # Construct wave function at a t value
                si_n[x_loc]=real_n[x_loc]+1j*imag_n[x_loc]
            real_n=real_new
            integrate_forward = 'imag'

        # Construct si squared
        for i in si_n:
            si_n_squared.append((i*i.conjugate()).real)
   
        ax2.clear()
        ax2.plot(x_list,si_n_squared)
        
        if v_harmonic == 1: # Plots where the classical maximum is
            x_potential_max=m.sqrt(k_0**2/(2*j))
            x_potential=[x_potential_max]*9+[-x_potential_max]*9
            y_location=[.1,.2,.3,.4,.5,.6,.7,.8,.9,.1,.2,.3,.4,.5,.6,.7,.8,.9]
            ax2.scatter(x_potential,y_location,c='r')
        if v_harmonic == 2: # Plots where wall is
            x_potential_max=0
            x_potential=[x_potential_max]*10
            y_location=[.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
            ax2.scatter(x_potential,y_location,c='r')
        if v_harmonic == 3 or v_harmonic == 4: # Plots where walls are
            x_potential_1=0
            x_potential_2=w
            x_potential=[x_potential_1]*10+[x_potential_2]*10
            y_potential=[.1,.2,.3,.4,.5,.6,.7,.8,.9,1,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
            ax2.scatter(x_potential,y_potential,c='r')
        
            
        ax2.axis([xmin,xmax,-.1,1])
        ax2.set_xlabel('X position')
        ax2.set_ylabel('Si Squared')
        ax2.set_title('Magnitude Squared vs. X  (Numerical Solution)')
    
        if integrate_forward == 'imag':
            imag_new=[0]*x_number
            for i in x_list:
                x_loc=x_list.index(i) 
                # Make end points always zero
                if x_loc == 0:
                    imag_n[x_loc]=0
                if x_loc == len(x_list)-1:
                    imag_n[x_loc]=0
                else:
                    imag_new[x_loc]=imag_n[x_loc]+t_step*(((1/(2*x_step**2))*(real_n[x_loc+1]+real_n[x_loc-1]-2*real_n[x_loc]))-(V[x_loc]*real_n[x_loc]))
            imag_n=imag_new
            integrate_forward = 'real'

    # If it is the first time step I set the numerical wave function equal to
    # the intial analitic solution at t=0. Then I set my first imaginary function
    # to the imaginary part of the analyitic solution at a time t_step. This
    # will allow me to start integrating and have the times be off by t_step.
    
    if t == tmin:

        # Sets intial wave function to the analyitic at t  =0 
        # and set the real part for integration as analyitic at t=0
        initial_si=initial_conditions(a,xmin,t)
        for i in initial_si:
            si_n.append(i)
            real_n.append(i.real)
            
        # Sets the imaginary part for integration as analyitic at time t=t_step
        initial_si_t_forward=initial_conditions(a,xmin,t_i)
        for i in initial_si_t_forward:
            imag_n.append(i.imag) 

        for i in si_n:
            si_n_squared.append((i*i.conjugate()).real)
            
        integrate_forward = 'real'
        
    # Increase time steps
    t+=t_step



# Plotting    
fig_1=plt.figure(figsize=(12,7))
if v_harmonic == 0:
    ax1=fig_1.add_subplot(1,2,1)
    ax2=fig_1.add_subplot(1,2,2)
    ani1=animation.FuncAnimation(fig_1,animate_leapfrog,interval=10)
else:
    ax2=fig_1.add_subplot(1,1,1)
    ani1=animation.FuncAnimation(fig_1,animate_leapfrog,interval=1)
plt.show() 
