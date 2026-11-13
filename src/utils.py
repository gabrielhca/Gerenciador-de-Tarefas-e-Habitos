""" Guarda funções utilitárias. """

import os
import unicodedata
from datetime import datetime
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
PASTA_DADOS = PASTA_RAIZ / "data"
PASTA_RELATORIOS = PASTA_RAIZ / "relatorios"


def formatar_data(data_str):
    """ Converte uma string de data no formato DD-MM-AAAA para um objeto date. """
    try:
        return datetime.strptime(data_str, "%d-%m-%Y").date()
    except ValueError:
        print("Formato de data invalido. Use DD-MM-AAAA.")
        return None


def normalizar_frequencia(texto):
    """ Converte variações como 'Diário', 'diária' ou 'semana' para 'diario' ou 'semanal'.

    Retorna None se a frequência não for reconhecida.
    """
    if not texto:
        return None
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    sem_acento = sem_acento.strip().lower()
    if sem_acento.startswith("diari"):
        return "diario"
    if sem_acento.startswith("semana"):
        return "semanal"
    return None


def formatar_data_para_string(data):
    """ Converte um objeto date para uma string no formato DD-MM-AAAA. """
    if not data:
        return ""
    if isinstance(data, str):
        return data
    return data.strftime("%d-%m-%Y")

def exportar_relatorio(texto, nome_arquivo):
    """ Exporta um texto para um arquivo de texto. """

    pasta = PASTA_RELATORIOS
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)
        print(f"Relatório exportado para {caminho_arquivo}")
    except IOError as e:
        print(f"Erro ao exportar o relatório: {e}")
            