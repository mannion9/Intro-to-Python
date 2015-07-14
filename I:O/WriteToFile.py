########################################
#### Using only built in functions #####
########################################

''' Say you have a list of values called x in this example, and you would like to input these into a .txt file to give 
    to someone for further analysis or just to save the data, you can use this method '''
x = [1,2,3]
# Write
f = open('SimpleList.txt','w')   # Creates a .txt file that you can write to in your directory
for i in x:
    f.write('%d \n' % i)         # Write each element on a new line (use %d for integers and %f for floats)
f.close()                        # Closes file and saves it
# Read
f = open('Test.txt','r')         # Opens .txt file that you can read (must be in your current directory)
data = []
for line in f:
    data.append(int(line))       # Must put line in parentheses to convert from string to a integrer or float
    
''' Say you have vector, or series of lists called r in this example, and you would like to input these into into a .txt file
    with each vector on each line, and each component seperated by a space, you can then use this method '''
r = [[1.2,2.1,3.4],[2.1,3.0,4.3]]
# Write
f = open('Vector.txt','w')      # Creates a .txt file that you can write to in your directory
for i in r:                     
    for j in i:
        if j == i[-1]:          # If this is the last element in the row vector
            f.write('%f\n' % j) # Make a new line after this element 
        else:
            f.write('%f ' % j)   
f.close()
# Read
f = open('Vector.txt','r')      # Opens .txt file that you can read(must be in your current directory)
f = f.read().splitlines()       # Opens the file and splits every line puts the lines into a list
vector = []
for line in f:                  # For every line
    row = []
    line = line.split(' ')      # Seperates each number               
    for col in line:            # For each element
        row.append(int(col))  # Insert that element into our row 
    vector.append(row)          # Put the whole row in the vector
    
    
########################################
#### Using json built in functions #####
#### (not suggested)               #####
########################################
# import json
#file = open('Teset_2.txt','w')
#x=[1,2,3]
#json.dump(x,file)
#file.close()
#
#### read it in later
#
#text_file = open('Test_2.txt','r')
#lines = text_file.readlines()
#inputer = []
#index = 1
#while index < len(lines)-2:
#    inputer.append(int(lines[0][index]))
#    index += 1
#    
    
