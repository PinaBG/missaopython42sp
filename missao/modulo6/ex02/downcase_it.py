#!/usr/bin/env python3

import sys

sys.argv.pop(0)

if(len(sys.argv) != 1):
    print("none")
else:
    print(sys.argv[0].lower())
