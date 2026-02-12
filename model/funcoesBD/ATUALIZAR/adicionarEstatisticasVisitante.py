from ..CRIAR.criarConexao import criarConexao, database
from ..ATUALIZAR.adicionarEstatVisitanteCalendario import adicionarEstatVisitanteCalendario
from flask import flash

def adicionarEstatisticasVisitante(id_partida, nome_estatistica, valor_time_visitante):
    try:  
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(f'UPDATE {database}.estatisticas_partida SET valor_time_visitante = %s WHERE fk_partida = %s AND fk_nome_estatistica = %s', (valor_time_visitante, id_partida, nome_estatistica))
    
        conexao.commit()

        if nome_estatistica == 'Gols' or nome_estatistica == 'Pontos' or nome_estatistica=='Eliminações':
            adicionarEstatVisitanteCalendario(id_partida, valor_time_visitante)
        if nome_estatistica == 'Sets':
            adicionarEstatVisitanteCalendario(id_partida, valor_time_visitante)

        flash(f"{nome_estatistica} adicionado(a) com sucesso!", "sucesso")
    except:
        conexao.rollback()
        flash("Ocorreu um erro inesperado!", "erro")
    finally:
        cursor.close()
        conexao.close()