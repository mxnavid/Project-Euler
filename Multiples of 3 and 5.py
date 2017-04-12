#Author : Mohammed Nafiuzzaman
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import math

def number():
    three = []
    five = []
    for i in list(range(1000)):
        if int(i) % 3 == 0:
            three.append(i)
        elif int(i) % 5 == 0:
            five.append(i)
    final = []
    final += three
    final += five
    a = sum(final)
    print(a)
number()

