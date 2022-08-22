# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab9b_Act1
# Date:         11/11/21
weather = open('CLLWeatherData.csv','r')
data = weather.read()
new_data = data.split('\n')
highest = 0
lowest = 100000000000000000000000000
precipitation_sum = 0
counter = 0
number_of_days = (len(new_data)) - 1
dates = []
all_dates = []
monthlyyearsum = 0
month_counter = 0
meandailytemp = 0
windsum = 0
total_precipitation = 0

#open file and initialize variables




#split string into list

for i in new_data:
  if i == new_data[0]:
    continue
  if i == new_data[-1]:
    continue
  new_new_data = i.split(',')
  


  
#successfuly gives highest, lowest value, and average precipitation 
  if int(new_new_data[4]) > highest:
    highest = int(new_new_data[4])
  if int(new_new_data[5]) < lowest:
    lowest = int(new_new_data[5])
  precipitation_sum += float(new_new_data[2])
  average = precipitation_sum / number_of_days

print('3-year maximum temperature: {:.0f} F'.format(highest))
print('3-year minimum temperature: {:.0f} F'.format(lowest))
print('3-year average precipitation: {:.3f} inches'.format(average))
print()

############PART 2###################

#converts months to numerical values

month = input('Please enter a month: ')
year = input('Please enter a year: ')
print()
numerical_month_value = 0
if month == 'January':
  numerical_month_value = 1
if month == 'February':
  numerical_month_value = 2
if month == 'March':
  numerical_month_value = 3
if month == 'April':
  numerical_month_value = 4
if month == 'May':
  numerical_month_value = 5
if month == 'June':
  numerical_month_value = 6
if month == 'July':
  numerical_month_value = 7
if month == 'August':
  numerical_month_value = 8
if month == 'September':
  numerical_month_value = 9
if month == 'October':
  numerical_month_value = 10
if month == 'November':
  numerical_month_value = 11
if month == 'December':
  numerical_month_value = 12 


#loop that splits the first term of the list so finds the term that matches the user inputted month and year
for i in new_data:
  if i == new_data[0]:
    continue
  if i == new_data[-1]:
    continue
  new_new_data = i.split(',')
  dates = new_new_data[0].split('/')
  new_new_data[0] = dates
  if new_new_data[0][0] == str(numerical_month_value):
    if new_new_data[0][2] == year:
      month_counter += 1
      monthlyyearsum += int(new_new_data[3])

      if float(new_new_data[1]) > 10:
        windsum += 1

      if len(new_new_data[2]) == 1:
        total_precipitation += 0
      if len(new_new_data[2]) > 1:
        total_precipitation += float(new_new_data[2])
      
# uses outputs to calculate the temp mean, percent, and precipitation mean
print('For {} {}:'.format(month,year))
meandailytemp = monthlyyearsum / month_counter

print('Mean daily temperature: {:.1f} F'.format(meandailytemp))


percentage = (windsum / month_counter) * 100

print('Percentage of days with average wind speed above 10 mph: {:.1f}%'.format(percentage))

precipmean = total_precipitation / month_counter

print('Mean daily precipitation: {:.4f} inches'.format(precipmean))

#close file

weather.close()
    

