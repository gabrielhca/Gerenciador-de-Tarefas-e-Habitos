from datetime import date, timedelta

from src.models import Habito
from src.relatorio_habitos import (
    calcular_consistencia_habito,
    calcular_execucoes_esperadas,
    gerar_desempenho_habitos,
    verificar_status_habito,
)

HOJE = date.today()


def criar_habito(frequencia, dias_desde_criacao, execucoes=0, dias_sem_fazer=None):
    ultima = None if dias_sem_fazer is None else HOJE - timedelta(days=dias_sem_fazer)
    return Habito(
        1, "Hábito", frequencia, execucoes, HOJE - timedelta(days=dias_desde_criacao), ultima
    )


def test_execucoes_esperadas_diario_conta_o_dia_de_hoje():
    assert calcular_execucoes_esperadas(criar_habito("diario", 9)) == 10


def test_execucoes_esperadas_semanal():
    assert calcular_execucoes_esperadas(criar_habito("semanal", 14)) == 3


def test_frequencia_com_acento_e_reconhecida():
    assert calcular_execucoes_esperadas(criar_habito("diária", 9)) == 10


def test_consistencia_e_limitada_a_100():
    habito = criar_habito("diario", 1, execucoes=50, dias_sem_fazer=0)
    assert calcular_consistencia_habito(habito) == 100.0


def test_consistencia_parcial():
    habito = criar_habito("diario", 9, execucoes=5, dias_sem_fazer=0)
    assert calcular_consistencia_habito(habito) == 50.0


def test_status_diario():
    assert (
        verificar_status_habito(criar_habito("diario", 30, 1, dias_sem_fazer=0))[0] == "Em chamas"
    )
    assert verificar_status_habito(criar_habito("diario", 30, 1, dias_sem_fazer=1))[0] == "Em dia"
    assert verificar_status_habito(criar_habito("diario", 30, 1, dias_sem_fazer=3))[0] == "Atenção"
    assert (
        verificar_status_habito(criar_habito("diario", 30, 1, dias_sem_fazer=4))[0] == "Congelado"
    )


def test_status_semanal():
    assert (
        verificar_status_habito(criar_habito("semanal", 60, 1, dias_sem_fazer=7))[0] == "Em chamas"
    )
    assert (
        verificar_status_habito(criar_habito("semanal", 60, 1, dias_sem_fazer=10))[0] == "Atenção"
    )
    assert (
        verificar_status_habito(criar_habito("semanal", 60, 1, dias_sem_fazer=15))[0] == "Congelado"
    )


def test_status_nunca_realizado():
    status, dias = verificar_status_habito(criar_habito("diario", 5))
    assert status == "Nunca realizado"
    assert dias == 5


def test_relatorio_conta_habitos_em_chamas():
    habitos = [
        criar_habito("diario", 9, execucoes=10, dias_sem_fazer=0),
        criar_habito("diario", 9, execucoes=1, dias_sem_fazer=8),
    ]
    relatorio = gerar_desempenho_habitos(habitos)

    assert relatorio["metricas"]["total_habitos"] == 2
    assert relatorio["metricas"]["habitos_em_chamas"] == 1
    assert relatorio["metricas"]["habitos_congelados"] == 1
