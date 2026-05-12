# 1.Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"

print ("Bem Vindo, jogador ")
Nick = (input("Digite seu Nick"))
Nivel = (input("Digite seu Nivel"))

print (f"Seu Nick {Nick} e o Seu Nível {Nivel}")

# 2.Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.

valor1 = float(input("digita o primeiro valor "))
valor2 = float(input("digita o segundo valor "))
operador = input("qual operador você deseja")

operador == "*"
multiplicação = valor1 * valor2
print("A sua renda no final do mês sera :", multiplicação)

# 3.Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024).

print ("Conversão de GB pra MB")

GB = float(input("Digite a quantidade de GB desejada"))
MB = float(input("Digite o valor de MB"))

multiplicação = GB * MB
print ("A quantidade de MB é:", multiplicação)

# 4.Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.

print("Media final do ano escolar")

Matematica = float(input("digite a sua nota em Matematica "))
portugues = float(input("digite a sua nota em portugues "))
media = (Matematica + portugues) / 2
print("sua media final foi:", round(media,2))

# 5.Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.

seguidores = int(input("Digite a quantidade de seguidores você posssui"))
novos = int(input("Digite a quantidade de seguidores novos: "))
total = seguidores + novos
print ("Você ganhou:", total, "seguidores :)")

# 6.Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).

idade = int(input("Digite sua idade "))
Dias = 365
total = idade * 365
print ("você viveu ate agora:", total, "de Dias ;-; ")

# 7.Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.

salgado = int(input("Digite o preço do salgado: "))
suco = int(input("Digite o preço do suco: "))

total = salgado + suco

print ("Deu um total de:",total,"reais, tenha uma boa refeição :)")

# 8.Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.

ano = int(input("Digite o Ano em que você esta: "))
idade = int(input("Digite sua idade atual: "))

total = ano - idade

print("Você nasceu em: ", total, " ;-; ")

# Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".


idade = int(input("Digite sua idade para verificar se esse conteúdo e permitido pra você. "))

if idade <= 13:
    print("você e uma criança!!, acesso restrito")
elif 13 <= idade < 18:
    print("você é um adolescente!, acesso restrito")
else:
    print("você e um adulto, acesso liberado")

# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".

import time
bateria = 100
while bateria in range (1, bateria+1):
    if bateria <= 100:
        bateria -= 10
        print(f"a bateria esta com {bateria}%.")
        time.sleep(1)

print("por favor, conecte no carregador! :( ")
        
# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".

curtidas = [1, 2, 3, 4, 5]
for like in curtidas :
    if like != 6:
        print(f"você possui muitas curtidas {like}")

# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).

item = ["item1", "item2", "item3", "item4"]




int(input("Digite o material desejado"))
