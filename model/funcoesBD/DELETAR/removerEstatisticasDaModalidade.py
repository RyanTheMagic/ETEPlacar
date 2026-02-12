from ..CRIAR.criarConexao import criarConexao, database
from ..BUSCAR.buscarPartidaPorModalidade import buscarPartidaPorModalidade
from flask import flash

def removerEstatisticasDaModalidade(esporte,estatistica=None):
    try:
        partidasDaModalidade = buscarPartidaPorModalidade(esporte)
        conexao = criarConexao()
        cursor = conexao.cursor()
        if estatistica is None:
            cursor.execute(f'DELETE FROM {database}.estatisticas_esporte WHERE fk_esporte = %s', (esporte,))
            conexao.commit()
        else:
            cursor.execute(f'DELETE FROM {database}.estatisticas_esporte WHERE fk_esporte = %s and fk_nome_estatistica = %s', (esporte, estatistica))
            conexao.commit()
            if partidasDaModalidade:
                for partida in partidasDaModalidade:
                    cursor.execute(f'DELETE FROM {database}.estatisticas_partida WHERE fk_partida = %s and fk_nome_estatistica = %s', (partida['pk_partida'], estatistica))
                    conexao.commit()
            flash(f'{estatistica} foi retirado(a) de {esporte}', 'sucesso')
    except:
        conexao.rollback()
        flash('Ocorreu um erro inesperado na remoção de uma estatística')
    finally:
        cursor.close()
        conexao.close()