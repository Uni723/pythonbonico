from mysql.connector import (connection)
from mysql.connector import errorcode
import os
from load_dotenv import load_dotenv
load_dotenv()
senha = os.getenv('SENHA_SQL')
bd_conexão = connection.MySQL.Connection(
    host='localhost',
    user= 'root'
    password=senha
    password= 'bd_python'
)