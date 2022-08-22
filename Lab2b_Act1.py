#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      ENGR 102-213
# Team:         TBA
# Assignment:   Lab 2b Activity Activity 1
# Date:         14 September 2021
from math import *
# Calculate the force in Newtons applied to an object with mass 2 kg and acceleration 5 m/s^2. 
#According to Newton’s    Second Law the net force applied to an object produces a proportional acceleration. 


#A) This code finds the Force of an object given the mass and the acceleration.
mass = 2 #kg
acceleration = 5 #m/s^2
force = mass * acceleration
print('Force is', force ,'N')


#B)Calculate the wavelength of x-rays scattering from a crystal lattice with a distance between 
#crystal layers of 0.025 nm, scattering angle of 25 degrees, and first order diffraction. 
#Bragg’s Lawdescribes the scattering of waves from a crystal using the equation

#B) This code finds the wavelength of an x-ray given the crystal layers, scattering angle, and order diffraction.
scattering_angle = 25 # degrees
crystal_layers = .025 # nm
wavelength = 2*(crystal_layers)*(sin(scattering_angle * (pi/180)))

print("Wavelength is", wavelength ,"nm")

#C) Calculate how much Radon-222 is left after 5 days of radioactive decay given an initial amount of 
# 3 g and a half-life of 3.8 days. The equation for radioactive decay is     
#𝑁𝑁(𝑡𝑡)=𝑁𝑁02−𝑡𝑡/𝑡𝑡1/2where 𝑁𝑁0 is the intial amount (units of grams), 𝑡𝑡 is the time (units of days), 
#and 𝑡𝑡1/2 is the half-life (units of days).

#C) This code finds the remaining Radon-222 given the days, initial amount amount, and half-life. 
days = 5
initial = 3 #g
half_life = 3.8 #days
remaining = (initial)*(2)**(-days/half_life)
print("Radon-222 left is", remaining , 'g' )

#D) Calculate the pressure of 5 moles of an ideal gas with a volume of 0.15 m^3, and temperature 
#of 425 K. The Ideal Gas Law is the equation of state of a hypothetical ideal gas and is a good 
#approximation of the behavior of gases under many conditions. Use a value of 8.314 m^3Pa/K·mol for the 
#gas constant. The standard unit of pressure in the SI system is kilopascals (kPa).
#Pressure is 117.78166666666667 kPa 

#D) This code finds the pressure of an ideal gas given moles, volume, and temperature.
moles = 5
temp = 425 #k
constant = .008314 #m^3Pa/K·mol 
volume = 0.15 #m^3
pressure = (moles * constant * temp)/volume
print("Pressure is", pressure , "kPa")



