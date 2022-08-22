# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab7b_Act1
# Date:         16 October 2021

#initialize variables
name = input('What is your name? ')
x = name[:]
y = name[1:]
d = name[2:]
z = name.lower()



#check if first letter is a vowel or not, create print statements accordingly
if (name[0] == 'a' or name[0] =='A') or (name[0] == 'e' or name[0] =='E') or (name[0] =='i' or name[0] =='I') or (name[0] =='o' or name[0] =='O') or (name[0] =='u' or name[0] =='U'):
    line1 =('{}, {}, Bo-B{}'.format(x,x,z))
    line2 =('Banana-Fana Fo-F{}'.format(z))
    line3 =('Me Mi Mo-M{}'.format(z))
    line4 =('{}!'.format(x))
#acounts for names with both 1 or 2 starting constonants
if (name[0] != 'a' and name[0] !='A') and (name[0] != 'e' and name[0] !='E') and (name[0] !='i' and name[0] !='I') and (name[0] !='o' and name[0] !='O') and (name[0] !='u' and name[0] !='U'):
    line1 =('{}, {}, Bo-B{}'.format(x,x,y))
    line2 =('Banana-Fana Fo-F{}'.format(y))
    line3 =('Me Mi Mo-M{}'.format(y))
    line4 =('{}!'.format(x))
    if (name[1] != 'a' and name[1] !='A') and (name[1] != 'e' and name[1] !='E') and (name[1] !='i' and name[1] !='I') and (name[1] !='o' and name[1] !='O') and (name[1] !='u' and name[1] !='U'):
        line1 =('{}, {}, Bo-B{}'.format(x,x,d))
        line2 =('Banana-Fana Fo-F{}'.format(d))
        line3 =('Me Mi Mo-M{}'.format(d))
        line4 =('{}!'.format(x))


# print statements
print(line1)
print(line2)
print(line3)
print(line4)
   
   
    


    

