# Expense Tracker

Gestor de gastos personales en Python.

## Versiones

| Versión | Descripción |
|--------|-------------|
| `tracker.py` | **Production Ready** – Validaciones, `datetime`, `match-case`, UX pro |
| `expense_tracker_tutorial.py` | **Tutorial Edition** |

## Conceptos (Tutorial Edition)
- `list` de `dict`
- **List comprehension**: `[g["monto"] for g in gastos]`
- **Set comprehension**: `{g["categoria"] for g in gastos}`
- `sorted()` con `key=lambda`
- `del` o `pop()`
- `for ... in`, `enumerate`

## Cómo ejecutar
```bash
python expense_tracker_tutorial.py