from datetime import date

import pytest

from src.models import Habito, Projeto, Tarefa


def test_tarefa_from_csv_le_todos_os_campos():
    tarefa = Tarefa.from_csv("3;Estudar;Lista 2;15-02-2026;1;07-02-2026;14-02-2026;1\n")

    assert tarefa.id == 3
    assert tarefa.titulo == "Estudar"
    assert tarefa.data_limite == date(2026, 2, 15)
    assert tarefa.concluida is True
    assert tarefa.data_conclusao == date(2026, 2, 14)
    assert tarefa.projeto_id == 1


def test_tarefa_from_csv_sem_projeto_e_sem_conclusao():
    tarefa = Tarefa.from_csv("1;Feira;Frutas;10-01-2026;0;05-01-2026;;\n")

    assert tarefa.concluida is False
    assert tarefa.data_conclusao is None
    assert tarefa.projeto_id is None


def test_habito_from_csv_contador_vazio_vira_zero():
    habito = Habito.from_csv("2;Meditar;diario;;07-02-2026;;2\n")

    assert habito.contador_execucoes == 0
    assert habito.data_ultima_execucao is None
    assert habito.projeto_id == 2


def test_projeto_from_csv():
    projeto = Projeto.from_csv("1;Faculdade;Matérias do semestre\n")

    assert projeto.id == 1
    assert projeto.nome == "Faculdade"


@pytest.mark.parametrize(
    "criar",
    [
        lambda: Tarefa(1, "  ", "desc", date.today()),
        lambda: Habito(1, "", "diario"),
        lambda: Habito(1, "Ler", ""),
        lambda: Projeto(1, "", "desc"),
    ],
)
def test_campos_obrigatorios_vazios_sao_rejeitados(criar):
    with pytest.raises(ValueError):
        criar()
