""" Módulo responsável pela persistência de dados (repositórios) de projetos. """

from pathlib import Path
from src.models import Projeto


class RepositorioProjetos:
    """ Gerencia a persistência e recuperação de projetos no arquivo CSV. """

    ARQUIVO_CSV = "data/projetos.csv"

    def __init__(self):
        """ Inicializa o repositório, carregando os projetos existentes. """
        self.lista_projetos = []
        self.ultimo_id = 0
        self.carrega_dados_csv()

    def arquivo_existe(self):
        """ Verifica se o arquivo CSV existe; se não, cria com o cabeçalho. """
        arquivo_existe = Path(self.ARQUIVO_CSV).exists()
        with open(self.ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
            if not arquivo_existe:
                arquivo.write("id;nome;descricao\n")

    def carrega_dados_csv(self):
        """ Lê os dados do arquivo CSV e popula a lista de projetos. """
        try:
            with open(self.ARQUIVO_CSV, mode="r", encoding='utf-8') as arquivo:
                next(arquivo)
                for linha in arquivo:
                    if not linha.strip():
                        continue
                    novo_projeto = Projeto.from_csv(linha)
                    if self.ultimo_id < novo_projeto.id:
                        self.ultimo_id = novo_projeto.id
                    self.lista_projetos.append(novo_projeto)
        except FileNotFoundError:
            self.arquivo_existe()

    def salvar_dados_csv(self, nome, descricao):
        """ Adiciona um novo projeto ao arquivo CSV. """
        self.arquivo_existe()

        with open(self.ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
            self.ultimo_id += 1
            arquivo.write(f"{self.ultimo_id};{nome};{descricao}\n")
            novo_projeto = Projeto(self.ultimo_id, nome, descricao)
            self.lista_projetos.append(novo_projeto)
            return novo_projeto

    def salvar_arquivo_completo(self):
        """ Reescreve o CSV inteiro para manter a integridade após edições ou exclusões. """
        with open(self.ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
            arquivo.write("id;nome;descricao\n")
            for proj in self.lista_projetos:
                arquivo.write(f"{proj.id};{proj.nome};{proj.descricao}\n")

    def editar_projeto(self, projeto_id, nome=None, descricao=None):
        """ Edita os dados de um projeto existente. """
        for proj in self.lista_projetos:
            if proj.id == projeto_id:
                if nome:
                    proj.nome = nome
                if descricao:
                    proj.descricao = descricao
                self.salvar_arquivo_completo()
                return proj
        return None

    def excluir_projeto(self, projeto_id):
        """ Remove um projeto da lista e do arquivo. """
        for proj in self.lista_projetos:
            if proj.id == projeto_id:
                self.lista_projetos.remove(proj)
                self.salvar_arquivo_completo()
                return proj
        return None

    def buscar_por_texto(self, termo):
        """ Filtra projetos por nome ou descrição. """
        termo = termo.lower()
        return [p for p in self.lista_projetos if termo in p.nome.lower() or termo in p.descricao.lower()]
