#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         YOUR TEAM NUMBER
# Assignment:   Lab 2b Activity #3
# Date:         9/10/21
from math import *
#Part 1
print("Part 1:")
#This program takes 2 coordinates and one time input, then outputs the distance of 
#the satellite from Houston.
coordinate1 = (10,2025)
coordinate2 = (55,23025)
#X is the time input.
x = 25
slope_of_given_points = (coordinate2[1]-coordinate1[1])/(coordinate2[0]-coordinate1[0])
position = coordinate1[1]+(x-coordinate1[0])*(slope_of_given_points)
print("For t =", x ,"minutes, the position p =",position ,"kilometers")

#Part2
print("Part 2:")
#This program takes 2 coordinates and one time input outside of linear interpolation , then outputs
#the distance of that satellite from Houston. 
coordinate1 = (10,2025)
coordinate2 = (55,23025) 
x = 5.0
#x is given in hours, must be converted to minutes.
new_x = x * 60
circumference_of_orbit = 6745 * 2 * pi
slope_of_given_points = (coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0])
position = coordinate1[1] + (new_x-coordinate1[0]) * (slope_of_given_points)
new_position = position % circumference_of_orbit
print("For t =", x ,"hours,","the position p =",new_position , "kilometers")



        
    




#Part 1: For t = 25 minutes, the 
#position p = 9025.0 kilometers 
#Part 2: For t = 5.0 hours, 
#the position p = 10218.078642554414 kilometers 