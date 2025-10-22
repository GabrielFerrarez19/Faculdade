from multiprocessing import connection
import psycopg2
from psycopg2 import OperationalError

DB_NAME = "biblioteca"
DB_USER = "postgres"
DB_PASSWORD = "gabri1234"
DB_HOST = "localhost"
DB_PORT = "5433"

def conectar():
    connection = None
    try:
        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host= DB_HOST,
            port=DB_PORT,
        )
        print("Conexão com o banco de dados estabelecida com sucesso")
    except OperationalError as e:
        print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")
    return connection



if __name__== "__main__":
    connection=conectar()
    if connection:
        print("Conexão com o bando de dados encerrada.")
    else:
        print("Nenhuma conexão para encerrar")

conectar()