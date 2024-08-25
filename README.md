# Survey Data API

Este projeto tem como objetivo consumir dados de diferentes endpoints, armazená-los em um banco de dados MySQL, e disponibilizá-los através de uma API desenvolvida em Python utilizando FastAPI.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

- Python
- MySQL Server
- Git (opcional, para clonar o repositório)

## Passos para rodar o projeto

### 1. Clonar o repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone https://github.com/pablomariz/survey.git
cd survey
```

### 2. Configurar as variáveis de ambiente

No arquivo .env.example, substitua as variáveis de ambiente com suas próprias configurações para conectar com sucesso ao banco de dados MySQL:

```bash
DB_USERNAME=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=seu_host
DB_PORT=sua_porta
DB_NAME=surveydb
```

Renomeie o arquivo para .env:

```bash
mv .env.example .env
```

### 3. Criar e ativar um ambiente virtual

É recomendado criar e ativar um ambiente virtual para gerenciar as dependências do projeto:

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Instalar as dependências

Com o ambiente virtual ativado, instale as dependências do projeto listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 5. Configurar o banco de dados e povoar as tabelas

Com as dependências instaladas, configure o banco de dados, crie as tabelas necessárias e insira os dados dos endpoints executando o script insert_data.py:

```bash
python insert_data.py
```

Este comando irá:

Conectar ao banco de dados MySQL utilizando as credenciais fornecidas no arquivo .env.
Criar o banco de dados se ele não existir.
Criar as tabelas necessárias para armazenar os dados das pesquisas.
Consumir os dados dos endpoints e inserir nas tabelas correspondentes.

### 6. Rodar a API

Após configurar e popular o banco de dados, rode a aplicação FastAPI usando o Uvicorn:

```bash
uvicorn main:app --reload
```

A API estará disponível em http://127.0.0.1:8000.

### 7. Documentação da API

Você pode visualizar a documentação interativa da API gerada automaticamente pelo FastAPI acessando a URL:

```bash
http://127.0.0.1:8000/docs#/
```

### 8. Consultar os dados da pesquisa

Para consultar os dados das pesquisas, você pode utilizar uma ferramenta como o Postman ou o próprio navegador. A API oferece os seguintes endpoints:

Obter uma pesquisa específica pelo ID:
```bash
GET http://127.0.0.1:8000/surveys/{id_da_pesquisa}
```

Obter todas as pesquisas:
```bash
GET http://127.0.0.1:8000/surveys/
```