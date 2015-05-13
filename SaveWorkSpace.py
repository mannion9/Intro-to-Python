#### Tutorial on how to save lists or arrays so you dont need to reproduce the
#### every time you run a code

import numpy as np

x=np.linspace(0,100,100)
y=np.linspace(0,100,100)

np.savez('TestFileName',x=x,y=y)

# This will create a file named "TestFileName' in your directory
# you can then read in this file by doing the following

data = np.load('TestFileName.npz')

# The .npz is just the file type that numpy creats
# The x=x and y=y used in the np.savez function is so that the
# varialbe is saved as itself i.e when I call the variable from
# my new data object from above... I can say x and it will get
# me what was saved as x from my np.savez statement

# Now you have data read in you can call a variable like so

x=data['x']
y=data['y']
