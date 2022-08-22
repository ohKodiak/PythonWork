# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Pack:         11
# Assignment:   Lab12_Act2
# Date:         8 December 2021
# import functions
from getpass import getpass
import turtle as t
from random import randint

# one thing beyond what is covered in the lectures - passwords
print("Password is 'i love coding'\n┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴") # gives fake password
password = getpass("Password: ") # asks for password
if password == "i hope i got an A on the final":
  print("Correct password!") # checks password validity
else:
  print("Kidding. ") # if password is wrong
  # while loop that that continues to ask for password until right password is inputted
while password != "i hope i got an A on the final":
  print("Wrong password!\nThe real password is 'i hope i got an A on the final'\n (ง ͠° ͟ل͜ ͡°)ง")
  password = getpass("Password: ")
  if password == "i hope i got an A on the final":
    print("Correct password!\nCome on in!\n¯\_(ツ)_/¯")
    break
def intro():
  '''This function prints the greeting and the instructions to the players. This function takes no parameters and returns nothing. '''
  print('Howdy! Welcome to PIG! X out of the pig drawing when it\'s finished to start.')
  pig_picture() # calls the pig picture function to draw the pig
  print('Here are the rules to play the game:')
  print("At the start of each turn, the player will roll the dice. \nIf the player rolls a 1, their turn immediately ends and their score for that turn is 0. \nIf the player rolls any other number, the number is added to their turn score and their turn continues.\nIf the player elects to hold their score by typing in 'h', their current turn score is added to their overall game score and it becomes the next player's turn. If the player types in 'k' or simply presses enter, the game will roll the dice again.")
  print('The first player to achieve an overall score of 100+ wins the game')
  # menu that gives options for player on their turn
  print('Menu options:')
  print('"k" or press enter to keep rolling')
  print('"h" to hold and stop round')

def pig_head():
  '''Uses turtle to draw the head of the pig, takes in no parameters and returns nothing'''
  t.goto(0,-60)
  t.pendown()
  t.begin_fill()
  t.circle(100)
  t.penup()
  t.end_fill()

def pig_eyes():
  '''Uses turtle to draw the eyes of the eyes of the pig, takes in no parameters and returns nothing'''
  t.goto(-50,40)
  t.pendown()
  t.color("white")
  t.begin_fill()
  t.circle(20)
  t.penup()
  t.end_fill()
  t.goto(50,40)
  t.pendown()
  t.color("white")
  t.begin_fill()
  t.circle(20)
  t.penup()
  t.end_fill()
  t.goto(-50,55)
  t.pendown()
  t.color("black")
  t.begin_fill()
  t.circle(5)
  t.penup()
  t.end_fill()
  t.goto(50,55)
  t.pendown()
  t.color("black")
  t.begin_fill()
  t.circle(5)
  t.penup()
  t.end_fill()

def pig_nose():
  """Uses turtle to draw the nose of the pig. Takes in no parameters and returns nothing"""
  t.goto(0,0)
  t.pendown()
  t.begin_fill()
  t.color((255, 155, 192), "pink")
  t.circle(25)
  t.shapesize(15,15,1)
  t.penup()
  t.end_fill()
  t.goto(-9,20)
  t.pendown()
  t.begin_fill()
  t.color("black")
  t.circle(5)
  t.shapesize(5,1,1)
  t.penup()
  t.end_fill()
  t.goto(11,20)
  t.pendown()
  t.begin_fill()
  t.color("black")
  t.circle(5)
  t.shapesize(5,1,1)
  t.penup()
  t.end_fill()

def pig_ears():
  """Uses turtle to draw the ears of the pig. Takes in no parameters and returns nothing"""
  t.goto(60, 110)
  t.pendown()
  t.setheading(-30)
  t.begin_fill()
  t.color((255, 155, 192), "pink")
  a = 0.4
  for i in range(120):
      if 0 <= i < 30 or 60 <= i < 90:
          a = a + 0.08
          t.left(3)
          t.forward(a)
      else:
          a = a - 0.08
          t.left(3)
          t.forward(a)
  t.penup()
  t.end_fill()
  t.goto(-55, 110)
  t.pendown()
  t.setheading(33)
  t.begin_fill()
  a = 0.4
  for i in range(120):
      if 0 <= i < 30 or 60 <= i < 90:
          a = a + 0.08
          t.left(3)
          t.forward(a)
      else:
          a = a - 0.08
          t.left(3)
          t.forward(a)
  t.end_fill()

