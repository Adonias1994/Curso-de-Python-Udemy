'''
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
fórmula de conversão é: C = K - 273,15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
'''

# k = Kelvin
k = float(input("\nInforme a temperatura em graus Kelvin para converter para graus Celsius: "))

# c = Celsius
c = k - 273.15
c = round(c, 2) # Limita o número de casas decimais após o ponto/vírgula

print("A temperatura em graus Celsius é:", c, "\n")
