#!/usr/bin/env python3

def array_de_nomes(dicionario):
    array = []
    for chave,valor in dicionario.items():
        nome_completo = f"{chave.capitalize()} {valor.capitalize()}"
        array.append(nome_completo)
    return array

pessoas = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_de_nomes(pessoas))
