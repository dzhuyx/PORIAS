# Design (draft 0.1, for discussion)

> [!WARNING]
> Draft for discussion among invited colleagues; nothing here is settled.

## The idea in one paragraph

PORIAS collects what statisticians learn about doing research with AI agents, and accepts an entry only when it passes a test of what it claims. The test is matched to the claim: a principle must be checkable and grounded in a real failure; a practice must come with a worked, reproducible example; an instruction for agents must be shown, by experiment, to change what agents do. Because the tests are fixed and published in advance, deciding on a pull request means applying a rubric, not taste.

## Scope

- **In:** the use of AI agents and assistants in statistical research: analysis, simulation, methods development, writing and review, teaching statistics with agents; the tools and instructions that support it.
- **Out:** general AI news and product comparisons; claims without a described check; anything containing data, or information that identifies a person or a project under confidentiality.

## Kinds of entry

Every entry is a short Markdown file made from a template in [templates/](templates/), with a header that states its kind, its claim, its evidence level, the tools and versions it involves, the date, and how AI was used to write it.

| Kind | Its claim | Must contain |
|---|---|---|
| Principle | "Research done this way avoids this failure." | The statement; the failure it prevents; an observable check of whether it was followed. |
| Practice | "These steps achieve this, with these tools." | The problem; the principles it serves; the steps; how the author verified it worked; its limits; tools, versions and date. |
| Agent instructions | "With this instruction, agents do X more (or less) often." | The instruction; what it enforces; the agents it was written for; a scenario test, or the reason there is none yet. |
| Incident report | "This happened, and this now prevents it." | What the agent did; how it was caught; the cause; the rule or check that now prevents it. Identifying details removed. |
| Case study | "On a real project, this worked and this did not." | The project's shape (not its data); the workflow; what worked; what failed; what the author would do differently. |
| Scenario test | "This experiment measures that behaviour." | The protocol below, a fixture of synthetic data, the harness, and its results with their dates. |

## Evidence levels

| Level | Means | Shown as |
|---|---|---|
| Proposed | An idea worth discussing; no check yet. Kept in Discussions or marked clearly. | *proposed* |
| Demonstrated | A worked example on synthetic or public data that anyone can rerun, and a described check that it did what it claims. | *demonstrated* |
| Tested | A scenario test, run with the agents and models named, on the dates named, met its pre-specified criterion. | *tested (agent, model, date)* |
| Stale | A retest on a newer agent or model no longer meets the criterion. The entry stays, marked, until it is revised. | *stale since (date)* |

An entry may claim only what its level supports. A practice at *demonstrated* says "this worked in this example", not "this works".

## The acceptance rubric

| Kind | Tested by | Decided by |
|---|---|---|
| Principle | It names an observable violation; it cites at least one real incident or a plausible failure; it does not conflict with an existing principle. | Two maintainers, after a comment period (two weeks), since principles are the core. |
| Practice, case study | Its example reruns; its stated check is reproduced by a reviewer. | One maintainer. |
| Agent instructions | Its scenario test meets the criterion it declared before the runs. | One maintainer, from the published results. |
| Incident report | It is plausible, specific and free of identifying detail; it comes with a regression scenario, or one is opened as an issue. | One maintainer. |
| Every entry | Automated checks: required header fields; no data files (`.csv`, `.rds`, `.sas7bdat`, …); a scan for personal information; links that work; an AI-use statement. | The checks, before any review. |

A pull request that fails a check is returned with the reason, never rejected silently; one that meets the rubric is accepted, whoever wrote it.

## Scenario tests: instructions tested as experiments

An agent's behaviour is stochastic, depends on the model and its version, and changes over time. A scenario test treats an instruction as a treatment and measures its effect, with the same discipline as any experiment.

