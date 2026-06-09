# Atividade 1: Mensagem de Boas-Vindas
# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
# programação em Python!".

# atividade 1

print("Bem-vindo ao mundo da programação em Python!")

#atividade 2

pergunta1 = input("Digite seu nome")
pergunta2 = int(input("Digite sua idade"))
print("Seu nome e sua idade são:",pergunta1, pergunta2)

#atividade 3 e 4

print("Calculadora de operações")

print("selecione uma opção")
print("calculo de soma + ")
print("calculo de subtração - ")
print("calculo de divisão / ")
print("calculo de multiplicação * ")


valor1 = float(input("digita o primeiro valor "))
valor2 =float(input("digita o segundo valor "))
operador = input("qual operador você deseja")

if operador == "+":
  soma = valor1 + valor2
  print("A soma foi:", soma)
  
elif operador == "-":
  subtração = valor1 - valor2
  print("A subtração foi:", subtração)

elif operador == "/":
 divisão = valor1 / valor2
 print("A divisão foi:", divisão)

elif operador == "*":
 multiplicação = valor1 * valor2
 print("A multiplicação foi:", multiplicação)

else:
 print("Obrigado por usar nossa calculadora")

# atividade 5

print("5 ** 3")

# atividade 6

nome = input("Digite seu nome")

sobrenome = input("Digite seu sobrenome")

print (nome  +  sobrenome)

#atividade 7

peçasboas = float(input("digite a quantidade de peças boas"))
peçasruins = float(input("digite a quantidade de peças ruins"))

total = (peçasboas + peçasruins)
total2 = peçasboas/total

print("calculo de divisão / ")
operador = input("qual operador você deseja")

if operador == "/":
 divisão = peçasboas / peçasruins
 print("A divisão foi:", divisão)

else:
 print ("Sua taxa de aproveitamento")

#  # atividade 8

idade = int(input("Voçê tem quantos anos?"))
print("daqui 10 ano, voçê vai ter", idade + 10)

#atividade 9

