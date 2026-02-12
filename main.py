from flask import Flask, render_template, redirect, request, session, jsonify, flash
from datetime import datetime, date
from calendar import *
from functools import wraps
from model import *

app = Flask(__name__)
app.secret_key = 'osegredodocabeca'

def requerSessao(f):
    @wraps(f)
    def verificandoSessao(*args, **kwargs):
        if 'nome' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return verificandoSessao

#Decorator para verificar se o usuario é Administrador
def requerAdmin(f):
    @wraps(f)
    def requerindoAdmin(*args, **kwargs):
        if session['nivel'] != "Administrador":
            return redirect('/')
        return f(*args, **kwargs)
    return requerindoAdmin

#Decorator para verificar se o usuario é Administrador ou AlunoMonitor
def requerAdminOuMonitor(f):
    @wraps(f)
    def requerindo(*args, **kwargs):
        if session['nivel'] == 'Aluno':
            return redirect('/')
        return f(*args, **kwargs)
    return requerindo

#Rota para definir calendário como rota primária
@app.route('/')
def defineRotaPrimaria():
    return redirect('/calendario')

@app.route('/login')
def login():
    if 'nome' in session:
        return redirect('/calendario')
    else:
        return render_template('login.html')
    
@app.route('/login', methods=['POST'])
def verificarLogin():
    usuario = request.form['usuario']
    senha = request.form['senha']
    buscaUsuarios = buscarUsuarios()
    for usuarios in buscaUsuarios:
        if usuario == usuarios['pk_usuario'] and senha == usuarios['senha']:
            session['nome'] = usuario
            session['nivel'] = usuarios['nivel']
            return redirect('/calendario')
    
    return redirect('/login')

#Calendario
@app.route('/calendario')
@app.route('/calendario/<int:ano>/<int:mes>')
@app.route('/calendario/<int:ano>/<int:mes>/<int:dia>')
def calendario(ano = None, mes = None, dia = None):
    # Lógica para obter o ano, mês e dia atuais caso não sejam fornecidos na URL
    #Parâmetros:
    #- ano (int): O ano para exibição do calendário. Se não fornecido, é o ano atual.
    #- mes (int): O mês para exibição do calendário. Se não fornecido, é o mês atual.
    #- dia (int): O dia selecionado. Se não fornecido, é o dia atual.
    if ano is None or mes is None:
        hoje = datetime.today()
        ano = hoje.year
        mes = hoje.month
    
    if dia is None:
        dia_selecionado = datetime.today().day
    else:
        dia_selecionado = dia
    
    # Ajuste de mês e ano caso o usuário navegue para meses anteriores ou seguintes:
    #Se o mes for igual a 0, significa que o usuario foi para o ano anterior, ou seja, mês se torna igual a 12 e ano = ano atual - 1
    #Se o mes for igual a 13, significa que o usuario foi para o ano posterior, ou seja, mês se torna igual a 1 e ano = ano atual + 1
    if mes == 0:
        mes = 12
        ano -=1
    elif mes == 13:
        mes = 1
        ano += 1

    turmas = buscarTurmas()

    #Busca eventos no calendario do mês de determinado ano    
    eventos = buscarEventosCalendario(ano, mes)
    eventosDoDia = set() #Evita que tenha duplicatas, pois apenas registra em quais dias tem partidas
    for evento in eventos:
        eventosDoDia.add(evento['dia_evento'].day)

    #Procura as partidas do dia que o usuário escolheu no calendário
    partidas_dia_selecionado = []
    for partida in eventos:
        if partida['dia_evento'].day == dia_selecionado:
            partidas_dia_selecionado.append(partida)

    #Define domingo como o primeiro dia da semana
    calendario_mes = Calendar(firstweekday=6)
    #Busca as semanas do mês de determinado ano
    semanas = calendario_mes.monthdatescalendar(ano, mes) 
    
    #Armazena os nomes dos meses para ser exibido no calendario
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    #nomeMes recebe meses[mes(numero do mês) - 1], pois em listas o primeiro indíce de uma lista é 0
    nomeMes = meses[mes - 1]

    #Funções necessárias para exibição do usuário
    membrosEquipes = buscarMembrosEquipe()
    modalidades = buscarModalidades()
    estatisticasPrincipal = buscarEstatisticasPrincipal()

    return render_template('home.html', 
        ptr = partidas_dia_selecionado,  
        turmas = turmas,
        hoje = date.today(),
        ano = ano,
        semanas = semanas,
        mes = mes,
        eventosDoDia = eventosDoDia,
        nomeMes = nomeMes,
        membrosEquipes = membrosEquipes,
        modalidades = modalidades,
        dia_selecionado = dia_selecionado,
        estatisticasPrincipal = estatisticasPrincipal)

