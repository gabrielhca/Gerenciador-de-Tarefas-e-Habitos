""" main """


def menu_tarefas():
    """Exibe o sub-menu de tarefas e trata as opções."""
    print("\n-- Gerenciar Tarefas --")
    print("1. Cadastrar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        # cadastrar_tarefa()
        print(">> Iniciando cadastro de tarefa...")
    elif opcao == '2':
        # listar_tarefas()
        print(">> Listando tarefas...")
    elif opcao == '3':
        # marcar_tarefa_concluida()
        print(">> Concluindo tarefa...")
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")


def menu_habitos():
    """Exibe o sub-menu de hábitos e trata as opções."""
    print("\n-- Gerenciar Hábitos --")
    print("1. Cadastrar Hábito")
    print("2. Listar Hábitos")
    print("3. Registrar Execução de Hábito")
    print("4. Voltar")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        # cadastrar_habito()
        print(">> Iniciando cadastro de hábito...")
    elif opcao == '2':
        # listar_habitos()
        print(">> Listando hábitos...")
    elif opcao == '3':
        # registrar_execucao_habito()
        print(">> Registrando execução...")
    elif opcao == '4':
        return
    else:
        print("Opção inválida.")


def main():
    """Função principal que inicia o programa."""
    print("Bem vindo ao Gerenciador de Tarefas e Hábitos!")

    while True:
        print("\n== Menu Principal ==")
        print("1. Gerenciar Tarefas")
        print("2. Gerenciar Hábitos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_tarefas()
        elif escolha == '2':
            menu_habitos()
        elif escolha == '3':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
