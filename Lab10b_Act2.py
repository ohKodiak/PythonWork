# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 10b Act2
# Date:         17 November 21

#import everything
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import matplotlib.mlab as mlab

#open file, initizalize variables

list_of_winds = []
list_of_temps = []
list_of_precipitation = []
actual_total_precip = []
list_of_min_temp = []
days_of_rain = 0
counter = 0
precip_sum = 0
all_dates = []
list_of_all_data = []

weather = open('CLLWeatherData.csv', 'r')
data = weather.read()


new_data = data.split('\n')
    
#loop like splits original data, and categorizes into each type of info for furture use 
for i in new_data:
  if i == new_data[0]:
    continue
  if i == new_data[-1]:
    continue
  new_new_data = i.split(',')
  list_of_winds.append(new_new_data[1])
  list_of_temps.append(new_new_data[3])
  list_of_precipitation.append(new_new_data[2])
  list_of_min_temp.append(new_new_data[5])
  dates = new_new_data[0].split('/')
  new_new_data[0] = dates
  list_of_all_data.append(new_new_data)


 

#these for loops convert the values of each respective list into float values

for i in range(len(list_of_winds)):
  list_of_winds[i] = float(list_of_winds[i])
  
for i in range(len(list_of_temps)):
  list_of_temps[i] = float(list_of_temps[i])
  

for i in range(len(list_of_precipitation)):
    if len(list_of_precipitation[i]) == 1:
        continue
    if len(list_of_precipitation[i]) != 1:
        actual_total_precip.append(list_of_precipitation[i])
for i in range(len(actual_total_precip)):
    actual_total_precip[i] = float(actual_total_precip[i])
    precip_sum += float(actual_total_precip[i])
    days_of_rain += 1

for i in range(len(list_of_min_temp)):
    list_of_min_temp[i] = float(list_of_min_temp[i])


#close file
weather.close()


######Graph 1#######
#graphs data  for wind and temp on the same plot
date = range(1096)

figure = plt.figure()
left_axis = figure.add_subplot(1, 1, 1)
right_axis = left_axis.twinx()


left_axis.plot(date, list_of_temps, 'r', label="Temp avg")
right_axis.plot(date, list_of_winds,'b',label="Wind avg")
right_axis.axis([-100,1190,0,20.0])

left_axis.set_xlabel('date')
left_axis.set_ylabel('Average Temperature, F')
left_axis.legend(loc="lower center")

right_axis.set_ylabel('Average Wind Speed, mph')
right_axis.legend(loc="lower left")

plt.title('Average Tempature and Wind Speed')
    
plt.show() 


#########Graph 2##########


#graphs precipitation data on a histogram 
#i could not find a command to make the lines of the histogram thicker 
plt.hist(actual_total_precip,bins= 49, range= (0.1,5.0), facecolor='blue')
plt.title('Histogram of precipitation') 
plt.xlabel('Precipitation, in')
plt.ylabel('Numbers of days')
#plt.axis('tight')
plt.show() 

####### Graph 3 ##########

#graphs wind and min temperature on a scatter plot
plt.scatter(list_of_min_temp,list_of_winds,color = 'k',s = 7)
plt.xlabel('Minimum Temperature, F')
plt.ylabel('Average Wind Speed, mph')
plt.title('Average Wind Speed vs Minimum Temperature')
plt.show() 

#######Graph 4#########
#initiallizing variables for the average temp sums, the number of days in each month, 
#and the lowest temperatures in each month, and the highest temp in each month
sum_of_all_temps1 = 0
sum_of_all_temps2 = 0
sum_of_all_temps3 = 0
sum_of_all_temps4 = 0
sum_of_all_temps5 = 0
sum_of_all_temps6 = 0
sum_of_all_temps7 = 0
sum_of_all_temps8 = 0
sum_of_all_temps9 = 0
sum_of_all_temps10 = 0
sum_of_all_temps11 = 0
sum_of_all_temps12 = 0
countdays1 = 0
countdays2 = 0
countdays3 = 0
countdays4 = 0
countdays5 = 0
countdays6 = 0
countdays7 = 0
countdays8 = 0
countdays9 = 0
countdays10 = 0
countdays11 = 0
countdays12 = 0
lowest1 = 10000000
lowest2 = 100000000
lowest3 = 10000000000
lowest4 = 100000000
lowest5 = 1000000000
lowest6 = 100000000
lowest7 = 1000000000
lowest8 = 1000000000
lowest9 = 100000000
lowest10 = 10000000
lowest11 = 100000000
lowest12 = 10000000000
highest1 = 0
highest2 = 0
highest3 = 0
highest4 = 0
highest5 = 0
highest6 = 0
highest7 = 0
highest8 = 0
highest9 = 0
highest10 = 0
highest11 = 0
highest12 = 0



