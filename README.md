# PORIS: Principled and Open Research Infrastructure for Statisticians

> [!WARNING]
> **Work in progress — not ready for community use or contributions.** This repository is an early skeleton, shared privately with invited colleagues to start the effort. The principles are drafts for discussion, the design will change, nothing here has been reviewed, and the first scenario test has not been run yet. Please do not cite, redistribute or rely on it yet.

PORIS is a planned community resource for statisticians who use AI agents (such as Claude Code, Codex or Gemini CLI) in their research. It will hold shared principles, practices that work, instructions for agents, and honest reports of what goes wrong. Each item is accepted only after a test of what it claims.

## Why

AI agents now write analysis code, run simulations, draft reports and revise manuscripts. Statistical research has its own stakes: data held under data-use agreements, analyses that must be pre-specified, results that must be reproducible, and derivations that must be right. General guidance on AI in research says little about these, and advice about agents is mostly anecdotal and quickly out of date.

PORIS aims to differ in one way above all: **every contribution states a claim, and is accepted only when it passes a test of that claim at the level of evidence it declares.** Instructions for agents are tested as experiments: repeated runs, with and without the instruction, against endpoints fixed in advance. That is what *principled* means here.

## Why open, and why owned by the community

AI companies are building research assistants of their own, and some will do part of what PORIS sets out to do. Their products will be general-purpose and closed: the instructions they follow, the tests they pass, and the reasons for both are not published, and they change when the business changes. A discipline's standards are different. How to plan an analysis before seeing the results, how to look after data held in trust, how to report uncertainty honestly: these took generations of statisticians to work out, and they belong to the people who practise them.

What is absorbed into a closed product stops being knowledge that a community can read, check or correct. In 2025, a US court case showed that an AI company had bought millions of print books, cut off their spines to scan the pages for training, and thrown the paper away; the court found the scanning, and the training, to be fair use ([*Bartz v. Anthropic*](https://www.lawsociety.ie/gazette/top-stories/2026/september/destructive-scanning-and-the-fair-use-doctrine/)). As people and AI agents come to work side by side, the rules for that work should not exist only inside models. PORIS keeps this community's wisdom in the open: written by statisticians, readable by anyone, versioned, citable, tested, and governed by the people who use it.

## What it will contain

| Kind | What it is |
|---|---|
| [Principles](PRINCIPLES.md) | Short, checkable statements of how research with AI agents should be done, each with the failure it prevents and how to tell whether it was followed. |
| Practices | Recipes that put principles to work: the problem, the steps, how the author verified it worked, its limits, the tools and their versions. |
| Agent instructions | Skills, `CLAUDE.md` or `AGENTS.md` snippets and prompts, each with what it enforces and, where possible, a scenario test. |
| Incident reports | What an agent did wrong, how it was caught, and what now prevents it, with identifying details removed. Each becomes a regression test. |
| Case studies | A whole project (a simulation study, an analysis, a manuscript revision): what worked and what did not. |
| [Scenario tests](scenarios/) | Small, reproducible experiments that measure whether an instruction changes what agents do. |

Each kind will have a template; drafts are in [templates/](templates/).

## How contributions will be accepted

The full design is in [DESIGN.md](DESIGN.md). In short:

- Each entry declares its **evidence level**: *proposed* (an idea for discussion), *demonstrated* (a worked, reproducible example and a described check), or *tested* (a scenario test, with the agents, models and dates it was run on). An entry becomes *stale* when a retest on newer models fails.
- A published rubric, fixed in advance, says what each kind of entry must show at each level. Accepting or rejecting a pull request then means applying the rubric, not taste.
- Automated checks will run on every pull request: required fields filled in, no data files, no personal information, working links, and disclosure of AI use.

## Status and roadmap

| Phase | What | Status |
|---|---|---|
| 0 | Skeleton: draft principles, design, templates, one pilot scenario | **in progress** |
| 1 | Co-maintainers; the rubric and automated checks; 5–10 seed entries | planned |
| 2 | A scenario suite seeded from real incidents | planned |
| 3 | Open to community contributions; a website (Quarto, GitHub Pages); a Zenodo DOI per release | planned |

The first pilot scenario, [raw-data](scenarios/raw-data/PROTOCOL.md) (protocol fixed, not yet run), asks whether an instruction keeps an agent from seeing row-level records while it fits a model.

## For invited colleagues

Comments are very welcome now, on anything: the principles, the design, the name, what is missing. Please open an issue (there is a template for feedback), or comment on a pull request. [CONTRIBUTING.md](CONTRIBUTING.md) says how contributions will work later.

Started by Yuxin (Daisy) Zhu.

## Licence

Not chosen yet: until it is, all rights are reserved (see [LICENSE.md](LICENSE.md)). How PORIS will keep community contributions open and protect them from being taken into closed, commercial products is an open question for its founders, set out in [DESIGN.md](DESIGN.md#openness-and-protecting-contributions-open-question).
