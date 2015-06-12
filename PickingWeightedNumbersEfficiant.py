''' This code picks a random event to occur by choosing a value out of a list which coresponds to the probability of that event occcuring.
    The method is as follows:
        1) Choose a random number ep in [0,1)
        2) Sum all the elements in the list and muliply the sum by ep
        3) Find which element in the list satisfies 
            sum of elements in list from 1 to k-1 < ep*sum(all elements) <= sum of elements in list from 1 to k
    This method works very well and is extremly efficant unlike my original method of doing this which was to create a huge list of numbers
    with the weighting of the events determing how many numbers in the huge list I put in corresonding to that event. Then choosing a random
    value out of the list I found which event occured. This worked well but was terribly inefficant.
    
    The list of evenets I am interested in here is everything in the interior of the list ,i.e not the zeros at the begining and end of the list.
    These are inserted in order to ensure the sum indexing is correct '''

events = [2,2]
events.insert(0,0) , events.append(0)
summer = sum(events)
import random as r
import matplotlib.pyplot as plt
counter = []

for numbers in range(20000):
    ep = r.random()
    index = 1
    while index <= len(events)-2:
        left = sum(events[0:index])
        right= sum(events[0:index+1])
        middle = ep*summer
        truth = left < middle <= right
        if truth == True:
            counter.append(index)
        #print('left sum',left,'middle',middle,'right sum',right,'event',index,'truth',truth)
        index += 1
plt.hist(counter)
