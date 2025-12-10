#!/usr/bin/env python3

import sys

printou = False

if(len(sys.argv) > 1):
    for letra in sys.argv[1]:
        if(letra == "z"):
            printou = True
            print(letra,end="")

if(printou==False):
    print("none")
