from ..CRIAR.criarConexao import criarConexao, database
from ..ATUALIZAR.adicionarEstatCasaCalendario  import adicionarEstatCasaCalendario
from flask import flash

def adicionarEstatisticasCasa(id_partida, nome_estatistica, valor_time_casa):
    try:  
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(f'UPDATE {database}.estatisticas_partida SET valor_time_casa = %s WHERE fk_partida = %s AND fk_nome_estatistica = %s', (valor_time_casa,id_partida, nome_estatistica))
    
        conexao.commit()

        if nome_estatistica == 'Gols' or nome_estatistica == 'Pontos' or nome_estatistica=='Eliminações':
            adicionarEstatCasaCalendario(id_partida, valor_time_casa)
        if nome_estatistica == 'Sets':
            adicionarEstatCasaCalendario(id_partida, valor_time_casa)

        flash(f"{nome_estatistica} adicionado(a) com sucesso!", "sucesso")
    except: 
        conexao.rollback()
        flash("Ocorreu um erro inesperado!", "erro")
    finally:
        cursor.close()
        conexao.close()