from ..CRIAR.criarConexao import criarConexao, database
from datetime import datetime

def buscarEventosCalendarioFiltros(ano, mes, modalidade=None,turma=None,descricao=None):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    primeiroDia = f'{ano}-{mes:02d}-01'
    proximoMes = mes + 1
    proximoAno = ano
    if proximoMes > 12:
        proximoMes = 1
        proximoAno += 1
    ultimoDia = f'{proximoAno}-{proximoMes:02d}-01'

    query = """
    SELECT 
        c.dia_evento,
        e.pk_esporte AS fk_esporte,
        e.grupo,
        p.fk_descricao AS fk_descricao,
        p.fk_equipe_casa,
        p.fk_equipe_visitante,
        p.pk_partida,
        p.pontos_turma_casa,
        p.pontos_turma_visitante,
        ec.fk_nome_turma AS fk_turma_casa,
        ev.fk_nome_turma AS fk_turma_visitante,
        ec.nome_equipe AS nome_equipe_casa,
        ev.nome_equipe AS nome_equipe_visitante
    FROM calendario AS c
    JOIN partidas AS p ON c.fk_partida = p.pk_partida
    JOIN esportes AS e ON p.fk_esporte = e.pk_esporte
    JOIN equipes AS ec ON p.fk_equipe_casa = ec.pk_equipe
    JOIN equipes AS ev ON p.fk_equipe_visitante = ev.pk_equipe
    WHERE c.dia_evento >= %s AND c.dia_evento < %s
    """
    params = [primeiroDia, ultimoDia]

    if modalidade:
        query += " AND e.pk_esporte = %s"
        params.append(modalidade)

    if turma:
        query += " AND (ec.fk_nome_turma = %s OR ev.fk_nome_turma = %s)"
        params.extend([turma, turma])

    if descricao:
        query += " AND p.fk_descricao = %s"
        params.append(descricao)

    cursor.execute(query, params)


    eventos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return eventos
