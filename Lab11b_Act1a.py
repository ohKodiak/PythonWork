# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 11b Act 1a
# Date:         11/28/21
from math import *

#part A
def parta(length,width,height,radius):
    '''finds volume of cube and subtracts volume of hole from that'''
    prismvolume = length * width * height
    holevolume = pi * (radius**2) * height
    volumeleft = prismvolume - holevolume
    #when radius overlaps the length or the length, you actually subtract too much volume from the cube, so you have to find the volume 
    #of the overlap and add it back to the volume left
    if radius > length/2:
        overlap = 2 * ((acos(length/(2*radius))) * (radius**2) - (((radius **2)/2)*sin(2*acos(length/(2*radius)))))
        volumeleft = volumeleft + overlap
    if radius > length/2 :
        overlap = 2 * ((acos(length/(2*radius))) * (radius**2) - (((radius **2)/2)*sin(2*acos(length/(2*radius)))))
        volumeleft = volumeleft + overlap
    # if the hole engulfs the the cube, the volume left is 0
    if 2*radius > sqrt(width**2 + length**2):
        volumeleft = 0

    return volumeleft

