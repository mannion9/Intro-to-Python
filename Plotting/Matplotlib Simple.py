'''
Matplotlib tutorial, which is probably the most usefully package, other than
numpy that is avaliable for Python
'''
# Importing
'''
Importing "matplotlib.pyplot as plt" will save you quite some time
because you can just call "plt" insteal of "matplotlib.pyplot" every
time you want to use a plotting feauture.
'''

import matplotlib.pyplot as plt


# Number One.... Line plots
'''
Make the most simple kind of plot, a line plot of two lists (or numpy arrays)
with no labels.
'''
x = [ 1 , 2 , 3 ]
y = [ 1 , 4 , 9 ]
plt.plot(x,y)
plt.show()

# Number Two.... Scatter plots
'''
Second morst simple kind of plot, a scatter plot of two lists (or numpy arrays)
with no lables
'''
x = [ 1 , 2 , 3 ]
y = [ 1 , 4 , 9 ]
plt.scatter(x,y)
plt.show()

# Number Three.... Line plot with labels and title
'''
Make the most simple kind of plot, a line plot of two lists (or numpy arrays)
with labels and a title.
'''
x = [ 1 , 2 , 3 ]
y = [ 1 , 4 , 9 ]
plt.plot(x,y)
plt.xlabel('X Label (Units)')
plt.ylabel('Y Label (Units)')
plt.title('Example Title Here')
plt.show()

# Number Four.... Histogram 
'''
This function is very useful in many applications. Matplotlib actually
bins your data for you into ten bins unless you specfiy otherwise (as
you will see). The input is just one LIST. 
'''
bins = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(bins)
plt.show()

# Number Five.... Error Bars
'''
I cannot figure out scatter plots with error bars this is the best I can do
, if you figure ths out please contact me on my email on the Github page 
'''
x = [ 1 , 2 , 3 ]
y = [ 1 , 4 , 9 ]
delta_x=[.1,.5,2]
delta_y=[0,0,.5]
plt.errorbar(x, y, yerr=delta_x, xerr=delta_y,fmt='--')  ## Error bar graph if no line wanted do fmt=None
plt.show()


# Number Size..... Change Limits of Axis
x = [ 1 , 2 , 3 ]
y = [ 1 , 4 , 9 ]
plt.scatter(x,y)
plt.xlim(xmax=3)    ## Sets X min and max , similiarly for y
plt.xlim(xmin=1)
plt.show()
