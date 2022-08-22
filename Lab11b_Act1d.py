# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab 11b Act 1d
# Date:         11/28/21

#part d
def partd(file):
    '''opens file, reads onto variable, makes into list, changes out commas for tabs, makes back into a string, writes onto new tsv file '''
    filename = str(file)
    openfile = open(file, 'r')
    filestring = openfile.read()
    #reads string onto variable 
    openfile.close()
    newname = filename[:-4] + '.tsv'
    #creates file name by replacing .csv ending with .tsv

    filestring = list(filestring)
    #converts to list
    # for loop that replaces commas with tabs
    for i in range(len(filestring)):

      if filestring[i] == ',':
        filestring[i] = '\t'
    filestring = ''.join(filestring)
    newfile = open(newname,'w')
    newfile.write(filestring)
    newfile.close()
    # closes file after writing to file 
    return 'Done!' 


