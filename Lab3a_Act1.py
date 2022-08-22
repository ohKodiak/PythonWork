# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         YOUR TEAM NUMBER
# Assignment:   Lab 3a Activity 1
# Date:         20 September 2021


#a) taking in float input of pounds and converting to Newtons 
pounds = float(input("Please enter the number of pounds to be converted to Newtons: "))
print('{:.2f} pounds is eqivalent to {:.2f} Newtons'.format(pounds, pounds * 4.45))

#b) taking in float input of kilometers and converting to miles
kilometers = float(input("Please enter the number of kilometers to be converted to miles: "))
print('{:.2f} kilometers is eqivalent to {:.2f} miles'.format(kilometers, kilometers * 1.69))

#c) taking in float input of atmospheres and converting to millimeters of mercury
atmospheres = float(input("Please enter the number of atmospheres to be converted to millimeters of mercury: "))
print('{:.2f} atmospheres is eqivalent to {:.2f} millimeters of mercury'.format(atmospheres, atmospheres * 760))

#d taking in float input of watts and converting to BTU per hour
watts = float(input("Please enter the number of watts to be converted to BTU per hour: "))
print('{:.2f} watts is eqivalent to {:.2f} BTU per hour'.format(watts, watts * 3.41))

#e  taking in float input of liters per second and converting to gallons per minute
liters = float(input("Please enter the number of liters per second to be converted to gallons per minute: "))
print('{:.2f} liters is eqivalent to {:.2f} gallons per minute'.format(liters, liters * 15.85))

#f) taking in float input of degrees Celsius and converting to degrees Rankine
degreesC = float(input("Please enter the number of degrees Celcius to be converted to degrees Rankine: "))
print('{:.2f} degrees Celcius is eqivalent to {:.2f} degrees Rankine'.format(degreesC, degreesC * (9/5) + 491.67))

