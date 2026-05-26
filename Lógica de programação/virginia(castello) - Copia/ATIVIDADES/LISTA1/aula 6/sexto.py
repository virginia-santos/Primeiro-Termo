# Clean code - Aula 6
# Para que usar?
# Como usar?
# print("Clean code - Aula 6")
# aula = 6
# print(f"Estamos na aula {aula} de Clean Code")

# Manipulação de Arquivos e Texto
# texto = "  Spfc maior do Brasil!  "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower()) # "python"
# print(texto.strip().capitalize()) # "Python"
# print(texto.strip().title()) # "Phyton"
# print(texto.strip().replace("" , "_")) # "Phyton"
# print(texto.strip().split()) # ["Python"]

# Escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar python hoje!")
#     arquivo.write("\nLer sobre Clean code")

#     #Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)


    # exercício 1:
#     Crie um programa que peça ao usuário para inserir uma frase e, em seguida , exiba a frase  com as seguintes transformações:
#  #- Remova os espaços extras no inicio e no final da frase.

# frase = input("Insira uma frase:")
# print(frase.strip().lower())

# Exemplo 1:
# crie um programa que leia o conteúdo de um arquivo de texto  e conte quantas vezes a palavra "Python" aparece no arquivo . Exiba o resultado para o usuário
# print("Contagem de palavras em arquivo")
# with open("notas.txt" , "r") as arquivo:
#     conteudo = arquivo.read()
# contagem = conteudo.count("Python")
# print(f"A contagem de palavras {contagem} é de...")

#Executar de comandos do sistema
import os # importa o módulo os para interagir com o sistema operacional
# #Onde estou?
# print(os.getcwd())
# #Listar arquivos na pasta
# print(os.listdir()) 
# print(os.listdir("..")) #lista arquivos da pasta pai
# print(os.listdir("..\\..")) #lista arquivos da pasta avô
# print(os.listdir("C:\\Users")) #lista arquivos da raiz do C
# print(os.listdir("C:\\Users")) #lista arquivos da pasta Users
# print(os.listdir("C:\\Users\\public")) #lista arquivos  da pasta Public

#Outros comandos úteis
# #Criar pasta
# os.mkdir("nova_pasta")
# # # # Renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# # # # # # # Excluir pasta
# os.rmdir("pasta_renomeada")

# Exercício 2:
#Crie um script que mostre o caminho da pasta atual
import os
# print(os.getcwd())
# # # Exercício 3:
# # # Liste os arquivos da pasta atual
# import os
# print(os.listdir())

# # Exercício 4:
# # Crie uma pasta chamada "projetos" e depois renomeie para "meus projetos". Por fim, exclua a pasta
# os.mkdir("projetos")
# os.rename("projetos", "meus_projetos")
# os.rmdir("meus_projetos")

# # Exercício 5:
# # crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades". Depois, leia o conteúdo do arquivo e exiba na tela
# with open("log.txt", "w") as arquivo:
#     arquivo.write("Log de  atividades")
# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# # Exemplo de dicionário:
# # Crie um dicionário com informações sobre uma pessoa e acessa um valor usando uma chave.
# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "profissão": "Engenharia"

# }
# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25, 
#     "cidade": "SP",
#     "profissão": "Designer"

# }
# print(pessoa["idade"])
# print(pessoa2["nome"], pessoa["idade"])

# supermercado = {
#     "doces": "trento",
#     "bebida": "suco de maracujá",
#     "comida": "batata inglesa",
#     "fruta": "melancia",

# }
# supermercado2 = {
#     "doces": "fini",
#     "bebida": "água com gás",
#     "comida": "batata doce",
#     "fruta": "melancia",


# }
# print(supermercado["fruta"])
# print(supermercado2["doces"], supermercado["bebida"])

# Exemplo 2: Desligar o Pc (comando para windows)
with open("desliga.bat", "w") as deligar:
    desligar.write("shutdown -s -t 3600 -c \"Desligamento programado para daqui a 1 hora. salve seu trabalho!\\")








