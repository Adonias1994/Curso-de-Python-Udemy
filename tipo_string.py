import os
os.system('cls')

print('\nLembre-se de também abrir o código e ler os comentários para um melhor entendimento.\n')

"""
Tipo String

Em Python, um dado é considerado string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

a_s = 'uma string'
a_d = "234"
a_s_t = '''a'''
a_d_t = """True"""

print('\nExemplo de aspas simples: ', a_s, '\nExemplo de aspas duplas: ', a_d, '\nExemplo de aspas simples triplas: ', a_s_t, '\nExemplo de aspas duplas triplas: ', a_d_t, '\n')

# Geralmente é mais utilizado as aspas simples, mas em alguns casos se faz necessário aspas duplas conforme exemplo abaixo

nome = "Gina's Bar" # A string possuia uma aspas simples no nome, logo se fez necessário a utilização de asplas duplas
print(nome)
print(type(nome), '\n')

# Exemploas para pular linhas em Python

nome_2 = 'Adonias\nPessoa' # O \n pula uma linha em Python
nome_3 = """Adonias
Pessoa""" # Assim também é possível pular uma linha em Python

print(nome_2)
print(type(nome_2), '\n')
print(nome_3)
print(type(nome_3), '\n')

nome_4 = 'Juliana Karoliny'

print(nome_4.upper(), '\n') # Transforma todas as letras em maiúsculas
print(nome_4.lower(), '\n') # Transforma todas as letras em minúsculas
print(nome_4.split(), '\n') # Transforma em uma lista de string
