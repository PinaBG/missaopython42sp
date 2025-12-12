#!/usr/bin/env python3

def selection(item):
    if(item[1] == "red"):
        return True
    else:
        return False

def find_the_redheads(dicionario):
    #filtro = dict(filter(lambda item: item[1] == "red", dicionario.items()))
    filtro = dict(filter(selection, dicionario.items()))
    return list(filtro.keys())

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
