""" Módulo responsável pela interface de usuário (visualizações) para tarefas e hábitos. """

from src.utils import formatar_data, formatar_data_para_string, exportar_relatorio
from src.relatorio_habitos import verificar_status_habito, calcular_consistencia_habito, calcular_execucoes_esperadas


def exibir_dados(dados, tipo):
    """ Exibe a lista de tarefas ou hábitos. """
    if not dados:
        print("Nenhuma informação cadastrada.")
        return
    print(f"\nLista de {tipo}:")
    for item in dados:
        print(item)


def preencher_dados_projeto():
    """ Solicita ao usuário os dados para criar um novo projeto. """
    nome = input("Nome do projeto: ")
    descricao = input("Descrição do projeto: ")
    return nome, descricao


def editar_dados_projeto(projeto):
    """ Solicita novos dados para um projeto, mantendo o atual se vazio. """
    print(f"Editando: {projeto.nome}")
    novo_nome = input("Novo nome (enter para manter): ")
    nova_desc = input("Nova descrição (enter para manter): ")
    return novo_nome, nova_desc


def preencher_dados_tarefa(repo_projetos=None):
    """ Solicita ao usuário os dados para criar uma nova tarefa. """
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")

    while True:
        data_limite = input("Data limite (DD-MM-AAAA): ")
        if formatar_data(data_limite):
            break
            
    projeto_id = None
    if repo_projetos:
        print("\nDeseja associar a um projeto? (Caso não, deixe vazio)")
        exibir_dados(repo_projetos.lista_projetos, "projetos")
        pid = input("ID do projeto: ").strip()
        if pid:
            try:
                projeto_id = int(pid)
            except ValueError:
                print("ID inválido, seguindo sem projeto.")
    
    return titulo, descricao, data_limite, projeto_id


def editar_dados_tarefa(tarefa):
    """ Solicita novos dados para uma tarefa, mantendo o atual se vazio. """
    print(f"Editando Tarefa: {tarefa.titulo}")
    print("Deixe em branco para manter o valor atual.")

    titulo = input(f"Novo título ({tarefa.titulo}): ")
    descricao = input(f"Nova descrição ({tarefa.descricao}): ")

    while True:
        data_limite_str = formatar_data_para_string(tarefa.data_limite)
        data_limite = input(f"Nova data limite ({data_limite_str}): ")
        if not data_limite:
            break
        if formatar_data(data_limite):
            break

    return titulo, descricao, data_limite


def editar_dados_habito(habito):
    """ Solicita novos dados para um hábito, mantendo o atual se vazio. """
    print(f"Editando Hábito: {habito.nome}")
    print("Deixe em branco para manter o valor atual.")

    nome = input(f"Novo nome ({habito.nome}): ")
    frequencia = input(f"Nova frequência ({habito.frequencia}): ")

    return nome, frequencia


def preencher_dados_habito(repo_projetos=None):
    """ Solicita ao usuário os dados para criar um novo hábito. """
    nome = input("Nome do hábito: ")
    frequencia = input("Frequência (diario, semanal): ")
    
    while True:
        try:
            contador_execucoes = int(input("Contador de execuções inicial: "))
            break
        except ValueError:
            print("Por favor, insira um número válido para o contador de execuções.")

    data_ultima = None
    if contador_execucoes > 0:
        print("Como você já executou esse hábito, informe a data da última execução.")
        while True:
            data_str = input("Data da última execução (DD-MM-AAAA): ")
            data_ultima = formatar_data(data_str)
            if data_ultima:
                break
    
    projeto_id = None
    if repo_projetos:
        print("\nDeseja associar a um projeto? (Caso não, deixe vazio)")
        exibir_dados(repo_projetos.lista_projetos, "projetos")
        pid = input("ID do projeto: ").strip()
        if pid:
            try:
                projeto_id = int(pid)
            except ValueError:
                print("ID inválido, seguindo sem projeto.")

    return nome, frequencia, contador_execucoes, data_ultima, projeto_id


