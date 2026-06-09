import tkinter as tk
from tkinter import messagebox

Janela = tk.Tk()
Janela.title("Registro de Operador:")
Janela.geometry("400x200")
Janela.configure(bg="#FFFFFF")

def janela_bemvindo():
   nome_operador = nome_operador_maq.get()
   pri_Turno = turno_operador.get()
#    seg_Turno = B_operador.get()
#    ter_Turno = C_operador.get()
   

   if pri_Turno == "" and nome_operador == "":
    messagebox.showwarning("Por favor, preencha todos os campos corretamente.")

   else:
    messagebox.showinfo("Registro Completo", f"Operador do pri_Turno: {pri_Turno}\nOperador: {nome_operador}")
                                                                                                                                        

lbl_mensagem = tk.Label(Janela, text="Digite seu Turno:)")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
lbl_mensagem.configure(bg="#FF0000")
lbl_operador = tk.Label(Janela, text="Digite seu nome:")
lbl_operador.grid(row=1, column=0, pady=10, padx=10)
lbl_operador.configure(bg="#940000")

turno_operador = tk.Entry(Janela, font=("Arial", 12))
turno_operador.grid(row=0, column=1, pady=10, padx=10)
nome_operador_maq = tk.Entry(Janela, font=("Arial", 12))
nome_operador_maq.grid(row=1, column=1, pady=10, padx=10)


btn_enviar = tk.Button(Janela, text="Enviar", command=janela_bemvindo)
btn_enviar.grid(row=2, column=0, pady=10, padx=10)
btn_enviar.configure(bg="#580000")

Janela.mainloop()

import tkinter as tk
from tkinter import messagebox

Janela = tk.Tk()
Janela.title("Regeistro de peças produzidas:")
Janela.geometry("400x200")
Janela.configure(bg="#FFFFFF")

def janela_bemvindo():
    peças_produzidas = int(peças_produzidas_entry.get())
    horas_gastas = int(horas_gastas_entry.get())

    if peças_produzidas == "" and horas_gastas == "":
        messagebox.showinfo("Digite o número de peças produzidas e as horas gastas, e  calcular a quantidade de peças produzidas por hora")
    else:
        resultado = int(peças_produzidas) / int(horas_gastas)
        messagebox.showinfo("Resultado", f"a quantidade de peças produzidas por hora é {resultado}")

lbl_mensagem = tk.Label(Janela, text="Digite o número de peças produzidas:")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
lbl_mensagem.configure(bg="#FF0000")

peças_produzidas_entry = tk.Entry(Janela, font=("Arial", 12))
peças_produzidas_entry.grid(row=0, column=1, pady=10, padx=10)

lbl_horas = tk.Label(Janela, text="Digite as horas gastas:")
lbl_horas.grid(row=1, column=0, pady=10, padx=10)
lbl_horas.configure(bg="#940000")

horas_gastas_entry = tk.Entry(Janela, font=("Arial", 12))
horas_gastas_entry.grid(row=1, column=1, pady=10, padx=10)

btn_calcular = tk.Button(Janela, text="Calcular", command=janela_bemvindo)
btn_calcular.grid(row=2, column=0, pady=10, padx=10)
btn_calcular.configure(bg="#580000")

Janela.mainloop()


import tkinter as tk
from tkinter import messagebox

Janela = tk.Tk()
Janela.title("Conversor de unidades:")
Janela.geometry("400x200")
Janela.configure(bg="#FFFFFF")

def janela_bemvindo():
    pressão_Bar = float(pressão_Bar_entry.get())
    pressão_PSI = pressão_Bar * 14.5038
    if pressão_Bar == "":
        messagebox.showinfo("Digite a pressão em Bar para converter para PSI")
    else:
        messagebox.showinfo("Resultado", f"A pressão em PSI é: {pressão_PSI:.2f}")

lbl_mensagem = tk.Label(Janela, text="Digite a pressão em Bar:")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
lbl_mensagem.configure(bg="#FF0000")

