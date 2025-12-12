#!/usr/bin/env python3

import sys

sys.argv.pop(0)

if(len(sys.argv) < 2):
    print("none")
else:
    count = len(sys.argv)-1
    while count >= 0:
        print(sys.argv[count])
        count -= 1

