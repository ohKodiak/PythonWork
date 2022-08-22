# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:  Lab 4b_Act4
# Date:         1 October 2021


from math import *
import sys
determinant = 0
answer = 0
root1 = 0
root2 = 0

A = int(input('Please enter the coefficient A: '))
B = int(input('Please enter the coefficient B: '))
C = int(input('Please enter the coefficient C: '))
if A == 0 and B == 0:
    print('You entered an invalid combination of coefficients')
    sys.exit()
    

# vets to make sure quadratic is needed 
if (A == 0) and (B != 0) and (C != 0):
    root1 = -1 * (C/B)
    print('The root is x = {}'.format(root1))
    

#tells us if determinant is positive or negative
determinantTest = B**2 - 4*A*C

#gives us value of complex number if determinant is negative 
if determinantTest < 0:
    newcomplexnumber = sqrt(abs(determinantTest))
    
    
#gives us value of determinant if positive 

if determinantTest >= 0:
    determinant = sqrt(determinantTest)


#finding roots under normal circumstances 
if (A != 0) and (determinantTest >= 0):
    root1 = (-1*B + determinant) / (2*A)
    root2 = (-1*B - determinant) / (2*A)
    if root1 != root2:
      print('The roots are x = {:.1f} and x = {:.1f}'.format(root1,root2))
    if root1 == root2:
      print('The root is x = {:.1f}'.format(root1))
    
#finding roots under complex circumstances 
if (A != 0) and (determinantTest < 0):
    newB = -1*B / (2 * A)
    newCN = newcomplexnumber / (2 * A)
    print('The roots are x = {:.1f} + {:.1f}i and x = {:.1f} - {:.1f}i'.format(newB,newCN,newB,newCN))
    
    
    







    
    
    
    

    


    
    






