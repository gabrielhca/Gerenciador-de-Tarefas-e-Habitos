""" Guarda funções utilitárias. """

from datetime import datetime


def ler_sim_nao(pergunta):
    """ 
    Faz uma pergunta ao usuario e retorna:
    - True se a resposta for 's', 'sim', 'y', 'yes'
    - False se a resposta for 'n', 'nao', 'no'
    Continua perguntando ate receber uma resposta valida.
    """
    respostas_positivas = {"s", "sim", "y", "yes"}
    respostas_negativas = {"n", "nao", "no"}

    while True:
        resposta = input(pergunta + " (s/n): ").strip().lower()
        if resposta in respostas_positivas:
            return True
        elif resposta in respostas_negativas:
            return False
        else:
            print("Resposta invalida. Por favor, responda com 's' ou 'n'.")


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
