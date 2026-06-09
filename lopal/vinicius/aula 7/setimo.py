# Projeto Cancela Automatica
# Meu primeiro commit

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

# print("Bem vindo ao Shopping Limeira")

# opcao_desejada = input("Digite a opção desejada")

# if opcao_desejada == "Ticket":
#     print("Retire seu ticket")


# elif opcao_desejada == "Tag":
#     print("Acesso Liberado ")

# elif opcao_desejada == "Interfone":
#     print("Ligando...")

# else:
#     print("Encerrando o Sistema")


# Modelo Correto 

# print("Bem-Vindo ao Shopping")
# print("Escolha as opções")
# print(" 1 - Ticket \n 2 - Tag \n 3 - Interforne")
# metodo_entrada = input("Ticket / Tag / Interfone")

# while True:
#     try:
    
#         numero = int(input("Digite um numero")) 
#         resultado = 10 / numero
#         print(f"O resultado é: {resultado}")

#     except Exception as erro:
#         print(f"Ocorreu um erro inesperado: {erro}")
#         break

#     except NameError:
#         print("Erro: Variável não definida.")
#         continue

#     except KeyboardInterrupt:
#         print("\nPrograma interrompido pelo usuário.")
#         break

# if metodo_entrada == "Ticket":
#     print("Bem-Vindo ao Shopping")
#     hora_entrada = float(input("Digite a hora de entrada"))
#     valor_estacionamento = float(input("Digite o valor a cobrar"))
#     hora_saida = float(input("Digite a hora de saida"))
#     total_permanencia = hora_saida - hora_entrada
#     print(f"Seu tempo de permanência {total_permanencia:.2f} em horas ")
#     total_estacionamento = total_permanencia * valor_estacionamento
#     print(f"O valor a ser cobrado foi de R${total_estacionamento:.2f}")

# elif metodo_entrada == "Tag":
#     print("Bem-Vindo ao Shopping")
#     print("Sua permanência no Shopping será cobrada na sua fatura")

# elif metodo_entrada == "Interfone":
#     print("Bem-Vindo ao Shopping")
#     print("Liberando acesso pelo Interfone")
#     print("Sua saída deverá ser feita também pelo Interfone")

# else:
#     print("Obrigado pela visita")
  





# versão 2.0

print("Bem-Vindo ao Shopping")
print("Escolha as opções:")
print(" 1 - Ticket \n 2 - Tag \n 3 - Interfone")

opcao = input("Digite o número (1, 2 ou 3) ou o nome da opção: ").strip().capitalize()

metodo_entrada = ""
if opcao == "1" or opcao == "Ticket":
    metodo_entrada = "Ticket"
elif opcao == "2" or opcao == "Tag":
    metodo_entrada = "Tag"
elif opcao == "3" or opcao == "Interfone":
    metodo_entrada = "Interfone"

print("\n--- Teste de Divisão ---")
while True:
    try:
        numero = int(input("Digite um numero: ")) 
        resultado = 10 / numero
        print(f"O resultado é: {resultado}")
        break

    except NameError:
        print("Erro: Variável não definida.")
        continue

    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
        break

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
        break


print("\n--- Fluxo do Shopping ---")

if metodo_entrada in ["Ticket", "Tag", "Interfone"]:
    print("Bem-Vindo ao Shopping")

if metodo_entrada == "Ticket":
    hora_entrada = float(input("Digite a hora de entrada (ex: 14.5): "))
    valor_estacionamento = float(input("Digite o valor a cobrar por hora: "))
    hora_saida = float(input("Digite a hora de saida (ex: 16.5): "))
    
    total_permanencia = hora_saida - hora_entrada
    print(f"Seu tempo de permanência {total_permanencia:.2f} em horas ")
    
    total_estacionamento = total_permanencia * valor_estacionamento
    print(f"O valor a ser cobrado foi de R${total_estacionamento:.2f}")

elif metodo_entrada == "Tag":
    print("Sua permanência no Shopping será cobrada na sua fatura")

elif metodo_entrada == "Interfone":
    print("Liberando acesso pelo Interfone")
    print("Sua saída deverá ser feita também pelo Interfone")

else:
    print("Obrigado pela vvisita")