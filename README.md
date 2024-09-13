# FastAPI Numbers API

A FastAPI Numbers API é uma aplicação desenvolvida utilizando o framework FastAPI, que permite a criação de APIs de forma rápida e eficiente. Esta API é projetada para realizar cálculos de soma e média com base em uma lista de números fornecida pelo usuário.

## Funcionalidades

- Soma: Recebe uma lista de números e retorna a soma total.
- Média: Recebe uma lista de números e retorna a média aritmética.

### Pré-requisitos

- É necessário ter o Docker e docker-compose instalado ou o Python na versão Python >= 3.10

## Instruções de Execução

Para configurar e executar a aplicação, você pode usar o Makefile. Aqui estão os comandos disponíveis:

### Configuração Local

Para configurar o ambiente local, execute:

```bash
make local-setup
```

### Executar Localmente

Para executar a aplicação localmente, use:

```bash
make local-run
```

### Construir Docker

Para construir a imagem Docker, execute:

```bash
make docker-build
```

### Executar Docker

Para iniciar a aplicação usando Docker, utilize:

```bash
make docker-run
```

## Documentação

A documentação da API pode ser visualizada em [localhost:8000/docs](http://localhost:8000/docs) após a execução da aplicação.

## Requisições com cURL

Para realizar requisições para os endpoints `/sum` e `/average`, você pode usar os seguintes comandos cURL:

### Endpoint: Soma

Para calcular a soma de uma lista de números, execute:

```bash
curl --request POST \
  --url http://localhost:8000/api/v1/numbers/sum \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.3.2' \
  --data '{ "numbers": [1, 2] }'
```

### Endpoint: Média

Para calcular a média de uma lista de números, execute:

```bash
curl --request POST \
  --url http://localhost:8000/api/v1/numbers/average \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.3.2' \
  --data '{ "numbers": [1, 2] }'
```

## Executar Testes

Para executar a suíte de testes, você pode usar o pytest. Aqui estão as instruções para executar os testes localmente e com docker-compose:

### Executar Testes Localmente

Para executar os testes localmente, use o seguinte comando:

```bash
pytest
```

### Executar Testes com Docker

Para executar os testes utilizando docker-compose, utilize o seguinte comando:

```bash
docker-compose run --rm web pytest
```
