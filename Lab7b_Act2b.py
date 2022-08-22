# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab7b_Act2b
# Date:         16 October 2021

#get input, add to string
user_input = input('Enter three or more values separated by spaces: ')
hourly_temperature = user_input.split()
user_input2 = input('Enter a two-character separator: ')

#for loop that prints with -> until the last one
for i in hourly_temperature:
    if i != hourly_temperature[-1]:
        print(i,end=' {} '.format(user_input2))
    else:
        print(i,'')




