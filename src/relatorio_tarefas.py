""" Módulo responsável pela geração de relatórios de tarefas. """

from datetime import date, timedelta


def filtrar_tarefas_pendentes(lista_tarefas):
    """ Retorna uma lista de tarefas que não estão concluídas. """
    return [tarefa for tarefa in lista_tarefas if not tarefa.concluida]


def filtrar_tarefas_concluidas(lista_tarefas):
    """ Retorna uma lista de tarefas que estão concluídas. """
    return [tarefa for tarefa in lista_tarefas if tarefa.concluida]


def filtrar_tarefas_atrasadas(lista_tarefas):
    """ Retorna uma lista de tarefas que estão atrasadas. """
    hoje = date.today()
    return [tarefa for tarefa in lista_tarefas if not tarefa.concluida and tarefa.data_limite < hoje]


def calcula_percentual_conclusao(lista_tarefas):
    """ Calcula o percentual de tarefas concluídas. """
    total_tarefas = len(lista_tarefas)
    if total_tarefas == 0:
        return 0.0

    tarefas_concluidas = len(filtrar_tarefas_concluidas(lista_tarefas))
    percentual = (tarefas_concluidas / total_tarefas) * 100
    return percentual


def obter_categoria_de_prazos(lista_tarefas):
    """ Categoriza as tarefas por urgência. """

    hoje = date.today()
    amanha = hoje + timedelta(days=1)
    semana = hoje + timedelta(days=7)

    pendentes = filtrar_tarefas_pendentes(lista_tarefas)

    radar = {
        "Atrasadas": [],
        "Urgentes": [],
        "Próximas": [],
        "Futuras": []
    }

    for tarefa in pendentes:
        if tarefa.data_limite < hoje:
            radar["Atrasadas"].append(tarefa)
        elif tarefa.data_limite <= amanha:
            radar["Urgentes"].append(tarefa)
        elif tarefa.data_limite <= semana:
            radar["Próximas"].append(tarefa)
        else:
            radar["Futuras"].append(tarefa)

    return radar


def calcular_pontualidade(lista_tarefas):
    """ Retorna a porcentagem de tarefas entregues no prazo. """

    if not lista_tarefas:
        return 0.0

    concluidas = filtrar_tarefas_concluidas(lista_tarefas)
    atrasadas = filtrar_tarefas_atrasadas(lista_tarefas)
    total_avaliado = len(concluidas) + len(atrasadas)

    if total_avaliado == 0:
        return 0.0

    no_prazo = 0
    for tarefa in concluidas:
        if tarefa.data_conclusao and tarefa.data_conclusao <= tarefa.data_limite:
            no_prazo += 1

    return (no_prazo / total_avaliado) * 100


def obter_diagnostico_tarefas(prazos, taxa_conclusao):
    """ Gera um diagnóstico baseado nos prazos das tarefas. """

    quantidade_atrasadas = len(prazos["Atrasadas"])
    quantidade_urgentes = len(prazos["Urgentes"])

    if quantidade_atrasadas > 0:
        return f"Critico: Você tem {quantidade_atrasadas} tarefas atrasadas. Priorize-as imediatamente."
    elif quantidade_urgentes > 0:
        return f"Atenção: Você tem {quantidade_urgentes} tarefas urgentes. Foque nelas em breve."
    elif taxa_conclusao == 100:
        return "Excelente: Todas as suas tarefas foram concluídas com sucesso!"
    else:
        return "Bom: Situação está sob controle, continue assim."


def gerar_desempenho_tarefas(lista_tarefas):
    """ Gera um relatório de desempenho para uma lista de tarefas. """

    if not lista_tarefas:
        return None

    total = len(lista_tarefas)
    pendentes = len(filtrar_tarefas_pendentes(lista_tarefas))
    concluidas = len(filtrar_tarefas_concluidas(lista_tarefas))
    atrasadas = len(filtrar_tarefas_atrasadas(lista_tarefas))
    taxa_conclusao = calcula_percentual_conclusao(lista_tarefas)
    taxa_pontualidade = calcular_pontualidade(lista_tarefas)
    prazos = obter_categoria_de_prazos(lista_tarefas)

    relatorio = {
        "metricas": {
            "total_tarefas": total,
            "tarefas_pendentes": pendentes,
            "tarefas_concluidas": concluidas,
            "tarefas_atrasadas": atrasadas,
            "taxa_conclusao_percentual": taxa_conclusao,
            "taxa_pontualidade_percentual": taxa_pontualidade
        },
        "prazos": prazos,
        "diagnostico": obter_diagnostico_tarefas(prazos, taxa_conclusao)
    }

    return relatorio
