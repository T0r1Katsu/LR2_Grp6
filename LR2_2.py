# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 21:37:17 2022

@author: user
"""

file = input('Please input the text file name : ')

numblines = []

with open(file, 'r') as f:
    for line in f:
        numblines.append(line.strip())

while True:
    print('Lines in text file:', len(numblines))
    
    
    if len(numblines) == 0:
        break
    lineNumber = int(input('Input the line number of the text you wish to display or press 0 to discontinue: '))
    if lineNumber == 0:
        print('Program Closing...')
        break
    elif lineNumber > len(numblines):
        print('The inputted line exceeds the amount of lines in the text file')    
    else:
        print('On line ',lineNumber, 'the text is: ', numblines[lineNumber - 1])
