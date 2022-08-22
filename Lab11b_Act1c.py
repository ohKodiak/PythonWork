# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 11b Act1c
# Date:         11/28/21
from math import *
#part c

#mailing labels are arranged in the following order: name, address, city, state, zipcode
def partc(name,city,state,zipcode,address):
    ''' this function makes a mailing label from given info '''
    label = '{}\n{}\n{}, {} {}'.format(name,address,city,state,zipcode)
    # uses format statement to insert inputted info into the mailing label template
    return label 
