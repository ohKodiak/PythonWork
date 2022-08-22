# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         YOUR TEAM NUMBER
# Assignment:   Lab 3a Activity 1
# Date:         20 September 2021


#f) taking in float input of degrees Celsius and converting to degrees Rankine
degreesC = float(input("Please enter the number of degrees Celsius to be converted to degrees Rankine: "))
print('{:.2f} degrees Celsius is equivalent to {:.2f} degrees Rankine'.format(degreesC, degreesC * (9/5) + 491.67))
