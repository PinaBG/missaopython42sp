#!/usr/bin/env python3

import sys

sys.argv.pop(0)

if(len(sys.argv) != 1):
    print("none")
else:
    mensagem = input("What was the parameter? ")
    if(mensagem == sys.argv[0]):
        print("Good job!")
    else:
        print("Nope, sorry...")
