## Overview


**RapidAPI CriptobotBR** é uma API desenvolvida para realizar a análise técnica de ativos das principais corretoras de **criptomoedas** do mundo. 

Sua função é obter os dados referentes a um determinado ativo e, utilizando bibliotecas de análise matemática e **inteligência artificial**, determinar o melhor momento para realizar a compra ou venda do ativo.

Essa API é voltada a desenvolvedores, que desejam desenvolver aplicações que utilizem esses dados para realização de operações financeiras com criptomoedas, como **trade** e **arbitragem**.

Com a lógica da análise técnica concentrada na API, você pode dedicar-se a desenvolver outras funcionalidades para sua aplicação.

Você pode desenvolver sua própria integração com a API utilizando o conjunto de endpoints disponibilizados pelo marketplace RapidAPI. 

Para ter acesso liberado aos endpoints, é necessário criar uma conta no site RapidAPI, criar uma aplicação e, em seguida, copiar o código de acesso da aplicação para ser enviado ao servidor em cada requisição.

Confira no manual [como criar um app no RapidAPI](https://docs.rapidapi.com/docs/add-a-new-app target='_blank').

Essa biblioteca é dedicada a desenvolvedores Python e tem o intuito de facilitar a integração das aplicações à API de análise técnica **RapidAPI CriptobotBR**.


## Instalação

Você pode clonar o conteúdo do repositório para dentro da pasta principal de seu projeto utilizando o `git clone` (pacote PIP em desenvolvimento).

```bash
mkdir meu-projeto
cd meu-projeto/
git clone https://github.com/leandrocorreasantos/rapidapi_criptobot_br.git
```

Basta, então, fazer o import da classe Client para sua aplicação

```python
from rapidapi_criptobot_br.api.client import Client
```

## Primeiros Passos

Exemplo de uso simples da biblioteca

```python
from rapidapi_criptobot_br.api.client import Client


exchange = 'crex24'
base = 'RDCT'
quote = 'BTC'
app_key = 'your-app-key'

client = Client(app_key)
client.set_exchange(exchange)
client.set_market(base, quote)
print(client.get_market_data())

```

## Métodos

### Set Exchange
### Set Market
### Get Markets
### Get Market Data
### Get Strategies
### Get Strategy
### Get Strategy Parameters
### Get Ticker
### Validate Timeframe
### Get Candles
### Get Signal
