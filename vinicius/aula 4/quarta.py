# 2.O laço While (repetições Indeterminadas)
# Use o While quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergêmcia)
# Exemplo: monitor de Temperatura (loop infinito Controlado)
# Repete enquanto a temperatura estiver segura
# Inicio

import time
temperatura = 30
while temperatura < 80:
    print(f"Temperatura atual: {temperatura}°C. Sistema Operando...")
    time.sleep(1)
    temperatura += 3 #Simulando o aquecimento da máquina
print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# Lista de temperatura lidas pelo sensor por minuto

# Exemplo 2: monitoramento de temperatura com lista de Leitura
# Lista de temperatura lidas pelo sensor por minuto

leituras = [70,75,82,98,110,85,80]

for temp in leituras:
    if temp > 100:
        print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência. ")
        break # O loop para aqui e NÂO lê os próximos valores (85 e 80)
    print(f"Temperatura está em {temp}°C. Operação normal.")

print("Sistema desligando. Aguardando manutenção")

# Exemplo 3

materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
for peca in materiais:
 if peca != "metal":
    print(f"Aviso: Peça de {peca} detectada. Desviando para o descarte...")
    continue # Pula o restante do código abaixo e vai para proxima peça
# Este código só roda se a peça for de metal
print(f"Processando peça de {peca}. Furando e polindo...")

print ("Fim do lote de produção. ")

# Execício 1
# tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número (simulando uma falha de sensor específica no item 5).

for sensor in range (1,11):
  if sensor == 5:
   print(f"Sensor n° {sensor} com falha")
  print(f"Sensor {sensor} sem falha")
  continue

print("Fim! :) ")

# Execício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa para cada cor. Use o continue para pular a com amarela 
# (Simulando um semáforo com defeito que não acende a luz amarela).

# import time

cores  = ["Verde", "Amarelo", "Vermelho"]
for Sinal in cores:
  if Sinal == "Amarelo":
    print(f"Semáforo com defeito, pulando a cor {Sinal}...")
    continue
    time.sleep(3)
    print(f"Semáforo na cor {Sinal}. parando por 3 segundos...")
    time.sleep(3)
    print("Fim do ciclo do semáforo.")

# Exercício 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. peça ao usuário (via input dentro do loop)
# O consumo em kwh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica

total_consumo = 0 
for maquina in range(1, 6):
  consumo = float(input(f"Digite o consumo em Kwk da maquina {maquina}:"))
  total_consumo += consumo #Acumulo o consumo total
  print(f"O consumo total da fabrica é de {total_consumo}KwH.")

# Exercicio 4 - Identificador de Peças Defeituosas (for + if)
# percorra uma lista de medidas de peças :
# Medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ele está "Aprovada" ou "Rejeitada".

peças = [50.1, 49.8, 52.0, 50.0, 48.5]

for medida in peças:
    if medida >= 50.0:
        print(f"Peça com medida {medida}mm: Aprovada") 
    else:
        print(f"Peça com medida {medida}mm: Rejeitada")

print("Fim da avaliação de peças.")

# Exercico 5 - Uma balança industrial esta pesando um lote de 6 sacos de insumos. O peso ideal de cada saco e 50kg, mas o sistema aceita variações.
# Crie um programa que peça ao usuario o peso de cada saco (via input dentro do loop) e, para cada um, informe se ele esta "dentro do limite" (entre 48kg e 52kg) ou "fora do limite".
# No final, exiba quantos sacos estão dentro do limite.

sacos_dl = 0
for saco in range(1, 7):
    peso = float(input(f"Digite o peso do saco {saco} em kg: "))
    if 48 <= peso <= 52:
        print(f"Saco {saco} com peso {peso}kg: Dentro do limite")
        sacos_dl +=1 # Conta os sacos dentro do limite
    else:
        print(f"Saco {saco} com peso {peso}kg: Fora do limite")
    print(f"Quantidade de sacos dentro do limite: {sacos_dl}")

    # Desafio: Gestão de Ciclo Térmico
    # Você deve criar um programa que monitora a temperatura de uma estufa que processa um lote de 5 peças 
    # Regra do Sistema:
    # O programa deve rodas em um loop até que 5 peças válidas sejam processadas.
    # Para cada peça, peça ao usuário a temperatura atual (input).
    # Filtro de Erro (continuar): se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa Leitura não conta como peça processada).
    # Parada de Emergência (break): Se a temperatura for maior que 150°C, o sistema deve exibir " ALERTA CRÍTICO: Risco de Explosão! ", interromper o loop imediatamente e encerrar o programa



temperatura = 0
while temperatura < 5:
    temp = int(input(f"Digite a temperatura da peça {temperatura +1}°C: Sistema operando..."))

    if temp < 0:
        print("Erro de leitura no sensor. Por favor, digite uma temperatura válida. ")
        continue
    if temp > 150:

        print(" ALERTA CRÍTICO: Risco de Explosão! ")
        break
    
    print(f"Peça {temperatura + 1} processando com temperatura {temperatura}°C. ")

    print(f"Peça {temperatura} processada com sucesso. Temperatura dentro do limite, ")

print("Fim do monitoramento de temperatura")

# Exercício 6 - Contador de peças com falha (while + if + continue)
# Uma linha de produção tem um sensor que detecta falhas em peças. O programa deve contar quantas peças com falhas foram detectadas. O usuário deve digitar "sim"
# para indicar que uma peça tem falha e "não" para indicar que está boa. O programa deve continuar pedindo a condição da peça até de usuário digite "FIM". No final, exiba o total de peças com falhas detectadas.