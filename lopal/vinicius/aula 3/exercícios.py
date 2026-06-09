# Exercício 1
# Cálculo de Notas
# Somativos 1 e somativos 2
# Valores de 0 a 100
# O valor deverá ser atribuido por duas notas e uma média final e ao final deverá ser apresentado o resultado

print ("Bem vindo ao Calculo de Notas")
print ("Notas do Senai")
print (" As notas Senai")

nota1 = float(input("digite a Somativa 1 "))
nota2 = float(input("digite a Somativa 2 "))
media = (nota1 + nota2) / 2
print("sua media final foi:", round(media,2))

# Exercício 2
# Criar um algoritimo para simular uma calculadora
# Deverá conter os operadores + - / *
# Ao inserir o valor 1 e o valor 2 ela deve apresentar o resultado

print("Bem vindo a calculadora de Operadores")
print("selecione uma opção")
print("calculo de soma + ")
print("calculo de subtração - ")
print("calculo de divisão / ")
print("calculo de multiplicação * ")

valor1 = float(input("digita o primeiro valor "))
valor2 = float(input("digita o segundo valor "))
operador = input("qual operador você deseja")

if operador == "+":
 soma = valor1 + valor2
 print("A soma foi:", soma)

elif operador == "-":
 subtração = valor1 - valor2
 print("A subtração foi:", subtração)

elif operador == "/":
 divisão = valor1 / valor2
 print("A soma foi:", divisão)

elif operador == "*":
 multiplicação = valor1 * valor2
 print("A multiplicação foi:", multiplicação)

else:
 print("Obrigado por usar nossa calculadora")


# Exercício 3
# Loja de Roupas, sapatos e perfumes
# Ao escolher uma das opções você perguntar o valor do produto,e quantidade e aplicar desconto
Roupas = 10
Sapatos = 5
Perfumes = 2

print("Bem vindo a loja")
print(" Nós trabalhamos com roupas, sapatos e perfumes")
print("selecione uma das opções para começar suas compras")
print("Digite 1 para Roupas")
print("Digite 2 para Sapatos")
print("Digite 3 para Perfumes")

opção = int(input("Digite a opção desejada"))

if opção == 1:
    print("Você escolheu o setor de roupas")
    prod = float(input("Digite o valor do produto:"))
    qtde = int(input("Digite a quantidade que deseja:"))
    desconto = 10 / 100
    total = (prod + qtde) - desconto
    print("Sua compra no setor de roupa foi de:", total)

elif opção == 2:
    print("Você escolheu o setor de Sapatos")
    prod = float(input("Digite o valor do produto:"))
    qtde = int(input("Digite a quantidade que deseja:"))
    desconto = 10 * 100 / 100
    total = (prod + qtde) - desconto
    print("Sua compra no setor de Sapatos foi de:", total)

elif opção == 3:
    print("Você escolheu o setor de Perfumes")
    prod = float(input("Digite o valor do produto:"))
    qtde = int(input("Digite a quantidade que deseja:"))
    desconto = 10 / 100
    total = (prod + qtde) - desconto
    print("Sua compra no setor de Perfumes foi de:", total)

else:
    print("Obrigado por comprar em nossa loja")
