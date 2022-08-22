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


print('This code finds the remaining Radon-222 given the days, initial amount, and half - life')
days = float(input('Please enter the time elapsed (days): '))
initial = float(input('Please enter the initial amount (g): '))
half_life = 3.8
remaining = (initial) * (2**(-days/half_life))
print('Radon-222 left is {:.2f} g'.format(remaining))

