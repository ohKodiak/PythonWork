# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab7b_Act2
# Date:         16 October 2021

#initialize variables
stock_prices = ''
list1 = []
list2 = []


#get inpput, add to string
stock_prices = input('Enter three or more prices separated by spaces: ').split()
list1 = stock_prices[:]

# add to liist as floats
for i in list1:
    list2.append(float(i))

#print, with right side justification
for price in stock_prices:
    print('$', price.rjust(6))


    
    
    


