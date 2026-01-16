""" Guarda funções utilitárias. """


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
