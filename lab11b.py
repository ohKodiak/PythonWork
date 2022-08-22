# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 11b
# Date:         11/28/21




from math import *

#part A
''' Write a function named parta that will take in as parameters the dimensions of the box (length,
width, and height) and the radius of the hole, and returns the volume of material remaining.
Assume the hole has been drilled along the height direction. Note: first write the function
assuming the hole has radius less than min(length/2, width/2). For full credit, you will
need to account for larger radii (bigger than half the length or width of the box). 

def parta(length,width,height,radius):
    #first part
    # if(radius < width/2) and (radius < length/2):
    prismvolume = length * width * height
    holevolume = pi * (radius**2) * height
    volumeleft = prismvolume - holevolume
    if radius > length/2:
        overlap = 2 * ((acos(length/(2*radius))) * (radius**2) - (((radius **2)/2)*sin(2*acos(length/(2*radius)))))
        volumeleft = volumeleft + overlap
    if radius > length/2 :
        overlap = 2 * ((acos(length/(2*radius))) * (radius**2) - (((radius **2)/2)*sin(2*acos(length/(2*radius)))))
        volumeleft = volumeleft + overlap
    if 2*radius > sqrt(width**2 + length**2):
        volumeleft = 0
    
        #base = length - sqrt(radius**2 - (width/2)**2)
        #hite = width - 
    return volumeleft

'''

# triangular prism is 1/2bhl


#partB
'''


lst1 = ['toms', 'ezras', 'lowes','sonjas']
lst2 = [10,5,6,0]
lst3 = [15,11,7,225]
def partb(list1,list2,list3):
    length = len(list1)
    list_of_profits = []
    for i in range(length):
        list_of_profits.append(list3[i] - list2[i])
    for i in range(len(list_of_profits)):
        if list_of_profits[i] == max(list_of_profits):
            highest_earning = list1[i]
    return highest_earning, max(list_of_profits)
    
'''
    
#part c


''' Write a function named partc that will take in as parameters a person’s name, city, state, zip
code, and address, and returns a single string of the person’s information formatted like a
mailing label. 
nam = 'eddy'
cit = 'little rock'
stat = 'ark'
zipcod = '76502'
addres = 'fenway park street'

def partc(name,city,state,zipcode,address):
    label = '{}\n{}\n{}, {}, {}'.format(name,address,city,state,zipcode)
    return label 
    

'''

#part d
'''  Write a function named partd that will take in as a parameter the name of a file with a .csv
extension (a comma-separated value file), and writes a new file that is equivalent (same name
and same data) but with a .tsv extension (a tab-separated value file: like a CSV but with tabs
instead of commas separating the elements of the file). Have the function return the string
"Done!". Note: the character used to represent a tab is "\t". 
def partd(file):
    filename = str(file)
    openfile = open(file, 'r')
    filestring = openfile.read()
    openfile.close()
    newname = filename[:-4] + '.tsv'

    filestring = list(filestring)

    for i in range(len(filestring)):
      #print(filestring[i])
      if filestring[i] == ',':
        filestring[i] = '\t'
    filestring = ''.join(filestring)
    newfile = open(newname,'w')
    newfile.write(filestring)
    newfile.close()
    return 'Done!' 


print(partd('weather.csv'))

#part e

''' Write a function named parte that takes in as a parameter a list and returns the minimum,
#median, and maximum value of the list, in that order. 

def parte(list1):
    counter = 0
    for i in list1:
        counter += 1
    average = sum(list1) / counter
    return min(list1), average, max(list1)

'''
#part f

''' Write a function named partf that takes in as parameters two parallel lists: a list of times (in
increasing order), and a list of distance traveled by that point in time. The function should return
a new list giving the average velocity between consecutive time measurements. The new list
should have a length of one less than the original lists. 

def partf(timeslist, listdistance):
    listspeeds = []
    for i in range(len(timeslist)):
        if timeslist[i] != timeslist[-1]:
            distance = listdistance[i + 1] - listdistance[i]
            time = timeslist[i + 1] - timeslist[i]
            velocity = distance / time
            listspeeds.append(velocity)
    return listspeeds

timeslist1 = [0,10,20,30,40,50,60,70]
listdistance1 = [0,100,200,300,400,500,600,700]
print(partf(timeslist1,listdistance1))
print(len(timeslist1))
print(len(partf(timeslist1,listdistance1)))
        
'''



    
    
    




