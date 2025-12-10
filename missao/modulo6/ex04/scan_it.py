#!/usr/bin/env python3

import sys
import re

if(len(sys.argv) <= 2):
    print("none")
else:
    array_encontradas = re.findall(sys.argv[1],sys.argv[2])
    quantidade = len(array_encontradas)
    if(quantidade == 0):
        print("none")
    else:
        print (len(array_encontradas))
