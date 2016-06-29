#!/usr/bin/python3
"""
Brain.py
A highly unoptimized Brainf*ck interpreter (obviously written in Python)
"""

import sys
import os.path

#Initialize memory banks as well as the default position
reg = [0] * 30000
pos = 0

#Read input file and put it in a list
arg = str(sys.argv[1:]).strip("[]'")
if not os.path.isfile(arg):
    print('Usage: brain.py foo.b');exit()
code = list(open(arg, 'r').read())
code = [x.strip() for x in code]

#Takes care of loop statements
def loop(code):
    temp = []
    blocks = {}
    for i in range (len(code)):
        if code[i] == '[':
            temp.append(i)
        elif code[i] == ']':
            blocks[i] = temp[-1]
            blocks[temp.pop()] = i
    return blocks

blocks = loop(code)

i = 0
while i < len(code) :
    if code[i] == '+':
        reg[pos]+=1
        if reg[pos] > 255 : reg[pos] = 0
    elif code[i] == '-' :
        reg[pos]-=1
        if reg[pos] < 0 : reg[pos] = 255
    elif code[i] == '>' :
        pos += 1
        if pos > len(reg): print('Out of memory !');pos = 0
    elif code[i] == '<' :
        pos -= 1
        if pos < 0: print('Out of memory !');pos = 0
    elif code[i] == '[':
        if reg[pos] == 0 : i = blocks[i]
    elif code[i] == ']' :
        if reg[pos] != 0 : i = blocks[i]
    elif code[i] == '.' :
        print(chr(reg[pos]), end='')
    elif code[i] == ',' :
        reg[pos] = ord(input('input ?'))
    i += 1
#print(reg[1], reg[2], reg[3], reg[4], reg[5],"\n")