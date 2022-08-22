# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab7b_Act3
# Date:         16 October 2021

from math import *
#initialize variables
a = input('Enter the elements for vector A: ')
b = input('Enter the elements for vector B: ')
lista = []
listb = []

#gets rid of spaces in strings
a1 = a.split(' ')
b1 = b.split(' ')

#adds input to lists as integers
for i in a1:
    lista.append(float(i))
    
for i in b1:
    listb.append(float(i))


if len(listb) == 3:
    
#function for magnitude
    def magnitude(vector):
        mag = sqrt((vector[0]**2) + (vector[1]**2) + (vector[2]**2))
        return mag

#function for addition
    def addition(vectorA,vectorB):
        x = vectorA[0] + vectorB[0]
        y = vectorA[1] + vectorB[1]
        z = vectorA[2] + vectorB[2]
        x1 = float(x)
        y1 = float(y)
        z1 = float(z)
        added = str(x1) + ', ' + str(y1) + ', ' + str(z1)
        return added

#function for subtraction
    def subtraction(vectorA,vectorB):
        x = vectorA[0] - vectorB[0]
        y = vectorA[1] - vectorB[1]
        z = vectorA[2] - vectorB[2]
        x1 = float(x)
        y1 = float(y)
        z1 = float(z)
        subtracted = str(x1) + ', ' + str(y1) + ', ' + str(z1)
        return subtracted

#function for dot product
    def dotproduct(vectorA,vectorB):
        x = vectorA[0] * vectorB[0]
        y = vectorA[1] * vectorB[1]
        z = vectorA[2] * vectorB[2]
        e = x + y + z
        e1 = float(e)
        dotproducted = e1
        return dotproducted

#print statements
    print('The magnitude of vector A is {:.4f}'.format(magnitude(lista)))
    print('The magnitude of vector B is {:.4f}'.format(magnitude(listb)))
    print('A + B is [{}]'.format(addition(lista,listb)))
    print('A - B is [{}]'.format(subtraction(lista,listb)))
    print('The dot product is {}'.format(dotproduct(lista,listb)))

##########If length is 4 ##########

if len(listb) == 4:
    
#function for magnitude
    def magnitude(vector):
        mag = sqrt((vector[0]**2) + (vector[1]**2) + (vector[2]**2) + (vector[3]**2))
        return mag

#function for addition
    def addition(vectorA,vectorB):
        x = vectorA[0] + vectorB[0]
        y = vectorA[1] + vectorB[1]
        z = vectorA[2] + vectorB[2]
        e = vectorA[3] + vectorB[3]
        x1 = float(x)
        y1 = float(y)
        z1 = float(z)
        e1 = float(e)
        added = str(x1) + ', ' + str(y1) + ', ' + str(z1) + ', ' + str(e1)
        return added

#function for subtraction
    def subtraction(vectorA,vectorB):
        x = vectorA[0] - vectorB[0]
        y = vectorA[1] - vectorB[1]
        z = vectorA[2] - vectorB[2]
        e = vectorA[3] - vectorB[3]
        x1 = float(x)
        y1 = float(y)
        z1 = float(z)
        e1 = float(e)
        subtracted = str(x1) + ', ' + str(y1) + ', ' + str(z1) + ', ' + str(e1)
        return subtracted

#function for dot product
    def dotproduct(vectorA,vectorB):
        x = vectorA[0] * vectorB[0]
        y = vectorA[1] * vectorB[1]
        z = vectorA[2] * vectorB[2]
        e = vectorA[3] * vectorB[3]
        s = x + y + z + e
        s1 = float(s)
        dotproducted = s1
        return dotproducted

#print statements
    print('The magnitude of vector A is {:.4f}'.format(magnitude(lista)))
    print('The magnitude of vector B is {:.4f}'.format(magnitude(listb)))
    print('A + B is [{}]'.format(addition(lista,listb)))
    print('A - B is [{}]'.format(subtraction(lista,listb)))
    print('The dot product is {}'.format(dotproduct(lista,listb)))
    
######################## if length of vector is 5

if len(listb) == 5:
    
#function for magnitude
    def magnitude(vector):
        mag = sqrt((vector[0]**2) + (vector[1]**2) + (vector[2]**2) + (vector[3]**2) + (vector[4]**2))
        return mag

#function for addition
    def addition(vectorA,vectorB):
        x = vectorA[0] + vectorB[0]
        y = vectorA[1] + vectorB[1]
        z = vectorA[2] + vectorB[2]
        e = vectorA[3] + vectorB[3]
        a = vectorA[4] + vectorB[4]
        x1 = float(x)
        y1 = float(y)
        z1 = float(z)
        e1 = float(e)
        a1 = float(a)
        added = str(x1) + ', ' + str(y1) + ', ' + str(z1) + ', ' + str(e1) + ', ' + str(a1)
        return added

#function for subtraction
    def subtraction(vectorA,vectorB):
        x = vectorA[0] - vectorB[0]
        y = vectorA[1] - vectorB[1]
        z = vectorA[2] - vectorB[2]
        e = vectorA[3] - vectorB[3]
        a = vectorA[4] - vectorB[4]
        x1 = float(x)
        y1 = float(y)
        z1 = float(z)
        e1 = float(e)
        a1 = float(a)
        subtracted = str(x1) + ', ' + str(y1) + ', ' + str(z1) + ', ' + str(e1) + ', ' + str(a1)
        return subtracted

#function for dot product
    def dotproduct(vectorA,vectorB):
        x = vectorA[0] * vectorB[0]
        y = vectorA[1] * vectorB[1]
        z = vectorA[2] * vectorB[2]
        e = vectorA[3] * vectorB[3]
        a = vectorA[4] * vectorB[4]
        s = x + y + z + e + a
        s1 = float(s)
        dotproducted = s1
        return dotproducted

#print statements
    print('The magnitude of vector A is {:.4f}'.format(magnitude(lista)))
    print('The magnitude of vector B is {:.4f}'.format(magnitude(listb)))
    print('A + B is [{}]'.format(addition(lista,listb)))
    print('A - B is [{}]'.format(subtraction(lista,listb)))
    print('The dot product is {}'.format(dotproduct(lista,listb)))






    
    