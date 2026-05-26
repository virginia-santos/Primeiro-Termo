# O laço while (repetições Indeterminadas)
# use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança pu um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)
# Repete enquanto a temperatura estiver segura
# início
import time
temperatura = 25
while temperatura < 40:
    print(f"Temperatura atual: (temperatura)°C. Sistema operando...")
    time.sleep(1) 
    temperatura += 3 #simulando o aquecimento da máquina 
    print("ALERTA! TTemperatura atingiu o limite. Desligando motor...")

    # Lista de temperatura lidas pelo sensor por minuto

    # Exemplo 2: Monitoramento de Temperatura com Lista de Leituras
    # Lista de temperaturas lidas pelo sensor por minuto
    leituras = [70, 75, 82, 98, 110, 85, 80]

    for temp in leituras:
        if temp > 100:
            print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
            break #O loop para aqui e NÃO lê os próximos valores (85 e 80)
        print(f"Temperatura está em {temp}°C. Operação normal.")

print("Sistema desligado. Aguardando manutenção.")

# Exemplo3
materiais = ["metal", "metal", "plástico", "metal", "vidro", "metal"]
for peca in materiais:
    print(f"Aviso: Peca de {peca} detectada. Desviando para o descarte...")
    continue #Pula o restante o código abaixo e vai para a próxima peça
 # Este código só roda se a peça for de metal
print(f"Processando peça de {peca}. Furando e polindo...")


print("fim do lote de produção.")


# exercício 1
# Tente criar um código que conte 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica do item 5)
for sensor in range(1,11):
    if sensor == 5:
     print(F"sensor n°{sensor}com falha")
     print(f"Sensor {sensor} sem falha")
     continue
print("Fim! :)")

# Exercício 2
# Simule um semáforo com parada para cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente para que quando mudar de cor ele represente uma uma pausa para cada cor. Use o continue para pular a cor amarela (simulando um samáforo com defeitp que não acenda a luz amarela).
cores = ["vermelho", "amarelo", "verde"]
for cor in cores:
    if cor == "amarelo":
        print(f"Semáforo com defeito, pulando a cor {cor}...")
        continue #Pula a cor amarela
    print(f"Semáforo na cor {cor}. Parando por 3 segundos...")
    time.sleep(3) #Simula a pausa para cada cor
print("Fim do ciclo do semáforo")

# Exemplo 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo de kwh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica. 
total_consumo =0
for maquina in range(1,6):
    consumo = float(input(f"Digite o consumo em kwh da máquina" {maquina}))
    total_consumo += consumo #Acumula o consumo total
print(f"O consumo total da fábrica é de `{total_consumo} kwh.")