#Rota necessária para a função de filtrar informações no calendário
@app.route('/calendarioFiltrado/<int:ano>/<int:mes>/<int:dia>', methods=['POST'])
def calendarioFiltrado(ano = None, mes = None, dia = None):
    modalidade = request.form['modalidade']
    descricao = request.form['descricao']
    turma = request.form['turma']

    if ano is None or mes is None:
        hoje = datetime.today()
        ano = hoje.year
        mes = hoje.month
    
    if dia is None:
        dia_selecionado = datetime.today().day
    else:
        dia_selecionado = dia
    
    if mes == 0:
        mes = 12
        ano -=1
    elif mes == 13:
        mes = 1
        ano += 1

    turmas = buscarTurmas()
    
    #Busca eventos de maneira especifica, conforme modalidade e/ou turma e/ou descrição -- OBS: Descrição = Masculino ou Feminino
    eventos = buscarEventosCalendarioFiltros(ano, mes, modalidade, turma, descricao)
    eventosDoDia = set()
    for evento in eventos:
        eventosDoDia.add(evento['dia_evento'].day)

    partidas_dia_selecionado = []
    for partida in eventos:
        if partida['dia_evento'].day == dia_selecionado:
            partidas_dia_selecionado.append(partida)
    
    calendario_mes = Calendar(firstweekday=6)
    semanas = calendario_mes.monthdatescalendar(ano, mes) 
    
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    nomeMes = meses[mes - 1]

    membrosEquipes = buscarMembrosEquipe()
    modalidades = buscarModalidades()
    estatisticasPrincipal = buscarEstatisticasPrincipal()

    return render_template('home.html', 
        ptr = partidas_dia_selecionado,  
        turmas = turmas,
        hoje = date.today(),
        ano = ano,
        semanas = semanas,
        mes = mes,
        eventosDoDia = eventosDoDia,
        nomeMes = nomeMes,
        membrosEquipes = membrosEquipes,
        modalidades = modalidades,
        dia_selecionado = dia_selecionado,
        filtroModalidade = modalidade,
        filtroDescricao = descricao,
        filtroTurmas = turma,
        estatisticasPrincipal = estatisticasPrincipal)

#Remove partida
@app.route('/removerPartida/<int:idPartida>/<int:ano>/<int:mes>/<int:dia_selecionado>')
@requerSessao
@requerAdmin
def removerPartida(idPartida, ano, mes, dia_selecionado):
    removerPartidasPorId(idPartida)
    return redirect(f'/calendario/{ano}/{mes}/{dia_selecionado}')

# -------------- ROTA PARA CRIAÇÃO DE PARTIDAS ARTIFICIAIS ---------------
@app.route('/criarPartidas')
@requerSessao
@requerAdmin
def exibirCriarPartida():
    modalidades = buscarModalidades()
    ptr = buscarPartidas()
    equipes = buscarEquipes()
    return render_template('registrarPartidas.html', ptr = ptr, modalidades = modalidades, equipes = equipes)


@app.route('/criarPartidas', methods=['POST'])
@requerSessao
@requerAdmin
def processarCriarPartida():
    modalidade = request.form['Modalidade']

    equipeCasa = request.form['equipeCasa']

    equipeVisitante = request.form['equipeVisitante']

    dataPartida = request.form['dataPartida']

    descricao = request.form['descricao']
    
    criarPartidas(modalidade, descricao, equipeCasa, equipeVisitante, dataPartida)

    return redirect('/criarPartidas')
# -------------- ROTA PARA CRIAÇÃO DE PARTIDAS ARTIFICIAIS ---------------

# ------------------------- GERENCIAR MODALIDADES ----------------------------
#Exibe a tela de gerenciarModalidade juntamente com as variáveis necessárias
@app.route('/gerenciarModalidades')
@app.route('/gerenciarModalidades/<int:ano>/<int:mes>/<int:dia_selecionado>')
@requerSessao
@requerAdmin
def exibirGerenciarModalidades(ano=None, mes=None, dia_selecionado=None):
    esportes = buscarModalidades()
    estatisticas = buscarEstatisticasRegistradas()
    esportesComEst = buscarEstatisticasDeModalidade()
    return render_template('gerenciarModalidades.html', esportes=esportes,estatisticas=estatisticas, esportesComEst=esportesComEst, ano = ano, mes = mes, dia = dia_selecionado)

