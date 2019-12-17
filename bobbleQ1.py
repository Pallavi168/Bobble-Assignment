#!/usr/bin/env python3

# To run this file:
# > python bobbleQ1.py inputFile
# or:
# > chmod +x bobbleQ1.py
# > ./bobbleQ1.py inputFile

import sys #system specific parameters and functions
import csv #reading and writing csv file
f = open(sys.argv[1]) #list 
r = csv.reader(f, delimiter=',', quotechar='\'', skipinitialspace=True)
data = []
for i in r:
    data.append(i)

output = []

#function to perform permutation
def func(i, t):
    if i == len(data):
        output.append(t)
        return

    for s in data[i]:
        func(i+1, t + s)
func(0, '')

print(*output, sep=', ')