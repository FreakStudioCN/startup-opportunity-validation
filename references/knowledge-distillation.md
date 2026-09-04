# Knowledge-distillation protocol

The goal is a smaller operational knowledge pack, not a lossy archive format.

## Two layers

1. **Algorithmic evidence distillation:** exact deduplication, TF-IDF character n-gram representation, MiniBatchKMeans topic clustering, and representative-record selection. This layer is reproducible and preserves record IDs, URLs, signal IDs, counts, and samples.
2. **Optional local-LLM synthesis:** summarize only one evidence cluster at a time into a claim, supporting evidence, counterevidence, confidence, and unresolved question. The model must not invent citations or numerical findings.

## Required output artifacts

- `manifest.json`: source inputs, algorithm configuration, record counts, and timestamp.
- `opportunity-atlas.md`: the 30 scored cross-signal clusters, sorted with their hypotheses and next experiments.
- `evidence-clusters.csv`: compact cluster cards with counts, signal composition, domains, and representative evidence IDs/titles.
- `lifecycle-summary.csv`: product-level aggregation of lifecycle and outcome proxy features.

## Local model recommendation

On this Windows RTX 4060 8GB machine, use a quantized multilingual Qwen GGUF through llama.cpp for the optional synthesis pass. A small model is suitable for extracting cluster cards; use a larger quantization only after spot-checking fidelity. Keep prompts structured and request JSON, then validate IDs and counts against the algorithmic artifacts.

Embeddings and LLM summaries improve retrieval and readability; they are not evidence and do not establish causality.
