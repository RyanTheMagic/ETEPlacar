from ..CRIAR.criarConexao import criarConexao, database
from flask import flash

def buscarEstatisticasPorModalidade(modalidade):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute(f'SELECT * FROM {database}.estatisticas_esporte WHERE fk_esporte = %s', (modalidade,))
        estatisticasBuscadas = cursor.fetchall()
        return estatisticasBuscadas
    except:
        conexao.rollback()
        flash('Ocorreu um erro inesperado', 'erro')
    finally:
        cursor.close()
        conexao.close()