#Cadastra modalidade juntamente com a classificação dela (Individual, Coletivo) e Quantidade de jogadores
@app.route('/cadastrarModalidades/<int:ano>/<int:mes>/<int:dia>', methods=['POST'])
@requerSessao
@requerAdmin
def processarCadastroModalidades(ano = None,mes = None, dia = None):
    esporte = request.form['esporte']
    esporte = esporte.title()
    grupo = request.form['grupo']
    qtdJogadores = request.form['qtdJogadores']
    cadastrarEsportes(esporte, grupo, qtdJogadores)
    return redirect(f'/gerenciarModalidades/{ano}/{mes}/{dia}')

#Remove modalidade
@app.route('/removerModalidades/<int:ano>/<int:mes>/<int:dia>', methods=['POST'])
@requerSessao
@requerAdmin
def processarRemoverModalidade(ano = None, mes = None, dia = None):
    esporte = request.form['esporte']
    removerModalidade(esporte)
    return redirect(f'/gerenciarModalidades/{ano}/{mes}/{dia}')
# ------------------------- GERENCIAR MODALIDADES ----------------------------

# -------------------- GERENCIAR ESTATISTICAS -------------------------------
#Exibe a tela de gerenciamento de estatisticas, juntamente com as variáveis necessárias
@app.route('/gerenciarEstatisticas')
@app.route('/gerenciarEstatisticas/<int:ano>/<int:mes>/<int:dia_selecionado>')
@requerSessao
@requerAdmin
def exibirGerenciarEstatisticas(ano=None, mes=None, dia_selecionado=None):
    esportes = buscarModalidades()
    estatisticas = buscarEstatisticasRegistradas()
    esportesComEst = buscarEstatisticasDeModalidade()
    return render_template('gerenciarEstatisticas.html', esportes=esportes,estatisticas=estatisticas, esportesComEst=esportesComEst, ano = ano, mes = mes, dia = dia_selecionado)

#Cria estatistica
@app.route('/criarEstatistica/<int:ano>/<int:mes>/<int:dia>', methods=['POST'])
@requerSessao
@requerAdmin
def processarCriarEstatistica(ano=None, mes=None, dia=None):
    estatistica = request.form['estatistica']
    estatistica = estatistica.title()
    criarEstatisticas(estatistica)
    return redirect(f'/gerenciarEstatisticas/{ano}/{mes}/{dia}')

#Remove estatistica
@app.route('/removerEstatistica/<int:ano>/<int:mes>/<int:dia>', methods=['POST'])
@requerSessao
@requerAdmin
def processarRemoverEstatistica(ano=None, mes=None, dia=None):
    estatistica = request.form['estatistica']
    removerEstatisticas(estatistica)
    return redirect(f'/gerenciarEstatisticas/{ano}/{mes}/{dia}')

#Cadastra estatistica para uma modalidade
@app.route("/cadastrarEstatisticasParaModalidade/<int:ano>/<int:mes>/<int:dia>", methods=['POST'])
@requerSessao
def processarCadastrarEstatisticaModalidade(ano=None, mes=None, dia=None):
    esporte = request.form['esporte']
    estatistica = request.form['estatistica']
    cadastrarEstatisticasParaModalidade(esporte, estatistica)
    return redirect(f'/gerenciarEstatisticas/{ano}/{mes}/{dia}')

#Remove estatistica de determinada modalidade
@app.route("/removerEstatisticasParaModalidade/<int:ano>/<int:mes>/<int:dia>", methods=["POST"])
@requerSessao
@requerAdmin
def processarRemoverEstatisticaModalidade(ano=None, mes=None, dia=None):
    esporte = request.form['esporte']
    estatistica = request.form['estatistica']
    if esporte == '':
        flash('Selecione um esporte valido!', 'erro')
    else:
        removerEstatisticasDaModalidade(esporte,estatistica)
    return redirect(f'/gerenciarEstatisticas/{ano}/{mes}/{dia}')

