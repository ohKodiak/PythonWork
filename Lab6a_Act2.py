# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab6a_Act2
# Date:         13 October 2021

# Create and initialize variables
status = True # boolean, status of if integer is prime or not
i = 0 # iterator valuable
num = 0 # iterator variable
counter = 0 # int, counts the number of prime numbers


# Function to determine if number is prime
def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
            # used to determine if it was divisible by any previous integer -> if so, it's not prime
                status = False
    return status

# Print each number and if it is prime (using is_prime function)
for num in range(2,101):
    if is_prime(num) == True:
        print(num, 'is prime')
        counter += 1
    else:
        print(num,"is not prime")
        counter += 0

# Print results
print('There are', counter, 'prime numbers between 2 and 100')