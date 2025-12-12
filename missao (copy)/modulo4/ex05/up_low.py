#!/usr/bin/env python3

texto = input("Insira uma String:\n")

for i in range(len(texto)):
    if(texto[i].isupper()):
        print(texto[i].lower(),end="")
    else:
        print(texto[i].upper(),end="")
print()