pressão_Bar_entry = tk.Entry(Janela, font=("Arial", 12))
pressão_Bar_entry.grid(row=0, column=1, pady=10, padx=10)

btn_calcular = tk.Button(Janela, text="Calcular", command=janela_bemvindo)
btn_calcular.grid(row=1, column=0, pady=10, padx=10)
btn_calcular.configure(bg="#FF0000")

Janela.mainloop()

import tkinter as tk
from tkinter import messagebox

Janela = tk.Tk()
Janela.title("Média de qualidade")
Janela.geometry("400x200")
Janela.configure(bg="#FFFFFF")

def janela_bemvindo():
    nota1 = float(nota1_entry.get())
    nota2 = float(nota2_entry.get())
    nota3 = float(nota3_entry.get())

    media = (nota1 + nota2 + nota3) / 3

    if nota1 == "" and nota2 == "" and nota3 == "":
        messagebox.showinfo("Digite as três notas para calcular a média de qualidade")
    else:
        messagebox.showinfo("Resultado", f"A média de qualidade é: {media:.2f}")

lbl_nota1 = tk.Label(Janela, text="Digite a primeira nota:")
lbl_nota1.grid(row=0, column=0, pady=10, padx=  10)

nota1_entry = tk.Entry(Janela, font=("Arial", 12))      
nota1_entry.grid(row=0, column=1, pady=10, padx=10)

lbl_nota2 = tk.Label(Janela, text="Digite a segunda nota:")
lbl_nota2.grid(row=1, column=0, pady=10, padx=10)

nota2_entry = tk.Entry(Janela, font=("Arial", 12))
nota2_entry.grid(row=1, column=1, pady=10, padx=10)

lbl_nota3 = tk.Label(Janela, text="Digite a terceira nota:")
lbl_nota3.grid(row=2, column=0, pady=10, padx=10)

nota3_entry = tk.Entry(Janela, font=("Arial", 12))
nota3_entry.grid(row=2, column=1, pady=10, padx=10)

btn_calcular = tk.Button(Janela, text="Calcular", command=janela_bemvindo)
btn_calcular.grid(row=3, column=0, pady=10, padx=10)
btn_calcular.configure(bg="#FF0000")

Janela.mainloop()


import tkinter as tk
from tkinter import messagebox

Janela = tk.Tk()
Janela.title("Termostato inteligente de um motor")
Janela.geometry("400x200")
Janela.configure(bg="#FFFFFF")

def janela_bemvindo():
    temperatura = float(temperatura_entry.get())
    if temperatura < 40:
        messagebox.showinfo("Status do Motor", "Baixa Carga.")
    elif 40 <= temperatura <= 70:
        messagebox.showinfo("Status do Motor", "Normal.")
    else:
        70 < temperatura
        messagebox.showinfo("Status do Motor", "ALERTA: Resfriamento Ativado!.")
    
lbl_temperatura = tk.Label(Janela, text="Digite a temperatura do motor em °C:")
lbl_temperatura.grid(row=0, column=0, pady=10, padx=10)

temperatura_entry = tk.Entry(Janela, font=("Arial", 12))
temperatura_entry.grid(row=0, column=1, pady=10, padx=10)

btn_calcular = tk.Button(Janela, text="Verificar Status", command=janela_bemvindo)
btn_calcular.grid(row=1, column=0, pady=10, padx=10)
btn_calcular.configure(bg="#FF0000")

Janela.mainloop()

import tkinter as tk
from tkinter import messagebox

Janela = tk.Tk()
Janela.title("Classificador de lotes")
Janela.geometry("400x200")
Janela.configure(bg="#FFFFFF")

def janela_bemvindo():

    código_lote = código_lote_entry.get().upper()
    
    if código_lote == "A":
            messagebox.showinfo("Classificação do Lote", "O lote é classificado como Alimentos.")
    elif código_lote == "E":
            messagebox.showinfo("Classificação do Lote", "O lote é classificado como Eletrônicos.")
    else:
            messagebox.showinfo("Classificação do Lote", "O lote é classificado como Desconecido.")

