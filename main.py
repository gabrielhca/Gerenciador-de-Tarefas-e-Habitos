""" Módulo principal da aplicação. """

from src.repositorio_projetos import RepositorioProjetos
from src.repositorio_tarefas import RepositorioTarefas
from src.repositorio_habitos import RepositorioHabitos
from src.views import (
    exibir_dados,
    preencher_dados_tarefa,
    preencher_dados_habito,
    preencher_dados_projeto,
    editar_dados_tarefa,
    editar_dados_habito,
    editar_dados_projeto,
    solicitar_termo_busca,
    solicitar_id,
    exibir_relatorio_tarefas,
    exibir_relatorio_habitos,
    exibir_status_habitos,
    exibir_relatorio_projeto,
    exibir_relatorio_geral_projetos
)
from src.relatorio_projetos import (
    gerar_dados_projeto,
    gerar_desempenho_geral_projetos
)
from src.relatorio_tarefas import (
    gerar_desempenho_tarefas,
    filtrar_tarefas_pendentes,
    filtrar_tarefas_concluidas,
    filtrar_tarefas_atrasadas
)
from src.relatorio_habitos import gerar_desempenho_habitos


def gerenciar_tarefas(repositorio, repo_projetos):
    """Exibe o sub-menu de gerenciamento de tarefas."""

    print("\n-- Gerenciar Tarefas --")
    print("1. Cadastrar Tarefa")
    print("2. Editar Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Excluir Tarefa")
    print("5. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dados = preencher_dados_tarefa(repo_projetos)
        repositorio.salvar_dados_csv(dados[0], dados[1], dados[2], dados[3])
    elif opcao == '2':
        termo = solicitar_termo_busca()
        if termo == '0':
            return
        resultados = repositorio.buscar_por_texto(termo)
        exibir_dados(resultados, "tarefas")
        tarefa_selecionada = solicitar_id(resultados)
        if tarefa_selecionada:
            novos_dados = editar_dados_tarefa(tarefa_selecionada)
            repositorio.editar_tarefa(
                tarefa_selecionada.id, novos_dados[0], novos_dados[1], novos_dados[2])
            print("Tarefa atualizada!")
    elif opcao == '3':
        termo = solicitar_termo_busca()
        if termo == '0':
            return
        resultados = repositorio.buscar_por_texto(termo)
        exibir_dados(resultados, "tarefas")
        tarefa_selecionada = solicitar_id(resultados)
        if tarefa_selecionada:
            tarefa_alterada = repositorio.marcar_tarefa_concluida(tarefa_selecionada.id)
            print(f"Tarefa '{tarefa_alterada.titulo}' marcada como concluída!")
    elif opcao == '4':
        termo = solicitar_termo_busca()
        if termo == '0':
            return
        resultados = repositorio.buscar_por_texto(termo)
        exibir_dados(resultados, "tarefas")
        tarefa_selecionada = solicitar_id(resultados)
        if tarefa_selecionada:
            tarefa_removida = repositorio.excluir_tarefa(tarefa_selecionada.id)
            print(f"Tarefa '{tarefa_removida.titulo}' excluída!")
    elif opcao == '5':
        return
    else:
        print("Opção inválida.")


def relatorios_tarefas(repositorio):
    """Exibe o sub-menu de relatórios de tarefas."""

    print("\n-- Relatórios de Tarefas --")
    print("1. Listar Todas as Tarefas")
    print("2. Listar Pendentes")
    print("3. Listar Atrasadas")
    print("4. Listar Concluídas")
    print("5. Relatório de Desempenho")
    print("6. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        exibir_dados(repositorio.lista_tarefas, "tarefas")
    elif opcao == '2':
        exibir_dados(filtrar_tarefas_pendentes(
            repositorio.lista_tarefas), "Tarefas Pendentes")
    elif opcao == '3':
        exibir_dados(filtrar_tarefas_atrasadas(
            repositorio.lista_tarefas), "Tarefas Atrasadas")
    elif opcao == '4':
        exibir_dados(filtrar_tarefas_concluidas(
            repositorio.lista_tarefas), "Tarefas Concluídas")
    elif opcao == '5':
        relatorio = gerar_desempenho_tarefas(repositorio.lista_tarefas)
        exibir_relatorio_tarefas(relatorio)
    elif opcao == '6':
        return
    else:
        print("Opção inválida.")


def gerenciar_habitos(repositorio, repo_projetos):
    """Exibe o sub-menu de gerenciamento de hábitos."""

    print("\n-- Gerenciar Hábitos --")
    print("1. Cadastrar Hábito")
    print("2. Editar Hábito")
    print("3. Registrar Execução de Hábito")
    print("4. Excluir Hábito")
    print("5. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dados = preencher_dados_habito(repo_projetos)
        repositorio.salvar_dados_csv(dados[0], dados[1], dados[2], dados[3], dados[4])
    elif opcao == '2':
        termo = solicitar_termo_busca()
        if termo == '0':
            return
        resultados = repositorio.buscar_por_texto(termo)
        exibir_dados(resultados, "hábitos")
        habito_selecionado = solicitar_id(resultados)
        if habito_selecionado:
            novos_dados = editar_dados_habito(habito_selecionado)
            repositorio.editar_habito(
                habito_selecionado.id, novos_dados[0], novos_dados[1])
            print("Hábito atualizado!")
    elif opcao == '3':
        termo = solicitar_termo_busca()
        if termo == '0':
            return
        resultados = repositorio.buscar_por_texto(termo)
        exibir_dados(resultados, "hábitos")
        habito_selecionado = solicitar_id(resultados)
        if habito_selecionado:
            habito_alterado = repositorio.registrar_execucao_habito(
                habito_selecionado.id)
            print(
                f"Hábito '{habito_alterado[0]}' executado! Total de execuções: {habito_alterado[1]}")
    elif opcao == '4':
        termo = solicitar_termo_busca()
        if termo == '0':
            return
        resultados = repositorio.buscar_por_texto(termo)
        exibir_dados(resultados, "hábitos")
        habito_selecionado = solicitar_id(resultados)
        if habito_selecionado:
            habito_removido = repositorio.excluir_habito(habito_selecionado.id)
            print(f"Hábito '{habito_removido.nome}' excluído!")
    elif opcao == '5':
        return
    else:
        print("Opção inválida.")


def relatorios_habitos(repositorio):
    """Exibe o sub-menu de relatórios de hábitos."""

    print("\n-- Relatórios de Hábitos --")
    print("1. Listar Hábitos")
    print("2. Status dos Hábitos")
    print("3. Relatório de Desempenho")
    print("4. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        exibir_dados(repositorio.lista_habitos, "hábitos")
    elif opcao == '2':
        exibir_status_habitos(repositorio.lista_habitos)
    elif opcao == '3':
        relatorio = gerar_desempenho_habitos(repositorio.lista_habitos)
        exibir_relatorio_habitos(relatorio)
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")

def gerenciar_projetos(repo_p):
    """ CRUD de Projetos: Focado apenas na gestão dos dados. """
    print("\n-- Gerenciar Projetos --")
    print("1. Cadastrar Projeto")
    print("2. Editar Projeto")
    print("3. Excluir Projeto")
    print("4. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome, desc = preencher_dados_projeto()
        repo_p.salvar_dados_csv(nome, desc)
        print(f"Projeto '{nome}' criado com sucesso!")
        
    elif opcao == '2':
        termo = solicitar_termo_busca()
        if termo == '0': return
        resultados = repo_p.buscar_por_texto(termo)
        exibir_dados(resultados, "projetos")
        selecionado = solicitar_id(resultados)
        if selecionado:
            novo_nome, nova_desc = editar_dados_projeto(selecionado)
            repo_p.editar_projeto(selecionado.id, novo_nome, nova_desc)
            print("Projeto atualizado.")

    elif opcao == '3':
        termo = solicitar_termo_busca()
        if termo == '0': return
        resultados = repo_p.buscar_por_texto(termo)
        exibir_dados(resultados, "projetos")
        selecionado = solicitar_id(resultados)
        if selecionado:
            repo_p.excluir_projeto(selecionado.id)
            print("Projeto removido.")
            
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")


def relatorios_projetos(repo_p, repo_t, repo_h):
    """ Relatórios de Projetos: Focado em análise e visualização. """
    print("\n-- Relatórios de Projetos --")
    print("1. Listar Projetos")
    print("2. Relatório Individual")
    print("3. Desempenho Geral")
    print("4. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        exibir_dados(repo_p.lista_projetos, "projetos")
        
    elif opcao == '2':
        exibir_dados(repo_p.lista_projetos, "projetos")
        selecionado = solicitar_id(repo_p.lista_projetos)
        if selecionado:
            dados = gerar_dados_projeto(selecionado, repo_t.lista_tarefas, repo_h.lista_habitos)
            exibir_relatorio_projeto(dados)
            
    elif opcao == '3':
        relatorio = gerar_desempenho_geral_projetos(repo_p.lista_projetos, repo_t.lista_tarefas, repo_h.lista_habitos)
        exibir_relatorio_geral_projetos(relatorio)
        
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")

def main():
    """ Função principal orquestradora. """
    repo_tarefas = RepositorioTarefas()
    repo_habitos = RepositorioHabitos()
    repo_projetos = RepositorioProjetos()

    print("Bem vindo ao Gerenciador de Sistemas Pessoais!")

    while True:
        print("\n== Menu Principal ==")
        print("1. Gerenciar Projetos")
        print("2. Relatórios de Projetos")
        print("3. Gerenciar Tarefas")
        print("4. Relatórios de Tarefas")
        print("5. Gerenciar Hábitos")
        print("6. Relatórios de Hábitos")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            gerenciar_projetos(repo_projetos)
        elif escolha == '2':
            relatorios_projetos(repo_projetos, repo_tarefas, repo_habitos)
        elif escolha == '3':
            gerenciar_tarefas(repo_tarefas, repo_projetos)
        elif escolha == '4':
            relatorios_tarefas(repo_tarefas)
        elif escolha == '5':
            gerenciar_habitos(repo_habitos, repo_projetos)
        elif escolha == '6':
            relatorios_habitos(repo_habitos)
        elif escolha == '7':
            print("Sistema encerrado. Mantenha o foco!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
