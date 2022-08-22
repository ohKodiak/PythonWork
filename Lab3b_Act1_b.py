# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      ENGR 102-213
# Team:         TBA
# Assignment:   Lab 3b Activity #1b
# Date:         20 September 2021
from math import *

#This program takes in the scattering angle, crystal_layers, and wavelength as inputted values, and puts them into the wavelength formula.
print('This program calculates the wavelength given distance and angle')
crystal_layers = float(input('Please enter the distance (nm): '))
scattering_angle = float(input('Please enter the angle (degrees): '))
wavelength = 2 * (crystal_layers) * (sin(scattering_angle * (pi/180)))
print('Wavelength is {:.4f} nm'.format(wavelength))