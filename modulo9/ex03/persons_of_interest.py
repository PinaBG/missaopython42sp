#!/usr/bin/env python3

def data_nascimento(chave_valor):
    return chave_valor[1]["date_of_birth"]

def famous_births(dicionario):
    #dicionario = dict(sorted(dicionario.items(), key=lambda chave_valor: chave_valor[1]['date_of_birth']))
    dicionario = dict(sorted(dicionario.items(), key=data_nascimento))
    for valor in dicionario.values():
        print(f"{valor.get('name')} is a great scientist born in {valor.get('date_of_birth')}")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
