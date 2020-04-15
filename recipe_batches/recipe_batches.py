#!/usr/bin/python
"""
Map over each recipe and map over each ingredients, check if any ingredient is less in quantity compared to the recipe, if so exit the loop and return error message saying not enough ingredients or something of the sort
Keep track of how many times can a quantity of ingredients go inside a recipe using remainer, based on that keep track if in a variable, return number of batches that can be done
"""

import math

def recipe_batches(recipe, ingredients):
  # initialise list with all numbers of possible batches
  num_batches = []

  # iterate over each ingredient in the recipe
  for ingredient in recipe:
    # if ingredient in recipe is found inside ingredients list
    if ingredient in ingredients.keys():
      # check if quantity in ingredient list is less then in recipe specifications
      if recipe[ingredient] > ingredients[ingredient]:
        # in that case return 0
        return 0
      else:
        # pass the num of batches that can be made with that ingredient
        num_batches.append(ingredients[ingredient] // recipe[ingredient])
    else:
      # return 0 if ingredient is missing from list of ingredients
      return 0

  # find the min value and pass that as the number of batches that can be made
  return min(num_batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))