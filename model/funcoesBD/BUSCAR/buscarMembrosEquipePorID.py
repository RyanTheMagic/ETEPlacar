from ..CRIAR.criarConexao import criarConexao, database

def buscarMembrosEquipePorID(idEquipe):
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute(f'SELECT * FROM {database}.membros_equipe WHERE fk_equipe = %s', (idEquipe,))
    equipesBuscadas = cursor.fetchall()

    return equipesBuscadas