#API relacionada a tela de gerenciar estatisticas na função remover estatisticas para modalidade
@app.route('/api/estatisticasPorModalidade/<string:esporte>')
def processarEstatisticasPorModalidade(esporte):
    estatisticasFiltras = buscarEstatisticasPorModalidade(esporte)
    return jsonify(estatisticasFiltras)
# -------------------- GERENCIAR ESTATISTICAS -------------------------------

#Exibe a tela de Adicionar estatisticas casa
@app.route('/adicionarEstatisticasCasa/<int:idPartidaEstatisticas>/<int:ano>/<int:mes>/<int:dia>')
@requerSessao
@requerAdminOuMonitor
def exibirEstatisticasCasa(idPartidaEstatisticas, ano, mes ,dia):
    partida = buscarPartidaPorId(idPartidaEstatisticas)
    estatisticas = buscarEstatisticasPorId(idPartidaEstatisticas)
    turmas = buscarTurmas()
    membrosEquipes = buscarMembrosEquipe()
    id = idPartidaEstatisticas
    return render_template('adicionarEstatisticasCasa.html', estatisticas=estatisticas, id=id, partida=partida, turmas=turmas, ano = ano, mes = mes, dia = dia, membrosEquipes = membrosEquipes)

#Exibe a tela de Adicionar estatisticas visitante
@app.route('/adicionarEstatisticasVisitante/<int:idPartidaEstatisticas>/<int:ano>/<int:mes>/<int:dia>')
@requerSessao
@requerAdminOuMonitor
def exibirEstatisticasVisitante(idPartidaEstatisticas, ano, mes ,dia):
    partida = buscarPartidaPorId(idPartidaEstatisticas)
    estatisticas = buscarEstatisticasPorId(idPartidaEstatisticas)
    turmas = buscarTurmas()
    membrosEquipes = buscarMembrosEquipe()
    id = idPartidaEstatisticas
    return render_template('adicionarEstatisticasVisitante.html', estatisticas=estatisticas, id=id, partida=partida, turmas=turmas, ano = ano, mes = mes, dia = dia, membrosEquipes = membrosEquipes)

#Adiciona estatisticas para o time casa da partida
@app.route('/adicionarEstatisticasCasa/<int:ano>/<int:mes>/<int:dia>', methods=['POST'])
@requerSessao
@requerAdminOuMonitor
def adicionaestatisticasCasa(ano,mes,dia):
    idPart = int(request.form['id'])
    estatisticas = buscarEstatisticasPorId(idPart)
    for estatistica in estatisticas:
        Quantestat = request.form[estatistica['fk_nome_estatistica']]
        adicionarEstatisticasCasa(idPart, estatistica['fk_nome_estatistica'], Quantestat)
    return redirect(f'/calendario/{ano}/{mes}/{dia}')

#Adiciona estatisticas para o time visitante da partida
@app.route('/adicionarEstatisticasVisitante/<int:ano>/<int:mes>/<int:dia>', methods=['POST'])
@requerSessao
@requerAdminOuMonitor
def adicionaestatisticasVisitante(ano,mes,dia):
    idPart = int(request.form['id'])
    estatisticas = buscarEstatisticasPorId(idPart)
    for estatistica in estatisticas:
        Quantestat = request.form[estatistica['fk_nome_estatistica']]
        adicionarEstatisticasVisitante(idPart, estatistica['fk_nome_estatistica'], Quantestat)
    return redirect(f'/calendario/{ano}/{mes}/{dia}')

#Rota para exibir as estatisticas do time da casa e visitante conforme a partida
@app.route('/detalhes/<int:idPartidaDetalhes>/<int:ano>/<int:mes>/<int:dia>')
def detalhes(idPartidaDetalhes, ano ,mes ,dia):
    partida = buscarPartidaPorId(idPartidaDetalhes)
    turmas = buscarTurmas()
    estatisticas = buscarEstatisticasPorId(idPartidaDetalhes)
    membrosEquipes = buscarMembrosEquipe()
    id = idPartidaDetalhes
    return render_template('detalhes.html', estatisticas=estatisticas, id=id, partida=partida, ano = ano, mes = mes, dia = dia, turmas = turmas, membrosEquipes = membrosEquipes)

#Rota para deslogar
@app.route('/logout')
def deslogar():
    if 'nome' and ('nivel') in session:
        session.pop('nome')
        session.pop('nivel')
    return redirect('/')

