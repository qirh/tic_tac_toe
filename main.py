# -*- coding: utf-8 -*-

import os
import sys
from random import randint, shuffle

class IllegalMove(Exception):
   pass

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
    self.list_of_random_moves = [i for i in range(row*col)]
    shuffle(self.list_of_random_moves)

  def __repr__(self):
    printed_board = ''
    printed_board += ' ' + '—'*self.col*6 + '\n'
    for row in range(self._row):
      printed_board += '| '
      for col in range(self.col):
        printed_board += self._board[col+row*self._row].__str__() + ' | '
      printed_board += '\n'
    printed_board += ' ' + '—'*self.col*6 + '\n'

    return printed_board

  def is_game_over(self, move):
    #TODO:
    return False

  def _is_move_legal(self, move):
    try:
      return self._board[move].is_free
    except Exception as e:
      print('here', e)
      return False

  def make_move(self, move, player):
    if not self._is_move_legal(move):
      raise IllegalMove(f'move {move} is not allowed')
    self._board[move].is_free = False
    self._board[move].player = player.char
    print(self._board[move])


HUMAN = Player('O', 'player')
COMPUTER = Player('X', 'computer')
PLAYERS = [HUMAN, COMPUTER]
board  = Board()

def welcome():
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
    human_input = input(f'the {player.name}\'s char is ({player.char}) enter a new char to change it or press enter to skip\n')

    if len(human_input) == 0:
      pass
    elif len(human_input) > 1 or ord(human_input) < AASCII_LOWER_BOUND or ord(human_input) > AASCII_LOWER_BOUND:
      print('invalid input, keeping default value')
    else:
      player.char = human_input

def who_plays_first(players):
  return randint(0, len(players) - 1)

def computer_pick_move(difficulty):
  if difficulty == 1:
    for move in board.list_of_random_moves:
      try:
        board.make_move(move, COMPUTER)
        break
      except IllegalMove:
        pass

  # TODO: board.is_game_over()
  return
def play(difficulty):
  turn_index = who_plays_first(PLAYERS)
  turn = PLAYERS[turn_index]

  while True:
    print(f'<<<{turn.name}\'s turn>>>')

    if turn.name == 'player':
      print(board)
      player_input = input('>> ')

      try:
        move = int(player_input)
        try:
          board.make_move(move, HUMAN)
        except IllegalMove:
          print('illegal move')
      except ValueError:
        print('invalid move')
        continue
    else:
      computer_pick_move(difficulty)
    print(board)
    turn_index = (turn_index + 1) % 2
    turn = PLAYERS[turn_index]

welcome()
