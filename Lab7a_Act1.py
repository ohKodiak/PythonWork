# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ezra Jeter, Nathan Hung, Maitri Shekar, Elliot Han
# Section:      213
# Team:         11
# Assignment:   Lab7a_Act1
# Date:         16 October 2021

# Create and initialize variables
user_input = '' # string
moving_piece = '' # string, tracks color of moving piece
checkers_board = [] # list
row = 0 # int, iterator variable
column = 0 # int, iterator variable
i = 0 # int, iterator variable for changing list values into integers
formatted_input = [] # list, split values of user_input
first_coordinate = [] # list
second_coordinate = [] # list
x1 = 0 # int
y1 = 0 # int
x2 = 0 # int
y2 = 0 # int
valid_characters = ' 01234567' # string, numbers 0-7 and spaces allowed
valid_character_input = True # boolean, if input only has numbers 0-7 and spaces
char = '' # string, iterator variable to check for valid characters in input

# Print user instructions
print('Input instructions:')
print('Type four numbers within the range of 0 to 7, separated with spaces.')
print('The first two numbers should represent the location of the piece you'
      '\nwant to move (row number starting from the top, then column number'
      '\nstarting from left), and the second two numbers should represent the'
      '\nlocation of where you want this piece to move (same coordinate system).')
print('Note: Row and column numbers start at 0. Ex: The top row is row 0.')
print('For example, a valid input would be “5 0 4 1”.')
print('Type “stop” if you want to end the game/program.')

# Create checkers board (in starting position)
checkers_board = [
['.', chr(9675), '.', chr(9675), '.', chr(9675), '.', chr(9675)],
[chr(9675), '.', chr(9675), '.', chr(9675), '.', chr(9675), '.'],
['.', chr(9675), '.', chr(9675), '.', chr(9675), '.', chr(9675)],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
[chr(9679), '.', chr(9679), '.', chr(9679), '.', chr(9679), '.'],
['.', chr(9679), '.', chr(9679), '.', chr(9679), '.', chr(9679)],
[chr(9679), '.', chr(9679), '.', chr(9679), '.', chr(9679), '.']]

# Initial user input to start game
user_input = input('Please click enter to begin.')

# loop that plays the game - checks for valid input and moves pieces
while (user_input != 'stop') and (user_input != 'Stop'):
  # display/print current checkers board
  print()
  for row in checkers_board:
    for column in row:
      print(column, end = ' ')
    print()
  print()

  # get next move/input from user
  user_input = input('Please type the coordinates of your next move, or type "stop" to end the game: ')
  if (user_input == 'stop') or (user_input == "Stop"):
    continue
  
  # check for valid input
  # check for invalid characters
  for char in user_input:
    if char not in valid_characters: # checks each character to make sure they are all valid
      valid_character_input = False
  if valid_character_input == False:
    print('Invalid character found in input. Only numbers 0-7 and spaces are allowed. Please try again.')
    continue
  # creates list out of the user input formatted by spaces
  formatted_input = user_input.split()
  # checks for length (wants 4)
  if len(formatted_input) != 4:
    print('Invalid input length (requires 4 numbers). Please try again.')
    continue
  # checks for each value being between 0 and 7
  for i in range(len(formatted_input)):
    # change values to integers
    formatted_input[i] = int(formatted_input[i])
  if formatted_input[0] not in range(8):
    print('Invalid input. Numbers can only be from 0 to 7. Please try again.')
    continue
  if formatted_input[1] not in range(8):
    print('Invalid input. Numbers can only be from 0 to 7. Please try again.')
    continue
  if formatted_input[2] not in range(8):
    print('Invalid input. Numbers can only be from 0 to 7. Please try again.')
    continue
  if formatted_input[3] not in range(8):
    print('Invalid input. Numbers can only be from 0 to 7. Please try again.')
    continue
  # checks if there is a piece on the first coordinate
  first_coordinate = [formatted_input[0], formatted_input[1]]
  # creates list that houses the coordinate of the initial selected space
  y1 = first_coordinate[0]
  x1 = first_coordinate[1]
  if checkers_board[y1][x1] == '.':
    print("Invalid input. There is no piece on your first coordinate. Please try again.")
    continue
  # checks if the second coordinate is a dark square
  second_coordinate = [formatted_input[2], formatted_input[3]]
  y2 = second_coordinate[0]
  x2 = second_coordinate[1]
  if y2 % 2 == 0:
    if x2 % 2 != 1:
      print("Invalid input. The second coordinate is not a dark square. Please try again.")
      continue
  if y2 % 2 == 1:
    if x2 % 2 != 0:
      print("Invalid input. The second coordinate is not a dark square. Please try again.")
      continue
  
  # move the piece
  moving_piece = checkers_board[y1][x1]
  checkers_board[y1][x1] = '.' # remove piece off of space
  checkers_board[y2][x2] = moving_piece # change location of piece to second coordinate

print()
print('Game over.')
print('Good game. Thanks for playing!')