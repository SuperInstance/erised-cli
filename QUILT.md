# Quilt — Mapping `erised-cli` to Quilt's 5 opcodes

`erised-cli` is the **headless form of the erised engine**. It maps onto Quilt's 5-opcode primitive as follows.

## The 5 opcodes

| Opcode | Role in Quilt | Role in `erised-cli` |
|--------|---------------|-----------------------|
| `BIND`  | Atomically associate a payload with a tag | Loading the scenario JSON (binds name + LLM + tendencies + keywords to a character) |
| `LINK`  | Create a typed edge between cells | Citation tracking in `run()` — references accumulate as `citations[from][to] += count` |
| `EFFECT`| Execute a side effect in the world | `call_llm()` — the LLM call is the side effect |
| `VIEW`  | Read the current shape of the tensor | `--quiet` mode (no per-round prints) — the result IS the tensor |
| `TICK`  | Advance the wall-clock by one step | One iteration of the `for r in range(rounds)` loop |

## Cadence as LLM assignment

Each character's LLM assignment IS its cadence. Z.AI glm-4.5 is terse and technical (the Mechanic's rhythm). DeepInfra Seed-2.0-mini is creative and poetic (the Shepherd's). Seed-2.0-code is numerical (the Chronicler's). **The LLM string IS the rhythm.**

## Conservation invariant

In the HTML product, ticks are explicit. In the CLI, ticks are implicit — they're a property of the character that doesn't get spent (since the CLI runs once and exits). The conservation invariant holds at the API-budget layer: **one LLM call per character per round, no more.**

## Negative space as payload

The CLI's `--quiet` flag is the negative space. When `--quiet` is on, the operator doesn't see the dialog — they only see the result file. The fiction is silent. The data is the message.

## Dehooker Axiom

The CLI is the **dehooker**. The operator stops parsing and runs a single command. The system runs. The transcript falls out. The operator reads it.

## See also

- [`erised`](https://github.com/SuperInstance/erised) — the HTML product
- `gsim.py` — the harness form
- `quilt-conversation` — the timing layer (Rust)
