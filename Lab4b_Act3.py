# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:  Lab 4b_Act3
# Date:         1 October 2021


import sys
from math import *
#inputs days
day = int(input('Please enter a positive value for day: '))
#if days is less than 11
if day < 0:
    print('You entered an invalid number!')
    sys.exit()
#if days is less than 11
if (day >= 0) and (day <= 10):
    widgets = day * 10
#if days is between 11 and 49 inclusive
if (day > 10) and (day <= 50):
    widgets = 100 + ((day - 10)*(day + 11)) /2
#if days is between 50-100 inclusive
if (day > 50) and (day <101):
    widgets = 1270 + ((day-49) * 50)
#if days is greater than 101 inclusive 
if day == 101:
    widgets = 1270 + ((day-50) * 50)
if day > 101:
    widgets = 3820

    
print('The total number of widgets produced on day {} is {:.0f}'.format(day,widgets))
    

    

    



