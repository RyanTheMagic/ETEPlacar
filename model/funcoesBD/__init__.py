from .ATUALIZAR import (
adicionarEstatisticasCasa,
adicionarEstatisticasVisitante,
adicionarEstatVisitanteCalendario,
adicionarEstatCasaCalendario,
subirCargo,
trocarSenha
)
from .CRIAR import (
cadastrarAlunos,
cadastrarEsportes,
cadastrarEstatisticasParaModalidade,
criarConexao,
criarEstatisticas,
criarPartidas
)
from .BUSCAR import (
buscarEstatisticasRegistradas,
buscarEstatisticasPorId,
buscarEquipesPorModalidade,
buscarMembrosEquipe,
buscarEstatisticasDeModalidade,
buscarEstatisticasPorModalidade,
buscarEventosCalendario,
buscarEstatisticasPrincipal,
buscarEventosCalendarioFiltros,
buscarModalidades,
buscarPartidaPorId,
buscarPartidas,
buscarTurmas,
buscarUsuarios,
buscarEquipes
)
from .DELETAR import (
    removerPartidasPorModalidade,
    removerEstatisticas,
    removerEstatisticasDaModalidade,
    removerModalidade,
    removerPartidasPorId
)