# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab5a_Act2
# Date:         06 October 2021

from math import *

# Create and initialize variables
sex = '' # string
age = 0 # int
smoking_status = True # smoker or nonsmoker, bool
total_cholesterol = 0 # int
hdl = 0 # HDL cholesterol (mg/dL), int
systolic_bp = 0 # systolic blood pressure (mmHg), int
treated_status = True # treated or untreated, bool
points_total = 0 # int
ten_year_risk = 0.0 # in percent, float

sex = (input('Enter your sex (M/F): '))
age = int(input('Enter your age (years): '))
smoking_status = input('Do you smoke cigarettes (Y/N)? ')
#total cholesterol 
total_cholesterol = int(input('Enter your total cholesterol (mg/dL): '))
hdl = int(input('Enter your HDL cholesterol (mg/dL): '))
#systolic blood pressure
systolic_bp =  int(input('Enter your systolic BP (mmHg): '))
#blood pressure medication
treated_status = input('Are you taking blood pressure medication (Y/N)? ')

# preliminary input conversions for smoking status, and treated status to booleans

if smoking_status == 'Y' or smoking_status == 'y':
  smoking_status = True
if smoking_status == 'N' or smoking_status == 'n':
  smoking_status = False

if treated_status == 'Y' or treated_status == 'y':
  treated_status = True
if treated_status == 'N' or treated_status == 'n':
  treated_status = False

# Male Branch
if sex == 'M' or sex == 'm':
  # Age sub branch
  if age >= 20 and age <= 34:
    points_total += -9
  elif age <= 39:
    points_total += -4
  elif age <= 44:
    points_total += 0
  elif age <= 49:
    points_total += 3
  elif age <= 54:
    points_total += 6
  elif age <= 59:
    points_total += 8
  elif age <= 64:
    points_total += 10
  elif age <= 69:
    points_total += 11
  elif age <= 74:
    points_total += 12
  else:
    points_total += 13
    
  # Cholesterol sub branch
  if age < 40:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 4
    elif total_cholesterol < 240:
      points_total += 7
    elif total_cholesterol < 280:
      points_total += 9
    else:
      points_total += 11
  elif age < 50:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 3
    elif total_cholesterol < 240:
      points_total += 5
    elif total_cholesterol < 280:
      points_total += 6
    else:
      points_total += 8
  elif age < 60:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 2
    elif total_cholesterol < 240:
      points_total += 3
    elif total_cholesterol < 280:
      points_total += 4
    else:
      points_total += 5
  elif age < 70:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 1
    elif total_cholesterol < 240:
      points_total += 1
    elif total_cholesterol < 280:
      points_total += 2
    else:
      points_total += 3
  elif age < 80:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 0
    elif total_cholesterol < 240:
      points_total += 0
    elif total_cholesterol < 280:
      points_total += 1
    else:
      points_total += 1
    
  # Smoking status sub branch
  if smoking_status == False:
    points_total += 0
  if smoking_status == True:
    if age >= 20 and age <=39:
      points_total += 8
    elif age <= 49:
      points_total += 5
    elif age <= 59:
      points_total += 3
    else:
      points_total += 1

  # HDL sub branch
  if hdl >= 60:
    points_total -= 1
  elif (hdl >= 50) and (hdl <= 59):
    points_total = points_total
  elif (hdl >= 40) and (hdl <= 49):
    points_total += 1
  elif (hdl < 40):
    points_total += 2

  # Systolic BP sub branch
  if treated_status == False:
    if systolic_bp < 120:
      points_total += 0
    elif systolic_bp <= 129:
      points_total += 0
    elif systolic_bp <= 139:
      points_total += 1
    elif systolic_bp <= 159:
      points_total += 1
    elif systolic_bp >= 160:
      points_total += 2
  if treated_status == True:
    if systolic_bp < 120:
      points_total += 0
    elif systolic_bp <= 129:
      points_total += 1
    elif systolic_bp <= 139:
      points_total += 2
    elif systolic_bp <= 159:
      points_total += 2
    elif systolic_bp >= 160:
      points_total += 3


# Female Branch
if sex == 'F' or sex == 'f':
  if age >= 20 and age <= 34:
    points_total += -7
  elif age <= 39:
    points_total += -3
  elif age <= 44:
    points_total += 0
  elif age <= 49:
    points_total += 3
  elif age <= 54:
    points_total += 6
  elif age <= 59:
    points_total += 8
  elif age <= 64:
    points_total += 10
  elif age <= 69:
    points_total += 12
  elif age <= 74:
    points_total += 14
  elif age <= 79:
    points_total += 16

