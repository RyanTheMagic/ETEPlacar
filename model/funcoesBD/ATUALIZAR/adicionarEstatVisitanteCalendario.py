from ..CRIAR.criarConexao import criarConexao, database
from flask import flash

def adicionarEstatVisitanteCalendario(id_partida, valor_time_visitante):
    try:  
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(f'UPDATE {database}.partidas SET pontos_turma_visitante = %s WHERE pk_partida = %s', (valor_time_visitante,id_partida))
    
        conexao.commit()
        flash("Estatísticas atualizadas com sucesso!", "sucesso")
    except:
        conexao.rollback()
        flash("Ocorreu um erro inesperado!", "erro")
    finally:
        cursor.close()
        conexao.close()