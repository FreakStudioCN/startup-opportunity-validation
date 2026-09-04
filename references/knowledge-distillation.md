# Knowledge-distillation protocol

The goal is a smaller operational knowledge pack, not a lossy archive format.

## Method

Use exact deduplication, multilingual TF-IDF representation, MiniBatchKMeans topic clustering, representative-record selection, and deterministic evidence-card templates. The method is reproducible and preserves record IDs, URLs, signal IDs, counts, and samples.

## Required output artifacts

- `manifest.json`: source inputs, algorithm configuration, record counts, and timestamp.
- `opportunity-atlas.md`: the 30 scored cross-signal clusters, sorted with their hypotheses and next experiments.
- `evidence-clusters.csv`: compact cluster cards with counts, signal composition, domains, and representative evidence IDs/titles.
- `lifecycle-summary.csv`: product-level aggregation of lifecycle and outcome proxy features.

The knowledge pack deliberately has no model or embedding dependency. It is small enough to inspect directly and is more auditable than an unconstrained generative summary.
