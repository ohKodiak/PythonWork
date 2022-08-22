# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab6b_Act3
# Date:         13 October 2021


#import module
from math import *
import sys
#initialize variables 
number = ''
counter = 0
integer = input('Enter a four-digit integer: ')
integer3 = integer

newint = ''
#check length of inputted number 

if len(integer) == 4:
    if (integer[0] == integer[1]) and (integer[1] == integer[2]) and (integer[2] == integer[3]):
        print('{} > 0'.format(integer))
        print("{} reaches 0 via Kaprekar's routine in 1 iterations".format(integer))
        sys.exit()
    
if len(integer) == 3:
    integer = '0' + integer
if len(integer) == 2:
    integer = '00' + integer
if len(integer) == 1:
    integer = '000' + integer

                       
#sorts number into ascending order

while (((integer[0] <= integer[1]) and (integer[1] <= integer[2]) and (integer[2] <= integer[3])) == False):
    if integer[1] < integer[0]:
        integer = integer[1] + integer[0] + integer[2] + integer[3]
    if integer[2] < integer[1]:
        integer = integer[0] + integer[2] + integer[1] + integer[3]
    if integer[3] < integer[2]:
        integer = integer[0] + integer[1] + integer[3] + integer[2]
    
# initializing more variables
intcopy = ''
integercopy = integer
integer_asc = integer
integer_desc = integer[::-1]
integersum = 0
nums_tracker = integer + ' > '

#performs calculation
while integersum != '6174':
    counter +=1
    integersum = str(int(integer_desc) - int(integer_asc))
    if len(integersum) == 3:
        integersum = '0' + integersum
        
    int1 = integersum
    if integersum != '6174':
        while (((int1[0] <= int1[1]) and (int1[1] <= int1[2]) and (int1[2] <= int1[3])) == False):
            if int1[1] < int1[0]:
                int1 = int1[1] + int1[0] + int1[2] + int1[3]
            if int1[2] < int1[1]:
                int1 = int1[0] + int1[2] + int1[1] + int1[3]
            if int1[3] < int1[2]:
                int1 = int1[0] + int1[1] + int1[3] + int1[2]

        integersum = int(integersum)
        integersum = str(integersum)
        nums_tracker += (integersum + ' > ')
        
        integer_asc = int1
        integer_desc = int1[::-1]



#print statements
if len(integer3) == 4:
    print('{} > {}{}'.format(integer3,nums_tracker[7:],6174))
    print("{} reaches 6174 via Kaprekar's routine in {} iterations".format(int(integer3),counter))

if len(integer3) == 3:
    print('{}{}'.format(nums_tracker[1:],6174))
    print("{} reaches 6174 via Kaprekar's routine in {} iterations".format(int(integer3),counter))

if len(integer3) == 2:
    print('{}{}'.format(nums_tracker[2:],6174))
    print("{} reaches 6174 via Kaprekar's routine in {} iterations".format(int(integer3),counter))

if len(integer3) == 1:
    print('{}{}'.format(nums_tracker[3:],6174))
    print("{} reaches 6174 via Kaprekar's routine in {} iterations".format(int(integer3),counter))





    
        
       
        
    
    
    



           
          



#sorted(e)
#[::-1] reverses the string 
    