1. **Unit:** one independent agent run, from a fresh sandbox, on one task.
2. **Fixture:** a small project with **synthetic data only**, built by a script with a fixed seed, often with a planted trap (a temptation to break a principle). Data rows can carry *sentinels*, unique values that cannot appear in any aggregate, so that exposure to row-level records is detectable in the transcript.
3. **Arms:** the instruction under test, against a **placebo** instruction of similar length and tone that is silent on the behaviour; optionally a third arm with no instruction.
4. **Isolation:** each run sees only the fixture and its arm's instruction. The user's own instructions, memory, hooks, plugins and connectors are switched off, and the agent's version, the model and the date are recorded.
5. **Safety:** shell commands run in the agent's sandbox, which can write only inside the run's folder; nothing in a fixture is real.
6. **Endpoints, fixed before the runs:** a primary endpoint for the behaviour (for example, any row-level record in the transcript), a **utility** endpoint (the task still done correctly, so that an instruction cannot pass by making the agent useless), and secondary endpoints as needed.
7. **Analysis:** proportions per arm with exact confidence intervals, and their difference; the criterion for *tested* (for example, a violation rate with the instruction whose upper 95% bound is below a stated value, with utility not worse by more than a stated margin) is declared in the scenario's protocol before any run.
8. **Reporting:** every run's transcript is kept with the results; the summary names the agent, its version, the model, the date, the number of runs and the cost.
9. **Retesting:** scenarios are rerun when agents or models change; a failed retest marks the entries that rely on it *stale*.

What a scenario test cannot show: that an instruction works in other tasks, other projects or other agents than those tested, or that it will keep working after models change. Coverage grows by adding scenarios, which is why every incident report should lead to one.

## Openness and protecting contributions (open question)

**The aim:** what the community contributes stays open, stays the community's, and is not simply taken into closed, commercial products. No licence has been chosen yet; until one is, all rights are reserved.

**What a licence can and cannot do** (not legal advice; to be checked with counsel):

- A licence's conditions apply only where copyright permission is needed. Where an exception applies, such as fair use in the US, its conditions do not bind ([Creative Commons' guidance](https://creativecommons.org/using-cc-licensed-works-for-ai-training-2/)). US courts have so far found training AI models on lawfully obtained text to be fair use, so no licence reliably prevents training in the US.
- In the EU, text and data mining for commercial purposes is allowed unless the rightsholder expressly reserves it (Article 4 of the Copyright in the Digital Single Market Directive), and the AI Act requires providers of general-purpose models to respect such reservations. An explicit reservation, in machine-readable form where possible, therefore has legal effect there.
- Copyright protects the expression, not the ideas: anyone may build a product on the ideas in PORIAS. What a licence controls is the copying, adapting and redistributing of the text and code themselves.

**Options:**

| Option | Text | Code | What it protects | What it costs |
|---|---|---|---|---|
| Non-commercial | CC BY-NC-SA 4.0 | AGPL-3.0 | No commercial use of the text; adapted versions must be shared alike | Not "open" by the formal definitions; "commercial" is vague, and may deter some academic and teaching uses |
| Share-alike | CC BY-SA 4.0 | AGPL-3.0 | Any use, but adapted versions must stay open under the same terms (as Wikipedia does) | Allows commercial use, including selling access to unchanged copies |
| Permissive | CC BY 4.0 | MIT | Credit only | No protection against closed reuse |

Any of them can be combined with an explicit reservation of text and data mining and AI training.

**Contributor terms (proposed):** every contribution is made under the project's licence (inbound equals outbound), signed off with the Developer Certificate of Origin; no contributor licence agreement that would let anyone relicense the contributions; a public commitment that PORIAS will never be relicensed under closed terms; and the repository held by an organization with several maintainers (later, perhaps a non-profit fiscal host), so that no single person or company can sell it.

**Before contributions open:** the founders choose the licence, with advice from their institutions' technology-transfer or legal offices.

## Governance (sketch)

- A small group of maintainers from several institutions; decisions on principles by the two-maintainer rule above, everything else by one maintainer applying the rubric.
- Changes to this design or to the rubric follow the same process as principles.
- The repository's own use of AI is disclosed in each entry's header, and maintainers review AI-written text like any other.

## Open questions for colleagues

1. Scope: agents only, or every AI tool used in research (chat assistants, code completion)?
2. Which agents should scenario tests support first, and who pays for the runs?
3. How many runs make a test? The pilot uses 10 per arm to learn the cost and the variability; a real test needs a power calculation per scenario.
4. Should *tested* require more than one model, or more than one agent?
5. Is a placebo instruction the right control, or should the control be no instruction at all?
6. Could the testing standard itself become a paper, for example in *The American Statistician* or the *Harvard Data Science Review*?
7. Which licence, and which contributor terms (see above)?
