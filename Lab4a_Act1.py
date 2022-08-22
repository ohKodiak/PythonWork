# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab4a_Act1
# Date:         28 September 2021

from math import *

# Create and initialize variables
parking_fee = 0.0 # dollars, float
total_hours_parked = 0.0 # float
input_total_hours_parked = 0.0 # float
days_parked = 0
hours_parked = 0

# print what user should input
print('Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.')

# User input
input_total_hours_parked = float(input('Please enter the hours parked: '))

# lost ticket charge
if input_total_hours_parked < 0:
  parking_fee += 36.00
  total_hours_parked = input_total_hours_parked * -1 # make it positive
else:
  total_hours_parked = input_total_hours_parked

# rounds up decimal hours
total_hours_parked = ceil(total_hours_parked)

#seperates the hours from the days (for charges more than 1 day)
days_parked = total_hours_parked // 24
additional_hours_parked = total_hours_parked - (24 * days_parked)

# whole day charge
if days_parked >= 1:
  parking_fee += 24.00 * days_parked

# maximum daily charge
if additional_hours_parked >= 21:
  parking_fee += 24.00
# not maximum daily charge
else:
  if additional_hours_parked == 0:
    parking_fee += 0
  # for additional hours between 0 - 2
  elif additional_hours_parked <= 2:
    parking_fee += 4.00
  # for additional hours between 3 - 4 ($4 + $3 = $7)
  elif additional_hours_parked <= 4:
    parking_fee += 7.00
  # for additional hours between 4 - 20 ($4 + $3 + $1 for each extra hour)
  else:
    parking_fee += 1 * (additional_hours_parked - 4) + 7.00

#outputs parking fee based on time parked
print("Parking for {} hours please pay ${:.0f}".format(input_total_hours_parked, parking_fee))
