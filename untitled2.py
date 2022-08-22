import numpy as np
from math import sqrt

with open('module11activity.txt','r') as stuff:
    numbers = stuff.read()
    
numbers.strip()
new_numbers = numbers.split('\n')

for i in range(len(new_numbers)):
    new_numbers[i] = int(new_numbers[i])
    
a = np.matrix([new_numbers]).reshape(100,100)

# i cannot figure out how to index through a matrix 

shift_right = 0
num = a[6,-5:]
for i in num:
    shift_right += i
    

print(shift_right)

number2 = a[25,:]

