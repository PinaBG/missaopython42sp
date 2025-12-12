#!/usr/bin/env python3

import sys

sys.argv.pop(0)

def downcase_it(string):
    return string.lower()

if(len(sys.argv) == 0):
    print("none")
else:
    for i in sys.argv:
        print(downcase_it(i))
