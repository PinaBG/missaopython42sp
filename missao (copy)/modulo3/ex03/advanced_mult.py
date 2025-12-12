#!/usr/bin/env python3

count = 0
while count <= 10:
    print(f"Table of {count}: ", end="")
    count2 = 0
    while count2 <= 10:
        print(f"{count*count2}", end=" ")
        count2 += 1
    print()
    count += 1
