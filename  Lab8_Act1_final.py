# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab8_Act1_Final
# Date:         29 October 2021

# Create and initialize variables
#list of temp vals (celsius)
temp_list = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
#list of volume vals
specific_volume_list = [0.0009977, 0.0009996, 0.0010057, 0.0010149, 0.0010267, 0.0010410, 0.0010576, 0.0010769, 0.0010988, 0.0011240, 0.0011531, 0.0011868, 0.0012268, 0.0012755]
#float that stores vol input
specific_volume = 0
#float that stores vol slope
slope_specific_volume = 0
#list of internal energy vals
specific_internal_energy_list = [0.04, 83.61, 166.92, 250.29, 333.82, 417.65, 501.91, 586.80, 672.55, 759.47, 847.92, 938.39, 1031.60, 1128.5]
#float that stores internal energy input
specific_internal_energy = 0
#float that stores internal energy slope
slope_specific_internal_energy = 0
#list of enthalpy vals
specific_enthalpy_list = [5.03, 88.61, 171.95, 255.36, 338.96, 422.85, 507.19, 592.18, 678.04, 765.09, 853.68, 944.32, 1037.70, 1134.90]
#float that stores enthalpy input
specific_enthalpy = 0
#float that stores enthalpy slope
slope_specific_enthalpy = 0
#list of entropy vals
specific_entropy_list = [0.0001, 0.2954, 0.5705, 0.8287, 1.0723, 1.3034, 1.5236, 1.7344, 1.9374, 2.1338, 2.3251, 2.5127, 2.6983, 2.8841]
#float that stores entropy input
specific_entropy = 0
#float that stores entropy slope
slope_specific_entropy = 0
#range of valid charaters
valid_characters = '0123456789.-'
#user input for temp
temperature = 0
#temp range index of temp input
temp_index = 0
# floats for changes in x and y vals
delta_y = 0
delta_x = 0

# User input
temperature = input('Enter a temperature between 0 and 260 deg C: ')

# Validity check
import sys
# valid character check
valid_characters = '0123456789.-'
for i in temperature:
    if i not in valid_characters:
        print('Please enter a number.')
        sys.exit()
temperature = float(temperature)
# correct temperature range (0-260)
if temperature < 0:
    print('Please enter a temperature greater than 0.')
    sys.exit()
if temperature > 260:
    print('Please enter a temperature less than 260.')
    sys.exit() 


# Calculations
# for top temperature value allowed
if temperature == 260:
    specific_volume = 0.0012755
    specific_internal_energy = 1128.50
    specific_enthalpy = 1134.90
    specific_entropy = 2.8841
else:
    # Slope Calculations
    # temperature (parent group)
    temp_index = -1
    for i in temp_list:
        if temperature <= i:
            delta_x = (temp_list[temp_index + 1] - temp_list[temp_index])
            delta_y = (specific_volume_list[temp_index + 1] - specific_volume_list[temp_index])
            slope_specific_volume = delta_y / delta_x
            break
        temp_index += 1
    # delta x always remains the same so it does not have to be recalculated every time
    # specific internal energy 
    delta_y = (specific_internal_energy_list[temp_index + 1] - specific_internal_energy_list[temp_index])
    slope_specific_internal_energy = delta_y / delta_x
    # Enthalpy 
    delta_y = (specific_enthalpy_list[temp_index + 1] - specific_enthalpy_list[temp_index])
    slope_specific_enthalpy = delta_y / delta_x
    # Entropy
    delta_y = (specific_entropy_list[temp_index + 1] - specific_entropy_list[temp_index])
    slope_specific_entropy = delta_y / delta_x
    # Property Value Calculations
    # Plug values into equation to solve for values (y = mx + b, where m is slope, b is starting value)
    specific_volume = slope_specific_volume * (temperature - temp_list[temp_index]) + specific_volume_list[temp_index]
    specific_internal_energy = slope_specific_internal_energy * (temperature - temp_list[temp_index]) + specific_internal_energy_list[temp_index]
    specific_enthalpy = slope_specific_enthalpy * (temperature - temp_list[temp_index]) + specific_enthalpy_list[temp_index]
    specific_entropy = slope_specific_entropy * (temperature - temp_list[temp_index]) + specific_entropy_list[temp_index]

# Print results
print('Properties at {:.1f} deg C are:'.format(temperature))
print('Specific volume (m^3/kg): {:.7f}'.format(specific_volume))
print('Specific internal energy (kJ/kg): {:.2f}'.format(specific_internal_energy))
print('Specific enthalpy (kJ/kg): {:.2f}'.format(specific_enthalpy))
print('Specific entropy (kJ/kgK): {:.4f}'.format(specific_entropy))


