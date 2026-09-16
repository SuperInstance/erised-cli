# erised-cell — The per-scenario directory

A `.erised/` directory is the **cell** — one scenario + cast + run history as a single identity. The cell IS the seam.

## Why cells

A scenario file alone is a recipe. A run alone is a transcript. Neither carries the lineage.

A cell carries the lineage: scenario, cast, history of runs, character evolution per run, scars that survive rewind. The cell IS what the operator authors. The cell IS what grows.

## Layout

```
.erised/
├── scenario.json          # the canonical scenario (parsed from JSON/YAML)
├── INDEX.md               # human-readable summary
├── cast/
│   ├── mechanic.json      # per-character sheet (keywords, llm, tendencies, history)
│   ├── chronicler.json
│   ├── ...
└── runs/
    ├── 20260916-154023.json    # each run produces one timestamped file
    ├── 20260916-160812.json
    └── ...
```

Each `runs/<timestamp>.json` has:
- `history`: full transcript (DM + per-character turns)
- `resonance`: per-character net shift
- `citations`: who-cites-whom edges
- `dm_opening`, `dm_closing`: the DM's bracketing prose
- `ran_by`: which form produced this (cli, cell, html)

Each `cast/<name>.json` has:
- `name`, `llm`, `tendencies`: the sheet
- `keywords`: parsed dict (after the bug fix)
- `ticks`: starting tick budget
- `version`: increments per run (the cell version-tracks itself)
- `history`: per-run delta_resonance + citations_in + citations_out

## Commands

```bash
./erised-cell init examples/apiary.json          # create a cell from a scenario
./erised-cell run                                # run it (2 ZAI + 12 deepinfra calls)
./erised-cell ls                                 # list all runs
./erised-cell diff 20260916-154023 20260916-160812  # compare resonance, citations, DM closings
./erised-cell index                              # regenerate INDEX.md
```

## Cells are the unit of work

A scenario file is a recipe. A run is a transcript. **A cell is the unit of work.**

When you fork a cell, you fork the lineage. When you rewind a cell, you rewind within the lineage. When you diff two runs in a cell, you measure growth.

The cell has a version number. The cell has a history. The cell can be cloned, archived, exported, imported.

## The seam-as-cell

The cell IS the seam — the place where one operator's hand meets the next. The seam carries the structure across the boundary between runs.

You can't patch over a scar. You can't patch over a cell either. You can only carry it forward.

## License

MIT. Cells are data. Run them anywhere.
