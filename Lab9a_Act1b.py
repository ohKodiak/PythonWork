# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Pack:         11
# Assignment:   Lab9a_Act1b
# Date:         5 November 2021

# Function that checks for valid input for each required field
def valid_test(p):
  counter = -1
  valid_input = True
  # loop through each element of list to find which required field needs to be tested for validity
  for i in p:
    counter += 1 # counter used to find which list element is accessed
    # birth year has to be 4 digits, between 1920-2005, inclusive
    if 'byr' in i:
      if len(i) != 8:
        valid_input = False
        break
      if int(p[counter][4:]) > 2005:
        valid_input = False
        break
      if int(p[counter][4:]) < 1920:
        valid_input = False
        break
    # issue year has to be 4 digits, between 2011-2021, inclusive
    elif 'iyr' in i:
      if len(i) != 8:
        valid_input = False
        break
      if int(p[counter][4:]) > 2021:
        valid_input = False
        break
      if int(p[counter][4:]) < 2011:
        valid_input = False
        break
    # expiration year has to be 4 digits, between 2021-2031, inclusive
    elif 'eyr' in i:
      if len(i) != 8:
        valid_input = False
        break
      if int(p[counter][4:]) > 2031:
        valid_input = False
        break
      if int(p[counter][4:]) < 2021:
        valid_input = False
        break
    # height
    elif 'hgt' in i:
      # height in inches has to be between 59-76, inclusive
      if 'in' in i:
        if len(i) != 8:
          valid_input = False
          break
        if int(p[counter][4:6]) > 76:
          valid_input = False
          break
        if int(p[counter][4:6]) < 59:
          valid_input = False
          break
      # height in centimeters has to be between 150-193, inclusive
      elif 'cm' in i:
        if len(i) != 9:
          valid_input = False
          break
        if int(p[counter][4:7]) > 193:
          valid_input= False
          break
        if int(p[counter][4:7]) < 150:
          valid_input = False
          break
      # if 'in' and 'cm' not found in height, invalid input
      else:
        valid_input = False
        break
    # hair color has to start with # and be followed by 6 characters (0-9 or a-f)
    elif 'hcl' in i:
      if len(i) != 11:
        valid_input = False
        break
      for j in i[5:]:
        if j not in 'abcdef0123456789':
          valid_input = False
          break
      if valid_input == False:
        break
    # eye color can only be one of the following colors: amb, blu, brn, gry, grn, hzl, oth
    elif 'ecl' in i:
      if len(i) != 7:
        valid_input = False # default false, if none of these colors are found, it is invalid (false) - has to be proven true
        break
      valid_input = False
      if p[counter][4:] == 'amb':
        valid_input = True
      if p[counter][4:] == 'blu':
        valid_input = True
      if p[counter][4:] == 'brn':
        valid_input = True
      if p[counter][4:] == 'gry':
        valid_input = True
      if p[counter][4:] == 'grn':
        valid_input = True
      if p[counter][4:] == 'hzl':
        valid_input = True
      if p[counter][4:] == 'oth':
        valid_input = True
      if valid_input == False:
        break
    # passport id has to be a 9-digit number
    elif 'pid' in i:
      # checks if there are 9 digits after the colon
      if len(i) != 13:
        valid_input = False
        break
      # loop checks if each character after the colon is a number
      for j in i[4:]:
        if j not in '0123456789':
          valid_input = False
          break
      if valid_input == False:
        break
  return valid_input

# Create and initialize variables
passport = '' # string, holds information of one person
passport_list = [] # list
passport_file = '' # string of all information
passport_info_list = [] # list, holds information of particular person
valid_passports = 0 # int, counter for valid passports
output_file = '' # string, writes to output file

# Calculations
with open('Lab9a_input.txt', 'r') as passport_file:
  output_file = open('Lab9a_Act1b_valid.txt', 'w')
  # opens output file in write designator
  passport_string = passport_file.read()
  # opens passport_string in read mode
  passport_list = passport_string.split('\n\n')
  # turns string to list, separated by empty lines
  for passport in passport_list:
    if 'cid' in passport: # searches for country ID in passport
    # if cid is present, there should be 8 passport information values
      passport_info_list = passport.split() # list split at each particular person
      if len(passport_info_list) == 8: # checks length
        if valid_test(passport_info_list) == True:
          valid_passports += 1 # increments if valid
          output_file.write(passport + '\n\n') # writes to output file and adds new line
    else:
      passport_info_list = passport.split()
      if len(passport_info_list) == 7:
      # if cid is not present, there should be 7 passport information values
        if valid_test(passport_info_list) == True:
          valid_passports += 1 # increments if valid
          output_file.write(passport + '\n\n') # writes to output file and adds new line
  output_file.close()

# Print results
print('There are {} valid passports'.format(valid_passports))





    
    
    

