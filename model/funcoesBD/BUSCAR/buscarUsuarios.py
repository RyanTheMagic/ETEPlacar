from ..CRIAR.criarConexao import criarConexao, database

def buscarUsuarios():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.login')

    usuariosBuscados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return usuariosBuscados
