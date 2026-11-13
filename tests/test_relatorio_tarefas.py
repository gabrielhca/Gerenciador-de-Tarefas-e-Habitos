from datetime import date, timedelta

from src.models import Tarefa
from src.relatorio_tarefas import (
    calcula_percentual_conclusao,
    calcular_pontualidade,
    gerar_desempenho_tarefas,
    obter_categoria_de_prazos,
)

HOJE = date.today()


def criar_tarefa(tarefa_id, dias_ate_prazo, concluida=False, dias_ate_conclusao=None):
    data_conclusao = None
    if concluida and dias_ate_conclusao is not None:
        data_conclusao = HOJE + timedelta(days=dias_ate_conclusao)
    return Tarefa(
        tarefa_id,
        f"Tarefa {tarefa_id}",
        "",
        HOJE + timedelta(days=dias_ate_prazo),
        concluida,
        HOJE,
        data_conclusao,
    )


def test_percentual_de_conclusao():
    tarefas = [criar_tarefa(1, 5, concluida=True), criar_tarefa(2, 5)]
    assert calcula_percentual_conclusao(tarefas) == 50.0


def test_percentual_de_conclusao_lista_vazia():
    assert calcula_percentual_conclusao([]) == 0.0


def test_categorias_de_prazo():
    tarefas = [
        criar_tarefa(1, -1),  # atrasada
        criar_tarefa(2, 1),  # urgente (vence amanhã)
        criar_tarefa(3, 5),  # próxima (na semana)
        criar_tarefa(4, 30),  # futura
        criar_tarefa(5, -10, concluida=True),  # concluída não entra
    ]

    radar = obter_categoria_de_prazos(tarefas)

    assert [t.id for t in radar["Atrasadas"]] == [1]
    assert [t.id for t in radar["Urgentes"]] == [2]
    assert [t.id for t in radar["Próximas"]] == [3]
    assert [t.id for t in radar["Futuras"]] == [4]


def test_pontualidade_conta_atrasadas_como_falha():
    tarefas = [
        criar_tarefa(1, 0, concluida=True, dias_ate_conclusao=-1),  # entregue no prazo
        criar_tarefa(2, -5, concluida=True, dias_ate_conclusao=-2),  # entregue atrasada
        criar_tarefa(3, -1),  # pendente e atrasada
    ]
    assert round(calcular_pontualidade(tarefas), 2) == 33.33


def test_diagnostico_com_tarefas_atrasadas():
    relatorio = gerar_desempenho_tarefas([criar_tarefa(1, -3)])
    assert relatorio["diagnostico"].startswith("Critico")


def test_relatorio_lista_vazia_retorna_none():
    assert gerar_desempenho_tarefas([]) is None
