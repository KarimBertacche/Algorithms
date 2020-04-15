#!/usr/bin/python
"""
UNDERSTANDING THE PROBLEM:
Given a list of numbers, check which is the highest in the list, store the index,
and based on that check from the first index to that index for the lowest value and store the index in a variable as well
Then, you want to subtract the highest by the lowest and return the result of that operation
"""

import argparse

def find_max_profit(prices):
  #store both lowest and highest prices in indexes
  highest_idx, lowest_idx = 1, 0

  # iterate over each price from first index 
  # as there are no prior value to compare it too
  for idx in range(1, len(prices)):
    # over each iteration check if new iteration price is 
    # higher then previously stored highest value
    if prices[idx] > prices[highest_idx]:
      # if so set new highest price index to highest_idx var
      highest_idx = idx
  
  # now iterate over the new array/list from start to highest value index
  for idx in range(highest_idx):
    # if new iteration stock price is lower than previously stored one
    if prices[idx] < prices[lowest_idx]:
      # store index for new lowest value
      lowest_idx = idx

  # return the subtraction of the highest recorded value, 
  # minus the lowest prior value 
  return int(prices[highest_idx]) - int(prices[lowest_idx])

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))