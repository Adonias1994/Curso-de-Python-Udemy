import tkinter as tk

# Função para calcular o quadrado do número e exibir o resultado em uma nova janela
def calcular_quadrado():
    numero = float(entry.get())
    quadrado = numero * numero

    # Criação da nova janela
    resultado_janela = tk.Toplevel(root)
    resultado_janela.title("Resultado")
    resultado_janela.geometry("200x100")

    # Rótulo para exibir o resultado
    resultado_label = tk.Label(resultado_janela, text=f"O quadrado é: {quadrado}")
    resultado_label.pack(pady=20)

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora de Quadrado")
root.geometry("300x200")

# Rótulo e entrada para receber o número
label = tk.Label(root, text="Digite um número:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

# Botão para calcular o quadrado
botao = tk.Button(root, text="Calcular", command=calcular_quadrado)
botao.pack(pady=10)

# Iniciar o loop de eventos da interface gráfica
root.mainloop()
