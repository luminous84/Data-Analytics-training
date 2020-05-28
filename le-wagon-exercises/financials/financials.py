# pylint: disable=missing-docstring
import math 
import unittest

# TODO: 1st exercise: Define the `forward_price` function
def forward_price(spot, interest_rate, time):
   forward_price = spot * math.exp(interest_rate * time)
   return round(forward_price, 2)


# TODO: 2nd exercise: Define the `short_pnl` function
def short_pnl(positions, mtm):
    i = 0
    result = 0
    for i in range(len(positions)):
        result = result + (positions[i] - mtm[i])
        i += 1
        print(result)
    return result

short_pnl([1, 2, 3],[4, 5, 6])    


# second try
def short_pnl2(positions, mtm):
    i = 0
    result = 0
    for i in range(len(positions)):
        result = result + (positions[i] - mtm[i])
        i += 1
    return result

print(short_pnl2([1, 2, 3],[4, 5, 6]))


