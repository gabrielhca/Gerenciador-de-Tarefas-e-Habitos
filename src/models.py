""" Estrutura de dados das tarefas e hábitos. """

from src.utils import formatar_data_para_string


class Tarefa:
    """ Constrói uma tarefa com título, descrição, data limite e status de conclusão. """

    def __init__(self, tarefa_id, titulo, descricao, data_limite, concluida=False):
        """ Inicializa uma nova tarefa. """
        self.id = tarefa_id
        self.titulo = titulo
        self.descricao = descricao
        self.data_limite = data_limite
        self.concluida = concluida

    def __str__(self):
        status = "[X]" if self.concluida else "[ ]"
        data_formatada = formatar_data_para_string(self.data_limite)
        return f"{self.id} - {status} {self.titulo} (Prazo: {data_formatada})"

    def __repr__(self):
        return f"Tarefa(id={self.id}, titulo={self.titulo}, descricao={self.descricao}, data_limite={self.data_limite}, concluida={self.concluida})"


class Habito:
    """ Constrói um hábito com nome, frequência e contador de execuções. """

    def __init__(self, habito_id, nome, frequencia, contador_execucoes):
        """ Inicializa um novo hábito. """
        self.id = habito_id
        self.nome = nome
        self.frequencia = frequencia
        self.contador_execucoes = contador_execucoes

    def __str__(self):
        return f"{self.id} - {self.nome} (Frequência: {self.frequencia}, Execuções: {self.contador_execucoes})"

    def __repr__(self):
        return f"Habito(id={self.id}, nome={self.nome}, frequencia={self.frequencia}, contador_execucoes={self.contador_execucoes})"
