#!/usr/bin/env python3

mensagem: str
mensagem = input("What you gotta say? ")
while True:
    if(mensagem == "STOP"):
        break
    mensagem = input("I got that! Anything else? : ")
