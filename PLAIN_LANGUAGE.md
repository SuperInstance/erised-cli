# Plain Language — What `erised-cli` actually does

*For developers. No jargon.*

## The problem

If you want to run a multi-agent cooperative fiction experiment on a server, in CI, or as part of a larger pipeline, you don't want to open a browser. You want a command.

## What `erised-cli` is

A single Python file that takes a JSON scenario, runs it, prints the transcript to stdout. No browser. No canvas. No UI. Just text in, text out.

## Quick start

```bash
export ZAI_TOKEN="..."
export DEEPINFRA_TOKEN="..."
./erised my-scenario.json
```

That's it. The script prints the transcript. Add `--out result.json` to save the structured result.

## API budget

This script is designed to be cheap. A 4-character, 3-round run costs:
- 2 Z.AI calls (DM opening + closing)
- 12 DeepInfra calls (3 rounds × 4 characters)

About 14 calls per run. Even on a free tier, you can run hundreds of these.

## Use cases

- **Headless experiments.** Run a scenario on a server without a browser.
- **Batch comparison.** Loop over model assignments and diff the results.
- **CI smoke tests.** Verify a scenario still produces valid output after a code change.
- **Embedding into larger systems.** Call `run(scenario)` as a Python function from your own code.

## Examples

Three scenarios ship in `examples/`:
- `quick-test.json` — 2 characters, fastest possible test
- `quilt-12mo.json` — The Quilt project, 1 year out
- `monastery.json` — The same dilemma in a monastic setting

## License

MIT. Use commercially, non-commercially, fork it, ship it.
