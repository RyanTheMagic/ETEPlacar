from ..CRIAR.criarConexao import criarConexao, database

def buscarEstatisticas():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.tipo_estatistica')

    estatisticasBuscadas = cursor.fetchall()

    return estatisticasBuscadas
    