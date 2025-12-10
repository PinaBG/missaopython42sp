#!/usr/bin/env python3

import sys

lista_parametros = sys.argv

if(len(lista_parametros) == 1):
    print("none")
else:
    lista_parametros.pop(0)
    print(f"parameters: {len(lista_parametros)}")
    for i in range(len(lista_parametros)):
        print(f"{lista_parametros[i]}: {len(lista_parametros[i])}")