def solicitar_termo_busca():
    """ Solicita ao usuário um termo para pesquisa. """
    return input("Informe o termo de busca (ou '0' para voltar):").strip()

def solicitar_id(dados):
    """ Solicita ao usuário um ID válido de tarefa ou hábito. """
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

def formatar_relatorio_tarefas(relatorio):
    """ Gera uma string formatada com os dados do relatório de tarefas. """

    if not relatorio:
        return "Nenhum dado de relatório disponível."
    
    m = relatorio["metricas"]
    linhas = []
    linhas.append("=== RELATÓRIO DE TAREFAS ===\n")
    linhas.append(f"Total: {m['total_tarefas']}")
    linhas.append(f"Concluídas: {m['tarefas_concluidas']} ({m['taxa_conclusao_percentual']:.2f}%)")
    linhas.append(f"Pendentes: {m['tarefas_pendentes']}")
    linhas.append(f"Atrasadas: {m['tarefas_atrasadas']}")
    linhas.append(f"Pontualidade: {m['taxa_pontualidade_percentual']:.2f}%")
    
    linhas.append("\n--- Detalhes por Categoria ---")
    for categoria, lista_tarefas in relatorio["prazos"].items():
        linhas.append(f"- {categoria}: {len(lista_tarefas)} tarefas")
        if not lista_tarefas:
            linhas.append("  (Nenhuma tarefa nesta categoria)")
        else:
            for t in lista_tarefas:
                data_str = formatar_data_para_string(t.data_limite)
                linhas.append(f"  - {t.titulo} (Vence: {data_str})")
    
    linhas.append("\nDiagnóstico:")
    linhas.append(relatorio["diagnostico"])
    
    return "\n".join(linhas)


def exibir_relatorio_tarefas(relatorio):
    """ Exibe o relatório e pergunta se deseja salvar. """

    texto_relatorio = formatar_relatorio_tarefas(relatorio)
    print(texto_relatorio)
    salvar = input("\nDeseja exportar este relatório? (s/n): ").lower()
    if salvar == "s":
        exportar_relatorio(texto_relatorio, "relatorio_tarefas.txt")

def formatar_relatorio_habitos(relatorio):
    """ Gera uma string formatada com os dados do relatório de hábitos. """

    if not relatorio:
        return "Nenhum dado de relatório disponível."
    
    m = relatorio["metricas"]
    linhas = []
    linhas.append("=== RELATÓRIO DE HABITOS ===\n")
    linhas.append(f"Total: {m['total_habitos']}")
    linhas.append(f"Em chamas: {m['habitos_em_chamas']} (Ativos)")
    linhas.append(f"Congelados: {m['habitos_congelados']} (Inativos)")
    linhas.append(f"Consistência Média: {m['consistencia_media']:.2f}%")
    
    linhas.append("\n--- Status dos Hábitos ---")
    for status, lista_dados in relatorio["detalhes"].items():
        if lista_dados:
            linhas.append(f"\n[{status.upper()}]")
            for d in lista_dados:
                linhas.append(f"  - {d['nome']}: {d['consistencia']:.2f}% consistência"
                              f"({d['execucoes_reais']}/{d['execucoes_esperadas']} execuções)")
    
    linhas.append("\nDiagnóstico:")
    linhas.append(relatorio["diagnostico"])
    
    return "\n".join(linhas)

def exibir_relatorio_habitos(relatorio):
    """" Exibe o relatório e pergunta se deseja salvar. """

    texto_relatorio = formatar_relatorio_habitos(relatorio)
    print(texto_relatorio)

    salvar = input("\nDeseja exportar este relatório? (s/n): ").lower()
    if salvar == "s":
        exportar_relatorio(texto_relatorio, "relatorio_habitos.txt")


