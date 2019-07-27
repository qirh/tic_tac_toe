# -*- coding: utf-8 -*-

class Player():
  def __init__(self, char, name):
    self.char = char
    self.name = name

class Board():
  board = [] # board of 9 slots
  def draw():
    pass

USER = Player('O', 'player')
COMPUTER = Player('X', 'computer')
PLAYERS = [USER, COMPUTER]

def welcome():
  import os
  import sys
  os.system('clear')

  print('welcome, to tic_tac_toe\n')
  print('please choose a difficulty')

  while True:
    print('1. Easy')
    print('2. Medium')
    print('3. Unmöglich!\n')

    difficulty_input = input('>> ')
    try:
      difficulty = int(difficulty_input)
      if difficulty not in [1, 2, 3]:
        print(f'invalid entry ({difficulty}) should be either 1, 2 or 3')
      else:
        print()
        break
    except ValueError:
      print(f'invalid entry ({difficulty_input}) is not an int')

  if sys.argv[1:] and '-skip_char' not in sys.argv[1:]:
    pick_char()

  play(difficulty)

def pick_char():
  print('accepted chars are ascii[33, 126]')

  for player in PLAYERS:
    user_input = input(f'the {player.name}\'s char is ({player.char}) enter a new char to change it or press enter to skip\n')

    if len(user_input) == 0:
      pass
    elif len(user_input) > 1 or ord(user_input) < 33 or ord(user_input) > 126:
      print('invalid input, keeping default value')
    else:
      player.char = user_input

def play(difficulty):
  print(f'plaaaay {difficulty}')


welcome()
