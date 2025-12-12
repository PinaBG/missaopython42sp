#!/usr/bin/env python3

def average(dicionario):
    media = 0
    qtd_notas = 0
    for valor in dicionario.values():
        qtd_notas += 1
        media += valor
    media = media / qtd_notas
    return media

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
