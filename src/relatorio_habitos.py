""" Módulo responsável pela geração de relatórios de hábitos. """

from datetime import date

STATUS_ATIVO = "Em chamas"
STATUS_INATIVO = "Congelado"

def calcular_execucoes_esperadas(habito):
    """ Calcula o número de execuções esperadas desde a criação do hábito. """
    if not habito.data_criacao:
        return 0

    hoje = date.today()
    dias_desde_criacao = (hoje - habito.data_criacao).days

    if dias_desde_criacao < 0:
        dias_desde_criacao = 0

    if "diaria" in habito.frequencia.lower():
        return dias_desde_criacao + 1
    elif "semanal" in habito.frequencia.lower():
        return (dias_desde_criacao // 7) + 1
    return 0


def calcular_consistencia_habito(habito):
    """ Calcula a porcentagem de consistência de um único hábito. """
    esperadas = calcular_execucoes_esperadas(habito)
    if esperadas == 0:
        return 0.0
    consistencia = (habito.contador_execucoes / esperadas) * 100
    return min(100.0, consistencia)


def verificar_status_habito(habito):
    """ Verifica o status da atividade com base na última execução. """

    if not habito.data_ultima_execucao:
        dias_sem_fazer = (date.today() - habito.data_criacao).days
        return "Nunca realizado", dias_sem_fazer

    hoje = date.today()
    dias_sem_fazer = (hoje - habito.data_ultima_execucao).days
    if dias_sem_fazer < 0:
        dias_sem_fazer = 0

    status = "Indefinido"

    # Lógica para hábitos diários
    if "diaria" in habito.frequencia.lower():
        if dias_sem_fazer == 0:
            status = STATUS_ATIVO
        elif dias_sem_fazer == 1:
            status = "Em dia"
        elif dias_sem_fazer <= 3:
            status = "Atenção"
        else:
            status = STATUS_INATIVO

    # Lógica para hábitos semanais
    elif "semanal" in habito.frequencia.lower():
        if dias_sem_fazer <= 7:
            status = STATUS_ATIVO
        elif dias_sem_fazer <= 14:
            status = "Atenção"
        else:
            status = STATUS_INATIVO
    return status, dias_sem_fazer


def gerar_desempenho_habitos(lista_habitos):
    """ Gera um relatório de desempenho para uma lista de hábitos. """

    if not lista_habitos:
        return None

    detalhes = []
    soma_consistencia = 0
    quantidade_em_chamas = 0
    quantidade_congelados = 0

    for habito in lista_habitos:
        consistencia = calcular_consistencia_habito(habito)
        esperadas = calcular_execucoes_esperadas(habito)
        status, dias_sem_fazer = verificar_status_habito(habito)

        soma_consistencia += consistencia
        if status == STATUS_ATIVO:
            quantidade_em_chamas += 1
        elif status == STATUS_INATIVO:
            quantidade_congelados += 1

        dados = {
            "nome": habito.nome,
            "frequencia": habito.frequencia,
            "execucoes_reais": habito.contador_execucoes,
            "execucoes_esperadas": esperadas,
            "consistencia": consistencia,
            "status": status,
            "dias_sem_fazer": dias_sem_fazer
        }

        detalhes.append(dados)

    total = len(lista_habitos)
    consistencia_media = soma_consistencia / total if total > 0 else 0

    if consistencia_media >= 80:
        diagnostico = "Excelente: Voce mantém uma rotina disciplinada."
    elif quantidade_congelados > total / 2:
        diagnostico = "Crítico: A maioria dos seus hábitos foi abandonado."
    elif quantidade_em_chamas > 0:
        diagnostico = "Bom: Você está ativo hoje, continue assim."
    else:
        diagnostico = "Regular: Há espaço para melhorias."

    relatorio = {
        "metricas": {
            "total_habitos": total,
            "consistencia_media": consistencia_media,
            "habitos_em_chamas": quantidade_em_chamas,
            "habitos_congelados": quantidade_congelados
        },
        "detalhes": detalhes,
        "diagnostico": diagnostico
    }

    return relatorio
