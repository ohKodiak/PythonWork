# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         YOUR TEAM NUMBER
# Assignment:   Lab 3a Activity 1
# Date:         20 September 2021


#e  taking in float input of liters per second and converting to gallons per minute
liters = float(input("Please enter the number of liters per second to be converted to gallons per minute: "))
print('{:.2f} liters per second is equivalent to {:.2f} gallons per minute'.format(liters, liters * 15.8503))