# Cholesterol sub branch
  
  if age < 40:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 4
    elif total_cholesterol < 240:
      points_total += 8
    elif total_cholesterol < 280:
      points_total += 11
    else:
      points_total += 13
  elif age < 50:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 3
    elif total_cholesterol < 240:
      points_total += 6
    elif total_cholesterol < 280:
      points_total += 8
    else:
      points_total += 10
  elif age < 60:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 2
    elif total_cholesterol < 240:
      points_total += 4
    elif total_cholesterol < 280:
      points_total += 5
    else:
      points_total += 7
  elif age < 70:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 1
    elif total_cholesterol < 240:
      points_total += 2
    elif total_cholesterol < 280:
      points_total += 3
    else:
      points_total += 4
  else:
    if total_cholesterol < 160:
      points_total += 0
    elif total_cholesterol < 200:
      points_total += 1
    elif total_cholesterol < 240:
      points_total += 1
    elif total_cholesterol < 280:
      points_total += 2
    else:
      points_total += 2
    
  # Smoking status sub branch
  if smoking_status == False:
    points_total += 0
  if smoking_status == True:
    if age >= 20 and age <=39:
      points_total += 9
    elif age <= 49:
      points_total += 7
    elif age <= 59:
      points_total += 4
    elif age <= 69:
      points_total += 2
    else:
      points_total += 1

  # HDL sub branch
  if hdl >= 60:
    points_total -= 1
  elif (hdl >= 50) and (hdl <= 59):
    points_total += 0
  elif (hdl >= 40) and (hdl <= 49):
    points_total += 1
  elif (hdl < 40):
    points_total += 2

  # Systolic BP sub branch
  if treated_status == False:
    if systolic_bp < 120:
      points_total += 0
    elif systolic_bp <= 129:
      points_total += 1
    elif systolic_bp <= 139:
      points_total += 2
    elif systolic_bp <= 159:
      points_total += 3
    elif systolic_bp >= 160:
      points_total += 4
  if treated_status == True:
    if systolic_bp < 120:
      points_total += 0
    elif systolic_bp <= 129:
      points_total += 3
    elif systolic_bp <= 139:
      points_total += 4
    elif systolic_bp <= 159:
      points_total += 5
    elif systolic_bp >= 160:
      points_total += 6


# Print statements for male, based on total points
if sex =='M' or sex == 'm':
  if points_total < 0:
    print('Your 10-year risk of a heart attack is <1%')
  if points_total == 0:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 1:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 2:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 3:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 4:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 5:
    print('Your 10-year risk of a heart attack is 2%')
  if points_total == 6:
    print('Your 10-year risk of a heart attack is 2%')
  if points_total == 7:
    print('Your 10-year risk of a heart attack is 3%')
  if points_total == 8:
    print('Your 10-year risk of a heart attack is 4%')
  if points_total == 9:
    print('Your 10-year risk of a heart attack is 5%')
  if points_total == 10:
    print('Your 10-year risk of a heart attack is 6%')
  if points_total == 11:
    print('Your 10-year risk of a heart attack is 8%')
  if points_total == 12:
    print('Your 10-year risk of a heart attack is 10%')
  if points_total == 13:
    print('Your 10-year risk of a heart attack is 12%')
  if points_total == 14:
    print('Your 10-year risk of a heart attack is 16%')
  if points_total == 15:
    print('Your 10-year risk of a heart attack is 20%')
  if points_total == 16:
    print('Your 10-year risk of a heart attack is 25%')
  if points_total >= 17:
    print('Your 10-year risk of a heart attack is >30%')
# print statements for female, based on point total
if sex == 'f' or sex == 'F':
  if points_total < 9:
    print('Your 10-year risk of a heart attack is <1%')
  if points_total == 9:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 10:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 11:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 12:
    print('Your 10-year risk of a heart attack is 1%')
  if points_total == 13:
    print('Your 10-year risk of a heart attack is 2%')
  if points_total == 14:
    print('Your 10-year risk of a heart attack is 2%')
  if points_total == 15:
    print('Your 10-year risk of a heart attack is 3%')
  if points_total == 16:
    print('Your 10-year risk of a heart attack is 4%')
  if points_total == 17:
    print('Your 10-year risk of a heart attack is 5%')
  if points_total == 18:
    print('Your 10-year risk of a heart attack is 6%')
  if points_total == 19:
    print('Your 10-year risk of a heart attack is 8%')
  if points_total == 20:
    print('Your 10-year risk of a heart attack is 11%')
  if points_total == 21:
    print('Your 10-year risk of a heart attack is 14%')
  if points_total == 22:
    print('Your 10-year risk of a heart attack is 17%')
  if points_total == 23:
    print('Your 10-year risk of a heart attack is 22%')
  if points_total == 24:
    print('Your 10-year risk of a heart attack is 27%')
  if points_total >= 25:
    print('Your 10-year risk of a heart attack is >30%')
