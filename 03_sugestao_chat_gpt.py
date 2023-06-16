import os

def calcular_soma(val1, val2, val3):
    return val1 + val2 + val3

def main():
    os.system('cls')  # Limpar a tela (para sistemas baseados em Unix)
    
    try:
        val1 = int(input('Digite o primeiro valor: '))
        val2 = int(input('Digite o segundo valor: '))
        val3 = int(input('Digite o terceiro valor: '))
        
        soma = calcular_soma(val1, val2, val3)
        print('\nA soma dos três valores é:', soma)
    except ValueError:
        print('Erro: Insira apenas valores inteiros válidos.')

if __name__ == '__main__':
    main()