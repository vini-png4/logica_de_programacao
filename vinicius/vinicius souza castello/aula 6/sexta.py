# clean Code - aula 6
# para que usar?
# como usar?
# print("Clean Code - aula 6")
# aula = 6
# print(f"Estamos na aula {aula} de Clean Code")

# Manipulação de arquivos e Texto
# texto = " pyton é Muito legal! "
# print(texto.strip().upper())# "PYTHON"
# print(texto.strip().lower())# "python"
# print(texto.strip().capitalize())# "python"
# print(texto.strip().title())# "python"
# print(texto.strip().replace(" ", "_"))# "python"
# print(texto.strip().split())# ["python"]

# Escrevendo 
# with open ("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje! ")
#     arquivo.write("\nLer sobre Clean Code.")

# # Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

 # Exerciccio 1 :
 # crie um programa que peça ao usuário para inserir uma frase e, em seguida, exiba a frase com as seguintes transformações:
 # - Remova os espaços extras no inicio e final da frase.   

# frase = input("Qual a frase você quer escrever")
# print(frase.strip().upper())

# Exemplo 1 :
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra
# "Python" aparece no arquivo. Exiba o resultado para o usuário.

# print("Contagem de palavras em arquivo")
# with open ("notas.txt", "r" ) as arquivo:
#     conteúdo = arquivo.read()
#     contagem = conteúdo.count("Python")
#     print (f"A contagem de palavras {contagem} é de...")

# Execução de comandos do sistema
# import os

# print(os.getcwd())
# print(os.listdir(".."))
# print(os.listdir("..\\.."))
# print(os.listdir("C:\\"))
# print(os.listdir("C:\\Users"))
# print(os.listdir("C:\\Users\\Public"))

# Outros comandos úteis:
# Criar pasta
# os.mkdir("pasta_nova")
# Renomear pasta
# os.rename("Nova_pasta", "pasta_renomeada")
# Excluir pasta
# os.rmdir("pasta_renomeada")


# Exercício 2:
# Liste um script que mostre o caminho da pasta atual
# print(os.getcwd())

# Exercício 3:
# Liste os arquivos da pasta atual
# print(os.listdir())


# Exercício 4:
# Crie uma pasta chamada "projetos" e depois para "meus projetos". Por fim, exclua a pasta.

# os.mkdir("projetos")
# os.rename("projetos", "meus projetos")
# os.rmdir ("meus projetos")


# Exercicio 5:
# Crie um arquivo chamado "log.txt" e escreva a mensagem "log de atividade".
# Depois, leia o conteudo do arquivo e exiba na tela.

# with open ("log.txt", "w") as arquivo:
#     arquivo.write("log de atividade")

# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exemplo de dicionario:
# Crie um dicionario com informações sobre uma pessoa e acesse um valor usando uma chave.

# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "profissão": "Engenheira"

#     }

# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "SP",
#     "profissão": "Designer"

#     }
# print(pessoa["cidade"])
# print(pessoa2["nome"], pessoa["idade"])


# comida = {
#     "comida": "Sushi",
#     "origem": "Japão",
#     "ano que surgiu": 1820,
# }

# comida2 = {
#     "comida": "Pizza",
#     "origem": "Itália",
#     "ano que surgiu": 1600,
# }
# print(comida["origem"])
# print(comida2["ano que surgiu"], comida["comida"])

# Exemplo 2; Desligar o PC (comando para Windows)
with open("Desligar.bat", "w") as desligar:
    desligar.write("Shutdown -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. salve seu trabalho'\"")