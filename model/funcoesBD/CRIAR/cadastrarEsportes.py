from .criarConexao import criarConexao, database
from ..BUSCAR.buscarModalidades import buscarModalidades
from flask import flash

def cadastrarEsportes(esporte, grupo, qtdjogadores):
    try:
        verifica = False
        conexao = criarConexao()
        cursor = conexao.cursor()
        modalidades = buscarModalidades()

        cursor.execute(f'INSERT INTO {database}.esportes (pk_esporte, grupo, qtd_jogadores) values (%s, %s, %s)', (esporte,grupo,qtdjogadores))
        conexao.commit()
        flash(f'{esporte} foi registrado com sucesso!', 'sucesso')
    except:
        conexao.rollback()
        for modalidade in modalidades:
            if esporte == modalidade['pk_esporte']:
                verifica = True
        if verifica:
            flash(f'{esporte} já está registrado!', 'erro')
        else:
            flash('Ocorreu um erro inesperado na criação de modalidade!','erro')
    finally:
        cursor.close()
        conexao.close()


