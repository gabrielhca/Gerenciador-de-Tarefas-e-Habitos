""" Módulo principal da aplicação. """

from src.repositorio_tarefas import RepositorioTarefas
from src.repositorio_habitos import RepositorioHabitos
from src.views import (
    exibir_dados,
    preencher_dados_tarefa,
    preencher_dados_habito,
    editar_dados_tarefa,
    editar_dados_habito,
    solicitar_id,
    exibir_relatorio_tarefas,
    exibir_relatorio_habitos,
    exibir_status_habitos
)
from src.relatorio_tarefas import (
    gerar_desempenho_tarefas,
    filtrar_tarefas_pendentes,
    filtrar_tarefas_concluidas,
    filtrar_tarefas_atrasadas
)
from src.relatorio_habitos import gerar_desempenho_habitos


def menu_tarefas(repositorio):
    """Exibe o sub-menu de tarefas e trata as opções."""

    print("\n-- Gerenciar Tarefas --")
    print("1. Cadastrar Tarefa")
    print("2. Editar Tarefa")
    print("3. Marcar Tarefa como Concluída")
    print("4. Excluir Tarefa")
    print("5. Listar Todas as Tarefas")
    print("6. Listar Pendentes")
    print("7. Listar Atrasadas")
    print("8. Listar Concluídas")
    print("9. Relatório de Desempenho")
    print("10. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dados = preencher_dados_tarefa()
        repositorio.salvar_dados_csv(dados[0], dados[1], dados[2])
    elif opcao == '2':
        id_tarefa = solicitar_id(repositorio.lista_tarefas, "tarefas")
        if id_tarefa:
            novos_dados = editar_dados_tarefa(id_tarefa)
            repositorio.editar_tarefa(
                id_tarefa.id, novos_dados[0], novos_dados[1], novos_dados[2])
            print("Tarefa atualizada!")
    elif opcao == '3':
        id_tarefa = solicitar_id(repositorio.lista_tarefas, "tarefas")
        if id_tarefa:
            tarefa_alterada = repositorio.marcar_tarefa_concluida(id_tarefa.id)
            print(f"Tarefa '{tarefa_alterada.titulo}' marcada como concluída!")
    elif opcao == '4':
        id_tarefa = solicitar_id(repositorio.lista_tarefas, "tarefas")
        if id_tarefa:
            tarefa_removida = repositorio.excluir_tarefa(id_tarefa.id)
            print(f"Tarefa '{tarefa_removida.titulo}' excluída!")
    elif opcao == '5':
        exibir_dados(repositorio.lista_tarefas, "tarefas")
    elif opcao == '6':
        exibir_dados(filtrar_tarefas_pendentes(
            repositorio.lista_tarefas), "Tarefas Pendentes")
    elif opcao == '7':
        exibir_dados(filtrar_tarefas_atrasadas(
            repositorio.lista_tarefas), "Tarefas Atrasadas")
    elif opcao == '8':
        exibir_dados(filtrar_tarefas_concluidas(
            repositorio.lista_tarefas), "Tarefas Concluídas")
    elif opcao == '9':
        relatorio = gerar_desempenho_tarefas(repositorio.lista_tarefas)
        exibir_relatorio_tarefas(relatorio)
    elif opcao == '10':
        return
    else:
        print("Opção inválida.")


def menu_habitos(repositorio):
    """Exibe o sub-menu de hábitos e trata as opções."""
    print("\n-- Gerenciar Hábitos --")
    print("1. Cadastrar Hábito")
    print("2. Editar Hábito")
    print("3. Registrar Execução de Hábito")
    print("4. Excluir Hábito")
    print("5. Listar Hábitos")
    print("6. Status dos Hábitos")
    print("7. Relatório de Desempenho")
    print("8. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dados = preencher_dados_habito()
        repositorio.salvar_dados_csv(dados[0], dados[1], dados[2])
    elif opcao == '2':
        id_habito = solicitar_id(repositorio.lista_habitos, "hábitos")
        if id_habito:
            novos_dados = editar_dados_habito(id_habito)
            repositorio.editar_habito(
                id_habito.id, novos_dados[0], novos_dados[1])
            print("Hábito atualizado!")
    elif opcao == '3':
        id_habito = solicitar_id(repositorio.lista_habitos, "hábitos")
        if id_habito:
            habito_alterado = repositorio.registrar_execucao_habito(
                id_habito.id)
            print(
                f"Hábito '{habito_alterado[0]}' executado! Total de execuções: {habito_alterado[1]}")
    elif opcao == '4':
        id_habito = solicitar_id(repositorio.lista_habitos, "hábitos")
        if id_habito:
            habito_removido = repositorio.excluir_habito(id_habito.id)
            print(f"Hábito '{habito_removido.nome}' excluído!")
    elif opcao == '5':
        exibir_dados(repositorio.lista_habitos, "hábitos")
    elif opcao == '6':
        exibir_status_habitos(repositorio.lista_habitos)
    elif opcao == '7':
        relatorio = gerar_desempenho_habitos(repositorio.lista_habitos)
        exibir_relatorio_habitos(relatorio)
    elif opcao == '8':
        return
    else:
        print("Opção inválida.")


def main():
    """Função principal que inicia o programa."""
    repo_tarefas = RepositorioTarefas()
    repo_habitos = RepositorioHabitos()
    print("Bem vindo ao Gerenciador de Tarefas e Hábitos!")

    while True:
        print("\n== Menu Principal ==")
        print("1. Gerenciar Tarefas")
        print("2. Gerenciar Hábitos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_tarefas(repo_tarefas)
        elif escolha == '2':
            menu_habitos(repo_habitos)
        elif escolha == '3':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
