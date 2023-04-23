"""
Tipo Booleano

Vem da Albebra Booleana que foi criada por George Boole

Existem duas constantes, Verdadeiro ou Falso
 
Em Python são representadas por:
True -> Verdadeiro
False -> Falso

Obs:. Sempre com a iniciação maiúscula

Errado:
true, false

Certo:
True, False

"""

ativo = False
print(ativo)

"""
Operações básicas:
"""

# Negação (not):

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro, ou seja, sempre o contrário.
"""
print(not ativo)

# Ou (or):

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro será verdadeiro.
"""

ou1 = True or True
ou2 = True or False
ou3 = False or True
ou4 = False or False

print(ou1, ou2, ou3, ou4)

# E (and):

"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os dois valores devem ser verdadeiro.
"""

e1 = True and True
e2 = True and False
e3 = False and True
e4 = False and False

print(e1, e2, e3, e4)
