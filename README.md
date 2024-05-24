# Conexão básica ao Banco de Dados MariaDb através do Python

Exemplo de uma conexão básica ao Banco de Dados MariaDb através do Python. Este exemplo simples conecta a um banco de dados MariaDB (MySQL) para obter informações de usuários.

## Requisitos

- Python 3.x;
- Biblioteca `mysql-connector-python` (você pode instalá-la com `pip install mysql-connector-python`);
- Biblioteca `tabulate` (você pode instalá-la com `pip install tabulate`);
- Banco de dados MariaDB (certifique-se de ter um servidor MariaDB em execução).

## Configuração

1. Clone este repositório para o seu ambiente local.
2. Crie um banco de dados chamado "agenda" no seu servidor MariaDB.
3. Execute o script SQL fornecido (`schema.sql`) para criar a tabela de usuários.
4. Atualize as credenciais de conexão no arquivo `app.py` com as informações do seu banco de dados.

## Biblioteca Tabulate
A biblioteca tabulate é uma biblioteca Python que facilita a formatação e exibição de dados tabulares em formato de tabela. Ela é especialmente útil quando você precisa apresentar informações de maneira organizada e legível, seja no console, em relatórios ou até mesmo em documentos Markdown.

Aqui estão os principais pontos sobre a biblioteca tabulate:

````1 - Formatação de Tabelas:
A tabulate permite criar tabelas a partir de listas, dicionários ou objetos iteráveis.
Você pode especificar o formato da tabela (por exemplo, “plain”, “grid”, “html”, “latex”, etc.) para atender às suas necessidades de exibição.```

```2 - Personalização:
É possível personalizar a aparência da tabela, incluindo a escolha de cabeçalhos, alinhamento de colunas, largura das colunas e muito mais.
A biblioteca oferece opções para controlar a formatação, como a capacidade de ocultar índices de linha ou coluna.```

```3 - Suporte a Diferentes Tipos de Dados:
A tabulate lida bem com diferentes tipos de dados, como números, strings e datas.
Ela pode formatar automaticamente os valores de acordo com o tipo de dado.```

from tabulate import tabulate

data = [
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Designer"],
    ["Carol", 22, "Developer"]
]

headers = ["Nome", "Idade", "Profissão"]

# Formatação da tabela em estilo "grid"
table = tabulate(data, headers, tablefmt="grid")
print(table)



## Executando o aplicativo

Execute o seguinte comando no terminal:

```bash
python mysql_example.py
