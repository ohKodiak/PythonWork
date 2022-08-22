# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 11b Act 1f
# Date:         11/28/21
from math import *

def partf(timeslist, listdistance):
    '''finds velocity of each interval by using distance over time '''
    listspeeds = []
    #iterates through number of items in list
    #finds distance travelled by subtracting distance at point x from distance at point x+1 
    # v = d/t
    for i in range(len(timeslist)):
        if timeslist[i] != timeslist[-1]:
            distance = listdistance[i + 1] - listdistance[i]
            time = timeslist[i + 1] - timeslist[i]
            velocity = distance / time
            listspeeds.append(velocity)
    return listspeeds