# Spring Simulation Animation

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Input 
damping=1 # Set to 1 for damping
forcing=0 # Set to 1 for damping of cos(wt+phi)

# System
m=1  # Mass (kg)
k=1  # Spring Constant
b=1  # Damping Constant
F=1  # Forcing 
w=math.sqrt(k/m) # Frequency of forcing
phi=0 #math.pi/2 

# Initial Conditions
x_i=10
y_i=0
v_i=-5
t_i=0

# Accuracy of Simulation
del_t=.1

# Lists of data
x_list=[]
y_list=[]
t_list=[]

def animate_spring(i):
    global x_i
    global v_i
    global t_i
    x=x_i
    v=v_i
    a=-k*x/m
    t=t_i
    if damping==1:
        a=(-k*x/m)-(b*v/m)
        if forcing==1:
            a=(-k*x/m)-(b*v/m)+(F*math.cos(w*t+phi)/m)
    v_i=v+a*del_t
    x_i=x+v*del_t+.5*a*del_t**2
    t_i=t_i+del_t
    x_list.append(x_i)
    y_list.append(y_i)
    t_list.append(t_i)
    ax1.clear()
    ax1.scatter(x,y_i,marker='s',s=100)
    ax1.set_xlabel('X Position')
    ax1.set_ylabel('Y Position')
    ax2.scatter(t_list,x_list)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('X Position')
    ax1.axis([-5,5,-1,1])


fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
ani=animation.FuncAnimation(fig,animate_spring,interval=1)
plt.show()
