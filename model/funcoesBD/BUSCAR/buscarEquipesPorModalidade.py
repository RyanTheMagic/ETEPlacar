from ..CRIAR.criarConexao import criarConexao, database

def buscarEquipesPorModalidade(esporte):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(f'SELECT * FROM {database}.equipes WHERE fk_esporte = %s ', (esporte,))
    equipesBuscadas = cursor.fetchall()

    return equipesBuscadas