def pig_picture():
  '''Uses turtle to draw the greatest picture of a pig you have ever seen. It takes in no parameters and returns nothing'''
  # turle graphics
  # set up
  t.pensize(4)
  t.hideturtle()
  t.colormode(255)
  t.color((255, 155, 192), "pink")
  t.setup(840, 500)
  t.speed(0)
  pig_head()
  pig_eyes()
  pig_nose()
  pig_ears()
  t.done()

def game(player_1_name, player_2_name, player_1_points, player_2_points):
  '''Runs the game. Takes in the arguments of 4 variables, the player names and their respective points. The function runs until a winner is decided, and until then, continues to loop and write the turn of the next player. Returns name of winner'''
  #while both players have less than 100 points, rounds continue. whichever player reaches 100 points first, they will be named the winner. points are added to each player's total. 
  round_number = 0
  # loop
  while player_1_points < 100 and player_2_points < 100:
    round_number += 1
    print("{}'s turn:".format(player_1_name))
    player_1_points += turn()
    if player_1_points >= 100:
      winner = player_1_name
    if player_1_points < 100:
      print("{}'s turn:".format(player_2_name))
      player_2_points += turn()
    if player_2_points >= 100:
      winner = player_2_name
    game_log(player_1_points, player_2_points, round_number)
  return winner
    
def game_log(player_1_points, player_2_points, round_number):
  '''Appends round data into output file. Takes in the parameters of the player points and the round number. Returns nothing'''
  # file output
  # opens file to append each round's point information
  with open('scoresbyround.csv', 'a') as outputfile:
    outputfile.write('{},{},{}'.format(round_number, player_1_points, player_2_points) + '\n')

def turn():
  '''Goes through a player's turn, takes in no parameters, returns: points earned during the turn'''
  next_input = ''
  input_letter = ''
  round_points = 0
  while next_input != 'h':
    # dice is rolled by random module
    dice_roll = randint(1,6)
    # if-elif-else statement
    if dice_roll == 1:
      print('You rolled a 1! :(')
      return 0
    elif dice_roll == 2:
      print('You rolled a 2!')
      round_points += 2
    elif dice_roll == 3:
      print('You rolled a 3!')
      round_points += 3
    elif dice_roll == 4:
      print('You rolled a 4!')
      round_points += 4
    elif dice_roll == 5:
      print('You rolled a 5!')
      round_points += 5
    else:
      print('You rolled a 6!')
      round_points += 6
    input_letter = input('Keep going (k or enter) or hold (h): ')
    next_input = valid_input_check(input_letter)
  return round_points

def valid_input_check(user_input):
  '''Takes in a variable input to check if the user input is valid. Parameter: user input. Returns the next step, or repeats depending on the user input'''
  while user_input not in 'kh':
    # try-except block
    try:
      user_input = user_input.lower()
      if (user_input != 'k') and (user_input != 'h'):
        while user_input not in 'kh':
          print('Invalid input. Try again. Remember valid input is only "k", "h", or pressing the enter key.')
          user_input = input('Keep going (k or enter) or hold (h): ')
    except:
      while user_input not in 'kh':
        print('Invalid input. Try again. Remember valid input is only "k", "h", or pressing the enter key.')
        user_input = input('Keep going (k or enter) or hold (h): ')
  return user_input


# Main Code - calls introduction and game function
# Calls intro function that prints greeting and instructions
intro()

# User input - both players' names
player_1 = input('Enter player 1 name: ')
player_2 = input('Enter player 2 name: ')

# Create game log file
# file output
with open('scoresbyround.csv', 'w') as outputfile:
  outputfile.write('Round #,' + player_1 + ' Points' + ',' + player_2 + ' Points' + '\n')

# Call game function to play game
winner = game(player_1, player_2, 0, 0)

# Game over message
print('[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅] Congrats! {} won! [̲̅$̲̅(̲̅5̲̅)̲̅$̲̅ '.format(winner))
print('Thanks for playing PIG!')