lbl_código_lote = tk.Label(Janela, text="Digite o código do lote (A para Alimentos, E para Eletrônicos):")
lbl_código_lote.grid(row=0, column=0, pady=10, padx=10)
código_lote_entry = tk.Entry(Janela, font=("Arial", 12))
código_lote_entry.grid(row=0, column=1, pady=10, padx=10)
btn_classificar = tk.Button(Janela, text="Classificar", command=janela_bemvindo)
btn_classificar.grid(row=1, column=0, pady=10, padx=10)
btn_classificar.configure(bg="#FF0000")

Janela.mainloop()

import tkinter as tk
from tkinter import messagebox

Janela = tk.Tk()
Janela.title("Segurança de Operação")
Janela.geometry("400x200")
Janela.configure(bg="#FFFFFF")

def janela_bemvindo():
    sensor_porta = sensor_porta_entry.get().upper()
    botão_emergencia = botão_emergencia_entry.get().upper()

    if sensor_porta == "Fechada" and botão_emergencia == "Desligado":
        messagebox.showinfo("Status de Segurança", "A operação é segura para iniciar.")
    else:
        messagebox.showinfo("Status de Segurança", "Digite novamente as informações para verificar a segurança da operação.")
   
lbl_sensor_porta = tk.Label(Janela, text="Digite o status do sensor de porta (Fechada ou Aberta):")
lbl_sensor_porta.grid(row=0, column=0, pady=10, padx=10)
sensor_porta_entry = tk.Entry(Janela, font=("Arial", 12))
sensor_porta_entry.grid(row=0, column=1, pady=10, padx=10)
lbl_botão_emergencia = tk.Label(Janela, text="Digite o status do botão de emergência (Ligado ou Desligado):")
lbl_botão_emergencia.grid(row=1, column=0, pady=10, padx=10)
botão_emergencia_entry = tk.Entry(Janela, font=("Arial", 12))
botão_emergencia_entry.grid(row=1, column=1, pady=10, padx=10)
btn_verificar = tk.Button(Janela, text="Verificar Segurança", command=janela_bemvindo)
btn_verificar.grid(row=2, column=0, pady=10, padx=10)
btn_verificar.configure(bg="#FF0000")

Janela.mainloop()

import tkinter as tk
from tkinter import messagebox

Janela = tk.Tk()
Janela.title("Cálculo de Descarte")
Janela.geometry("400x200")
Janela.configure(bg="#FFFFFF")

def janela_bemvindo():
    # Usamos try/except para o caso de o usuário digitar letras ou deixar vazio
    try:
        total = int(var_total.get())
        defeituosas = int(var_defeituosas.get())
        
        if total == 0:
            messagebox.showwarning("Aviso", "O total de peças produzidas não pode ser zero.")
            return

        limite_descarte = total * 0.05

        if defeituosas > limite_descarte:
            messagebox.showinfo("Resultado", "Revisar Processo")
        else:
            messagebox.showinfo("Resultado", "Processo Otimizado")
            
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números inteiros válidos.")

lbl_total = tk.Label(Janela, text="Digite o total de peças produzidas:", bg="#FF0000")
lbl_total.grid(row=0, column=0, pady=10, padx=10)
var_total = tk.Entry(Janela, font=("Arial", 12))
var_total.grid(row=0, column=1, pady=10, padx=10)

lbl_defeituosas = tk.Label(Janela, text="Digite o número de peças defeituosas:", bg="#FF0000")
lbl_defeituosas.grid(row=1, column=0, pady=10, padx=10)
var_defeituosas = tk.Entry(Janela, font=("Arial", 12))
var_defeituosas.grid(row=1, column=1, pady=10, padx=10)

btn_calcular = tk.Button(Janela, text="Calcular", command=janela_bemvindo, bg="#FF0000", fg="white")
btn_calcular.grid(row=2, column=0, columnspan=2, pady=10, padx=10) # usei columnspan para centralizar melhor

Janela.mainloop()





