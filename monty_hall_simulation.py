#!/usr/bin/python

import random as rand

number_games = 1000000

def set_stage():
  winning_door = rand.randint(0,2)
  stage = [0, 0, 0]
  stage[winning_door] = 1
  return stage

def play_game(switch):
    stage = set_stage()
    selected_door = rand.randint(0,2)
    # Open wrong door
    return (stage[selected_door] == 1 and not switch) or (stage[selected_door] == 0 and switch)


if __name__ == '__main__':
    number_wins = 0
    number_losses = 0
    switch = False
    for game_number in range(number_games):
      if play_game(switch):
        number_wins+=1
      else:
         number_losses+=1
    print("We are " + ("not " if not switch else "") + "switching")
    print("Number of wins: " + str(number_wins))
    print("Number of losses: " + str(number_losses))

    number_wins = 0
    number_losses = 0
    switch = True
    for game_number in range(number_games):
      if play_game(switch):
        number_wins+=1
      else:
         number_losses+=1
    print("We are " + ("not " if not switch else "") + "switching")
    print("Number of wins: " + str(number_wins))
    print("Number of losses: " + str(number_losses))
