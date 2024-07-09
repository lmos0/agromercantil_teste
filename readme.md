# Projeto Django: Dados Financeiros de Commodities

Este projeto Django tem como objetivo gerenciar e visualizar dados financeiros de commodities utilizando a API da Alpha Vantage. O projeto foi desenvolvido para fins de avaliação e utiliza chaves de API demo.


## Requerimentos:

Django==5.0.4
requests==2.31.0

## Funcionalidades

- Listagem de Commodities: Exibe todas as commodities cadastradas no banco de dados.
- Busca e Atualização de Dados: Permite a atualização dos dados das commodities a partir da API da Alpha Vantage.
- Visualização de Dados: Exibe os dados detalhados de uma commodity selecionada.
- Edição de Notas: Permite adicionar ou remover notas associadas aos dados de uma commodity.
- Exclusão de Dados: Permite a exclusão dos dados de uma commodity.

### Após clonar o repositório, siga os seguintes passos para instalar e configurar o projeto Django:

Na raíz do projeto, realize as migrações do banco de dados:

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

Inicie o servidor:

```bash
python3 manage.py runserver
```

### Abra o navegador e vá para http://127.0.0.1:8000/


## Como Utilizar

A interface possui duas principais funcionalidades:

### Atualizar Banco de Dados via API:

Utilize este botão para buscar e atualizar as informações da commodity selecionada na API AlphaVantage.
Selecione a commodity desejada no menu suspenso e clique no botão para iniciar a atualização.
As novas informações serão armazenadas no banco de dados.

### Consultar Banco de Dados:

Utilize este botão para visualizar os dados já registrados no banco de dados.
Selecione a commodity desejada no menu suspenso e clique no botão para carregar as informações.
Os dados carregados incluirão as anotações associadas a cada entrada, que podem ser editadas ou deletadas diretamente na interface utilizando os respectivos botões.

**Nota Importante:**
Por padrão, o banco de dados inicia vazio. Portanto, é necessário utilizar a função de Atualizar Banco de Dados via API antes de realizar qualquer consulta no banco de dados.


### Opcional Instalar via Ambiente Virtual

1. Instale o ambiente virtual 
    ```bash
    python3 -m venv env
    ```
2. Acesse o diretório 
    ```bash
    cd your_directory
    ```
3. Ative o ambiente virtual
    ```bash
    source env/bin/activate
    ```
4. Instale os pacotes necessários:
    ```bash
    pip install -r requirements.txt
    ```