#!/usr/bin/env python3

array_original =  [2, 8, 9, 48, 8, 22, -12, 2]

array_modificado = []

for i in range(len(array_original)):
    array_modificado.append(array_original[i] + 2)

print(f"Original array: {array_original}")
print(f"New array: {array_modificado}")
