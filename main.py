#!/usr/bin/python3
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
  def __repr__(self):
    return self.char

class Board:

  class Cell:
    def __init__(self, index):
      self.index = index
      self.player = ''
      self.is_free = True

    def __repr__(self):
      if self.is_free:
        return f'({self.index})'
      else:
        return f'({self.player})'

    def __eq__(self, other):
      if isinstance(other, self.__class__):
        return self.__str__() == other.__str__()
      return False

  def __init__(self, size=3, col=3):
    self._size = size
    self._board = [self.Cell(i) for i in range(size*size)]
    self.list_of_random_moves = [i for i in range(size*size)]
    self.free_cells = len(self.list_of_random_moves)
    shuffle(self.list_of_random_moves)

  def __repr__(self):
    printed_board = ''
    printed_board += ' ' + '—'*self._size*6 + '\n'
    for row in range(self._size):
      printed_board += '| '
      for col in range(self._size):
        printed_board += self._board[col+row*self._size].__str__() + ' | '
      printed_board += '\n'
    printed_board += ' ' + '—'*self._size*6

    return printed_board

  def is_game_over(self, move, player):
    #1. win condition
    #1(a). row & col win
    for i in range(self._size):
      if move >= i*self._size and move < (i+1)*self._size:
        # check row victory
        row = [self._board[j] for j in range(i*self._size, (i+1)*self._size)]
        if all(cell==row[0] for cell in row):
          return {
            'game_over': True,
            'win': True,
            'player': player,
            'win_condition': 'row',
            'index': i,
          }

        # check col victory
        first_row = move
        while first_row >= self._size:
          first_row -= self._size
        col = [self._board[k] for k in range(first_row, (self._size*self._size), self._size)]
        if all(cell==col[0] for cell in col):
          return {
            'game_over': True,
            'win': True,
            'player': player,
            'win_condition': 'col',
            'index': first_row,
          }
    #1(b). diagonal win, only odd sized boards
    if self._size%2 != 0:
      if move == (self._size//2)*self._size + (self._size//2):
        pass # this is diag

    #2. no one won, but no more moves (tie)
    if self.free_cells <= 0:
      return {
        'game_over': True,
        'tie': True
      }

    #3. no one won and there are still moves
    return {
        'game_over': False,
      }
  def _is_move_legal(self, move):
    try:
      return self._board[move].is_free
    except Exception as e:
      return False

  def make_move(self, move, player):
    if not self._is_move_legal(move):
      raise IllegalMove(f'move {move} is not allowed')
    self._board[move].is_free = False
    self._board[move].player = player
    self.free_cells -= 1

    return {
      'move': move,
      **self.is_game_over(move, player),
    }

HUMAN = Player('O', 'human')
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
  chars = 'players will play with the following chars\n'
  for player in PLAYERS:
    chars += f'\t- {player.name} ({player.char})\n'
  print(chars)

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
    for index, move in enumerate(board.list_of_random_moves[:]):
      try:
        result = board.make_move(move, COMPUTER)
        board.list_of_random_moves = board.list_of_random_moves[index:]
        result['move']  = move
        return result
      except IllegalMove:
        pass

  else:
    # TODO: difficulty
    pass

def play(difficulty):
  turn_index = who_plays_first(PLAYERS)
  turn = PLAYERS[turn_index]

  while True:
    print(f'<<<{turn.name}\'s turn>>>')

    if turn.name == 'human':
      print(board)
      player_input = input('>> ')

      try:
        move = int(player_input)
        try:
          result = board.make_move(move, HUMAN)
        except IllegalMove:
          print('illegal move\n')
          continue
      except ValueError:
        print('invalid move\n')
        continue
    else:
      result = computer_pick_move(difficulty)

    if result['game_over']:
      print(board)
      print('Game Over.', end=' ')
      if result.get('win'):
        print(f'player {turn.name} has won. Winning {result["win_condition"]} @index #{result["index"]}')
      elif result.get('tie'):
        print('¡Game Tied!')
      break
    else:
      print(f'{turn.name} played at index {result["move"]}\n')
      turn_index = (turn_index + 1) % 2
      turn = PLAYERS[turn_index]

welcome()
