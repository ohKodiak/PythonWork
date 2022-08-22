# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# 
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab6b_Act1
# Date:         13 October 2021


#import module
from math import *

#initialize variables, take user input
counter = 0
user_input = input('Enter a positive integer to compute the Collatz sequence: ')
list1 = [int(user_input)]
undefiled_userinput = user_input

#using a while loop to perform required operations until the inputted number == 1
# converts to float, int, string as needed to iterate and perform mathematical manipulation
#keeps track of values of input as its manipulated and the number of iterations
while user_input != '1':
    if int(user_input) % 2 == 0:
        user_input = int(int(user_input) / 2)
        list1.append(user_input)
        counter += 1
        user_input = str(user_input)
    else:
        user_input = int(3*(int(user_input)) + 1)
        list1.append(user_input)
        counter += 1
        user_input = str(user_input)
        

print('Here is the Collatz sequence starting at {}:'.format(undefiled_userinput))

for i in list1:
    if i != list1[-1]:
        print(i,end = ', ')
    elif i == list1[-1]:
        print(i) 
    

print('It took {} iterations to reach 1'.format(counter))



        

        
    
    

