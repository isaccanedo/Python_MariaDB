import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

try:
    # Conectar ao banco de dados
    connection = mysql.connector.connect(
        host='localhost',
        database='agenda',
        user='root',
        password='root'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Executar uma consulta SELECT na tabela usuario
        cursor.execute("SELECT * FROM usuario")
        
        # Obter os resultados
        registros = cursor.fetchall()

        # Exibir os registros
        print(tabulate(registros, headers=["ID", "Nome", "Senha"], tablefmt="pretty"))

except Error as e:
    print(f"Erro ao conectar ao MariaDB: {e}")

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("Conexão ao MariaDB foi fechada")
