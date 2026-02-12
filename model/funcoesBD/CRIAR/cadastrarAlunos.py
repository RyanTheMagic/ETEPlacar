from .criarConexao import criarConexao, database

def cadastrarAlunos(matricula):
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute(f'INSERT INTO {database}.login (pk_usuario, senha, nivel) values (%s,%s,%s)', (matricula, f'etemfl@{matricula}','Aluno'))
    conexao.commit()

    cursor.close()
    conexao.close()

    return print('Cadastrado com sucesso')
