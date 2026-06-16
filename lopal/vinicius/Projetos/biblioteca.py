# import tkinter as tk
# from tkinter import messagebox


# def classificação_do_usuário():

#     Opção1= aluno_usuário.get()
#     opção2 = comunidade_usuário.get()

#     if Opção1 == 1 :
#         messagebox.showwarning("Você pode ficar com o livro por até 14 fias de graça")
#     else:
#         messagebox.showinfo("Boa leitura, não se esqueca de devolver o livro de acordo com o prazo")


# janela  = tk.Tk()
# janela.title("Sistema de Empréstimo de Livros ")
# janela.geometry("300x300")
# janela.configure(bg="white")

# lbl_aluno = tk.Label(janela, text="Olá aluno :)")
# lbl_aluno.grid(row=0, column=0, pady=10, padx=10)

# lbl_comunidade = tk.Label(janela, text="Olá comunidade :)")
# lbl_comunidade.grid(row=1, column=0, pady=10, padx=10)

# aluno_usuario = tk.Entry(janela, font=("Arial", 12))
# aluno_usuario.grid(row=0, column=1, pady=10, padx=10)

# comunidade_usuario = tk.Entry(janela, font=("Arial", 12))
# comunidade_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enter", command=classificação_do_usuário)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()

# são 4 def
# 1 menu 
# 2 aluno
# 3 comunidade
# 4 categoria 

import tkinter as tk
from tkinter import messagebox, ttk

# .get() serve para buscar informação na caixa de texto
def janela_bemvindo():
    nome = nome_usuario.get()
    idade = idade_usuario.get()

    if nome == "" and idade == "":
        messagebox.showwarning("Aviso", "Digite seu nome e sua idade :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, {nome} e {idade} - Seja bem-vindo ao nosso sistema")

def segunda_janela():
    segunda_janela = tk.Toplevel(janela)
    segunda_janela.tilte("Segunda Janela")
    segunda_janela.geometry("300x300")


# Configurações da Janela
janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="#CA996F")

lbl_mensagem = tk.Label(janela, text="Digite seu nome :)")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
lbl_mensagem.configure(bg="#754D2A")
lbl_idade = tk.Label(janela, text="Digite sua idade :)")
lbl_idade.grid(row=1, column=0, pady=10, padx=10)
lbl_idade.configure(bg="#754D2A")

nome_usuario = tk.Entry(janela, font=("Arial", 12))
nome_usuario.grid(row=0, column=1, pady=10, padx=10)
idade_usuario = tk.Entry(janela, font=("Arial", 12))
idade_usuario.grid(row=1, column=1, pady=10, padx=10)


sel_nivel = tk.Spinbox(janela, from_=1, to=10, width=10)
sel_nivel.grid(row=2, column=1, pady=10, padx=10)


combo_nivel = tk.ttk.Combobox(janela, values=["Fácil", "Médio", "Difícil"], width=10)
combo_nivel.grid(row=3, column=1, pady=10, padx=10)


btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
btn_mensagem.grid(row=2, column=0, pady=10, padx=10)
btn_mensagem.configure(bg="#754D2A")

btn_segunda_janela = tk.Button(janela, text="Abrindo Segunda Janela", command=segunda_janela)
btn_segunda_janela.grid(row=3, column=0, pady=10, padx=10)
btn_segunda_janela.configure(bg="#754D2A")
e
janela.mainloop()

