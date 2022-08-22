# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         YOUR TEAM NUMBER
# Assignment:   Lab 3b-activity 2
# Date:         21 September 21


from math import *
area = float(input('Please enter the area: '))

#Finds radius of circle given area
def radius(area):
    radius = sqrt(area/pi)
    return radius

print('A circle with area {:.2f} has a radius {:.3f}'.format(area, radius(area)))


#Finds the length of the side of a equilateral triangle given the area
def eside(area):
    side_length = (2/3) * (3 ** (3/4)) * (sqrt(area))
    return side_length

print('An equilateral triangle with area {:.2f} has a side {:.3f}'.format(area, eside(area)))


#Finds length of side of square given the area
def sside(area):
    side_length_for_square = sqrt(area)
    return side_length_for_square

print('A square with area {:.2f} has a side {:.3f}'.format(area, sside(area)))



def pside(area):
    squareof20 = sqrt(20)
    part_one = 2*(5**(3/4))
    part_two = sqrt(area)
    part_three = 5* (( squareof20 +5 )**(1/4))     
    side_length_for_pentagon = (part_one * part_two) / part_three
    return side_length_for_pentagon

print('A pentagon with area {:.2f} has a side {:.3f}'.format(area, pside(area)))


def dside(area):
    side_length_for_dod = sqrt((area) / ((sqrt(3) + 2) * 3))
    return side_length_for_dod

print('A dodecagon with area {:.2f} has a side {:.3f}'.format(area, dside(area)))