def exibir_status_habitos(lista_habitos):
    """ Exibe uma lista com o status de cada hábito. """
    if not lista_habitos:
        print("Nenhum hábito cadastrado.")
        return

    print("\nStatus dos Hábitos:")
    for habito in lista_habitos:
        status, dias = verificar_status_habito(habito)
        print(f"[{status}] {habito.nome} - Dias sem fazer: {dias}")

def formatar_relatorio_projeto_individual(dados):
    """ Gera string formatada para o relatório de um único projeto. """
    p = dados["projeto"]
    m = dados["metricas"]
    tarefas = dados.get("tarefas", [])
    habitos = dados.get("habitos", [])
    
    linhas = []
    linhas.append(f"=== PROJETO: {p.nome.upper()} ===\n")
    linhas.append(f"Descrição: {p.descricao}")
    linhas.append(f"Progresso Geral: {dados['progresso_geral']:.1f}%")
    linhas.append(f"Diagnóstico: {dados['diagnostico']}")
    
    linhas.append("\n[Tarefas]")
    linhas.append(f"Total: {m['tarefas_total']}")
    if m['tarefas_total'] > 0:
        linhas.append(f"Conclusão: {m['tarefas_conclusao']:.1f}%")
        for t in tarefas:
            data_str = formatar_data_para_string(t.data_limite)
            linhas.append(f"  - {t.titulo} (Vence: {data_str})")
    
    linhas.append("\n[Hábitos]")
    linhas.append(f"Total: {m['habitos_total']}")
    if m['habitos_total'] > 0:
        linhas.append(f"Consistência Média: {m['habitos_consistencia']:.1f}%")
        for h in habitos:
            consistencia = calcular_consistencia_habito(h)
            esperadas = calcular_execucoes_esperadas(h)
            linhas.append(f"  - {h.nome}: {consistencia:.2f}% consistência({h.contador_execucoes}/{esperadas} execuções)")
        
    return "\n".join(linhas)

def exibir_relatorio_projeto(dados):
    """ Exibe o relatório individual e oferece exportação. """
    texto = formatar_relatorio_projeto_individual(dados)
    print("\n" + texto)
    
    salvar = input("\nDeseja exportar este relatório? (s/n): ").lower()
    if salvar == "s":
        nome_arq = f"relatorio_projeto_{dados['projeto'].id}.txt"
        exportar_relatorio(texto, nome_arq)

def formatar_relatorio_geral_projetos(relatorio):
    """ Gera string formatada para o desempenho sistêmico (todos os projetos). """
    if not relatorio:
        return "Nenhum projeto cadastrado."
        
    m = relatorio["metricas"]
    cats = relatorio["categorias"]
    
    linhas = []
    linhas.append("=== DESEMPENHO SISTÊMICO (PROJETOS) ===\n")
    linhas.append(f"Total de Projetos: {m['total_projetos']}")
    linhas.append(f"Média Global de Progresso: {m['media_global']:.1f}%\n")
    
    linhas.append("--- Detalhamento por Categoria ---")
    
    ordem = ["Excelente", "Bom", "Regular", "Crítico", "Vazio"]
    for categoria in ordem:
        lista = cats.get(categoria, [])
        if lista:
            linhas.append(f"\n[{categoria.upper()}]")
            for item in lista:
                p = item["projeto"]
                prog = item["progresso_geral"]
                linhas.append(f"  - {p.nome}: {prog:.1f}%")
    
    linhas.append("\n=== DIAGNÓSTICO GERAL ===")
    linhas.append(relatorio["diagnostico_geral"])
    
    return "\n".join(linhas)

def exibir_relatorio_geral_projetos(relatorio):
    """ Exibe o relatório geral e oferece exportação. """
    texto = formatar_relatorio_geral_projetos(relatorio)
    print("\n" + texto)
    
    salvar = input("\nDeseja exportar este relatório? (s/n): ").lower()
    if salvar == "s":
        exportar_relatorio(texto, "desempenho_projetos.txt")
