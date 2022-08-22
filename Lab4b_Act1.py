# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:  Lab 4b_Act1
# Date:         1 October 2021
import sys
#Activity 1
#each variable is assigned a corresponding input value
one = float(input('Enter number 1: '))
two = float(input('Enter number 2: '))
three = float(input('Enter number 3: '))

#if branches
#finds smallest value and prints it




    
#if one is the smallest number 
if (one <= two) and (one <= three):
    print('The smallest number is',float(one))
    
#if two is the smallest number 
if ((two < one) and (two <= three)) and (two != one) :
    print('The smallest number is',float(two))
    
#if three is the smallest number
if ((three < two) and (three < one)) and ((three != one) and (three != two)):
    print('The smallest number is',float(three))
    
    