# -*- coding: utf-8 -*-

class Player():
  def __init__(self, char, name):
    self.char = char
    self.name = name

class Board():

  class Cell():
    def __init__(self, index):
      self.index = index
      self.player = ''
      self.is_free = True

    def __repr__(self):
      if self.is_free:
        return f'({self.index})'
      else:
        return f'({self.player})'

  def __init__(self, row=3, col=3):
    self._row = row
    self.col = col
    # self._board = [[self.Cell(i+row*j) for i in range(col)] for j in range(row)] TODO: variable board
    self._board = [self.Cell(i) for i in range(row*col)]

  def draw(self):
    print(self._board)
    print('', '—'*self.col*6)
    for row in range(self._row):
      print('|', end=' ')
      for col in range(self.col):
        print(self._board[col+row*self._row], end=' | ')
      print()
    print('', '—'*self.col*6)

  def is_game_over(self):
    #TODO:
    return False

  def is_move_legal(self, place):
    return board[place].is_free

USER = Player('O', 'player')
COMPUTER = Player('X', 'computer')
PLAYERS = [USER, COMPUTER]
board  = Board()

def welcome():
  import os
  import sys
  os.system('clear')

  print('welcome, to tic_tac_toe\n')
  print('please choose a difficulty')

  while True:
    print('1. Regular (default)')
    print('2. Unmöglich!\n')

    difficulty_input = input('>> ')
    if difficulty_input == '':
        difficulty = 1
        break
    else:
      try:
        difficulty = int(difficulty_input)
        if difficulty not in [1, 2]:
          print(f'invalid entry ({difficulty}) should be either 1 or 2 or press enter to skip')
        else:
          print()
          break
      except ValueError:
        print(f'invalid entry ({difficulty_input}) is not an int')

  if sys.argv[1:] and '-skip_char' not in sys.argv[1:]:
    pick_char()

  play(difficulty)

def pick_char():
  AASCII_LOWER_BOUND = 65
  AASCII_LOWER_BOUND = 126

  print(f'accepted chars are ascii[{AASCII_LOWER_BOUND}, {AASCII_LOWER_BOUND}]')

  for player in PLAYERS:
    user_input = input(f'the {player.name}\'s char is ({player.char}) enter a new char to change it or press enter to skip\n')

    if len(user_input) == 0:
      pass
    elif len(user_input) > 1 or ord(user_input) < AASCII_LOWER_BOUND or ord(user_input) > AASCII_LOWER_BOUND:
      print('invalid input, keeping default value')
    else:
      player.char = user_input

def who_plays_first(players):
  from random import shuffle
  shuffle(players)
  return PLAYERS[0]

def make_move():
  pass
def play(difficulty):
  turn = who_plays_first(PLAYERS)

  while not board.is_game_over():
    print(f'{turn.name}\'s turn')
    board.draw()

    if turn.name == 'player':
      player_input = input('>> ')

      try:
        move = int(player_input)
        if board.is_move_legal(move):
          pass
        else:
          print('illegal move')
      except ValueError:
        print('invalid move')
    else:
      make_move()

welcome()
