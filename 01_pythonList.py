"""
This file uses list comprehensions and list in order to display the list of values to the console.
The below file show how to use list comprehensions for the project.

"""
import os
import random
import timeit


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn):
  return txn * (1 + TAX_RATE)


final_prices = [get_price_with_tax(i) for i in txns]
print(final_prices)



colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)
