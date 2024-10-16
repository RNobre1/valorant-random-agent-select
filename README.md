# Valorant Random Agent Select 🎮

Este projeto é um script automatizado que seleciona de forma aleatória um agente em diferentes classes (Iniciador, Duelista, Controlador ou Sentinela) no jogo **Valorant**, utilizando as bibliotecas `pyautogui` e `pygetwindow`. O script simula cliques e movimentos do mouse para interagir com a interface do jogo, escolhendo um agente de acordo com a função sorteada.

## 🔧 Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/RNobre1/valorant-random-agent-select.git
   ```

2. **Instale as dependências:**

Este projeto depende das bibliotecas `pyautogui`, `pygetwindow` e `time`. Para instalá-las, execute:

```bash
pip install pyautogui pygetwindow
```

## 🚀 Uso

1. **Inicie o Valorant:**

Certifique-se de que o Valorant esteja aberto e com a janela visível.

2. **Execute o script:**

Após garantir que o jogo esteja em execução, execute o script `main.py`:

```bash
python main.py
```

3. **Seleção Automática:**

O script irá automaticamente:

- Restaurar a janela do Valorant se estiver minimizada.
- Movimentar o cursor até a área de seleção de agentes.
- Selecionar um agente de forma aleatória dentro de uma das classes: Iniciador, Duelista, Controlador ou Sentinela.
- Confirmar a escolha do agente.

## 🛠️ Funcionamento

- O script primeiro restaura a janela do Valorant, caso ela esteja minimizada.
- Em seguida, move o cursor até a área de seleção de agentes, simulando o clique em uma das funções (Iniciador, Duelista, Controlador, Sentinela).
- A partir da função escolhida, o script faz uma seleção aleatória de um agente e confirma a seleção clicando no botão correspondente.

## 📋 Requisitos

- Python 3.x
- `pyautogui` e `pygetwindow`
- Jogo Valorant instalado e rodando em um sistema operacional compatível.

## 🤖 Bibliotecas Utilizadas

- [pyautogui](https://pyautogui.readthedocs.io/en/latest/): Utilizada para controlar o mouse e teclado automaticamente.
- [pygetwindow](https://pypi.org/project/PyGetWindow/): Usada para gerenciar e manipular janelas de programas no sistema.
- [time](https://docs.python.org/3/library/time.html): Utilizada para adicionar pausas entre as ações do script.

## 🛡️ Avisos de Segurança

Este script interage diretamente com a interface do Valorant, portanto, use-o por sua própria conta e risco. Certifique-se de que ele não viola as políticas da Riot Games.

## 🌐 Versão em Inglês

[**Switch to English**](#)
