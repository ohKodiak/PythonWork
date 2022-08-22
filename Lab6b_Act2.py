# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab6b_Act2
# Date:         13 October 2021


#import module
from math import *
#initialize variables
sum1 = 0
product =  1

# takes input and lends value to variables for both loops
integer = input('Enter an integer: ')
integer1 = integer
integer2 = integer

# loops for both the sum and product 
while integer1 != '0':
    sum1 += int(integer1)
    integer1 = str(int(integer1) - 1)
    

while integer2 != '1':
    product *= int(integer2)
    integer2 = str(int(integer2) - 1)

    
#print statements
print('The sum of all integers from 0 to {} is {}'.format(integer,sum1))
print('The product of all integers from 1 to {} is {}'.format(integer, product))
    
    

    
    

    
    

