# erised-cli

> *desire reversed — terminal runner*

The companion to [erised](https://github.com/SuperInstance/erised) (the HTML product). This is a **single-file Python CLI** for running cooperative-fiction scenarios in the terminal. No build, no deps beyond the Python stdlib.

## What it does

Reads a scenario (JSON or YAML), runs the simulation, prints the transcript. One LLM call per character per round, in parallel.

- **Z.AI glm-4.5** for the DM (opening + closing)
- **DeepInfra Seed-2.0-mini / Seed-2.0-code** for characters
- Threads run characters in parallel via `concurrent.futures.ThreadPoolExecutor`

## Quick start

```bash
# 1. Set tokens
export ZAI_TOKEN="..."
export DEEPINFRA_TOKEN="..."

# 2. Scaffold a template
./erised --init > my-scenario.json

# 3. Run
./erised my-scenario.json --rounds 4

# 4. Output to file (for further analysis)
./erised my-scenario.json --out result.json
```

## API budget (conservative by design)

- **1 Z.AI call** per scenario (DM opening) + **1 Z.AI call** per scenario (DM closing) = **2 Z.AI calls per run**
- **1 DeepInfra call** per character per round (4 characters × 3 rounds = **12 DeepInfra calls per run**)
- A 4-round run costs roughly **14 API calls total**

That fits inside any free tier.

## Examples

Ten scenarios ship in `examples/`:

- `quick-test.json` — 2 characters, 4 rounds. Cheapest test.
- `quilt-12mo.json` — The Quilt project, 1 year out. 4 characters.
- `monastery.json` — Same dilemma, monastic setting.
- `fract-canon.json` — Self-referential library.
- `monorail.json` — Rail car with no operator.
- `100yr-out.json` — The Quilt, 100 years forward.
- `patron-library.json` — Community library, books by patrons.
- `coral-atoll.json` — Floating research station over a transplant.
- `apiary.json` — Beekeeper's legacy tended by neighbors.
- `root-cellar.json` — Communal cellar, blight has taken the founder's seed.

## erised-cell — the per-scenario directory

For a scenario with lineage (multiple runs, versioned cast, run history),
use `erised-cell`:

```bash
./erised-cell init examples/apiary.json   # creates .erised/
cd .erised/                               # (auto-detected by walking up)
./erised-cell run                          # produces runs/<timestamp>.json
./erised-cell ls                           # list runs
./erised-cell diff <run1> <run2>           # compare resonance + citations
```

See [CELL.md](CELL.md) for full docs.

## YAML support

`yq.py` is a tiny YAML-to-JSON converter that ships alongside. It supports the limited YAML we use (no pyyaml dep):

```bash
./yq.py scenario.yaml > scenario.json
./erised scenario.json
```

## Lineage

Built on the simulation harness in `/workspace/research/ttrpg-night/gsim.py`. The harness was the experiment; `erised` (HTML) is the product form; this CLI is the headless/server-side form.

## License

MIT.
