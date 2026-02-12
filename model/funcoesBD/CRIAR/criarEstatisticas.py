from .criarConexao import criarConexao, database
from ..BUSCAR.buscarEstatisticasRegistradas import buscarEstatisticasRegistradas
from flask import flash

def criarEstatisticas(nomeDaEstatistica):
    try:
        estatisticas = buscarEstatisticasRegistradas()
        verifica = False
        conexao = criarConexao()
        cursor = conexao.cursor()
        cursor.execute(f'INSERT INTO {database}.tipo_estatistica(pk_nome_estatistica) values (%s)', (nomeDaEstatistica,))

        conexao.commit()
        flash(f'{nomeDaEstatistica} foi criada com sucesso!', 'sucesso')
    except:
        conexao.rollback()
        for estatistica in estatisticas:
            if estatistica['pk_nome_estatistica'] == nomeDaEstatistica:
                verifica = True
        if verifica:
            flash(f'{nomeDaEstatistica} já está registrado(a) no banco de dados', 'erro')
        else:
            flash('Ocorreu um erro inesperado ao criar estatisticas', 'erro')
            
        
    finally:
        cursor.close()
        conexao.close()