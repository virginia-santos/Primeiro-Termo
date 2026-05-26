# projeto cancela automática 
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
# # Revisão do código
# print("Bem vindo ao ShoppingCenter")
# print("Qual opcão você deseja?")
# print("1 -Ticket \n2- Tag \n3- Interfone")
# metodo_entrada = input("Ticket / Tag / Interfone")

# if metodo_entrada == "Ticket":
#     print("Bem vindo ao ShoppingCenter")

# hora_entrada = int(input("Digite o horário de entrada"))
# valor_estacionamento = float(input("Digite o valor a ser cobrado"))
# hora_saida = float(input("Digite o horário de chegada"))

# tempo_permanencia = hora_saida - hora_entrada

# print(f"Seu tempo de permanência {tempo_permanencia} em horas")
# total_estacionamento = tempo_permanencia * valor_estacionamento
# print(f"O valor total a ser cobrado foi de R${total_estacionamento: .2f}")
# print("Devolver o ticket")
    
# elif metodo_entrada == "Tag":
# print("Bem vindo ao ShoppingCenter")
# print("Sua permanência será cobrada na sua fatura")
    
# elif metodo_entrada == "interfone":
# print("Bem vindo ao ShoppingCenter")
# print("Liberando acesso pelo interfone")
# print("Sua saída deverá ser feita também pelo interfone")


# else:
# print("Obrigada pela visita")
print("Bem vindo ao ShoppingCenter")
print("Qual opção você deseja?")
print("1 - Ticket\n2 - Tag\n3 - Interfone")

metodo_entrada = input("Ticket / Tag / Interfone: ").lower()

if metodo_entrada == "ticket":
    print("Bem vindo ao ShoppingCenter")

    hora_entrada = int(input("Digite o horário de entrada: "))
    valor_estacionamento = float(input("Digite o valor a ser cobrado: "))
    hora_saida = float(input("Digite o horário de saída: "))

    tempo_permanencia = hora_saida - hora_entrada

    print(f"Seu tempo de permanência foi de {tempo_permanencia} horas")

    total_estacionamento = tempo_permanencia * valor_estacionamento

    print(f"O valor total a ser cobrado foi de R$ {total_estacionamento:.2f}")
    print("Devolver o ticket")

elif metodo_entrada == "tag":
    print("Bem vindo ao ShoppingCenter")
    print("Sua permanência será cobrada na sua fatura")

elif metodo_entrada == "interfone":
    print("Bem vindo ao ShoppingCenter")
    print("Liberando acesso pelo interfone")
    print("Sua saída deverá ser feita também pelo interfone")

else:
    print("Opção inválida")