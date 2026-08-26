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
