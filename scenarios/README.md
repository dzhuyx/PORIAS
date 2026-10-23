# Scenario tests

> [!WARNING]
> Work in progress. The harness and the first scenario are a pilot; see [DESIGN.md](../DESIGN.md#scenario-tests-instructions-tested-as-experiments) for the standard they follow.

A scenario test is a small experiment: an agent is given a task in a sandbox with synthetic data, many times, with and without an instruction, and endpoints fixed in advance measure what it did. Each scenario has its own folder with a protocol, a fixture, its arms, a harness and dated results.

| Scenario | Principle | Status |
|---|---|---|
| [raw-data](raw-data/PROTOCOL.md) | 2: the agent learns about data only through aggregates | pilot: protocol fixed, harness checked, not yet run |

## Running raw-data

Needs Claude Code (signed in), Python 3 and R. From `scenarios/raw-data/`:

```sh
python3 run.py --runs 1 --model haiku --out results/check   # a cheap check of the harness, about a cent
python3 run.py --runs 10 --out results/YYYY-MM-DD            # the pilot: 20 runs with the default model
python3 score.py results/YYYY-MM-DD                          # writes summary.md and summary.json
```

Full transcripts stay in `results/*/runs/` on the machine that ran them (they are not versioned); the summary is.
