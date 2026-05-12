#1. Laço "for" (repetições determinadas)
#use o "for" quando voçê sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou preocessar uma lista de peças)
#Exemplo: Relatório de produção Diaria
# Imagine que voçê tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
for lote in range(1, 6):
    print(f"processando lote número {lote}...")
    print("Qualidade verificada. [OK]")
    print("Produção do dia finalizada!")

# Exemplo 2
for b in range(10):
    print(f"Quantidade total {b} foi...")

# Eemplo 3
# #imagine o seguinte cenário, iremos produzir 20 discos de vinil.

for disco in range(21):
    print(f"Quantidade de disco {disco}...")
    
#Exemplo 4
peças = ["engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]

for item in peças:

    print(f"Item em estoque: {item}")

#Exemplo 5
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção voçê deseja e a partir da seleção ele listar os produtosre

print("Loja da Nazareth")
print("Opção 1- peças")
print("Opção 2- Item Peças")
menu = int(input("Escolha uma opção"))

peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "chave de Fenda"]
itempeças = ["Cilindro", "Eixo Cônico", "Radiais", "Madeira", "Bola","Cabeça chata", "Chave metalica Verde"]

if menu == 1:
    for item in peças:
        print(f"Sua lista de peças {peças} são...")
elif menu == 2:
    print(f"sua lista de itens de peças {itempeças} são...")
else:
    print("Opção inválida: Encerrando o sistema")

#Exercicio 1 
# 1.contador de produção (for)
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada numero, imprima: "peça n ° x processada com sucesso". No final, exiba "ciclo de produção concluida"

for ciclo in range(1, 11):
    print(f"Peça numero {ciclo} processada com sucesso!")
    print("Ciclo de podução concluido...")

#Exercicio 2
#Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. com uma quantidade 10 bananas, 5 mangas, 10 melancias e 13 abacaxi

print("Bem vindo ao Hortifruti")
int(input("escolha uma opção"))
print("banana = 1")
print("manga = 2")
print("melancia = 3")
print("abacaxi = 4")

fruta = ["banana", "manga", "melancia", "abacaxi"]

if fruta == 1:
    for banana in range(1, 10):
        print(f"Deu um total de {banana} são...")
elif fruta == 2:
    for manga in range(1, 6):
        print(f"Deu um total de {manga} são...")
elif fruta == 3:
    for melancia in range(1, 11):
        print(f"Deu um total de {melancia} são...")
elif fruta == 4:
    for abacaxi in range(1, 14):
        print(f"Deu um total de {abacaxi} são...")
else:
    print("Obrigado por comprar em nossa Feira")


#Exercicio 3
#Montar uma Tabuada inicialmente pode ter usado por um valor fixo e depois usar a pergunta
