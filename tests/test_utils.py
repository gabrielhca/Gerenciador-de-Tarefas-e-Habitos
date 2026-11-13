from datetime import date

import pytest

from src.utils import formatar_data, formatar_data_para_string, normalizar_frequencia


def test_formatar_data_valida():
    assert formatar_data("07-02-2026") == date(2026, 2, 7)


def test_formatar_data_invalida_retorna_none():
    assert formatar_data("2026-02-07") is None


def test_formatar_data_para_string():
    assert formatar_data_para_string(date(2026, 2, 7)) == "07-02-2026"
    assert formatar_data_para_string(None) == ""


@pytest.mark.parametrize(
    ("entrada", "esperado"),
    [
        ("diario", "diario"),
        ("Diário", "diario"),
        ("diária", "diario"),
        ("semana", "semanal"),
        (" Semanal ", "semanal"),
        ("mensal", None),
        ("", None),
    ],
)
def test_normalizar_frequencia(entrada, esperado):
    assert normalizar_frequencia(entrada) == esperado
