

print("Olá esse é o elevador, por gentileza não fique parado na porta !")
andar_atual = 0

while True:
    try:
   
        
        pessoas = int(input("Digite o numero mas a capacidade max e 5 pessoas"))
        if pessoas > 5:
            print("limite alcançado")
        

        destino = int(input("Digite o andar de destino (0 a 10): "))
        if destino < 0 or destino > 10 :
         raise ValueError ("Andar inválido. Por favor, digite um número entre 0 e 10.")
        
        print(f"Elevador se movendo do andar {andar_atual} para o andar {destino}...")
        andar_atual= destino
        print(f"Chegamos ao andar {andar_atual}!")

        if input("Deseja outro andar ? (s/n): ").lower() != 's':
           print("Obrigado por usar o Elevador, até a próxima!")
           break
        for listagem in range(10):
           print(f"Andar {listagem} -{'[X]' if listagem == andar_atual else '[ ]'}")

        

    except ValueError:
        print()

    else:
        print("Erro número inválido, digite novamente")
