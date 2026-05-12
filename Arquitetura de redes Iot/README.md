# # Arquitetura de Redes IoT: Aula 01
## Programação de Dispositivos e Integração (C++ & Python)

### 1. Objetivos da Disciplina
* Compreender a arquitetura de camadas em IoT (Percepção, Rede, Aplicação).
* Programar microcontroladores Arduino utilizando **C++**.
* Desenvolver scripts em **Python** para coleta e processamento de dados.
* Implementar protocolos de comunicação (Serial, MQTT, HTTP).

---

### 2. O Lado do Dispositivo: Arduino (C++)
No contexto de IoT, o Arduino atua na **Camada de Percepção**, lendo sensores e atuando no mundo físico.

#### Estrutura Básica do Código
```cpp
// Definições de Pinos
const int sensorPin = A0;

void setup() {
  Serial.begin(9600); // Inicializa comunicação serial
  pinMode(sensorPin, INPUT);
}

void loop() {
  int leitura = analogRead(sensorPin);
  
  // Envio de dados formatados para o computador/gateway
  Serial.print("DATA:");
  Serial.println(leitura);
  
  delay(1000); // Sample rate de 1Hz
}
```

---

### 3. O Lado do Gateway/Servidor: Python
O Python é utilizado na **Camada de Rede/Aplicação** devido à sua facilidade em lidar com JSON, bancos de dados e dashboards.

#### Exemplo: Lendo Dados do Arduino via Serial
Para rodar este exemplo, é necessário instalar a biblioteca: `pip install pyserial`

```python
import serial
import time

# Configuração da porta (ajuste para COMx no Windows ou /dev/ttyUSBx no Linux)
porta = "COM3" 
baudrate = 9600

try:
    ser = serial.Serial(porta, baudrate, timeout=1)
    print(f"Conectado em {porta}")

    while True:
        if ser.in_waiting > 0:
            linha = ser.readline().decode('utf-8').rstrip()
            if "DATA:" in linha:
                valor = linha.split(":")[1]
                print(f"Sensor capturado: {valor}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Encerrando conexão...")
    ser.close()
```

---

### 4. Fluxo de Dados na Arquitetura
1. **Sensor** -> Analógico/Digital -> **Arduino**.
2. **Arduino** -> Processamento Local (C++) -> **Serial/Wi-Fi**.
3. **Python** -> Tratamento de Erros/Filtros -> **Banco de Dados/Nuvem**.

---

### 5. Exercício Prático
**Desafio:** Crie um sistema de alerta.
1. No **Arduino**: Se o sensor ultrapassar o valor 700, envie a mensagem `ALERTA`.
2. No **Python**: Ao receber `ALERTA`, o script deve salvar o horário atual em um arquivo `.txt` de log.

---

### 6. Links Úteis e Referências
* [Documentação Oficial Arduino](https://arduino.cc)
* [PySerial Documentation](https://pythonhosted.org)
* [Protocolo MQTT com Python (Paho-MQTT)](https://pypi.org)
