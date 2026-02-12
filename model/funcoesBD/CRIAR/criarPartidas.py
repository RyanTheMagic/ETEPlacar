from .criarConexao import criarConexao, database
from ..BUSCAR.buscarEstatisticasPorModalidade import buscarEstatisticasPorModalidade
from ..BUSCAR.buscarEquipesPorModalidade import buscarEquipesPorModalidade
from flask import flash

def criarPartidas(esporte, descricao, turma_casa, turma_visitante, dia):
    try:
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(f"""
            INSERT INTO {database}.partidas (fk_esporte, fk_descricao, fk_equipe_casa, pontos_turma_casa, fk_equipe_visitante, pontos_turma_visitante)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (esporte, descricao, turma_casa, 0, turma_visitante, 0))

        idNovaPartida = cursor.lastrowid

        conexao.commit()

        cursor.execute(f'INSERT INTO {database}.calendario (dia_evento, fk_partida) values (%s,%s)', (dia, idNovaPartida))

        conexao.commit()

        for nome_estatistica in buscarEstatisticasPorModalidade(esporte):
            cursor.execute(f'insert into {database}.estatisticas_partida (fk_partida, fk_nome_estatistica, valor_time_casa, valor_time_visitante) values (%s,%s,%s,%s)', (idNovaPartida, nome_estatistica['fk_nome_estatistica'], 0, 0))

            conexao.commit()

        flash('Partida criada com sucesso!', 'sucesso')
    except:
        conexao.rollback()
        flash('Ocorreu um erro inesperado na criação da partida')
    finally:
        cursor.close()
        conexao.close()