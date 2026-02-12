from ..CRIAR.criarConexao import criarConexao, database

def subirCargo(matricula,nivel):
    conexao = criarConexao()
    cursor = conexao.cursor()

    cursor.execute(f'UPDATE {database}.login SET nivel = %s WHERE pk_usuario = %s',(nivel,matricula))

    conexao.commit()
    cursor.close()
    conexao.close()