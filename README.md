# Agenda

Exemplo de uma conexão básica ao Banco de Dados MariaDb através do Python. Este exemplo simples conecta a um banco de dados MariaDB (MySQL) para obter informações de usuários.

## Requisitos

- Python 3.x
- Biblioteca `mysql-connector-python` (você pode instalá-la com `pip install mysql-connector-python`)
- Banco de dados MariaDB (certifique-se de ter um servidor MariaDB em execução)

## Configuração

1. Clone este repositório para o seu ambiente local.
2. Crie um banco de dados chamado "agenda" no seu servidor MariaDB.
3. Execute o script SQL fornecido (`schema.sql`) para criar a tabela de usuários.
4. Atualize as credenciais de conexão no arquivo `app.py` com as informações do seu banco de dados.

## Executando o aplicativo

Execute o seguinte comando no terminal:

```bash
python app.py
