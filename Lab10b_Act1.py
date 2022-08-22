# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 10b Act1
# Date:         17 November 21

#imports modules

import numpy as np
import matplotlib.pyplot as plt

#creates matrix
A = np.matrix('1,0')
B = np.matrix('1.00583,-0.087156; 0.087156, 1.00583')

#initializes empty lists
x_ = []
y_ = []

#loop that multiplies and stores values
for i in range(250):
    A = A@B
    print(A)
    x_.append(A.item(0))
    y_.append(A.item(1))

#plots graph
plt.plot(x_,y_)
plt.title('My Spiral Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()




    
    
