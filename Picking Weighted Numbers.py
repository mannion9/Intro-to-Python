import random
import time
initial_time = time.time()
# This code allows you to pick numbers at random, but weigh you choising
# by some known probability. This program works such that the list is as
# large as you need. For example if I have two options that are equally likely.
# Then I just need a list of length two, with option 1 and option 2. Then if
# randomly draw a number from this list, I will have equal probability of finding
# option 1 or option 2. If I have different set of probabilities like say 9% option 1
# and 91% option two, then this code produces a list of length 100, having
# 9 elements be option 1 and 91 being option 2. It works the same with larger
# accuracy, for example if option 1's probability is .005 and option 2 has probability
# .995 the list is 10^3 elements long, with 995 elements being option 2 and 5 options
# 1

def random_choice_weighted(prob_1,prob_2,precision):
    

 # This tells you how many decimal places you have for probability 1
 # and the two is subtracted because the way I am doing if prob_1 = .2
 # python reads this as 0.2 then when it reads the string of prob_1
 # it reads this zero and the decimal as elements, but I just want the
 # numer of decimal places so I subtract 2, on for the zero one for the decimal place


    prob_1 = round(prob_1,precision)
    prob_2 = round(prob_2,precision)

    if prob_1+prob_2 != 1:
        prob_2 = 1 - prob_1

    option_length = 10**precision

    options_list = [0]*option_length
    

    max_1=prob_1*option_length
    max_2=prob_2*option_length

    counter_1=0
    counter_2=0
    index=0

    while counter_1 < max_1:
        options_list[index]=1
        index+=1
        counter_1+=1
    while counter_2 < max_2:
        if index == option_length:
            break
        options_list[index]=2
        index+=1
        counter_2+=1
    
    return options_list

##    index_choice=random.randrange(0,option_length)
##    choice=options_list[index_choice]
##    
##    return choice 

## This block below is proof that this works. If you un comment you will see that
## if you look pick a random value from this list, there is a 9% chance of finding
## number 1 and a 91% of finding number 2

prob_1=.8000001
prob_2=.1999999
decimal_precision=7

trial=0
max_trial=1000
counter_of_1=0
counter_of_2=0
choice_list=random_choice_weighted(prob_1,prob_2,decimal_precision)
while trial <= max_trial:
    choice_index = random.randrange(0,len(choice_list))
    choice = choice_list[choice_index]
    if choice == 1:
        counter_of_1+=1
    else:
        counter_of_2+=1
    trial+=1

final_time = time.time()
total_time = final_time - initial_time

print('Probability of finding choice 1 is:',counter_of_1*100/max_trial)
print('Probability of finding choice 2 is:',counter_of_2*100/max_trial)
print('Time to run',total_time)


    



