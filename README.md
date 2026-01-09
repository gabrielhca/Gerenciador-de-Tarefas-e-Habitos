# Projeto D: Gerenciador de Tarefas e Hábitos

> Projeto 1 desenvolvido durante as Semanas 4 e 5 do Onboarding LIPAI.

## Sobre o Projeto

Este repositório contém a implementação do **Projeto D**, um sistema de linha de comando (CLI) focado na organização pessoal e produtividade. O software permite o gerenciamento de tarefas pontuais e o acompanhamento de hábitos recorrentes, aplicando conceitos de persistência de dados e modularização.

O projeto foi desenvolvido como parte do treinamento prático de **Python e Lógica de Programação**, consolidando conhecimentos em:
* Estruturas de Controle e Funções;
* Programação Orientada a Objetos (POO);
* Manipulação e Persistência de Arquivos (.csv).

---

## Funcionalidades

O sistema atende aos requisitos obrigatórios do Projeto D:

### ✅ Gestão de Tarefas
* **Cadastrar:** Registro de novas tarefas com título, descrição e data limite.
* **Listar:** Visualização de tarefas pendentes e concluídas separadamente.
* **Concluir:** Mecanismo para marcar tarefas como finalizadas.

### 🔄 Gestão de Hábitos
* **Cadastrar:** Definição de novos hábitos (ex: "Leitura 30min") e frequência.
* **Registrar Execução:** Incremento do contador de vezes que o hábito foi realizado ("Check-in").
* **Relatório Simples:** Visualização de quantas vezes cada hábito foi cumprido.

---

## Estrutura do Projeto

O código foi organizado seguindo princípios de modularização para facilitar a manutenção:

```text
projeto-d/
│
├── data/                  # Armazenamento de dados (Persistência)
│   ├── tarefas.csv        # Banco de dados das tarefas
│   └── habitos.csv        # Banco de dados dos hábitos
│
├── src/                   # Código Fonte
│   ├── main.py            # Ponto de entrada (Menu Principal)
│   ├── models.py          # Definição das Classes (Tarefa, Habito)
│   ├── repositories.py    # Leitura e Escrita nos arquivos CSV
│   ├── reports.py         # Lógica de relatórios
│   └── utils.py           # Funções auxiliares e validadores
│
└── README.md              # Documentação do Projeto

```

---

## Como Executar

Pré-requisitos: Python 3.x instalado.

1. Clone o repositório:
```bash
git clone [https://github.com/gabrielhca/Gerenciador-de-Tarefas-e-Habitos.git](https://github.com/gabrielhca/Gerenciador-de-Tarefas-e-Habitos.git)

```


2. Navegue até a pasta do projeto:
```bash
cd Gerenciador-de-Tarefas-e-Habitos

```


3. Execute o arquivo principal:
```bash
python src/main.py

```


---

## Contexto: LIPAI Onboarding

Este projeto faz parte do treinamento do **Laboratório Interdisciplinar de Processamento e Análise de Imagens (LIPAI)**, vinculado à FACOM/UFU.

**Stack Tecnológico do Treinamento:**

* **Linguagem:** Python 3.x
* **Versionamento:** Git / GitHub
* **Paradigmas:** Estruturado e Orientado a Objetos


