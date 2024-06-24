# Sistema de Conversão de Moeda

Este projeto é uma aplicação gráfica simples desenvolvida em Python usando a biblioteca Dear PyGui. A aplicação permite converter valores entre diferentes moedas, como Real, Dólar e Euro, com base na opção selecionada pelo usuário.

## Funcionalidades

- **Opções de Conversão:**
  - **Real para Dólar:** Digite `1`
  - **Dólar para Real:** Digite `2`
  - **Real para Euro:** Digite `3`
  - **Euro para Real:** Digite `4`
  - **Dólar para Euro:** Digite `5`
  - **Euro para Dólar:** Digite `6`

- **Entrada de Dados:**
  - **Opção:** Campo de texto para o usuário inserir a opção de conversão desejada.
  - **Moeda:** Campo de texto para o usuário inserir o valor da moeda a ser convertida.

- **Cálculo do Valor Convertido:**
  - A aplicação calcula e exibe o valor convertido com base na opção selecionada.
  - Exibição de mensagens de erro caso os valores inseridos não sejam válidos.

- **Interface Gráfica:**
  - Interface intuitiva com campos de texto e botão para cálculo.
  - Exibição do resultado do cálculo na própria janela da aplicação.
  - Botão para sair da aplicação.

## Requisitos

- Python 3.x
- Biblioteca Dear PyGui

Você pode instalar a biblioteca necessária utilizando o pip:
```sh
pip install dearpygui