#loop that sorts month specific data to find the averages, mins and maxes

for i in range(len(list_of_all_data)):
    list_of_all_data[i][3] = int(list_of_all_data[i][3])
    if list_of_all_data[i][0][0] == '1':
        sum_of_all_temps1 += list_of_all_data[i][3]
        countdays1 += 1
        if float(list_of_all_data[i][5]) < float(lowest1):
            lowest1 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest1):
            highest1 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '2':
        sum_of_all_temps2 += list_of_all_data[i][3]
        countdays2 += 1
        if float(list_of_all_data[i][5]) < float(lowest2):
            lowest2 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest2):
            highest2 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '3':
        sum_of_all_temps3 += list_of_all_data[i][3]
        countdays3 += 1
        if float(list_of_all_data[i][5]) < float(lowest3):
            lowest3 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest3):
            highest3 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '4':
        sum_of_all_temps4 += list_of_all_data[i][3]
        countdays4 += 1
        if float(list_of_all_data[i][5]) < float(lowest4):
            lowest4 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest4):
            highest4 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '5':
        sum_of_all_temps5 += list_of_all_data[i][3]
        countdays5 += 1
        if float(list_of_all_data[i][5]) < float(lowest5):
            lowest5 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest5):
            highest5 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '6':
        sum_of_all_temps6 += list_of_all_data[i][3]
        countdays6 += 1
        if float(list_of_all_data[i][5]) < float(lowest6):
            lowest6 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest6):
            highest6 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '7':
        sum_of_all_temps7 += list_of_all_data[i][3]
        countdays7 += 1
        if float(list_of_all_data[i][5]) < float(lowest7):
            lowest7 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest7):
            highest7 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '8':
        sum_of_all_temps8 += list_of_all_data[i][3]
        countdays8 += 1
        if float(list_of_all_data[i][5]) < float(lowest8):
            lowest8 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest8):
            highest8 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '9':
        sum_of_all_temps9 += list_of_all_data[i][3]
        countdays9 += 1
        if float(list_of_all_data[i][5]) < float(lowest9):
            lowest9 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest9):
            highest9 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '10':
        sum_of_all_temps10 += list_of_all_data[i][3]
        countdays10 += 1
        if float(list_of_all_data[i][5]) < float(lowest10):
            lowest10 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest10):
            highest10 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '11':
        sum_of_all_temps11 += list_of_all_data[i][3]
        countdays11 += 1
        if float(list_of_all_data[i][5]) < float(lowest11):
            lowest11 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest11):
            highest11 = float(list_of_all_data[i][4])
    if list_of_all_data[i][0][0] == '12':
        sum_of_all_temps12 += list_of_all_data[i][3]
        countdays12 += 1
        if float(list_of_all_data[i][5]) < float(lowest12):
            lowest12 = float(list_of_all_data[i][5])
        if float(list_of_all_data[i][4]) > float(highest12):
            highest12 = float(list_of_all_data[i][4])

#calculating averages of each month
average1 = sum_of_all_temps1 / countdays1
average2 = sum_of_all_temps2 / countdays2
average3 = sum_of_all_temps3 / countdays3
average4 = sum_of_all_temps4 / countdays4
average5 = sum_of_all_temps5 / countdays5
average6 = sum_of_all_temps6 / countdays6
average7 = sum_of_all_temps7 / countdays7
average8 = sum_of_all_temps8 / countdays8
average9 = sum_of_all_temps9 / countdays9
average10 = sum_of_all_temps10 / countdays10
average11 = sum_of_all_temps11 / countdays11
average12 = sum_of_all_temps12 / countdays12

#assigning values to a list
average_temperatures_by_month = [average1,average2,average3,average4,average5,average6,average7,average8,average9,average10,average11,average12]
lowest_temperature = [lowest1,lowest2,lowest3,lowest4,lowest5,lowest6,lowest7,lowest8,lowest9,lowest10,lowest11,lowest12]
highest_temperature = [highest1,highest2,highest3,highest4,highest5,highest6,highest7,highest8,highest9,highest10,highest11,highest12]
months = [1,2,3,4,5,6,7,8,9,10,11,12]

#plotting graph for average temp, lowest temp, and highest temp per month
plt.plot(lowest_temperature,c='k',label = 'Low T')
plt.legend(loc='center left')
plt.plot(highest_temperature,label = 'High T',c = 'r')
plt.legend(loc='upper left')
plt.bar(months,average_temperatures_by_month)
plt.xlabel('Month')
plt.ylabel('Average Temperature, F')
plt.title('Average Temperature by Month')
plt.show()  