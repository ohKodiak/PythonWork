#Ezra Jeter
#Phys 216 509
#2/7/21
#Homework 6 


#homework6.py
import numpy as np
from math import *


########### Problem 1 ########### 
A1 = np.array([3.5,-2,4,-1,0,6,-2.4,8,-2,0,0,5,3,-4.7,1,0]).reshape(4,4)
print('A =\n', A1)
print('Compute determinant of A: det(A) =', np.linalg.det(A1))

b1 = np.array([12,-15,7,5]).reshape(4,1) # create column vector b: 3 rows, 1 column
print('b =\n', b1)
print()
xyzw = np.linalg.solve(A1,b1) # variable xyz represents column vector x in Ax=b
print('xyzw =\n', xyzw) # column vector: 3 rows, 1 column
print('x =', xyzw[0][0])
print('y =', xyzw[1][0])
print('z =', xyzw[2][0])
print('w =', xyzw[3][0]) 

########### Problem 2 ########### 

A1 = np.array([6,-2,-15,5]).reshape(2,2)
print('A =\n', A1)
print('Compute determinant of A: det(A) =', np.linalg.det(A1))




########### Problem 3 ########### 

A2 = np.array([2,1,4,1,-1,5,2,4,-2]).reshape(3,3)
print('A =\n', A2)
print('Compute determinant of A: det(A2) =', np.linalg.det(A2))

b1 = np.array([2,-2,8]).reshape(3,1) # create column vector b: 3 rows, 1 column
print('b =\n', b1)
print()
#xyzw = np.linalg.solve(A1,b1) # throws error 


########### Problem 4 ########### 

A1 = np.array([0.04,0.08,0.96,0.92]).reshape(2,2)
print('A =\n', A1)
#print('Compute determinant of A: det(A) =', np.linalg.det(A1))

b1 = np.array([75.25,1156.25]).reshape(2,1) # create column vector b: 3 rows, 1 column
print('b =\n', b1)
print()
xy = np.linalg.solve(A1,b1) # variable xyz represents column vector x in Ax=b

print('xyzw =\n', xy) # column vector: 3 rows, 1 column
print('B1 =', xy[0][0])
print('B2 =', xy[1][0]) 

########### Problem 5 ########### 



#############
A1 = np.array([.20,.25,.35,1,0,1,.80,.75,.65]).reshape(3,3)
print('A =\n', A1)


b1 = np.array([123.5,171,389.5]).reshape(3,1) # added 18% moisture and 38 removed together for moisture, used 475 - 475(2/3) for second
print('b =\n', b1)
print()
xyz = np.linalg.solve(A1,b1) 

print('xyz  =\n', xyz) 
print('Wet Oats =', xyz[0][0])
print('Wet Corn =', xyz[1][0])
print('Barley =', xyz[2][0])  




