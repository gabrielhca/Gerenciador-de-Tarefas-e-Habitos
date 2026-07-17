# Blueprint — MVP Web

Aplicação web funcional (HTML + CSS + JS puro, sem dependências externas de build)
que implementa o sistema **Blueprint**: gestão de Projetos, Tarefas e Hábitos,
seguindo o design definido nos protótipos (tela de login e dashboard).

## Como rodar
Basta abrir o `index.html` em qualquer navegador (duplo clique) ou hospedar a pasta
inteira em qualquer servidor estático (GitHub Pages, Netlify, Vercel, etc.):

```bash
# opção rápida local
cd blueprint-app
python3 -m http.server 8000
# depois acesse http://localhost:8000
```

## Estrutura
```
blueprint-app/
├── index.html      # aplicação inteira (HTML + CSS + JS)
└── assets/         # imagens usadas no design (fundo, perfil, carrossel)
```

## Funcionalidades
- **Tela de Login/Landing**: replica o protótipo com o hero, carrossel de fotos e rodapé.
- **Dashboard**: replica o protótipo com sidebar (foto, calendário, indicadores),
  navegação por abas (Progresso / Projetos / Tarefas / Hábitos) e cartão principal.
- **CRUD completo** de Projetos, Tarefas e Hábitos.
- **Regras de negócio** replicadas do backend Python original: categorização de
  prazos (atrasadas/urgentes/próximas/futuras), cálculo de consistência de hábitos,
  status (em chamas / atenção / congelado) e progresso sistêmico dos projetos.
- **Persistência de dados**: usa a API de armazenamento do ambiente Claude quando
  disponível; fora dele (uso normal em navegador), usa `localStorage` do próprio
  navegador — sem necessidade de banco de dados.
- **Exportação de relatório** de projeto em `.txt` (equivalente ao `exportar_relatorio`
  do backend Python).

Dados de exemplo (os mesmos projetos/tarefas/hábitos do `data/*.csv` original) já
vêm pré-carregados na primeira execução, para simular o funcionamento do sistema.
