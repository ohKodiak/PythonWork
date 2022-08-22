#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      ENGR 102-213
# Team:         TBA
# Assignment:   Lab 1b Activity #3
# Date:         5 September 2021


from math import *
#Write a program named Lab1b_Act3.pythat performs the following tasks for the 
#function𝑓𝑓(𝑥𝑥)=(𝑒𝑒𝑥𝑥−1)/𝑥𝑥 evaluated close to 𝑥𝑥= 0. Use values of 𝑥𝑥 ranging from 1   to 10−7 in steps 
#of 1/10 of the previous value (𝑥𝑥= 1, 𝑥𝑥= 0. 1, 𝑥𝑥= 0. 01...). 


#First, print a line of text stating the purpose of the program2)
#Next, print a line of text stating your guess for the final calculated value.
#a).There are no wrong answers, just make a guess
#b.Think about the answer then see if your guess was close
#3)Next, print out a sequence of 8 numbers, representing evaluating the function at 8 different values
#4)Finally, print one blank line, followed by a statement of how good your guess is


#As an example, for the equation 𝑓𝑓(𝑥𝑥)= tan(𝑥𝑥)/𝑥𝑥 evaluated close to 𝑥𝑥= 0, 
#your output would look like what’s shown below. Make sure your code evaluates 𝑓𝑓(𝑥𝑥)=(𝑒𝑒𝑥𝑥−1)/𝑥𝑥 . 

print("This shows the evaluation of (e^x-1)/x evaluated close to x=0")
print("My guess is 2.13456787654356")
print((((pow(e,1))-1)/1))
print((((pow(e,.1))-1)/.1))
print((((pow(e,.01))-1)/.01))
print((((pow(e,.001))-1)/.001))
print((((pow(e,.0001))-1)/.0001))
print((((pow(e,.00001))-1)/.00001))
print((((pow(e,.000001))-1)/.000001))
print((((pow(e,.0000001))-1)/.0000001))
print('')
print("My guess was more accurate than I expected.")