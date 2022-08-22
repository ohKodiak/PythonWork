# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         YOUR TEAM NUMBER
# Assignment:   Lab 3a Activity 1
# Date:         20 September 2021


#c) taking in float input of atmospheres and converting to millimeters of mercury
atmospheres = float(input("Please enter the number of atmospheres to be converted to millimeters of mercury: "))
print('{:.2f} atmospheres is equivalent to {:.2f} millimeters of mercury'.format(atmospheres, atmospheres * 760))