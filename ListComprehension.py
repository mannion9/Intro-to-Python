''' Explains list comprehension which is much faster than looping through list '''
''' The general method is this ' mylist = [ SOME_EXPRESION_WITH_i for i in ITERABLE_LIST ] '
'''
# Loop (slow)
iterer = list(range(10))
double = list(range(10))

mylist = []
for i in iterer:
    mylist.append(i+1)

print('Loop result',mylist)
# List Comprehension (fast)
mylist = [ i+1 for i in iterer]
print('List comprehension result',mylist)


