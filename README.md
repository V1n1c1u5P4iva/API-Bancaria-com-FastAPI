# 🏦 API Bancária com FastAPI

Esta é uma API RESTful assíncrona desenvolvida em **Python** usando o framework **FastAPI**. A API permite gerenciar operações bancárias, como depósitos e saques, vinculadas a contas correntes. Além disso, a API utiliza autenticação **JWT** para proteger os endpoints.

> **Nota**: Este projeto foi criado **para estudos** e é bem simples, destinado apenas para **teste de conhecimento**. Não deve ser utilizado em produção.

## 🚀 Funcionalidades

- **Criação de Contas**: Crie contas bancárias com um nome de titular.
- **Depósitos e Saques**: Realize transações de depósito e saque em contas existentes.
- **Extrato**: Consulte o extrato de uma conta, listando todas as transações realizadas.
- **Autenticação JWT**: Proteção dos endpoints com autenticação baseada em tokens.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para construção da API.
- **SQLAlchemy**: ORM para gerenciamento do banco de dados.
- **JWT**: Autenticação baseada em tokens.
- **Poetry**: Gerenciamento de dependências e ambiente virtual.
- **SQLite**: Banco de dados embutido para desenvolvimento.

---

## 🚀 Como Executar o Projeto

### 📋 Pré-requisitos

- Python 3.7 ou superior.
- Poetry instalado (`pip install poetry`).

### 🛠️ Passos para Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/api-bancaria-fastapi.git
   cd api-bancaria-fastapi

2. **Instale as dependências**:
   ```bash
   poetry install
3. **Execute o servidor**:
   ```bash
    poetry run uvicorn api_bancaria.main:app --reload

3. **Acesse a API**:
   ```bash
    A API estará disponível em http://127.0.0.1:8000.
    A documentação interativa estará disponível em http://127.0.0.1:8000/docs.

## 📡 Endpoints da API

### 🔐 Autenticação
```http
POST /token
````
### 💳 Contas
```http
POST /contas/: Cria uma nova conta bancária.
GET /contas/{conta_id}/extrato: Retorna o extrato de uma conta.
````
### 💸 Transações
```http
POST /transacoes/: Realiza uma transação (depósito ou saque).
````
