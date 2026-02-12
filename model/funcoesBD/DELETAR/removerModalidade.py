from ..CRIAR.criarConexao import criarConexao, database
from ..BUSCAR.buscarPartidaPorModalidade import buscarPartidaPorModalidade  
from ..BUSCAR.buscarEstatisticasPorModalidade import buscarEstatisticasPorModalidade
from ..BUSCAR.buscarEstatisticasPorPartida import buscarEstatisticasPorPartida
from ..BUSCAR.buscarEquipesPorModalidade import buscarEquipesPorModalidade
from ..BUSCAR.buscarMembrosEquipePorID import buscarMembrosEquipePorID
from .removerEstatisticasDaModalidade import removerEstatisticasDaModalidade
from .removerPartidasPorModalidade import removerPartidasPorModalidade
from .removerEquipesPorModalidade import removerEquipesPorModalidade
from flask import flash

def removerModalidade(esporte):
    try:
        verificaSeModalidadeTemEstatisticas = buscarEstatisticasPorModalidade(esporte)
        verificaSeModalidadeTemPartidas = buscarPartidaPorModalidade(esporte)
        verificaSeModalidadeTemEquipes = buscarEquipesPorModalidade(esporte)

        conexao = criarConexao()
        cursor = conexao.cursor()

        if verificaSeModalidadeTemEstatisticas:
            removerEstatisticasDaModalidade(esporte)

        if verificaSeModalidadeTemPartidas:
            for id in verificaSeModalidadeTemPartidas:
                cursor.execute(f'DELETE FROM {database}.calendario WHERE fk_partida = %s', (id['pk_partida'],))
                conexao.commit()
                if buscarEstatisticasPorPartida(id['pk_partida']):
                    cursor.execute(f'DELETE FROM {database}.estatisticas_partida WHERE fk_partida = %s', (id['pk_partida'],))
                    conexao.commit()   

        for equipe in verificaSeModalidadeTemEquipes:
            verificaSeEquipeTemMembros = buscarMembrosEquipePorID(equipe['pk_equipe'])
            if verificaSeEquipeTemMembros:
                cursor.execute(f'DELETE FROM {database}.membros_equipe WHERE fk_equipe = %s', (equipe['pk_equipe'],))
                conexao.commit()

        if verificaSeModalidadeTemEquipes:
            removerPartidasPorModalidade(esporte)
            removerEquipesPorModalidade(esporte)
            
        cursor.execute(f'DELETE FROM {database}.esportes WHERE pk_esporte = %s', (esporte,))
        conexao.commit()
        flash(f'{esporte} removido com sucesso!', 'sucesso')
    except:
        conexao.rollback()
        flash(f'Ocorreu um erro inesperado ao remover {esporte}!', 'erro')
    finally:
        cursor.close()
        conexao.close() 