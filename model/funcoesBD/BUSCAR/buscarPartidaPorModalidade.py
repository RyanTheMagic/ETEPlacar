from ..CRIAR.criarConexao import criarConexao, database

def buscarPartidaPorModalidade(esporte):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(f'SELECT * FROM {database}.partidas WHERE fk_esporte = %s', (esporte,))
    partidaBuscada = cursor.fetchall()

    return partidaBuscada