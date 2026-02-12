from ..CRIAR.criarConexao import criarConexao, database

def buscarPartidaPorId(id):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(f"""
        SELECT 
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
        FROM {database}.partidas AS p
        JOIN {database}.esportes AS e ON p.fk_esporte = e.pk_esporte
        JOIN {database}.equipes AS ec ON p.fk_equipe_casa = ec.pk_equipe
        JOIN {database}.equipes AS ev ON p.fk_equipe_visitante = ev.pk_equipe
        WHERE p.pk_partida = %s
    """, (id,))

    partidaBuscada = cursor.fetchone()
    cursor.close()
    conexao.close()

    return partidaBuscada
