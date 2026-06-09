# Interface Gráfica com TKINTER
# Componentes Principais (Midgets)

# tk: Janela principal
# Label: Texto ou rotulo
# Button: Um botão clicável
# Entry: Um campo de entrada de texto

import tkinter as tk
from tkinter import messagebox

# 1.Criar a janela principal

Janela = tk.Tk()
Janela.title("Minha primeira janela GUI")
Janela.geometry("400x200") # Largura x Altura

# 2.Criar a função que o botão irá executar
def mostrar_messagem():
    messagebox.showinfo("Sucesso!", " Você clicou no botão :")

# 3.Criar os componentes
lbl_titulo_pagina = tk.Label(Janela, text="Bem-vindo a aula de Interface Gráfica! Aula12(PYTHON)", font=("Arial", 14, "bold"))
btn_clique_pagina = tk.Button(Janela, text= "clique Aqui", font=("Arial", 14, "bold"), bg="#ff0000", fg="black", command=mostrar_messagem)
btn_fechar_Janela = tk.Button(Janela, text="Fechar", font=("Arial", 14), bg="#ffee00", fg="black", command=mostrar_messagem)
# 4.Posicionar os componentes na Janela
lbl_titulo_pagina.pack(pady=20)
btn_clique_pagina.pack(pady=10)


# 5. Rodar o loop da interface
Janela.mainloop()
