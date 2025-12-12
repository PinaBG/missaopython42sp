#!/usr/bin/env python3

import sys

sys.argv.pop(0)

if(len(sys.argv)==0):
    print("none")
else:
    for i in sys.argv:
        if(i.find("ism",len(i)-3,len(i)) == -1):
            print(i,end="ism\n")
