""" Módulo responsável pela interface de usuário (visualizações) para tarefas e hábitos. """

from src.utils import formatar_data
from src.relatorio_habitos import verificar_status_habito


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


def exibir_relatorio_tarefas(relatorio):
    """ Exibe o relatório de desempenho das tarefas. """

    if not relatorio:
        print("Nenhum dado de relatório disponível.")
        return

    m = relatorio["metricas"]

    print("\n=== RELATORIO DE TAREFAS ===")
    print(f"Total: {m['total_tarefas']}")
    print(
        f"Concluídas: {m['tarefas_concluidas']} ({m['taxa_conclusao_percentual']:.2f}%)")
    print(f"Pendentes: {m['tarefas_pendentes']}")
    print(f"Atrasadas: {m['tarefas_atrasadas']}")
    print(f"Pontualidade: {m['taxa_pontualidade_percentual']:.2f}%")

    print("\nPor Categorias:")
    prazos = relatorio["prazos"]
    for categoria, lista_tarefas in prazos.items():
        print(f"- {categoria}: {len(lista_tarefas)} tarefas")

    print("\nDiagnóstico:")
    print(relatorio["diagnostico"])


def exibir_relatorio_habitos(relatorio):
    """ Exibe o relatório de desempenho dos hábitos. """

    if not relatorio:
        print("Nenhum dado de relatório disponível.")
        return

    m = relatorio["metricas"]

    print("\n=== RELATORIO DE HABITOS ===")
    print(f"Total: {m['total_habitos']}")
    print(f"Em chamas: {m['habitos_em_chamas']} (Ativos)")
    print(f"Congelados: {m['habitos_congelados']} (Inativos)")
    print(f"Consistência Média: {m['consistencia_media']:.2f}%")

    print("\nDetalhes por Hábito:")
    for detalhe in relatorio["detalhes"]:
        print(
            f"- {detalhe['nome']}: {detalhe['status']} | "
            f"Execuções: {detalhe['execucoes_reais']}/{detalhe['execucoes_esperadas']} | "
            f"Consistência: {detalhe['consistencia']:.2f}% | "
            f"Dias sem fazer: {detalhe['dias_sem_fazer']}"
        )

    print("\nDiagnóstico:")
    print(relatorio["diagnostico"])


def exibir_status_habitos(lista_habitos):
    """ Exibe uma lista com o status de cada hábito. """
    if not lista_habitos:
        print("Nenhum hábito cadastrado.")
        return

    print("\nStatus dos Hábitos:")
    for habito in lista_habitos:
        status, dias = verificar_status_habito(habito)
        print(f"[{status}] {habito.nome} - Dias sem fazer: {dias}")
