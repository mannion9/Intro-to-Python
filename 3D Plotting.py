#####################################
# All you must do with this code    #
# is change the first three lines   #
# to either a 0 or a 1 to turn them #
# on or off and see what happens.   #
#####################################

threeD_line_plot_choice = 1
threeD_scatter_plot_choice = 0

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 3D line plots
if threeD_line_plot_choice == 1:

    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt

    fig = plt.figure()  # Creates figure to draw on
    ax = fig.add_subplot(1,1,1, projection='3d')  # The projection makes it 3d

    X, Y, Z = [1,2,3,4,5,12],[1,2,3,4,9,5],[1,2,3,3,4,5]  # Creates 3 lists for X Y Z data

    ax.plot_wireframe(X,Y,Z)
    plt.show()


# 3D Scatter
if threeD_scatter_plot_choice == 1:
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')

    X=[1,2,3,4,5,6,7,8,9]
    Y=[9,8,7,6,5,4,3,2,1]
    Z=[1,2,3,4,5,6,7,4,3]

    ax.scatter(X,Y,Z, c='r',marker='o')
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')

    plt.show()
