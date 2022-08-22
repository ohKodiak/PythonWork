# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab11a_Act1
# Date:         17 November 2021

def readfile(namefile):
  '''readline function: reads file and creates list, argument is filename, returns a list of lists'''
  finallist = [] # list, returned after file operations
  with open(namefile, 'r') as file: # open files in read mode
    fileread = file.read() # reads whole string into variable
    filelist = fileread.split('\n') #splits at each new line
    filelist.pop(0) # delete the first line (header)
    # loop iterates through filelist, splits at commas
    for point in filelist:
      coordinateslist = point.split(',')
      nestedlist = [int(coordinateslist[0]), int(coordinateslist[1])] # converts to integers, created nested list for each point
      finallist.append(nestedlist) # add list to end of finallist
  return finallist

def cross(a, b):  
  '''cross function: finds cross product of two arguments, takes 2 arguments (both are lists of one point), returns the cross product'''
  cross_prod = a[0] * b[1] - a[1] * b[0] # calculates the cross product
  return cross_prod

def shoelace(finallist):
  '''shoelace function: finds area of polygon, takes argument of list of points (same list returned by readfile), returns area of polygon'''
  cross_prod_total = 0 # intitializes cross product total
  for i in range(-len(finallist), 0):
    cross_prod_total += cross(finallist[i], finallist[i+1]) # call cross function
  area = abs(cross_prod_total) / 2 
  return area # returns area

def main():
  '''main function: takes user input and prints area of polygon, takes no arguments, returns nothing'''
  filename = input('Please enter the filename: ')
  print('The area of the polygon is {}'.format(shoelace(readfile(filename)))) # calls readfile function and shoelace functions

if __name__ == '__main__':
  main() # calls main function
