#!/usr/bin/env python3

array_original =  [2, 8, 9, 48, 8, 22, -12, 2]

array_modificado = []

for i in range(len(array_original)):
    if(array_original[i]>5):
        array_modificado.append(array_original[i] + 2)

array_modificado = sorted(set(array_modificado))

print(array_original)
print(array_modificado)

