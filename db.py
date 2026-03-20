import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class DataBase:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME"),
            port = 3306
        )
        self.cursor = self.conn.cursor(buffered=True)
        self.create_table()
        
    def desconecta_db(self):
        self.conn.close()
        print("Banco de dados desconectado!")

    def create_table(self):
        #self.cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_de_cadastro")
        #self.cursor.execute("USE sistema_de_cadastro")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                senha VARCHAR(50) NOT NULL
            )
        """)
        self.conn.commit()
        print("Banco de dados criado com sucesso!")
        
if __name__ == "__main__":
    db = DataBase()
    db.create_table()
    