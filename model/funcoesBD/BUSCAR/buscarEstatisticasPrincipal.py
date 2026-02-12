from ..CRIAR.criarConexao import criarConexao, database

def buscarEstatisticasPrincipal():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'''
    SELECT * 
    FROM {database}.estatisticas_esporte
    ORDER BY 
        CASE
            WHEN fk_nome_estatistica IN ('Sets') THEN 1
            WHEN fk_nome_estatistica IN ('Gols', 'Pontos') THEN 2
            WHEN fk_nome_estatistica IN ('Finalizações', 'Arremessos de Três') THEN 3
            WHEN fk_nome_estatistica IN ('Passes', 'Rebotes') THEN 4
            ELSE 5
        END;
    ''')

    estatisticasBuscadas = cursor.fetchall()

    return estatisticasBuscadas
    