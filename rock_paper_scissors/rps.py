#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  def results_builder(plays_list, num_of_plays):
    # base case to stop recursive function and append combinations for a single play
    # on the results list
    if num_of_plays == 0:
      return results.append(plays_list)

    # iterate over each play and play out all possible combination 
    # for each concatonating the list of plays to the current iterated play
    # decrease num of plays by one on each recursion so to activate base case and 
    # return combination, then repeat same process for the next play
    for play in rps_list:
      results_builder([*plays_list, play], num_of_plays - 1)

  rps_list = ['rock', 'paper', 'scissors'];
  results = []

  results_builder([], n)
  
  return results


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')