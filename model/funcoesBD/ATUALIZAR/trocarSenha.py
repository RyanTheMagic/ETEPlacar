from ..CRIAR.criarConexao import criarConexao, database
def trocarSenha(matricula, senha):
    conexao = criarConexao()
    cursor = conexao.cursor()
    cursor.execute(f'UPDATE {database}.login SET senha = %s WHERE pk_usuario = %s', (senha, matricula))

    conexao.commit()
    cursor.close()
    conexao.close()