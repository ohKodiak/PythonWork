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

#This program takes inputted values for mass and acceleration, and puts them into the force equation.
print('This program calculates the applied force given mass and acceleration')
mass = float(input('Please enter the mass (kg): '))
acceleration = float(input('Please enter the acceleration (m/s^2): '))
force = mass * acceleration
print('Force is {:.1f} N'.format(force))

