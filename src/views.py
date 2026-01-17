""" Módulo responsável pela interface de usuário (visualizações) para tarefas e hábitos. """

from src.utils import formatar_data


def exibir_dados(dados, tipo):
    """ Exibe a lista de tarefas ou hábitos. """
    if not dados:
        print("Nenhuma informação cadastrada.")
        return
    print(f"\nLista de {tipo}:")
    for item in dados:
        print(item)


def preencher_dados_tarefa():
    """ Solicita ao usuário os dados para criar uma nova tarefa. """
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")

    while True:
        data_limite = input("Data limite (DD-MM-AAAA): ")
        if formatar_data(data_limite):
            break
    return titulo, descricao, data_limite


def preencher_dados_habito():
    """ Solicita ao usuário os dados para criar um novo hábito. """
    nome = input("Nome do hábito: ")
    frequencia = input("Frequência (diária, semanal, mensal): ")
    contador_execucoes = int(input("Contador de execuções inicial: "))
    return nome, frequencia, contador_execucoes


def solicitar_id(dados, tipo):
    """ Solicita ao usuário um ID válido de tarefa ou hábito. """
    exibir_dados(dados, tipo)
    if not dados:
        return None

    while True:
        try:
            entrada = input("Informe o ID (ou '0' para voltar): ")
            if entrada == '0':
                return None
            id_item = int(entrada)

            for item in dados:
                if item.id == id_item:
                    return item
            print("ID não encontrado.\n")
        except ValueError:
            print("Por favor, insira um número válido.")
