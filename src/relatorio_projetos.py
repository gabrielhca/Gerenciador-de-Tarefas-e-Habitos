""" Módulo responsável pela geração de relatórios relacionados a projetos. """

from src.relatorio_tarefas import calcula_percentual_conclusao
from src.relatorio_habitos import calcular_consistencia_habito


def filtrar_itens_por_projeto(projeto_id, lista_tarefas, lista_habitos):
    """ Retorna as tarefas e hábitos vinculados a um projeto específico. """
    tarefas_proj = [t for t in lista_tarefas if t.projeto_id == projeto_id]
    habitos_proj = [h for h in lista_habitos if h.projeto_id == projeto_id]
    return tarefas_proj, habitos_proj


def calcular_progresso_geral(taxa_tarefas, consistencia_habitos):
    """ Calcula o progresso geral de 0 a 100 para o projeto. """
    if taxa_tarefas is None and consistencia_habitos is None:
        return 0.0
    if taxa_tarefas is None:
        return consistencia_habitos
    if consistencia_habitos is None:
        return taxa_tarefas
    
    return (taxa_tarefas + consistencia_habitos) / 2


def obter_diagnostico_projeto(progresso, total_itens):
    """ Define a categoria do projeto baseada no progresso. """
    if total_itens == 0:
        return "Vazio"
    
    if progresso >= 90:
        return "Excelente"
    elif progresso >= 70:
        return "Bom"
    elif progresso >= 50:
        return "Regular"
    else:
        return "Crítico"


def gerar_dados_projeto(projeto, lista_tarefas, lista_habitos):
    """ Gera os dados individuais de um projeto para o relatório. """
    tarefas, habitos = filtrar_itens_por_projeto(projeto.id, lista_tarefas, lista_habitos)
    
    total_tarefas = len(tarefas)
    taxa_tarefas = calcula_percentual_conclusao(tarefas) if total_tarefas > 0 else None

    total_habitos = len(habitos)
    
    soma_consistencia = 0
    for h in habitos:
        soma_consistencia += calcular_consistencia_habito(h)
    
    media_consistencia = 0.0
    if total_habitos > 0:
        media_consistencia = soma_consistencia / total_habitos
    else:
        media_consistencia = None

    progresso = calcular_progresso_geral(taxa_tarefas, media_consistencia)
    diagnostico = obter_diagnostico_projeto(progresso, total_tarefas + total_habitos)

    exib_tarefas = taxa_tarefas if taxa_tarefas else 0.0
    exib_habitos = media_consistencia if media_consistencia else 0.0

    return {
        "projeto": projeto,
        "tarefas": tarefas,
        "habitos": habitos,
        "metricas": {
            "tarefas_total": total_tarefas,
            "tarefas_conclusao": exib_tarefas,
            "habitos_total": total_habitos,
            "habitos_consistencia": exib_habitos
        },
        "progresso_geral": progresso,
        "diagnostico": diagnostico
    }


def gerar_desempenho_geral_projetos(lista_projetos, lista_tarefas, lista_habitos):
    """ Gera um relatório agrupando projetos por categorias (diagnóstico). """
    
    if not lista_projetos:
        return None

    categorias = {
        "Excelente": [],
        "Bom": [],
        "Regular": [],
        "Crítico": [],
        "Vazio": []
    }

    total_projetos = len(lista_projetos)
    soma_progresso_global = 0
    projetos_ativos = 0

    for proj in lista_projetos:
        dados = gerar_dados_projeto(proj, lista_tarefas, lista_habitos)
        diagnostico = dados["diagnostico"]
        
        if diagnostico in categorias:
            categorias[diagnostico].append(dados)
        
        if diagnostico != "Vazio":
            soma_progresso_global += dados["progresso_geral"]
            projetos_ativos += 1

    media_global = soma_progresso_global / projetos_ativos if projetos_ativos > 0 else 0
    
    diagnostico_geral = ""
    if media_global >= 80:
        diagnostico_geral = "Sistêmico: Você está gerenciando suas áreas com maestria."
    elif len(categorias["Crítico"]) > len(categorias["Bom"]):
        diagnostico_geral = "Alerta: Muitas áreas da sua vida estão em estado crítico."
    else:
        diagnostico_geral = "Equilibrado: Continue mantendo o ritmo nos projetos principais."

    return {
        "metricas": {
            "total_projetos": total_projetos,
            "media_global": media_global
        },
        "categorias": categorias,
        "diagnostico_geral": diagnostico_geral
    }