""" Guarda funções utilitárias. """

from datetime import datetime


def formatar_data(data_str):
    """ Converte uma string de data no formato DD-MM-AAAA para um objeto date. """
    try:
        return datetime.strptime(data_str, "%d-%m-%Y").date()
    except ValueError:
        print("Formato de data invalido. Use DD-MM-AAAA.")
        return None


def formatar_data_para_string(data):
    """ Converte um objeto date para uma string no formato DD-MM-AAAA. """
    if not data:
        return ""
    if isinstance(data, str):
        return data
    return data.strftime("%d-%m-%Y")
