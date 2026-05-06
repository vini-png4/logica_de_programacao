# Meu primeiro Robô 

print("Bem Vindo a coleta de peças")
pecas = input("Qual peça você deseja ")

peça1 = "vermelha"
peça2 = "verde"

if pecas == peça1:
    print(f"buscar a peça {peça1} defeituosa, andando 50m ")
    print("Agachando e pegando a peça")
    print("virando a 180° e entregando ao programador a peça desejada ")

elif pecas == peça2:
    print(f"buscar a peça {peça2} boa, andadando 25m ")
    print("Agachando e pegando a peça")
    print("virando a 180° e entregando a peça solicitada ao Bruno ")

else:
    print("Falha no sistema cor não identificada. Por favor peça as cores disponiveis ")

