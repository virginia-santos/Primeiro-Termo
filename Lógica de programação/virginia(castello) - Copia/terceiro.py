# 1. O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
#  Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 
for lote in range(1, 6):
    print(f"Processando lote  número {lote}...")
    print("Qualidade verificada. [OK]")
    print("Produção do dia finalizada!")

    # Exemplo 2
    for b in range(10):
     print(f"Quantidade total {b} foi...")

    #  Exemplo 3
    #  Imagine o seguinte cenário, iremos produzir 20 discos de vinil
    for discos in range(21):
       print(f"Quantidade total de discos {discos} foi... ")
       
    #    Exemplo 4 
    pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
    itempecas = ["Cilíndricas", "Eixo cônico", "Radicais", "Madeira", "Bola", "Cabeça Chata", "Chave Metálica"]
    for item  in pecas:
       print(f"item em estoque: {item} e {itempecas}")
    for item2 in itempecas:
       print(f"Item de pecas em estoque: {itempecas}")

    #    Exemplo 5
    # Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos
    print("Virginia's store")
    print("opcao1- Peças")
    print("opcao2-Item Peças")
    menu = int(input("Escolha uma opcao"))

    pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de fenda"]
    itempecas = ["Cilíndricas", "Eixocônico", "Radiais", "Madeira", "Bola", "Cabeca chata", "Chave metálica verde"]

    if menu == 1:
       for item1 in pecas:
          print(f"Sua lista de itens de peças {pecas} são...")
    elif menu == 2:
       for item1 in itempecas:
          print(f"Sua lista de itens de peças {itempecas} são...")
    else:
       print("Opçao inválida; Encerrando o sistema")

    #    Exercício 1
    #  1. Contador  de produção (for)
    # Uma esteira processa 10 peças por um ciclo. Crie um programa que use um for para contar de  1 a 10 e, para cada número, imprima: "peça número x processada com sucesso".
    # No final exiba ciclo de produção concluída

    for ciclo in range(1,11):
       print(f"Peça n° {ciclo} processada com sucesso...")
    print("Ciclo de produção concluído...")

    # Exercício 2
    # Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi.
    for banana in range(1, 10):
       print(f"A quantidade de {banana} foi...")
    for manga in range(1, 5):
       print(f"A qauntidade de {manga} foi...")
    for melancia in range(1,10):
        print(f"A qauntidade de {melancia} foi...")
        for abacaxi in range(1, 13):
       print(f"A quantidade de {abacaxi} foi...")

# Exercício 3
# Montar uma tabuada inicialmente pode ser usada por um valor fixo e depois usar a pergunta.
 for ta