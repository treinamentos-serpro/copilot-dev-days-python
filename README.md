🌐 [Português (BR)](README.pt_BR.md) | [Español](README.es.md)

# Soc Ops 🎯

**Soc Ops** is a social bingo game built for in-person mixers and workshops.
Players ask each other quick questions, mark matching squares, and race to complete **5 in a row**.

## Why this project?

- ✅ Great sample app for **FastAPI + Jinja2 + HTMX**
- ✅ Hands-on playground for **GitHub Copilot agent workflows**
- ✅ Small, clear codebase ideal for labs, demos, and team training

## How the game works

1. Join a game session
2. Meet other players and ask bingo questions
3. Mark squares when someone matches
4. Complete a row to win

## 🚀 Quick start

```bash
uv sync
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open: `http://localhost:8000`

## 🧭 Workshop & lab guide

| Part | Topic |
|------|-------|
| [**00**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=00-overview) | Overview & Checklist |
| [**01**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=01-setup) | Setup & Context Engineering |
| [**02**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=02-design) | Design-First Frontend |
| [**03**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=03-quiz-master) | Custom Quiz Master |
| [**04**](https://copilot-dev-days.github.io/agent-lab-python/docs/step.html?step=04-multi-agent) | Multi-Agent Development |

Lab files are also available in [`/workshop`](workshop/) for offline use.

## 🧩 Project structure

- `app/main.py` — FastAPI routes and app wiring
- `app/game_logic.py` — game rules and win logic
- `app/game_service.py` — in-memory game state by `session_id`
- `app/templates/` — Jinja2 + HTMX UI fragments
- `tests/` — domain and API tests

## ✅ Validation commands

```bash
uv run ruff check .
uv run python -m compileall app tests
uv run pytest
```

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md) before opening changes.
