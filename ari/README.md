# # Aula de IoT: 

## 📝 Visão Geral
Explicação de como o **Arduino (C++)** e o **Python** vão interagir neste projeto (ex: Arduino lê sensores e Python gera o gráfico).

---

## 🔧 Requisitos de Hardware
*   **Placa:** Arduino [Uno/Mega/Nano]
*   **Componentes:** [Lista de componentes]
*   **Conexão:** Cabo USB (Comunicação Serial)

---

## 💻 Programação do Hardware (C++)
*Desenvolvido na Arduino IDE. Responsável pelo controle físico e leitura de sinais.*

```cpp
/* 
   Código C++ para Arduino 
*/

void setup() {
  Serial.begin(9600); // Inicializa comunicação serial
}

void loop() {
  // Exemplo: Enviar dados para o Python
  int leitura = analogRead(A0);
  Serial.println(leitura);
  delay(500);
}
```

---

## 🐍 Integração e Dados (Python)
*Responsável por receber, processar ou exibir os dados do Arduino no computador.*

**Bibliotecas recomendadas:** `pyserial`, `time`, `matplotlib` (opcional).

```python
import serial
import time

# Configuração da porta (ajuste 'COM3' ou '/dev/ttyUSB0')
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def read_arduino():
    time.sleep(2) # Espera a conexão estabilizar
    while True:
        data = arduino.readline().decode('utf-8').strip()
        if data:
            print(f"Dados recebidos do Arduino: {data}")

if __name__ == "__main__":
    read_arduino()
```

---

## 🔌 Diagrama de Montagem

| Componente | Pino Arduino | Observação |
| :--- | :--- | :--- |
| Sensor (S) | A0 | Entrada Analógica |
| LED | D13 | Indicador Visual |

---

## 🚀 Exercício de Fixação
1. Modifique o código **C++** para enviar um alerta se o valor passar de X.
2. Altere o script **Python** para salvar esses dados em um arquivo `.txt` ou `.csv`.

---
*Referência: [Documentação Arduino](https://arduino.cc)*