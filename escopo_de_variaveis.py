import os
os.system('cls')

"""
Escopo de variáveis

Escopo é a propriedade que determina onde uma variável pode ser utilizada como um identificador em um programa.
Uma variável declarada em uma função é normalmente local; o contexto define o escopo.

Dois casos de escopos:

1 - Variáveis globais;
    Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais
    Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado ao
    bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_varivavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o
tipo de dado dela. Este tipo é inferido ao atribuírmos um valor a mesma.
"""

numero = 42
print(numero)
print(type(numero))
