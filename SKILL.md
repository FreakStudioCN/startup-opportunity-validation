---
name: startup-opportunity-validation
description: Evaluate, rank, and design 3–7 day validation experiments for startup opportunities using the bundled behavior-signal, opportunity-structure, lifecycle, and evidence datasets. Use for opportunity screening, comparing candidate ideas, evidence-gap analysis, and experiment-card design; not for predicting business success or investment returns.
---

# Startup Opportunity Validation

Use this skill to decide which opportunity should receive the next low-cost market experiment. Treat its outputs as an experiment-priority recommendation, never as a success, revenue, valuation, or investment forecast.

## Select the mode

- **Evaluate one idea:** turn the idea into a falsifiable opportunity card, cite its supplied or local evidence, score it, and identify the single most valuable next test.
- **Rank a batch:** normalize each candidate to the same evidence schema; report incomplete evidence separately from low scores.
- **Discover from the local corpus:** begin with the bundled cross-signal cluster table, then inspect traceable evidence before proposing a candidate.
- **Design an experiment:** read `references/experiment-design.md` and produce a 3–7 day card with an offer, channel, strong signal, kill rule, and cost/time cap.
- **Review results:** update the evidence level and make only `Kill`, `Modify`, `Escalate`, or `Deliver` recommendations.
- **Distill a corpus:** use `scripts/distill_corpus.py` to create a compact, evidence-linked knowledge pack before using an optional local LLM for prose synthesis.

## Operating rules

1. Read `references/framework.md` for any evaluation. Read `references/scoring.md` before assigning a score.
2. Separate **observed evidence**, **inference**, and **unknowns**. Every local-data claim must name its data file and an identifying row, cluster ID, URL, or query.
3. Do not add points merely for AI novelty, launch attention, waitlists, upvotes, or market size. Prefer evidence of workaround, repeated labor, self-build, budget, comparison, replacement, pricing, trial, usage, support, or repeat behavior.
4. An automatic score is only a pre-screen. Explicitly flag buyer identity, budget, delivery feasibility, unit economics, compliance, and hardware supply-chain risk for human review when not directly evidenced.
5. Use the supplied research tables by default. Do not rerun crawlers, fetch new data, send outreach, or contact prospects unless the user explicitly requests that action.
6. For hardware, split the output into a market-validation line and an engineering-validation line. Preorders, demos, and launch attention do not establish ongoing use or repeat demand.
7. For knowledge compression, retain record IDs, source URLs/paths, counts, and representative evidence. Do not call an LLM a replacement for the source corpus.

## Standard output

Return: (1) one-sentence opportunity; (2) target buyer and existing alternative; (3) evidence ledger; (4) A–F score with missing-data notes; (5) main disconfirming risk; (6) next experiment card; and (7) decision.

Use `scripts/score_opportunity.py` only for transparent arithmetic after the facts have been assessed. Its output must retain its source evidence and cannot replace human judgment.

## Bundled material

- Read `references/data-catalog.md` to locate the copied tables and their scope.
- Read `references/source-limitations.md` whenever interpreting lifecycle or HN-derived evidence.
- `research/core-materials/` contains the nine local research documents used to construct this skill.
- `research/data/` contains lightweight, traceable derived tables. Raw crawl archives remain outside this repository.
