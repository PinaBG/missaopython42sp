#!/usr/bin/env python3

import sys

def shrink(string):
    string_slice = slice(0,8)
    print(string[string_slice])

def enlarge(string):
    count = len(string)
    while count < 8:
        string = string + "Z"
        count += 1;
    print(string)

sys.argv.pop(0)

if(len(sys.argv) == 0):
    print("none")
else:
    for i in range(len(sys.argv)):
        qtdLetras = len(sys.argv[i])
        if(qtdLetras > 8):
            shrink(sys.argv[i])
        elif(qtdLetras < 8):
            enlarge(sys.argv[i])
        else:
            print(sys.argv[i])
