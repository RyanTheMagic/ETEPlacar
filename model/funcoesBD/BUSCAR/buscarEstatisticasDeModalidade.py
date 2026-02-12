from ..CRIAR.criarConexao import criarConexao, database
def buscarEstatisticasDeModalidade():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(f'''SELECT DISTINCT fk_esporte, fk_nome_estatistica FROM {database}.estatisticas_esporte ORDER by 
                   CASE
                        WHEN fk_nome_estatistica IN ('Gols', 'Sets', 'Pontos') THEN 1
                        WHEN fk_nome_estatistica IN ('Finalizações', 'Arremessos de Três') THEN 2
                        WHEN fk_nome_estatistica IN ('Passes', 'Rebotes') THEN 3
                        ELSE 4
                    END;
                   ''')
    esportesComEst = cursor.fetchall()
    
    cursor.close()
    conexao.close()

    return esportesComEst
     