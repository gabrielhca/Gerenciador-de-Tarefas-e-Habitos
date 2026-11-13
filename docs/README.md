# Blueprint — MVP Web

Versão web do gerenciador, feita em HTML, CSS e JavaScript puro, sem etapa de build.
Ela reproduz no navegador as regras do programa em Python, para dar para ver o sistema
funcionando sem instalar nada.

Versão publicada: https://gabrielhca.github.io/Gerenciador-de-Tarefas-e-Habitos/

## Como rodar localmente
Abra o `index.html` no navegador ou sirva a pasta `docs/`:

```bash
cd docs
python3 -m http.server 8000
# depois acesse http://localhost:8000
```

## Estrutura
```
docs/
├── index.html      # aplicação inteira (HTML + CSS + JS)
└── assets/         # imagens usadas no layout (fundo, perfil, carrossel)
```

## Funcionalidades
- **Tela inicial** com carrossel de fotos e **dashboard** com abas
  (Progresso / Projetos / Tarefas / Hábitos).
- **CRUD** de projetos, tarefas e hábitos.
- **Mesmas regras do programa em Python**: categorias de prazo
  (atrasadas, urgentes, próximas, futuras), consistência e status dos hábitos
  e progresso dos projetos.
- **Dados salvos no navegador** (`localStorage`), sem banco de dados.
  Na primeira visita, os dados de exemplo de `data/*.csv` já vêm carregados.
- **Exportação** do relatório de um projeto em `.txt`.
