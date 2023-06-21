while True:
    try:
        print("\nDigite um número real ou 'sair' para encerrar o programa.")

        entrada = input("Informe um número real: ")

        if entrada.lower() == "sair":
            break

        real = float(entrada)
        quinta = real / 5

        # Formatar o resultado com duas casas decimais
        quinta_formatada = "{:.2f}".format(quinta)

        print(f"A quinta parte do número é: {quinta_formatada}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número real válido.")
