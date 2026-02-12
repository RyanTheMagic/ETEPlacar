from ..CRIAR.criarConexao import criarConexao, database

def buscarEquipes():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(f'SELECT * FROM {database}.equipes ')
    equipesBuscadas = cursor.fetchall()

    return equipesBuscadas