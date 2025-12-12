#!/usr/bin/env python3

import sys

sys.argv.pop(0)

lista_retorno = []

if(len(sys.argv) != 2):
    print("none")
elif(sys.argv[0] > sys.argv[1]):
    print("none")
else:
    for i in range(int(sys.argv[0]),int(sys.argv[1])+1):
        lista_retorno.append(i)

    print(lista_retorno)
    
