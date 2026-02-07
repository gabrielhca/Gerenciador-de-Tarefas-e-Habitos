# Projeto D: Gerenciador de Tarefas, Hábitos e Projetos
> Projeto 1 desenvolvido durante as Semanas 4 e 5 do Onboarding LIPAI.

## Sobre o Projeto
Este repositório contém a implementação de um sistema de linha de comando (CLI), desenvolvido em Python, para organização pessoal e gestão de produtividade.

Diferente de listas de tarefas e hábitos comuns, foi implementado uma **Abordagem Sistêmica**: além de gerenciar tarefas pontuais e hábitos recorrentes, o sistema introduz a entidade **Projetos**. Os projetos atuam como agregadores (contextos), permitindo que o usuário vincule suas ações diárias a objetivos maiores, criando um mine ecossistema de planejamento.

O projeto consolida os conhecimentos do treinamento prático de **Python e Lógica de Programação**, com ênfase em:

* **Programação Orientada a Objetos (POO):** Classes, propriedades e encapsulamento.
* **Relacionamento entre Objetos:** Implementação de relações 1:N (Um Projeto possui várias Tarefas/Hábitos).
* **Modularização:** Arquitetura separada em camadas de Persistência, Modelagem, Visualização e Regras de Negócio (Relatórios).
* **Persistência de Dados:** Manipulação robusta de arquivos .csv simulando um banco de dados relacional.

## Funcionalidades
O sistema oferece três pilares de gestão:

### Gestão de Projetos (Contextos)
* **Visão Sistêmica:** Criação de áreas de foco (ex: "Faculdade", "Vida Saudável") que agrupam itens.
* **Relatórios Integrados:** Diagnóstico automático que cruza o progresso das tarefas com a consistência dos hábitos daquele projeto.
* **Ranking de Desempenho:** Análise comparativa para identificar quais áreas da vida estão "Em Chamas" e quais estão "Críticas".

### Gestão de Tarefas
* **CRUD Completo:** Cadastro, edição, exclusão e conclusão de tarefas.
* **Vínculo Opcional:** Tarefas podem ser "soltas" ou pertencer a um Projeto específico.
* **Análise de Prazos:** Categorização automática em Atrasadas, Urgentes, Próximas e Futuras.

### Gestão de Hábitos
* **Rastreamento de Frequência:** Suporte a hábitos diários e semanais.
* **Gamificação:** Status dinâmicos ("Em chamas", "Congelado", "Em dia") baseados na última execução.
* **Vínculo Opcional:** Hábitos podem contribuir para o progresso de um Projeto específico.

## Estrutura do Projeto

```plaintext
projeto-d/
│
├── data/                      # Persistência de Dados (CSV)
│   ├── projetos.csv           # Armazena os contextos (agregadores)
│   ├── tarefas.csv            # Armazena tarefas (com chave estrangeira projeto_id)
│   └── habitos.csv            # Armazena hábitos (com chave estrangeira projeto_id)
│
├── relatorios/                # Saída de Dados
│   └── *.txt                  # Relatórios exportados pelo sistema
│
├── src/                       # Código Fonte Modularizado
│   ├── models.py              # Classes: Projeto, Tarefa, Habito
│   ├── views.py               # Interface: Inputs e Prints formatados
│   ├── utils.py               # Utilitários: Formatação de datas e exportação
│   │
│   ├── repositorio_projetos.py # CRUD e persistência de Projetos
│   ├── repositorio_tarefas.py  # CRUD e persistência de Tarefas
│   ├── repositorio_habitos.py  # CRUD e persistência de Hábitos
│   │
│   ├── relatorio_projetos.py   # Lógica de Diagnóstico Sistêmico e Ranking
│   ├── relatorio_tarefas.py    # Lógica de Prazos e Taxa de Conclusão
│   └── relatorio_habitos.py    # Lógica de Consistência e Status
│
├── main.py                    # Orquestrador Principal (Menus e Fluxo)
└── README.md                  # Documentação do Projeto
```

## Como Executar
**Pré-requisitos:** Python 3.x instalado.

1. Clone o repositório:
```bash
git clone https://github.com/gabrielhca/Gerenciador-de-Tarefas-e-Habitos.git
```

2. Navegue até a pasta do projeto:
```bash
cd Gerenciador-de-Tarefas-e-Habitos
```

3. Execute o arquivo principal:
```bash
python main.py
```
> **Nota:** Na primeira execução, o sistema criará automaticamente a pasta `data/` e os arquivos `.csv` necessários.

## Contexto: LIPAI Onboarding
Este projeto faz parte do treinamento do **Laboratório Interdisciplinar de Processamento e Análise de Imagens (LIPAI)**, vinculado à **FACOM/UFU**.

**Conceitos Chave Aplicados:**

* **Classes e Objetos:** Modelagem do mundo real.
* **Persistência em Arquivo:** Leitura/Escrita e tratamento de exceções (try/except).
* **Design de Software:** Separação de responsabilidades (MVC simplificado).
* **Interconexão:** Uso de IDs para relacionar entidades diferentes, permitindo análises complexas a partir de dados simples.
