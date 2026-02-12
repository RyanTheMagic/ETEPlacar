from ..CRIAR.criarConexao import criarConexao, database

def buscarModalidades():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM {database}.esportes')

    modalidadesBuscadas = cursor.fetchall()

    return modalidadesBuscadas
    