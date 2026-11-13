# Gerenciador de Tarefas, Hábitos e Projetos

Programa de terminal em Python para organizar tarefas, hábitos e projetos, com relatórios de progresso salvos em arquivos CSV.

**Versão web para testar no navegador:** https://gabrielhca.github.io/Gerenciador-de-Tarefas-e-Habitos/

## Como rodar

Pré-requisito: Python 3.10 ou mais recente. O programa só usa a biblioteca padrão.

```bash
git clone https://github.com/gabrielhca/Gerenciador-de-Tarefas-e-Habitos.git
cd Gerenciador-de-Tarefas-e-Habitos
python3 main.py
```

O repositório já vem com dados de exemplo em `data/`. Se essa pasta não existir, o programa cria a pasta e os arquivos `.csv` na primeira execução. Os relatórios exportados vão para `relatorios/`.

### Testes e lint

Para os testes e o lint é preciso o [uv](https://docs.astral.sh/uv/):

```bash
uv sync               # instala pytest e Ruff
uv run pytest         # roda os testes
uv run ruff check .   # verifica o código
```

## Funcionalidades

- **Projetos:** agrupam tarefas e hábitos de uma mesma área (ex.: "Faculdade", "Vida Saudável"). O relatório de cada projeto junta a conclusão das tarefas com a consistência dos hábitos e classifica o projeto como Excelente, Bom, Regular ou Crítico.
- **Tarefas:** cadastro, edição, conclusão e exclusão. As pendentes são separadas em atrasadas, urgentes, próximas e futuras, e o relatório mostra a taxa de conclusão e a pontualidade.
- **Hábitos:** diários ou semanais, com contador de execuções. O status muda conforme a última execução ("Em chamas", "Em dia", "Atenção", "Congelado").
- **Relatórios:** podem ser exportados em `.txt`.

## Estrutura

```plaintext
├── data/                     # CSVs com os dados (projetos, tarefas, hábitos)
├── docs/                     # MVP web publicado no GitHub Pages
├── src/
│   ├── models.py             # Classes Projeto, Tarefa e Habito
│   ├── repositorio_*.py      # Leitura e gravação de cada CSV
│   ├── relatorio_*.py        # Cálculos dos relatórios
│   ├── views.py              # Entradas e saídas no terminal
│   └── utils.py              # Datas, caminhos e exportação
├── tests/                    # Testes com pytest
└── main.py                   # Menus e fluxo principal
```

## Tecnologias

- Python 3 (biblioteca padrão: `datetime`, `pathlib`)
- Arquivos CSV como armazenamento
- pytest para testes e Ruff para lint e formatação, gerenciados com uv
- HTML, CSS e JavaScript puro no MVP web

## O que aprendi

Esse foi o projeto em que eu realmente usei orientação a objetos. Cada entidade virou uma classe, e usei `@property` para validar os dados na hora de criar o objeto: uma tarefa sem título, por exemplo, nem chega a existir. Também usei `@classmethod` para montar o objeto direto de uma linha do CSV, o que deixou a leitura dos arquivos bem mais limpa.

Separar o código em camadas me ajudou muito. Os repositórios só leem e gravam arquivos, os relatórios só fazem contas e a `views.py` só conversa com o usuário. Quando precisei mudar um cálculo, mexi em um lugar só, e deu para testar os relatórios sem abrir o menu.

Usar CSV como "banco de dados" me ensinou na prática por que bancos existem. Troquei o separador de `,` para `;` porque as descrições tinham vírgula, tive que tratar linha vazia e data em formato errado, e percebi que excluir um projeto deixava tarefas apontando para um ID que não existia mais. São problemas pequenos, mas me mostraram o que é integridade de dados.

Também aprendi a ter cuidado com coisas que parecem detalhe: datas (`datetime` e formatos), caminhos de arquivo (troquei `os.path` por `pathlib` e passei a montar os caminhos a partir da pasta do projeto) e entrada do usuário, como alguém digitar "diária" com acento quando o código esperava "diario".

Por fim, fiz uma versão web simples em JavaScript para quem quiser ver o sistema sem instalar Python. Precisei reescrever as mesmas regras em outra linguagem, e isso me fez entender melhor a lógica que eu tinha criado.

## Estado atual

Concluído. O programa de terminal e o MVP web estão funcionando.
