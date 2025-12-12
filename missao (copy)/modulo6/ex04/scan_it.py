#!/usr/bin/env python3

import sys
import re

sys.argv.pop(0)

if(len(sys.argv) != 2):
    print("none")
else:
    array_encontradas = re.findall(sys.argv[0],sys.argv[1])
    quantidade = len(array_encontradas)
    if(quantidade == 0):
        print("none")
    else:
        print (len(array_encontradas))
