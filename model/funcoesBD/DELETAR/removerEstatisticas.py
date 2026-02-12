from ..CRIAR.criarConexao import criarConexao, database
from ..BUSCAR.buscarEstatisticasDeModalidade import buscarEstatisticasDeModalidade
from ..BUSCAR.buscarEstatisticasDasPartidas import buscarEstatisticasDasPartidas
from ..DELETAR.removerEstatisticasDasPartidas import removerEstatisticasDasPartidas
from ..DELETAR.removerEstatisticasDasModalidades import removerEstatisticasDasModalidades
from flask import flash

def removerEstatisticas(estatistica):
    try:
        conexao = criarConexao()
        cursor = conexao.cursor()
        estatModalidades = buscarEstatisticasDeModalidade()
        estatPartidas = buscarEstatisticasDasPartidas()

        if estatPartidas:
            removerEstatisticasDasPartidas(estatistica)
        if estatModalidades:
            removerEstatisticasDasModalidades(estatistica)
        cursor.execute(f'DELETE FROM {database}.tipo_estatistica WHERE pk_nome_estatistica = %s', (estatistica,))
        conexao.commit()
        flash(f'{estatistica} foi removido(a) com sucesso!', 'sucesso')
    except:
        conexao.rollback()
        flash('Ocorreu um erro inesperado!', "erro")
    finally:
        cursor.close()
        conexao.close() 