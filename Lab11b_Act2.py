# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 11b Act2
# Date:         11/28/21
from random import *
counter = 1
#counter has to start at 1

def introduction():
    ''' generates random number, introduces rules to player '''
    # number is made a global variable so that it can be referenced both in every function and in the main body code
    global number
    number = randint(1,100)
    print('Howdy! Welcome to the Aggie Guessing Game! This program has selected a number between 1 and 100. \nTry to guess the number by entering numbers. You will be given a hint if you are wrong!')
  
def game():
    '''checks if the user guessed wrong, gives advice'''
    #prints wrong guess everytime called 
    if numberguessed != number:
        print('Wrong guess!')
        if numberguessed > number:
            print('Your guess was too high')
        if numberguessed < number:
            print('Your guess was too low!')
        
def ending():
    '''congratulates user, gives the number of attempts '''
    print('WHOOP! You guessed the number!')
    print('It only took you {} tries!'.format(counter))
    # takes counted number of iterations and inserts into print statements

introduction()
numberguessed = int(input('Please enter a number between 1 and 100: '))
#while loop checks if guess is right, calls game function, tells user to try again, counts number of iterations.
while numberguessed != number:
    game()
    numberguessed = int(input('Try again! Enter another number: '))
    counter += 1

ending()

    



