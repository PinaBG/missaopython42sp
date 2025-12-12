#!/usr/bin/env python3

idade = int(input("Por favor, me diga sua idade: "))
soma_idades = (10,20,30)
print(f"Você tem atualmente {idade} anos de idade.")

for i in soma_idades:
    print(f"Em {i} anos, você terá {idade+i} anos de idade.")

