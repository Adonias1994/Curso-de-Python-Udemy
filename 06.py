'''
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius
'''

# c = graus em Celsius
c = float(input("\nInforme a temperatura em graus Celsius que você deseja converter para Fahrenheit: "))

# f = graus em Fahrenheit
f = c * (9.0/5.0) + 32.0

print("Em Fahrenheit são: ", f, "\n")
