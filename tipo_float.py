import os
os.system('cls')

"""
Tipo Float ou Tipo real, decimal

O separador de casas decimais em Python é o ponto(.) não a vírgula(,).
"""

# Errado se a intenção for executar um float, mas certo se a intenção for executar uma tuple
valor1 = 1, 44
print(valor1)
print(type(valor1)) # Ao ser reproduzido Python vai achar que trata-se de uma tuple

# Certo se a intenção for executar um float
valor2 = 1.44
print(valor2)
print(type(valor2))

# Exemplo de dupla atribuição
valor3, valor4 = 1, 44
print(valor3, valor4)

# Exemplo de conversão do tipo Float para Int
conversao = (int(valor2))
print(conversao)
print(type(conversao))
