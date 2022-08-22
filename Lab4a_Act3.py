# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab4a_Act3
# Date:         26 September 2021


########### Part A ###########

a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

#variable a
if a == "True" or a == "T" or a == "t":
    a = True
elif a == "False" or a == "F" or a == "f":
    a = False
else:
    print("Invalid input for a")

#variable b
if b == "True" or b == "T" or b == "t":
    b = True
elif b == "False" or b == "F" or b == "f":
    b = False
else:
    print("Invalid input for b")

#variable c
if c == "True" or c == "T" or c == "t":
    c = True
elif c == "False" or c == "F" or c == "f":
    c = False
else:
    print("Invalid input for c")

########### Part B ###########

print("a and b and c:", a and b and c)
print("a or b or c:", a or b or c)

########### Part C ###########

XOR = (a and (not b)) or (b and (not a))
justa = a and (not (b or c))
justb = b and (not (a or c))
justc = c and (not (a or b))

print("XOR:", XOR)
print("Odd number:", (a and b and c) or justa or justb or justc)

########### Part D ###########

complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
complex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simple1 = (not b) or ((not a) and (not c))
simple2 = ((not b) and c) or (a and b) or (a and (not c))

print("Complex 1:", complex1)
print("Complex 2:", complex2)
print("Simple 1:", simple1)
print("Simple 2:", simple2)