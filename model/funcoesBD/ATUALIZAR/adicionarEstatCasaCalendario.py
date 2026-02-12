from ..CRIAR.criarConexao import criarConexao, database
from flask import flash

def adicionarEstatCasaCalendario(id_partida, valor_time_casa):
    try:  
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(f'UPDATE {database}.partidas SET pontos_turma_casa = %s WHERE pk_partida = %s', (valor_time_casa,id_partida))
    
        conexao.commit()
        flash("Estatísticas atualizadas com sucesso!", "sucesso")
    except:
        conexao.rollback()
        flash("Ocorreu um erro inesperado!", "erro")
    finally:
        cursor.close()
        conexao.close()