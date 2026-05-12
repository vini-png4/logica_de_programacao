# Exercícios de Programação Python: "O Caça-Erros"

# 1. O Problema da Idade
# idade = input("Digite sua idade:")
# if idade >= 18:
#     print("Você é maior de idade") 

# Corrigido 

idade = int(input("Qual é sua idade? :"))
if idade >= 18:
    print ("Acesso liberado")
else:
    print("Acesso negado!")

# melhorado 

idade = int(input("Digite sua idade:"))
if idade >= 18:
    print("Você é maior de idade")
else: 
 print("Você é menor de idade ")

#  2. A Escrita Fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# Corrigido 
nome = input("Digite seu nome")
print(f"Seja Bem-Vinda, {nome}!")

# Melhorado

nome = input("Digite seu nome")
print ("Seja bem_vinda, {nome}!")

# 3. Falta de Espaço
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# Corrigido

numero = 10
if numero > 5:
  print("O número é maior que cinco.")
else:
  print("O número é menor ou igual a cinco.")

# Melhorado

# 4. Esquecimento Fatal

# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

# Corrigido

usuario = "aluno123"
if usuario == "aluno123":
   print("usuario autorizado")
else:
  print("Login realizado com sucesso.")

# Melhorado


# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

# Corrigido

clima = "ensolarado"
if clima == "chuvoso":
 print("Leve um guarda-chuva!")

else:
 print("Sistema encerrado")

# Melhorado

# 6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# Corrigido
pontos = 50
print("Parabéns! Você fez ", pontos ," pontos.")

# Melhorado

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

# Corrigido
nota = 9.5

if nota >= 9:
 print("Excelente!")

elif nota >= 7:
 print("Aprovado")

# Melhorado

# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

# Corrigido

for i in range(1, 6):
 print(i)

# Melhorado 

# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas

# Corrigido 
tentativas = 1
while tentativas <= 3:
 tentativas +=1
 print("Tentando conectar...")
 
# Melhorado

# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Corrigido

senha = input("Digite sua senha")
while senha == "python123":
 senha = input("Digite a senha secreta: ")
 print("Acesso concedido!") 
 break 