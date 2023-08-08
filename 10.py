'''
Leia uma velocidade em km/h (quilômetros por hora) e apresenta-a convertida em m/s
(metros por segundo). A fórmula da conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s. 
'''

import os
os.system('cls')

vel_k = float(input('\nInforme a velocidade em km/h: ')) # vel_k -> velocidade em km/h
vel_m = vel_k / 3.6 # vel_m -> velocidade em metros por segundos
vel_m = round(vel_m, 2) # Limita o número de casas decimais
print('A velocidade em metros por segundo são:', vel_m, '\n')
