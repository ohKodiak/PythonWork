
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab6a_Act1a
# Date:         8 October 2021

from math import *

# Create and initialize variables
side_length = 0.0 # float
layers = 0 # int
gold_foil_SA = 0.0 # surface area in square meters, float
top_layer_SA = 0.0 # surface area in square meters, float
edge_cubes = 0 # number of cubes on edge of layer (not including corners), int
CORNER_CUBES = 4 # number of cubes in corner of layer, int
side_SA = 0.0 # surface area of a side in square meters, float
layer_num = 0 # int


# User input
side_length = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))


# Calculations
side_SA = (side_length ** 2)

# Creates top layer
top_layer_SA = side_SA * 5 # five exposed sides on top cube
gold_foil_SA += top_layer_SA

# For the rest of the layers
for layer_num in range(2, (layers + 1)):
  gold_foil_SA += edge_cubes * side_SA * 1.5
  gold_foil_SA += CORNER_CUBES * side_SA * 2.75
  edge_cubes += 4
  

# Print results
print('You need {:.2f} square meters of gold foil to cover the pyramid'.format(gold_foil_SA))
