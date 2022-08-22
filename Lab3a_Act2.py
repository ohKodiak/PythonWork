# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         YOUR TEAM NUMBER
# Assignment:   Lab 3a Activity 2
# Date:         20 September 2021

# variables for each input of time and position

#function which takes in inputs for time and position and inserts them into the interpolation formula
def interpolate(t,t1,t2,x1,x2,y1,y2,z1,z2):
    x = x1 + (t-t1) * (x2 - x1) / (t2 - t1)
    y = y1 + (t-t1) * (y2 - y1) / (t2 - t1)
    z = z1 + (t-t1) * (z2 - z1) / (t2 - t1)
    print('At time {:.1f} seconds the object is at ({:.2f}, {:.2f}, {:.2f})'.format(t,x,y,z))
#user inputs for time and position
time1 = float(input('Enter time 1: '))
x_pos1 = float(input('Enter the x position of the object at time 1: '))
y_pos1 = float(input('Enter the y position of the object at time 1: '))
z_pos1 = float(input('Enter the z position of the object at time 1: '))
time2 = float(input('Enter time 2: '))
x_pos2 = float(input('Enter the x position of the object at time 2: '))
y_pos2 = float(input('Enter the y position of the object at time 2: '))
z_pos2 = float(input('Enter the z position of the object at time 2: '))
print('')

#values of interest between inputted time values 
increment = (time2 - time1) / 4

time_of_interest = time1
interpolate(time_of_interest,time1,time2,x_pos1,x_pos2,y_pos1,y_pos2,z_pos1,z_pos2)

time_of_interest += increment
interpolate(time_of_interest,time1,time2,x_pos1,x_pos2,y_pos1,y_pos2,z_pos1,z_pos2)

time_of_interest += increment
interpolate(time_of_interest,time1,time2,x_pos1,x_pos2,y_pos1,y_pos2,z_pos1,z_pos2)

time_of_interest += increment
interpolate(time_of_interest,time1,time2,x_pos1,x_pos2,y_pos1,y_pos2,z_pos1,z_pos2)

time_of_interest += increment
interpolate(time_of_interest,time1,time2,x_pos1,x_pos2,y_pos1,y_pos2,z_pos1,z_pos2)