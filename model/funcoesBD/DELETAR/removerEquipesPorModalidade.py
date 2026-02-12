from ..CRIAR.criarConexao import criarConexao, database

def removerEquipesPorModalidade(esporte):
    try:
        conexao = criarConexao()
        cursor = conexao.cursor()

        cursor.execute(f'DELETE FROM {database}.equipes WHERE fk_esporte = %s', (esporte,))
        conexao.commit()
    except:
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()