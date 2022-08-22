# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab4a_Act2
# Date:         26 September 2021
#

# Create and initialize variables
A = 0 # int
B = 0 # int
C = 0 # int
string_A = '' # string
string_B = '' # string
string_C = '' # string
sign_A = '' # string
sign_B = '' # string
sign_C = '' # string

# Input values
A = int(input('Please enter the coefficient A: '))
B = int(input('Please enter the coefficient B: '))
C = int(input('Please enter the coefficient C: '))

# if all values are 0, there is no quadratic equation
if ((A == 0) and (B == 0) and (C == 0)):
    print('There is no quadratic equation.')
    
# A-block
# no ax^2 term needed if a equals 0, so blank string created
if A == 0:
    string_A = ''
else:
    # adds negative sign if needed (A does not need + sign)
    if A < 0:
        sign_A = '- '
    else:
        sign_A = ''
    # finds absolute value of A
    # (sign already determined and added into the string if necessary)
    if A < 0:
        A = -A
    # if A equals 1, no need for the number 1, so make the string blank
    if A == 1:
        A = ''
    A = str(A)
    # combines strings to make the correct ax^2 term
    string_A = ' ' + sign_A + A + 'x^2'

# B-block
# no bx term needed if b equals 0, so blank string created
if B == 0:
    string_B = ''
else:
    # adds correct sign to B (positive or negative)
    if B < 0:
        sign_B = ' - '
    elif B > 0:
        # checks to make sure that there is an A term
        # if not, no plus sign is needed
        if (A != 0):
            sign_B = ' + '
        else:
            sign_B = ' '        
    else:
        sign_B = ''
    # finds absolute value of B
    # (sign already determined and added into the string if necessary)
    if B < 0:
        B = -B
    # if B equals 1, no need for the number 1, so make the string blank
    if B == 1:
        B = ''
    B = str(B)
    # combines strings to make the correct bx term
    string_B = sign_B + B + 'x'

# C-block
# no c term needed if c equals 0, so blank string created
if C == 0:
    string_C = ''
else:
    # adds correct sign to C (positive or negative)
    if C < 0:
        sign_C = ' - '
    elif C > 0:
        # checks to make sure that there is an A or B term
        # if not, no plus sign is needed
        if ((A != 0) or (B != 0)):
            sign_C = ' + '
        else:
            sign_C = ' '
    else:
        sign_C = ''
    # finds absolute value of C
    # (sign already determined and added into the string if necessary)
    if C < 0:
        C = -C
    C = str(C)
    # combines strings to make the correct c term
    string_C = sign_C + C

# Print results if there is a quadratic equation (if a, b, or c are nonzero)
if ((A != 0) or (B != 0) or (C != 0)):
    print('The quadratic equation is{}{}{} = 0'.format(string_A, string_B, string_C))