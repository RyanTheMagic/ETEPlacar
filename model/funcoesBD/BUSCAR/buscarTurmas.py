from ..CRIAR.criarConexao import criarConexao, database

def buscarTurmas():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.turmas')

    turmasBuscadas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return turmasBuscadas

