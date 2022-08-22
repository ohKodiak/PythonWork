# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      ENGR 102-213
# Team:         TBA
# Assignment:   Lab 3b Activity #1c
# Date:         20 September 2021
from math import *

#This code takes days initial amount as inputted values, and plugs them into the half life equation.
print('This program calculates how much Radon-222 is left given time and initial amount')
days = float(input('Please enter the time (days): '))
initial = float(input('Please enter the initial amount (g): '))
half_life = 3.8
remaining = (initial) * (2**(-days/half_life))
print('Radon-222 left is {:.2f} g'.format(remaining))

