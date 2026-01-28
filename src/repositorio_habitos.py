""" Módulo responsável pela persistência de dados (repositórios) de hábitos. """

from pathlib import Path
from datetime import date
from src.models import Habito
from src.utils import formatar_data_para_string


class RepositorioHabitos():
    """ Gerencia a persistência e recuperação de hábitos no arquivo CSV. """

    ARQUIVO_CSV = "data/habitos.csv"

    def __init__(self):
        """ Inicializa o repositório, carregando os dados existentes. """
        self.lista_habitos = []
        self.ultimo_id = 0
        self.carrega_dados_csv()

    def arquivo_existe(self):
        """ Verifica se o arquivo CSV existe; se não, cria com o cabeçalho. """
        arquivo_existe = Path(self.ARQUIVO_CSV).exists()
        with open(self.ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
            if not arquivo_existe:
                arquivo.write(
                    "id;nome;frequencia;contador_execucoes;data_criacao;data_ultima_execucao\n")

    def carrega_dados_csv(self):
        """ Lê os dados do arquivo CSV e popula a lista de hábitos. """
        try:
            with open(self.ARQUIVO_CSV, mode="r", encoding='utf-8') as arquivo:
                next(arquivo)
                for linha in arquivo:
                    if not linha.strip():
                        continue
                    novo_habito = Habito.from_csv(linha)
                    if self.ultimo_id < novo_habito.id:
                        self.ultimo_id = novo_habito.id
                    self.lista_habitos.append(novo_habito)
        except FileNotFoundError:
            self.arquivo_existe()

    def salvar_dados_csv(self, nome, frequencia, contador_execucoes):
        """ Adiciona um novo hábito ao arquivo CSV. """
        self.arquivo_existe()

        data_criacao = date.today()
        data_criacao_str = formatar_data_para_string(data_criacao)
        data_ultima_execucao = None
        data_ultima_execucao_str = ""

        with open(self.ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
            self.ultimo_id += 1
            arquivo.write(
                f"{self.ultimo_id};{nome};{frequencia};{contador_execucoes};{data_criacao_str};{data_ultima_execucao_str}\n")
            novo_habito = Habito(self.ultimo_id, nome,
                                 frequencia, contador_execucoes, data_criacao, data_ultima_execucao)
            self.lista_habitos.append(novo_habito)

    def salvar_arquivo_completo(self):
        """ Reescreve o CSV inteiro com o estado atual dos hábitos, garantindo a integridade dos dados. """
        with open(self.ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
            arquivo.write(
                "id;nome;frequencia;contador_execucoes;data_criacao;data_ultima_execucao\n")
            for habito in self.lista_habitos:
                data_criacao_str = formatar_data_para_string(
                    habito.data_criacao)
                data_ultima_execucao_str = formatar_data_para_string(
                    habito.data_ultima_execucao) if habito.data_ultima_execucao else ""

                arquivo.write(
                    f"{habito.id};{habito.nome};{habito.frequencia};{habito.contador_execucoes};{data_criacao_str};{data_ultima_execucao_str}\n")

    def registrar_execucao_habito(self, habito_id):
        """ Registra a execução de um hábito, incrementando seu contador."""
        for habito in self.lista_habitos:
            if habito.id == habito_id:
                habito.contador_execucoes += 1
                habito.data_ultima_execucao = date.today()
                self.salvar_arquivo_completo()
                return habito.nome, habito.contador_execucoes

    def excluir_habito(self, habito_id):
        """ Excluir um hábito do repositório. """
        for habito in self.lista_habitos:
            if habito.id == habito_id:
                self.lista_habitos.remove(habito)
                self.salvar_arquivo_completo()
                return habito

    def editar_habito(self, habito_id, nome=None, frequencia=None):
        """ Edita os dados de um hábito existente. """
        for habito in self.lista_habitos:
            if habito.id == habito_id:
                if nome:
                    habito.nome = nome
                if frequencia:
                    habito.frequencia = frequencia
                self.salvar_arquivo_completo()
                return habito

    def buscar_por_texto(self, termo):
        """ Filtra os habitos que contém o termo no nome. """
        termo = termo.lower()
        return [h for h in self.lista_habitos if termo in h.nome.lower()]