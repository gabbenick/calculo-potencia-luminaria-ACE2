# 💡 Cálculo de Potência Estimada para Lâmpadas

Este projeto em Python tem como objetivo **calcular a potência estimada de luminárias** com base em parâmetros fornecidos pelo usuário — como iluminância desejada, área do ambiente, número de luminárias, etc.

---

## 🧠 Como Funciona

O programa usa a seguinte fórmula para estimar o fluxo luminoso total necessário:

Φ_total = (Emed × Área) / (U × FM × FFL)

E, a partir disso, estima a **potência da luminária** com base na eficácia luminosa (lm/W):

Potência (W) = Φ_por_luminária / Eficácia

---

## 🗂 Estrutura do Projeto

├── main.py # Arquivo principal, orquestra tudo
├── calculos.py # Funções de cálculo do fluxo e potência
├── entrada.py # Entrada de dados com valores padrão
├── README.md # Explica o funcionamento do código.

---

## 🚀 Como Rodar

1. Clone este repositório ou baixe os arquivos.
2. No terminal, entre na pasta do projeto:
cd calulo-potencia-luminaria-ACE2

3. Execute o programa:
python main.py

---

## ✅ Exemplo de Entrada

Durante a execução, você verá prompts como:

Emed (padrão: 150): Área (padrão: 30): Eficácia luminosa da lâmpada (lm/W) (padrão: 100):

Você pode digitar o valor desejado ou apenas apertar `Enter` para usar o padrão.

---

## 📌 Requisitos

- Python 3.7 ou superior
- Nenhuma biblioteca externa necessária

---

## 💻 Possíveis Melhorias Futuras

- Interface gráfica (Tkinter ou Streamlit)
- Exportar resultado em PDF ou CSV
- Suporte para múltiplos ambientes

---

## 🧑‍💻 Autor

Feito com ❤️ por [gabus]  
📧 Entre em contato: `joao.gabriel@ceca.ufal.br`

---

## 🪄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar!
