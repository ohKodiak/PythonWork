# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 11b Act 1 b
# Date:         11/28/21

from math import *
#partB
def partb(list1,list2,list3):
    ''' this function finds the prfit by subtracting the cost from the assets, and then pairs the max with its company '''
    length = len(list1)
    list_of_profits = []
    # loop that finds profit of each company and adds to list
    for i in range(length):
        list_of_profits.append(list3[i] - list2[i])
    # loop that finds max profits and locates company that corresponds with that highest profit
    for i in range(len(list_of_profits)):
        if list_of_profits[i] == max(list_of_profits):
            highest_earning = list1[i]
    return highest_earning, max(list_of_profits)
    
