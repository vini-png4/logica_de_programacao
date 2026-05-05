# Condições logicas e decisões 
# O programa toma caminhos diferentes dependendo da condição
# funções de logicas SE e Senão
#  If , elif e else
# If = Se (verdadeiro)
# elif = continua sendo (verdadeiro)
# else = falso

# Exemplo 1
print("Bem-vindo as lógicas e Decisões")
print("para iniciar digite a opção desejada")
print("Digite 1 para filmes e 2 para Séries e 3 para Novelas")

escolha = int(input("Digite a opção que deseja"))

if escolha == 1:
    print("Você escolheu Filmes")
elif escolha == 2:    
    print("Você escolheu Séries")
elif escolha == 3:
    print("Você escolheu Novelas")
else: 
    print("Você não escolheu nenhuma opção do catalogo")

# # Exemplo 2
print("Pokemo")
print("Escolha seu Personagem")
print("Pikachu = P")
print("Charizard = C")
print("Mewtow = M")

pokemons = input("Digite a letra do seu personagem")

if pokemons == "P":
    print("Você escolheu PIKACHU")
elif escolha == "C":    
    print("Você escolheu CHARIZARD")
elif escolha == "M":
    print("Você escolheu MEWTWO")
else: 
    print("ESpero você na proxíma, até mais!!")

# Exemplo 3
# Valores nùmericos e flutuantes
print("Valores")
print("Comparações de nùmeros")

numeros = int(input("Digite um nùmero"))

if numeros > 100:
    print("Nùmero Alto")
elif numeros < 100:
    print("Nùmero Baixo")
else:
    print("Escolher um valor que não temos ")
