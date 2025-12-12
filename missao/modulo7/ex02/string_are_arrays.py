#!/usr/bin/env python3

import sys

sys.argv.pop(0)

printou = False

if(len(sys.argv) > 0):
    for letra in sys.argv[0]:
        if(letra == "z"):
            printou = True
            print(letra,end="")

print()
if(printou==False):
    print("none")
