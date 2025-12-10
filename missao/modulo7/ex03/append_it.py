#!/usr/bin/env python3

import sys

if(len(sys.argv)==1):
    print("none")
else:
    sys.argv.pop(0)
    for i in sys.argv:
        if(i.find("ism") == -1):
            print(i,end="ism\n")
