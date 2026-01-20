""" Módulo responsável pela persistência de dados (repositórios) de tarefas. """

import os
from datetime import date
from src.models import Tarefa
from src.utils import formatar_data, formatar_data_para_string


class RepositorioTarefas():
    """ Gerencia a persistência e recuperação de tarefas no arquivo CSV. """

    ARQUIVO_CSV = "data/tarefas.csv"

    def __init__(self):
        """ Inicializa o repositório, carregando os dados existentes. """
        self.lista_tarefas = []
        self.ultimo_id = 0
        self.carrega_dados_csv()

    def arquivo_existe(self):
        """ Verifica se o arquivo CSV existe; se não, cria com o cabeçalho. """
        arquivo_existe = os.path.exists(self.ARQUIVO_CSV)
        with open(self.ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
            if not arquivo_existe:
                arquivo.write(
                    "id,titulo,descricao,data_limite,concluida,data_criacao,data_conclusao\n")

    def carrega_dados_csv(self):
        """ Lê os dados do arquivo CSV e popula a lista de tarefas. """

        try:
            with open(self.ARQUIVO_CSV, mode="r", encoding='utf-8') as arquivo:
                next(arquivo)
                for linha in arquivo:
                    partes = linha.strip().split(",")
                    tarefa_id = int(partes[0])
                    if self.ultimo_id < tarefa_id:
                        self.ultimo_id = tarefa_id
                    titulo = partes[1]
                    descricao = partes[2]
                    data_limite = formatar_data(partes[3])
                    status_conclusao = partes[4].lower()

                    # Protege contra IndexError
                    if len(partes) > 5 and partes[5]:
                        data_criacao = formatar_data(partes[5])
                    else:
                        data_criacao = date.today()
                    if len(partes) > 6 and partes[6]:
                        data_conclusao = formatar_data(partes[6])
                    else:
                        data_conclusao = None

                    nova_tarefa = Tarefa(
                        tarefa_id, titulo, descricao, data_limite, status_conclusao == "true", data_criacao, data_conclusao)
                    self.lista_tarefas.append(nova_tarefa)
        except FileNotFoundError:
            self.arquivo_existe()

    def salvar_dados_csv(self, titulo, descricao, data_limite_str):
        """ Adiciona uma nova tarefa ao arquivo CSV. """
        self.arquivo_existe()
        concluida = False

        data_criacao = date.today()
        data_criacao_str = formatar_data_para_string(data_criacao)
        data_conclusao = None
        data_conclusao_str = ""

        data_limite = formatar_data(data_limite_str)

        with open(self.ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
            self.ultimo_id += 1
            arquivo.write(
                f"{self.ultimo_id},{titulo},{descricao},{data_limite_str},{concluida},{data_criacao_str},{data_conclusao_str}\n")
            nova_tarefa = Tarefa(
                self.ultimo_id,
                titulo,
                descricao,
                data_limite,
                concluida,
                data_criacao,
                data_conclusao
            )
            self.lista_tarefas.append(nova_tarefa)

    def salvar_arquivo_completo(self):
        """ Reescreve o CSV inteiro com o estado atual das tarefas, garantindo a integridade dos dados. """
        with open(self.ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
            arquivo.write(
                "id,titulo,descricao,data_limite,concluida,data_criacao,data_conclusao\n")
            for tarefa in self.lista_tarefas:

                data_limite_str = formatar_data_para_string(tarefa.data_limite)
                data_criacao_str = formatar_data_para_string(
                    tarefa.data_criacao)
                data_conclusao_str = formatar_data_para_string(
                    tarefa.data_conclusao) if tarefa.data_conclusao else ""
                arquivo.write(
                    f"{tarefa.id},{tarefa.titulo},{tarefa.descricao},{data_limite_str},{tarefa.concluida},{data_criacao_str},{data_conclusao_str}\n")

    def marcar_tarefa_concluida(self, tarefa_id):
        """ Marca uma tarefa como concluída. """
        for tarefa in self.lista_tarefas:
            if tarefa.id == tarefa_id:
                tarefa.concluida = True
                tarefa.data_conclusao = date.today()
                self.salvar_arquivo_completo()
                return tarefa

    def excluir_tarefa(self, tarefa_id):
        """ Excluir uma tarefa do repositório. """
        for tarefa in self.lista_tarefas:
            if tarefa.id == tarefa_id:
                self.lista_tarefas.remove(tarefa)
                self.salvar_arquivo_completo()
                return tarefa
