#!/usr/bin/python

import random as rand

number_of_tries = 1000

def set_stage():
  winning_door = rand.randint(1, 3)
  stage = [0, 0, 0]
  stage[winning_door] = 1
  return stage

if __name__ == '__main__':
    stage = set_stage()
