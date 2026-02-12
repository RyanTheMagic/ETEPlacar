from .criarConexao import criarConexao, database
from ..BUSCAR.buscarEstatisticasPorModalidade import buscarEstatisticasPorModalidade
from ..BUSCAR.buscarPartidaPorModalidade import buscarPartidaPorModalidade
from flask import flash

def cadastrarEstatisticasParaModalidade(esporte,estatistica):
    try:
        partidasDaModalidade = buscarPartidaPorModalidade(esporte)
        conexao = criarConexao()
        cursor = conexao.cursor()
        verifica = False
        estatisticasDaModalidade = buscarEstatisticasPorModalidade(esporte)

        cursor.execute(f'INSERT INTO {database}.estatisticas_esporte (fk_esporte, fk_nome_estatistica) values (%s,%s)', (esporte, estatistica))
        conexao.commit()
        if partidasDaModalidade:
            for partida in partidasDaModalidade:
                cursor.execute(f'INSERT INTO {database}.estatisticas_partida (fk_partida, fk_nome_estatistica, valor_time_casa, valor_time_visitante) values (%s,%s,%s,%s)', (partida['pk_partida'], estatistica, 0, 0))
                conexao.commit()

        flash(f"{estatistica} foi cadastrada para {esporte}!", 'sucesso')
    except:
        conexao.rollback()
        for estatisticas in estatisticasDaModalidade:
            if estatistica == estatisticas['fk_nome_estatistica']:
                verifica = True
        if verifica:
            flash(f"{estatistica} já está cadastrada em {esporte}", 'erro')
        else:
            flash(f"Ocorreu um erro inesperado no cadastro de estatísticas", 'erro')
    finally:
        cursor.close()
        conexao.close()