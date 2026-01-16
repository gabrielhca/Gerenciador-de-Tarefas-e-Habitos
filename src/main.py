""" Módulo principal da aplicação. """

from src.repositories import RepositorioTarefas, RepositorioHabitos
from src.views import exibir_dados, preencher_dados_tarefa, preencher_dados_habito, solicitar_id


def menu_tarefas(repositorio):
    """Exibe o sub-menu de tarefas e trata as opções."""
    print("\n-- Gerenciar Tarefas --")
    print("1. Cadastrar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dados = preencher_dados_tarefa()
        repositorio.salvar_dados_csv(dados[0], dados[1], dados[2], dados[3])
    elif opcao == '2':
        exibir_dados(repositorio.lista_tarefas, "tarefas")
    elif opcao == '3':
        id_tarefa = solicitar_id(repositorio.lista_tarefas, "tarefas")
        if id_tarefa:
            tarefa_alterada = repositorio.marcar_tarefa_concluida(id_tarefa.id)
            print(f"Tarefa '{tarefa_alterada.titulo}' marcada como concluída!")
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")


def menu_habitos(repositorio):
    """Exibe o sub-menu de hábitos e trata as opções."""
    print("\n-- Gerenciar Hábitos --")
    print("1. Cadastrar Hábito")
    print("2. Listar Hábitos")
    print("3. Registrar Execução de Hábito")
    print("4. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dados = preencher_dados_habito()
        repositorio.salvar_dados_csv(dados[0], dados[1], dados[2])
    elif opcao == '2':
        exibir_dados(repositorio.lista_habitos, "hábitos")
    elif opcao == '3':
        id_habito = solicitar_id(repositorio.lista_habitos, "hábitos")
        if id_habito:
            habito_alterado = repositorio.registrar_execucao_habito(
                id_habito.id)
            print(
                f"Hábito '{habito_alterado[0]}' executado! Total de execuções: {habito_alterado[1]}")
    elif opcao == '4':
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
