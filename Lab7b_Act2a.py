# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab8_Act1_EJ
# Date:         29 October 2021


import sys 


temperature = input('Enter a temperature between 0 and 260 deg C: ')

valid_characters = '0123456789.-'

for i in temperature:
    if i not in valid_characters:
        print('Please enter a number.')
        sys.exit()
    
temperature = float(temperature)


if temperature <= 0:
    print('Please enter a temperature greater than 0.')
    sys.exit()
if temperature >= 260:
    print('Please enter a temperature less than 260.')
    sys.exit() 





    
    
    

