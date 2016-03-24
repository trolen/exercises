#!/usr/bin/env python
from math import *

# Main program
while True:
    try:
        number = input("Enter a non-negative integer (ctrl-c to quit): ")
        n = int(number)
    except:
        break
    if not (number == n and n >= 0):
        continue
    fact_str = str(factorial(n))
    count_zeros = 0
    for i in range(1,len(fact_str)+1):
        if not fact_str[-i] == "0":
            break
        count_zeros += 1
    print str(n) + "! = " + fact_str + " -- " + str(count_zeros) + " trailing zero(s)"
