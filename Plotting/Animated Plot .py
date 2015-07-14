##########################################
# Tutorial of using matplotlib animation #
# Produces animation of plotting y=x^2   #
##########################################

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()            # Creates a figure (need to do this always unless just using plot or scatter')
ax1 = fig.add_subplot(1,1,1)  # Creates a subplot in a that hold 1 X 1 plots and this is the first one  input is (rows, colums, number)
 
### This is the function that holds the information in which you plot and all the
### data.
x=0
def animate(i):
    global x
    x=x+1
    y=x**2               
    ax1.scatter(x,y)

# animation? it animates on fig , the function animate, every 1s (units are ms)
ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
    

    
    
