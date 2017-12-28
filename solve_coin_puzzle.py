#!/usr/bin/env python
"""
This module attempts to solve the coin puzzle found in the maze.

Each of the coins has a given value (when you look at them)

    red      - 2
    concave  - 7
    corroded - 3
    blue     - 9
    shiny    - 5
"""
import itertools


COINS = (2, 3, 5, 7, 9)

for combination in itertools.permutations(COINS):
    a, b, c, d, e = combination
    if a + b * c ** 2 + d ** 3 - e == 399:
        print "Found! Combination is %s" % ', '.join(map(str, combination))
