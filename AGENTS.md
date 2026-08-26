# AGENTS.md

## Checklist obrigatório

Antes de concluir qualquer mudança:

- [ ] Lint: `uv run ruff check .`
- [ ] Build/importação: `uv run python -m compileall app tests`
- [ ] Testes: `uv run pytest`

Prepare o ambiente com `uv sync`. Para executar a aplicação:

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Contexto e convenções

Soc Ops é um Social Bingo em Python 3.13+, FastAPI, Jinja2 e HTMX. Separe regras (`app/game_logic.py`), estado em memória por `session_id` (`app/game_service.py`), rotas (`app/main.py`) e apresentação (`app/templates/`). Dados e modelos ficam em `app/data.py` e `app/models.py`; testes de API e domínio ficam em `tests/`.

- Preserve `hx-*`, `hx-target` e `hx-swap` nos fragmentos HTMX.
- Modelos Pydantic são congelados: use `model_copy(update=...)`.
- Sessões em memória não são persistência de produção.
- Atualize testes ao mudar comportamento ou endpoints.
- Consulte as [instruções](.github/instructions/), o [README](README.md), o [guia](workshop/GUIDE.md) e as [regras de contribuição](CONTRIBUTING.md).

## Guia de design

Soc Ops deve parecer uma experiência social, clara e convidativa, com personalidade própria para um jogo de bingo colaborativo.

- Prefira uma direção visual coesa, com tipografia expressiva, cores de alto contraste e variáveis CSS em `app/static/css/app.css`.
- Evite layouts genéricos, fontes comuns como Arial/Inter/Roboto, gradientes roxos e excesso de cartões decorativos.
- Use os utilitários existentes antes de criar novos; quando um utilitário faltar, adicione-o ao `app.css` seguindo o padrão atual.
- Mantenha o tabuleiro como foco principal: células com dimensões estáveis, estados marcado/não marcado evidentes e boa leitura em telas pequenas.
- Garanta que controles tenham foco visível, contraste adequado, rótulos claros e áreas de toque confortáveis.
- Use CSS para animações curtas e significativas, como entrada escalonada e confirmação de marcação; respeite `prefers-reduced-motion`.
- Preserve `hx-*`, `hx-target` e `hx-swap` ao estilizar ou reorganizar fragmentos HTMX.
- Teste a composição em desktop e mobile, verificando especialmente quebra de texto, sobreposição e mudanças de tamanho durante interações.
