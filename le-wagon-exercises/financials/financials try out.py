#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 18:42:04 2020

@author: Lena
"""

import math 
import unittest


def forward_price(spot, interest_rate, time):
    counter = 0
    while counter < time:
        forward_price = spot * math.exp(interest_rate * counter)
        counter += 1
        print (round(forward_price, 2))
    return round(forward_price, 2)

forward_price(5,2.5,7)
              