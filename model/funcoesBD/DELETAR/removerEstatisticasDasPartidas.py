from ..CRIAR.criarConexao import criarConexao, database

def removerEstatisticasDasPartidas(estatistica):
    try:
        conexao = criarConexao()
        cursor = conexao.cursor()

        cursor.execute(f'DELETE FROM {database}.estatisticas_partida WHERE fk_nome_estatistica = %s', (estatistica,))
        conexao.commit()
    except:
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()