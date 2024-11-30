import random
import json


# Função para carregar os tokens gerados
def carregar_tokens():
    try:
        with open("tokens_gerados.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Função para salvar os tokens gerados
def salvar_tokens(tokens):
    with open("tokens_gerados.json", "w") as f:
        json.dump(tokens, f)


# Lista de tokens gerados
tokens_gerados = carregar_tokens()


# Função para gerar um token único
def gerar_token_unico():
    while True:
        token = random.randint(1000, 9999)
        if token not in tokens_gerados:
            tokens_gerados.append(token)
            salvar_tokens(tokens_gerados)
            return token
