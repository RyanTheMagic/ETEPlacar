import mysql.connector

database = 'etemfl83_inter_classe'

def criarConexao():
    conexaoBD = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database=database
    )
    return conexaoBD