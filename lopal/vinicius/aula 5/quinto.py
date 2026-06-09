# 1
nick = input ("Qual é o nome do jogador? ...")
nivel = int(input("Qual é seu nivel? ..."))
print(f"O jogador {nick} está no nivel {nivel} e pronto para a partida!")

# 2
valor_semana = float(input("Quanto você ganha por semana? ..."))
total = valor_semana * 4
print(f"Sua mesada no final do mês foi de... {total}")

# 3

print("conversor de internet")
GB = float(input("Digite o valor em Gigabytes..."))
meg = GB * 1024
print(f"O valor convertido em Megabytes seria de ... {meg}")

# 4

print ("Média das Notas")
mat = float(input("Digite sua nota em Matemática"))
port = float(input("Digite sua nota em português"))
media = (mat + port) / 2
print (f"Sua média de matemática e português .....`{media}")


# 5

seg_atual = int(input("Quantos seguidores você possui?"))
seg_novos = int(input("Quantos novos você ganhou ?"))
seg_atualizado = seg_atual + seg_novos
print(f"Você possui {seg_atualizado} um total atualizado de seguidores")

# 6

print("Idade em dias")
idade = int(input("Digite sua idade"))
idade_dias = idade * 365
print(f"A quantidade de dias vividos são {idade_dias}")

# 7

print ("Consumo do salgado")
salgado = float(input("Qual é o valor do salgado..."))
suco = float(input("Qual é o valor do Suco...?"))
total = salgado + suco
print(f"Sua compra ficou no valor de ... {total:.2f}")
print("Sua compra foi um total de R$... ",round(total,2))

# 8

print ("Ano de Nascimento")
ano_atual = int(input("Digite o ano do seu ano atual"))
idade = int(input("Quantos você ira fazer esse ano?"))
ano_nasc = ano_atual - idade
print(f"O ano que você nasceu {ano_nasc}")

# 9

print ("Filtro de idade (tiktok)")
idade = int(input("Qual é sua idade...?"))

if idade < 13:
    print("Acesso restrito")
elif idade in range (13,18):
    print("Acesso moderado")
elif 13 < idade < 17:
    print("Acesso moderado")
elif idade >= 18:
    print ("Acesso liberado")
else :
    print("Idade inválida")

# 10

print ("Bateria de celular...Carregamento")
import time
bateria = 100

while bateria > 10:
    print(f"Bateria em {bateria}%")
    bateria -= 10
    time.sleep (1)

print("Por favor conecte o carregador")

# 11

print("Contagem de curtidas")
import time 
limite = int(input("Digite a quantidade de curtidas"))
for curtidas in range(1, limite + 1):
    print(f"Curtidas n° {curtidas} recebidas")
    time.sleep(0.5)

# 12

print ("Carrinho de compras Online")
print ("Digite Sair para encerrar o Sistema")
contador = 0
produto = ""

while produto.lower() != "sair":
    contador =+1
    produto = input("Digite o nome do produto ou Sair para finalizar...")

if produto.lower != "sair":
    print(f"Produto '{produto}' acicionado ao carrinho!")
    print(f"Compra finalizada você adicionou {contador} itens ao seu carrinho!")

print ("Obrigado por comprar conosco! :)")

print("Carrinho de compras Online - versão 2.0 ")
contador = 0
produto = 0 
while produto != "sair":
    contador =+ 1
    produto = input("Digite o nome do produto ou sair para finalizar")

print(f"Você adicionou {contador-1} Itens ao carrinho ")
print("Obrigado por comprar conosco!")