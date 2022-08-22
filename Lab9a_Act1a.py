# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab9a_Act1a
# Date:         5 November 2021

# Create and initialize variables
passport = '' # string, holds information of one person
passport_list = [] # list
passport_file = '' # string of all information
passport_info_list = [] # list, holds information of particular person
valid_passports = 0 # int, counter for valid passports
output_file = '' # string, writes to output file

# Calculations
with open('Lab9a_input.txt', 'r') as passport_file:
  output_file = open('Lab9a_Act1a_valid.txt', 'w')
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
        valid_passports += 1 # increments if valid
        output_file.write(passport + '\n\n') # writes to output file and adds new line
    else:
    # if cid is not present, there should be 7 passport information values
      passport_info_list = passport.split()
      if len(passport_info_list) == 7:
        valid_passports += 1
        output_file.write(passport + '\n\n')
  output_file.close()

# Print results
print('There are {} valid passports'.format(valid_passports))

    
    
    

