""" Estrutura de dados das tarefas e hábitos. """

from src.utils import formatar_data_para_string, formatar_data
from datetime import date


class Tarefa:
    """ Constrói uma tarefa com título, descrição, data limite e status de conclusão. """

    def __init__(self, tarefa_id, titulo, descricao, data_limite, concluida=False, data_criacao=None, data_conclusao=None):
        """ Inicializa uma nova tarefa. """
        self.id = tarefa_id
        self.titulo = titulo
        self.descricao = descricao
        self.data_limite = data_limite
        self.concluida = concluida
        self.data_criacao = data_criacao
        self.data_conclusao = data_conclusao

    @classmethod
    def from_csv(cls, linha):
        """ Cria uma instância de Tarefa a partir de uma linha CSV. """

        partes = linha.strip().split(",")
        tarefa_id = int(partes[0])

        titulo = partes[1]
        descricao = partes[2]
        data_limite = formatar_data(partes[3])
        status_conclusao = partes[4] == "1"

        # Protege contra IndexError
        if len(partes) > 5 and partes[5]:
            data_criacao = formatar_data(partes[5])
        else:
            data_criacao = date.today()
        if len(partes) > 6 and partes[6]:
            data_conclusao = formatar_data(partes[6])
        else:
            data_conclusao = None

        return cls(tarefa_id, titulo, descricao, data_limite, status_conclusao, data_criacao, data_conclusao)

    def __eq__(self, outro):
        if isinstance(outro, Tarefa):
            return self.id == outro.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        status = "[X]" if self.concluida else "[ ]"
        data_formatada = formatar_data_para_string(self.data_limite)
        return f"{self.id} - {status} {self.titulo} (Prazo: {data_formatada})"

    def __repr__(self):
        return f"Tarefa(id={self.id}, titulo={self.titulo}, descricao={self.descricao}, data_limite={self.data_limite}, concluida={self.concluida}, data_criacao={self.data_criacao}, data_conclusao={self.data_conclusao})"


class Habito:
    """ Constrói um hábito com nome, frequência e contador de execuções. """

    def __init__(self, habito_id, nome, frequencia, contador_execucoes, data_criacao=None, data_ultima_execucao=None):
        """ Inicializa um novo hábito. """
        self.id = habito_id
        self.nome = nome
        self.frequencia = frequencia
        self.contador_execucoes = contador_execucoes
        self.data_criacao = data_criacao
        self.data_ultima_execucao = data_ultima_execucao

    @classmethod
    def from_csv(cls, linha):
        """ Cria uma instância de Habito a partir de uma linha CSV. """

        partes = linha.strip().split(",")
        habito_id = int(partes[0])

        nome = partes[1]
        frequencia = partes[2]
        contador_execucoes = int(partes[3])

        # Protege contra IndexError
        if len(partes) > 4 and partes[4]:
            data_criacao = formatar_data(partes[4])
        else:
            data_criacao = date.today()
        if len(partes) > 5 and partes[5]:
            data_ultima_execucao = formatar_data(partes[5])
        else:
            data_ultima_execucao = None

        return cls(habito_id, nome, frequencia, contador_execucoes, data_criacao, data_ultima_execucao)

    def __eq__(self, outro):
        if isinstance(outro, Habito):
            return self.id == outro.id
        return False

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.id} - {self.nome} (Frequência: {self.frequencia}, Execuções: {self.contador_execucoes})"

    def __repr__(self):
        return f"Habito(id={self.id}, nome={self.nome}, frequencia={self.frequencia}, contador_execucoes={self.contador_execucoes}, data_criacao={self.data_criacao}, data_ultima_execucao={self.data_ultima_execucao})"
