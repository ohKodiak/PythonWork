# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter
# Section:      213
# Team:         11
# Assignment:   Lab9b_Act1
# Date:         11/11/21

#open file, read it into variable

with open('game.txt', 'r') as myfile:
    game = myfile.read()
coinsum = 0
coinstring = ''

#split into list
my_game = game.split('\n')

#open file
coins = open('coins.txt','w')

#while loop that executes instructions, writes coin values to coin.txt andf counts number of coins
i = 0
while i < len(my_game):

        if 'jump' in my_game[i]:
            if '-' in my_game[i]:
                i -= int(my_game[i][6:])
            else:
                i += int(my_game[i][6:])
            
        elif 'coin' in my_game[i]:
            
            if my_game[i][5] == '-':
                coinsum -= int(my_game[i][6:])
                coinstring += my_game[i][5:]
                coins.write(my_game[i][5:] + '\n')
            else:
                coinsum += int(my_game[i][6:])
                coinstring += my_game[i][6:]
                coins.write(my_game[i][6:] + '\n')
            i += 1
        else:
            i += 1
            continue
        
#close file
coins.close()
print('Total coins:',coinsum)




        
            

    

                
    
   
    
    
    
    