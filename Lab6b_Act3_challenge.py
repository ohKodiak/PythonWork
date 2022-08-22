# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab6b_Act3 challenge
# Date:         13 October 2021

#import module
from math import *
#initialize variables 
counter = 0
#loop to insert numbers from 1-1000
for i in range(1,10000):
    integer = str(i)
    if integer == '6174':
        continue
    
    if len(integer) == 1:
        integer = '000' + integer
    if len(integer) == 3:
        integer = '0' + integer
    if len(integer) == 2:
        integer = '00' + integer
    

    
    
                       
# puts numbers into ascending order

    while (((integer[0] <= integer[1]) and (integer[1] <= integer[2]) and (integer[2] <= integer[3])) == False):
        if integer[1] < integer[0]:
            integer = integer[1] + integer[0] + integer[2] + integer[3]
        if integer[2] < integer[1]:
            integer = integer[0] + integer[2] + integer[1] + integer[3]
        if integer[3] < integer[2]:
            integer = integer[0] + integer[1] + integer[3] + integer[2]
   #initialize more variables inside of my loop 
    number = ''

    counter1 = 0
    intcopy = ''
    integercopy = integer
    integer_asc = integer
    integer_desc = integer[::-1]
    integersum = 0
    
    
#loop that does the math
    while integersum != '6174' and integer != 6174:
        integersum = str(int(integer_desc) - int(integer_asc))
        counter += 1
     
        if len(integersum) == 3:
            integersum = '0' + integersum
        if len(integersum) != 4:

            break
        int1 = integersum
        if integersum != '6174':
            while (((int1[0] <= int1[1]) and (int1[1] <= int1[2]) and (int1[2] <= int1[3])) == False):
                if int1[1] < int1[0]:
                    int1 = int1[1] + int1[0] + int1[2] + int1[3]
                if int1[2] < int1[1]:
                    int1 = int1[0] + int1[2] + int1[1] + int1[3]
                if int1[3] < int1[2]:
                    int1 = int1[0] + int1[1] + int1[3] + int1[2]
    
            
            integer_asc = int1
            integer_desc = int1[::-1]


print("Kaprekar's routine takes {} total iterations for all four-digit numbers".format(counter))




    





