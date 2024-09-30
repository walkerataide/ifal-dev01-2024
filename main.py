from ifal_library import get_int, get_float, get_string

idade = get_int("Digite sua idade: ")
altura = get_float("Digite sua altura: ")
nome = get_string("Digite seu nome: ")

print(f"Olá, {nome}! Você tem {idade} anos e {altura} metros de altura.")
