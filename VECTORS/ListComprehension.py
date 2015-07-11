''' Explains list comprehension which is much faster than looping through list '''
''' The general method is this ' mylist = [ SOME_EXPRESION_WITH_i for i in ITERABLE_LIST ] '
'''
# Loop (slow)
iterer = [1,2,3]
mylist = []
for i in iterer:
    mylist.append(i+1)
print('Loop result',mylist)
# List Comprehension (fast)
mylist = [ i+1 for i in iterer]
print('List comprehension result',mylist)


