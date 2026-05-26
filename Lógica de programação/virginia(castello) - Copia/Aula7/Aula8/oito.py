#Exercícios de Programação Python: "O Caça-Erros"
# 1.
#errado
# idade = input("Digite sua idade: ")
# if idade >= 18:
# print("Você é maior de idade.")

#corrigido
# idade = int(input("Digite sua idade:"))
# if idade >= 18:
#     print("você é maior de idade.")

#melhorado
# idade = int(input("Digite sua idade:"))
# if idade <= 18:
#     print("Você é menor de idade")

# else:
#     print("Você é menor de idade")

# 2.
# nome = "Mariana"
# print("Seja bem vinda, nome!")

#corrigido
# nome = input("Qual é o seu nome?")
# print("Seja bem-vinda" , nome , "!" )

#melhorado
# nome = input("Qual é o seu nome?")
# print("Seja bem-vindo (a)" , nome , "!" )

# 3.
#errado
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

#corrigido
# numero = 10
# if numero >5:
#     print("O número é maior que cinco.")


#melhorado
# numero = int(input("Digite um número"))
# if numero >5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# 4.
#errado
# usuario = "aluno123"
# if usuario == "aluno 123"
# print("Login realizado com sucesso")

#corrigido
# usuario = input("Digite o nome do usuário")
# if usuario == "aluno123":
#     print("Login realizado com sucesso")


#melhorado
# usuario = input("Digite o nome do usuário")
# if usuario == "aluno123":
#     print("Login realizado com sucesso")
# else:
#     print("Não foi possível realizar o login")

# 5.
# errado
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva")

#corrigido
# clima = input("O clima está ensolarado ou chuvoso?")
# if clima == "chuvoso":
#      print("Leve um guarda-chuva")

#melhorado
# clima = input("O clima está ensolarado ou chuvoso?")
# if clima == "chuvoso":
#      print("Leve um guarda-chuva")
# else:
#      print("Não é necessário levar o guarda-chuva, está sol!")

6.
#errado
# pontos = 50
# print("Parabéns! Você fez "+ pontos + "pontos")

#corrigido
# pontos = 50 
# print("Parabéns! Você fez:" ,  pontos , "pontos")

#melhorado


# 7.
#errado
# O sistema deve dar "Exelente" para notas 9 ou 10.

# nota=9.5
# if nota >=7:
#     print("Aprovado")
# elif nota>= 9:
#     print("Excelente!")

#corrigido
# nota = float(input("Qual foi sua nota?"))

# if nota >=9:
#     print("Excelente!")
# else:
#     print("Aprovado")



#melhorado
# nota = float(input("Qual foi sua nota?"))

# if nota >=9:
#     print("Excelente!")
# elif nota >=7:
#     print("Aprovado")
# else:
#     print("Reprovado!")

# 8.
#errado
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

#corrigido
# for numeros in range(1, 6):
#     print(f"{numeros}")

#melhorado:
# for v in range(6):
#     print(f"{v}")