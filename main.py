from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()
senha = os.getenv('SENHA_SQL')

try:
    bd_conexao = connection.MySQLConnection(
        host='localhost',
        user='root',
        password=senha,
        database='bd_python'
    )
    print("Conexão bem sucedida!")

except mysql.connection.Error as erro:
    if erro.erno == errorcode.ER_DB_ERROR:
        print("O banco de dados não existe!")
    elif erro.erno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou senha incorretos!")
    else:
            print(erro)

comando = bd_conexao.cursor()
select = comando.execute("SELECT * FROM ALUNOS")
resultado = comando.fetchall()
for linha in resultado:
    print(linha)

## INSERIR ALUNO
sql_insert = "INSERT INTO ALUNOS (nome, ano) VALUES (%s, %s)"
valores1 = ('Caio', '3 TEC')
valores2 = ('Leonardo', '2 TEC')

comando.execute(sql_insert, valores1)
comando.execute(sql_insert, valores2)

print("==TESTE INSERT==\n")
select = comando.execute("SELECT * FROM ALUNOS")
resultado = comando.fetchall()
for linha in resultado:
    print(linha)

bd_conexao.commit()
comando.close()
bd_conexao.close()