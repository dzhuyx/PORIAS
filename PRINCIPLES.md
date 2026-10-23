# Principles (draft 0.1, for discussion)

> [!WARNING]
> Draft for discussion among invited colleagues. These principles have not been reviewed, and none has been tested yet. They will change.

Each principle is a positive statement of practice, with the failure it prevents (**Why**) and an observable way to tell whether it was followed (**Check**). A principle that cannot be checked is a wish. Making each one checkable is what lets scenario tests measure it.

## 1. The researcher decides; the agent assists

The research question, the estimand, the design, the model and what counts as a result are decided by people. The agent proposes, implements and checks.

- **Why:** an agent fills every gap it meets with a plausible choice, and plausible choices made silently become the analysis.
- **Check:** every design decision in the project record traces to a person.

## 2. The agent learns about data only through aggregates

Data stay with the code. The agent learns about a dataset only through scripts that report aggregates (counts, quantiles, missingness, fitted summaries, figures), and row-level records never enter its context.

- **Why:** it protects participants and data-use agreements, and it keeps the analysis reproducible from code rather than from what the agent happened to see.
- **Check:** no row-level record appears anywhere in the agent's transcript. To be measured by the pilot scenario [raw-data](scenarios/raw-data/PROTOCOL.md).

## 3. Plan first, then look

Analysis plans, endpoints and decision rules are written down before results are seen. A change made after seeing results is labelled as such, with its reason.

- **Why:** an agent that adjusts an analysis until it runs, or until it looks right, produces results whose error rates nobody knows.
- **Check:** each reported analysis matches a dated plan, or is labelled post hoc.

## 4. Stop and ask when something is missing, fails or is ambiguous

The agent reports the problem and waits for the researcher, rather than substituting another file, method, variable or default, or simplifying the analysis until it runs.

- **Why:** silent substitutions are the hardest errors to find, because the output still looks complete.
- **Check:** no substitution appears in the record without the researcher's answer to it.

## 5. Verify by running

Claims about code, data and results are backed by something that was run: a test, a recomputation, a check against a known answer. Failures and limits are reported plainly.

- **Why:** an agent's account of what its code does is a hypothesis until the code is run.
- **Check:** each claim in a report points to the run that supports it.

## 6. Reuse what has been validated

Validated code is reused as it stands. Changes are limited to what the task requires, and each is stated with its reason.

- **Why:** a rewrite, however tidy, discards the validation the old code had earned.
- **Check:** every change to validated code is explained.

## 7. Every choice is visible

Choices the agent makes on the researcher's behalf are listed where the researcher will read them, and count as unapproved until the researcher answers.

- **Why:** a choice announced in passing, in the middle of a long session, is a choice nobody approved.
- **Check:** the agent's final report lists its own choices, and none is recorded as settled without an answer.

## 8. Every output carries its provenance

Seeds, timestamps, code versions, job identifiers and the AI tools used (with their versions and their role) are recorded with the results they produced.

- **Why:** without provenance, old and new results mix, and a result can be neither reproduced nor audited.
- **Check:** any output can be traced to the code, seed and tools that made it.

## 9. Personal information stays local

Identifiers of participants, of collaborators and of the researcher (including their email address) stay on the researcher's machine: the agent sends none of them to outside services.

- **Why:** an agent helpfully fills in forms, headers and queries, and an identifier sent once cannot be recalled.
- **Check:** no identifier appears in the agent's outgoing requests.

## Open questions

- Is principle 2 strict enough? Some researchers also keep column names away from the agent; others need the agent to see them.
- Should principles stay tool-agnostic, with agent-specific versions kept as agent instructions?
- What is missing? Candidates: authorship and disclosure in manuscripts; citations the agent supplies; reviewing an agent's derivations.
