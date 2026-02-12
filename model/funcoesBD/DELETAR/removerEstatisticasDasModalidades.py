from ..CRIAR.criarConexao import criarConexao, database

def removerEstatisticasDasModalidades(estatistica):
    try:
        conexao = criarConexao()
        cursor = conexao.cursor()

        cursor.execute(f'DELETE FROM {database}.estatisticas_esporte WHERE fk_nome_estatistica = %s', (estatistica,))
        conexao.commit()
    except:
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()