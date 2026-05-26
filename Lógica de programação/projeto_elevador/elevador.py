# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.


print(" 0 - Térreo\n 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10")
print("Bem-vindo ao Elevador Python!")
andar_atual = 0
while True:
    try:
        destino = int(input("Digite o andar de destino (0-10): "))
        pessoas = int(input("Digite a quantidade de pessoas dentro do elevador"))
        if destino < 0 or destino > 10:
            raise ValueError("Andar inválido. Por favor, digite um número entre 0 e 10.")
        if pessoas > 5:
            raise ValueError("O número de pessoas excede o que o elevador suporta.")
        
        print(f"Elevador se movendo do andar {andar_atual} para o andar {destino}...")
        andar_atual = destino
        print(f"Chegamos ao andar {andar_atual}!")

        if input("Deseja escolher outro andar? (s/n): ").lower() != 's':
            print("Obrigado por usar o Elevador Python! Até a próxima!")
            break
        for listagem in range(10):
            print(f"Andar {listagem} - {'[X]' if listagem == andar_atual else '[ ]'}")

    except ValueError as erro:
        print(f"Erro: {erro}. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")
        print("Programa encerrado.")
        break

              


   