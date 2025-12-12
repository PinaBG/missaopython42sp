#!/usr/bin/env python3

def greetings(nome=None):
    if(nome == None):
        print("Hello, noble stranger.")
    elif(isinstance(nome,str) == False):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {nome}")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
