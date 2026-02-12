from ..CRIAR.criarConexao import criarConexao, database

def removerPartidasPorModalidade(esporte):
    try:
        conexao = criarConexao()
        cursor = conexao.cursor()

        cursor.execute(f'DELETE FROM {database}.partidas WHERE fk_esporte = %s', (esporte,))
        conexao.commit()
    except:
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()