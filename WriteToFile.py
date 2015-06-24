import json

f = open('Test.txt','w')   # Creates a .txt file that you can write to in your directory
x = [1,2,3]
for i in x:
    f.write('%d,' % i)
f.close()

### or 

file = open('Teset_2.txt','w')
x=[1,2,3]
json.dump(x,file)
file.close()

### read it in later

text_file = open('Test_2.txt','r')
lines = text_file.readlines()
inputer = []
index = 1
while index < len(lines)-2:
    inputer.append(int(lines[0][index]))
    index += 1
    
    
