import mysql.connector

bancoDeDados = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    port = '3306',
    passwd = 'abq@47667075'
)


# preparar objeto cursor
cursor = bancoDeDados.cursor()

#criar banco de dados
cursor.execute("CREATE DATABASE django")

print("Tudo pronto!")