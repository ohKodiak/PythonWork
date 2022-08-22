# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      ENGR 102-213
# Team:         TBA
# Assignment:   Lab 3b Activity #1a
# Date:         20 September 2021
from math import *

#This code takes in moles, volume, and temperature as inputted values and plugs them into the ideal gas law equation.
print('This program calculates the pressure given moles, volume, and temperature')
moles = float(input('Please enter the number of moles: '))
volume = float(input('Please enter the volume (m^3): '))
temp = float(input('Please enter the temperature (K): '))
constant = .008314
pressure = (moles * constant * temp)/volume
print('Pressure is {:.0f} kPa'.format(pressure))


