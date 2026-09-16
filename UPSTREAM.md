# Upstream — `erised` (HTML) + `gsim.py` (harness)

This CLI is the **headless / server-side form** of the same engine.

| Component | `gsim.py` | `erised` (HTML) | `erised-cli` (this) |
|-----------|-----------|------------------|---------------------|
| Language | Python | JavaScript | Python |
| Interface | script + JSON output | browser + canvas | terminal + transcript |
| State | in-memory | localStorage | in-memory (or `--out` JSON) |
| LLM routing | `llm_router.py` | inline `callLLM()` | inline (minimal) |
| Parallel | ThreadPoolExecutor | implicit (browser) | ThreadPoolExecutor |
| Time economy | implicit (energy) | explicit (ticks) | implicit (in `result.resonance`) |
| Scars | log file | side panel | not yet |
| Use case | batch scripting | authoring | one-shot CI |

## What changed

- **Removed**: time-economy UI, scars panel, citation graph visualization, character sheet editing UI. The CLI is **read-only with respect to state** — you edit the JSON, you run, you read.
- **Added**: `--init` scaffold, `--out` JSON export, optional `yq.py` YAML→JSON converter.
- **Reduced deps**: `gsim.py` imports `llm_router.py` (4-LLM dispatcher). `erised-cli` inlines the two most-used backends (Z.AI + DeepInfra) and falls back gracefully if a key is missing.

## License

Both: MIT.
