from ..CRIAR.criarConexao import criarConexao, database

def buscarEstatisticasPorPartida(id):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.estatisticas_partida WHERE fk_partida = %s', (id,))

    estatisticasBuscadas = cursor.fetchall()

    return estatisticasBuscadas
    

#########################DELETAR ARQUIVO (DEIXE PRA RYAN FAZER ISSO)