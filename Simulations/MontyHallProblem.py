# Simulates the famous monty hall problem to determine if you should
# stay or switch

import random
x = int(input("Pick 1 to stay and 0 to change"))        #Want to stay or trade doors?
win = 0                                                      # Start counting wins and losese at 0
lose = 0
count = range(1, 1000)                                       # Run the program 1000 times

for i in count:
    
    prize_door = random.randint(1,3)                        # Choose random numbers for the doors
    chosen_door = random.randint(1,3)     
    open_door = random.randint(1,3)
    

    while open_door == prize_door or open_door == chosen_door:    # Makes sure the door we will open is not the winning door or the door "you" chose 
        open_door = random.randint(1,3)                           

    if x == 1:                                                 # If you stay this is how we find if you win or lose
        if prize_door == chosen_door:
            win = win + 1
        else:
            lose = lose + 1

    elif x == 0:
        chosen_door2 = random.randint(1,3)                               # If you switch this is how we find if you win or lose
        while chosen_door2 == open_door or chosen_door2 == chosen_door:  # Makes sure the door you switch to is not the door we opened or the previous door you chose
            chosen_door2 = random.randint(1,3)
        if prize_door == chosen_door2:
            win = win + 1
        else:
            lose = lose + 1
    else:
        print ("You have entered wrong input")

   
        

print ("The Probability of winning is:")
print (float(win) / float(max(count)))            # Probability




    
    
    
