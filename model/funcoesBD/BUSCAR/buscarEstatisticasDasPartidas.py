from ..CRIAR.criarConexao import criarConexao, database

def buscarEstatisticasDasPartidas():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.estatisticas_partida')

    estatisticasBuscadas = cursor.fetchall()

    return estatisticasBuscadas
    