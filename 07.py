'''
Leia uma temperatura em graus Frahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius
e F a temperatura em Frahrenheit.
'''

# f = Celsius
f = float(input("\nInforme a temperatura em Fahrenheit que você deseja converter para graus Celsius: "))

c = 5 * (f - 32.0) / 9.0
c = round(c, 2) # Função para arrendondar para apenas duas casas decimais após o ponto

print("Em graus Celsius são: ", c, "\n")
