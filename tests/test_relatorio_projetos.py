from datetime import date, timedelta

from src.models import Habito, Projeto, Tarefa
from src.relatorio_projetos import (
    calcular_progresso_geral,
    gerar_dados_projeto,
    gerar_desempenho_geral_projetos,
    obter_diagnostico_projeto,
)

HOJE = date.today()


def test_progresso_geral_e_a_media_quando_ha_tarefas_e_habitos():
    assert calcular_progresso_geral(80.0, 40.0) == 60.0


def test_progresso_geral_usa_so_o_que_existe():
    assert calcular_progresso_geral(None, 40.0) == 40.0
    assert calcular_progresso_geral(80.0, None) == 80.0
    assert calcular_progresso_geral(None, None) == 0.0


def test_diagnostico_por_faixa():
    assert obter_diagnostico_projeto(95, 3) == "Excelente"
    assert obter_diagnostico_projeto(75, 3) == "Bom"
    assert obter_diagnostico_projeto(55, 3) == "Regular"
    assert obter_diagnostico_projeto(10, 3) == "Crítico"
    assert obter_diagnostico_projeto(0, 0) == "Vazio"


def test_dados_do_projeto_consideram_apenas_itens_vinculados():
    projeto = Projeto(1, "Faculdade", "")
    tarefas = [
        Tarefa(1, "A", "", HOJE, True, HOJE, HOJE, projeto_id=1),
        Tarefa(2, "B", "", HOJE, False, HOJE, None, projeto_id=1),
        Tarefa(3, "Outra", "", HOJE, False, HOJE, None, projeto_id=2),
    ]
    habitos = [Habito(1, "Ler", "diario", 2, HOJE - timedelta(days=1), HOJE, projeto_id=1)]

    dados = gerar_dados_projeto(projeto, tarefas, habitos)

    assert dados["metricas"]["tarefas_total"] == 2
    assert dados["metricas"]["tarefas_conclusao"] == 50.0
    assert dados["metricas"]["habitos_consistencia"] == 100.0
    assert dados["progresso_geral"] == 75.0
    assert dados["diagnostico"] == "Bom"


def test_desempenho_geral_ignora_projetos_vazios_na_media():
    projetos = [Projeto(1, "Com itens", ""), Projeto(2, "Vazio", "")]
    tarefas = [Tarefa(1, "A", "", HOJE, True, HOJE, HOJE, projeto_id=1)]

    relatorio = gerar_desempenho_geral_projetos(projetos, tarefas, [])

    assert relatorio["metricas"]["media_global"] == 100.0
    assert len(relatorio["categorias"]["Vazio"]) == 1
