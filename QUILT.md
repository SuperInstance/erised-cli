# Quilt — Mapping `erised-cli` to Quilt's 5 opcodes

`erised-cli` is the **headless form of the erised engine**. It maps onto Quilt's 5-opcode primitive as follows.

## I. BIND + LINK

**BIND**: scenario loading + character sheets bind payload to tag.
At-most-once: each character has a unique `name` field. If `name` collides,
the second one overwrites the first. Missing fields are tolerated
(`tendencies`, `keywords`, `ticks` all default). The binding is **atomic**
— the scenario is parsed in full before any LLM call fires.

**LINK**: citations and resonance are edges between character cells.
When a character's text mentions another character by name, a citation
edge is added: `citations[from][to] += count`. The shape is the same as
Quilt's LINK opcode: typed edge, weight on the edge, character-as-node.

The CLI tracks this in `result.citations`. Each run accumulates edges.
Diff two runs of the same scenario with different casts — the citations
graph shows whose voice dominates.

## II. EFFECT + VIEW + TICK

**EFFECT**: the LLM call is the world's side effect.
One LLM call per character per round. The dispatch (`zai:glm-4.5` or
`deepinfra:ByteDance/Seed-2.0-mini`) is the type of effect. Threads run
characters in parallel via `concurrent.futures.ThreadPoolExecutor`. The
side effect is bounded — no character can produce more than one
utterance per round.

**VIEW**: `--quiet` / `--out` / the result JSON is the tensor read.
The result has `.title`, `.history`, `.resonance`, `.citations`,
`.dm_opening`, `.dm_closing`. The shape is the same as Quilt's VIEW:
read the tensor without mutation. The `result.json` is the
**read-only projection** of the scenario after running.

**TICK**: the round loop is the wall-clock advance.
Each iteration of `for r in range(rounds - 1)` is one TICK. The DM
opens (round 1, DM only), the characters respond in parallel (rounds
2..N), the DM closes (final round). The tick counter is **immutable**
— it advances; it never resets, never goes backwards.

## III. Conservation, Negative Space, Dehooker

**Conservation**: the API budget IS the conservation invariant.
2 Z.AI calls for the DM (opening + closing) + 1 DeepInfra call per
character per round = the **total energy available**. Conservation
holds at the API-budget layer. The CLI never escalates. If the budget
is exceeded, the run fails silently and the operator reads the result.

**Negative space**: `--quiet` is the silent fiction.
When `--quiet` is on, the operator doesn't see the dialog. The fiction
is silent. The data is the message. Negative space is also encoded in
the gaps between turns — the silent rhythm. The operator reads the
JSON and infers what was said.

**Dehooker Axiom**: the CLI is the dehooker.
The operator stops parsing and runs a single command. The system runs.
The transcript falls out. The operator reads it. No state to maintain,
no UI to navigate, no canvas to position. The CLI is the **zero-UI form
of the engine** — the operator's hand on the canvas becomes the
operator's hand on the keyboard.

## IV. Cadence as LLM assignment

Each character's LLM assignment IS its cadence. Z.AI glm-4.5 is terse
and technical (the Mechanic's rhythm). DeepInfra Seed-2.0-mini is
creative and poetic (the Shepherd's). Seed-2.0-code is numerical
(the Chronicler's). **The LLM string IS the rhythm.** Replace
`zai:glm-4.5` with `deepinfra:ByteDance/Seed-2.0-mini` and the same
character with the same tendencies will produce a different voice.

## V. Scenario as witness log

A scenario is a **witness log** of the dilemma before it played out.
The setting is the dilemma's frame. The cast is the dilemma's voices.
The keywords are the dilemma's drift terms. Running the scenario is
the dilemma **speaking itself** through the cast.

Six scenarios ship in `examples/`. Each is a witness log of a
different shape of the same dilemma: a system of cells, sustained by
a small crew, growing past its first year.

## See also

- [`erised`](https://github.com/SuperInstance/erised) — the HTML product
- `gsim.py` — the harness form (legacy)
- `quilt-conversation` — the timing layer (Rust)
