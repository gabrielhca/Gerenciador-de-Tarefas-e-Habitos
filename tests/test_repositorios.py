import pytest

from src.repositorio_habitos import RepositorioHabitos
from src.repositorio_projetos import RepositorioProjetos
from src.repositorio_tarefas import RepositorioTarefas


@pytest.fixture
def pasta_dados(tmp_path, monkeypatch):
    """Faz os repositórios usarem uma pasta temporária em vez de data/."""
    pasta = tmp_path / "data"
    monkeypatch.setattr(RepositorioTarefas, "ARQUIVO_CSV", pasta / "tarefas.csv")
    monkeypatch.setattr(RepositorioHabitos, "ARQUIVO_CSV", pasta / "habitos.csv")
    monkeypatch.setattr(RepositorioProjetos, "ARQUIVO_CSV", pasta / "projetos.csv")
    return pasta


def test_cria_pasta_e_arquivo_quando_nao_existem(pasta_dados):
    RepositorioTarefas()
    assert (pasta_dados / "tarefas.csv").exists()


def test_tarefa_salva_e_recarregada(pasta_dados):
    repo = RepositorioTarefas()
    repo.salvar_dados_csv("Estudar", "Capítulo 1", "20-02-2026")

    recarregado = RepositorioTarefas()

    assert len(recarregado.lista_tarefas) == 1
    assert recarregado.lista_tarefas[0].titulo == "Estudar"
    assert recarregado.ultimo_id == 1


def test_titulo_vazio_nao_e_gravado_no_csv(pasta_dados):
    repo = RepositorioTarefas()
    with pytest.raises(ValueError):
        repo.salvar_dados_csv("", "desc", "20-02-2026")

    # O app precisa continuar abrindo depois do erro
    assert RepositorioTarefas().lista_tarefas == []


def test_registrar_execucao_de_habito(pasta_dados):
    repo = RepositorioHabitos()
    repo.salvar_dados_csv("Ler", "diario", 0)

    nome, total = repo.registrar_execucao_habito(1)

    assert (nome, total) == ("Ler", 1)
    assert RepositorioHabitos().lista_habitos[0].contador_execucoes == 1


def test_excluir_projeto_e_desvincular_itens(pasta_dados):
    repo_p = RepositorioProjetos()
    repo_t = RepositorioTarefas()
    repo_h = RepositorioHabitos()
    projeto = repo_p.salvar_dados_csv("Faculdade", "")
    repo_t.salvar_dados_csv("Prova", "", "20-02-2026", projeto.id)
    repo_h.salvar_dados_csv("Estudar", "diario", 0, projeto_id=projeto.id)

    repo_p.excluir_projeto(projeto.id)

    assert repo_t.desvincular_projeto(projeto.id) == 1
    assert repo_h.desvincular_projeto(projeto.id) == 1
    assert RepositorioTarefas().lista_tarefas[0].projeto_id is None
    assert RepositorioHabitos().lista_habitos[0].projeto_id is None
