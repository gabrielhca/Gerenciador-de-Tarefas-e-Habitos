""" Estrutura de dados das tarefas e hábitos. """

from src.utils import formatar_data_para_string


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

    def __str__(self):
        return f"{self.id} - {self.nome} (Frequência: {self.frequencia}, Execuções: {self.contador_execucoes})"

    def __repr__(self):
        return f"Habito(id={self.id}, nome={self.nome}, frequencia={self.frequencia}, contador_execucoes={self.contador_execucoes}, data_criacao={self.data_criacao}, data_ultima_execucao={self.data_ultima_execucao})"
