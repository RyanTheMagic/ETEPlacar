from ..CRIAR.criarConexao import criarConexao, database
from flask import flash

def removerPartidasPorId(idPartida):
    try:
        conexao = criarConexao()
        cursor = conexao.cursor()

        cursor.execute('DELETE FROM calendario WHERE fk_partida = %s', (idPartida,))
        conexao.commit()

        cursor.execute('DELETE FROM estatisticas_partida WHERE fk_partida =%s', (idPartida,))
        conexao.commit()

        cursor.execute('DELETE FROM partidas WHERE pk_partida = %s', (idPartida,))
        conexao.commit()

        flash("Partida Removida com sucesso!", "sucesso")
    except:
        flash("Ocorreu um erro inesperado", "erro")
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()