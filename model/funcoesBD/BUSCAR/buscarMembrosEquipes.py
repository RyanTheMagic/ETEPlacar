from ..CRIAR.criarConexao import criarConexao, database

def buscarMembrosEquipe():
    conexao = criarConexao()
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("""
        SELECT 
            m.fk_equipe,
            m.fk_matricula,
            a.nome_aluno,
            a.fk_nome_turma,
            a.fk_classificacao
        FROM 
            membros_equipe AS m 
        JOIN 
            alunos AS a ON m.fk_matricula = a.pk_matricula
    """)
    
    equipesBuscadas = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return equipesBuscadas