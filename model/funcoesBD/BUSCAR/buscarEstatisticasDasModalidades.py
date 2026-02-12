from ..CRIAR.criarConexao import criarConexao, database

def buscarEstatisticasDasModalidades():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.estatisticas_esporte')

    estatisticasBuscadas = cursor.fetchall()

    return estatisticasBuscadas
    