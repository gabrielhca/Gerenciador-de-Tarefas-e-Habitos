""" Módulo responsável pela persistência de dados (repositórios) de hábitos. """

import os
from src.models import Habito


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
        arquivo_existe = os.path.exists(self.ARQUIVO_CSV)
        with open(self.ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
            if not arquivo_existe:
                arquivo.write("id,nome,frequencia,contador_execucoes\n")

    def carrega_dados_csv(self):
        """ Lê os dados do arquivo CSV e popula a lista de hábitos. """

        try:
            with open(self.ARQUIVO_CSV, mode="r", encoding='utf-8') as arquivo:
                next(arquivo)
                for linha in arquivo:
                    partes = linha.strip().split(",")
                    habito_id = int(partes[0])
                    if self.ultimo_id < habito_id:
                        self.ultimo_id = habito_id
                    nome = partes[1]
                    frequencia = partes[2]
                    contador_execucoes = int(partes[3])

                    nova_habito = Habito(
                        habito_id, nome, frequencia, contador_execucoes)
                    self.lista_habitos.append(nova_habito)
        except FileNotFoundError:
            self.arquivo_existe()

    def salvar_dados_csv(self, nome, frequencia, contador_execucoes):
        """ Adiciona um novo hábito ao arquivo CSV. """
        self.arquivo_existe()
        with open(self.ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
            self.ultimo_id += 1
            arquivo.write(
                f"{self.ultimo_id},{nome},{frequencia},{contador_execucoes}\n")
            novo_habito = Habito(self.ultimo_id, nome,
                                 frequencia, contador_execucoes)
            self.lista_habitos.append(novo_habito)

    def salvar_arquivo_completo(self):
        """ Reescreve o CSV inteiro com o estado atual dos hábitos, garantindo a integridade dos dados. """
        with open(self.ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
            arquivo.write("id,nome,frequencia,contador_execucoes\n")
            for habito in self.lista_habitos:
                arquivo.write(
                    f"{habito.id},{habito.nome},{habito.frequencia},{habito.contador_execucoes}\n")

    def registrar_execucao_habito(self, habito_id):
        """ Registra a execução de um hábito, incrementando seu contador."""
        for habito in self.lista_habitos:
            if habito.id == habito_id:
                habito.contador_execucoes += 1
                self.salvar_arquivo_completo()
                return habito.nome, habito.contador_execucoes
