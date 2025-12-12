#!/usr/bin/env python3

import sys

sys.argv.pop(0)

lista_parametros = sys.argv

if(len(lista_parametros) == 0):
    print("none")
else:
    print(f"parameters: {len(lista_parametros)}")
    for i in range(len(lista_parametros)):
        print(f"{lista_parametros[i]}: {len(lista_parametros[i])}")
