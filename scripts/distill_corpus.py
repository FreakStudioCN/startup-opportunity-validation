#!/usr/bin/env python3
"""Create a compact, traceable knowledge pack from the bundled derived tables.

Uses only stdlib and scikit-learn: source IDs and provenance are retained so that
the resulting pack is a semantic index, not an untraceable LLM summary.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "research" / "data"


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict], fields: list[str]):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def top_terms(vectorizer, center, n=10):
    names = vectorizer.get_feature_names_out()
    indices = center.argsort()[-n:][::-1]
    return " | ".join(names[i] for i in indices)


def multilingual_tokens(text):
    """Keep meaningful English tokens and contiguous Chinese terms for labels."""
    tokens = re.findall(r"[a-z][a-z0-9_+.-]{1,}|[\u4e00-\u9fff]{2,}", text.lower())
    return tokens + [f"{left} {right}" for left, right in zip(tokens, tokens[1:])]


def distinct(values):
    return sorted({v for v in values if v})


def build_evidence_clusters(rows, requested_clusters):
    # Existing evidence IDs are retained. Exact title/domain duplicates are
    # collapsed only for vectorization, never silently counted as new evidence.
    canonical = {}
    for row in rows:
        key = hashlib.sha1((row.get("domain", "") + "\n" + row.get("title", "")).lower().encode("utf-8")).hexdigest()
        canonical.setdefault(key, row)
    records = list(canonical.values())
    texts = [" ".join((r.get("title", ""), r.get("matched_queries", ""), r.get("signal_ids", ""))) for r in records]
    vectorizer = TfidfVectorizer(analyzer=multilingual_tokens, min_df=3, max_df=0.75, max_features=30000, sublinear_tf=True)
    matrix = vectorizer.fit_transform(texts)
    clusters = min(requested_clusters, len(records))
    model = MiniBatchKMeans(n_clusters=clusters, random_state=42, batch_size=2048, n_init=5, max_iter=100)
    labels = model.fit_predict(matrix)
    grouped = defaultdict(list)
    for row, label in zip(records, labels):
        grouped[int(label)].append(row)
    cards = []
    for label, members in grouped.items():
        signal_counts = Counter(x for row in members for x in row.get("signal_ids", "").split(",") if x)
        domain_counts = Counter(row.get("domain", "") for row in members if row.get("domain"))
        samples = sorted(members, key=lambda r: (len(r.get("signal_ids", "").split(",")), len(r.get("title", ""))), reverse=True)[:5]
        cards.append({
            "cluster_id": f"tfidf-{label:03d}",
            "record_count": len(members),
            "signals": "; ".join(f"{k}:{v}" for k, v in signal_counts.most_common(8)),
            "top_domains": "; ".join(f"{k}:{v}" for k, v in domain_counts.most_common(6)),
            "terms": top_terms(vectorizer, model.cluster_centers_[label]),
            "representative_evidence_ids": " | ".join(r.get("evidence_id", "") for r in samples),
            "representative_titles": " | ".join(r.get("title", "").replace("\n", " ")[:180] for r in samples),
            "source_table": "01_deduplicated_evidence.csv",
        })
    return sorted(cards, key=lambda r: int(r["record_count"]), reverse=True), len(records), matrix.shape[1]


def opportunity_atlas(rows):
    rows = sorted(rows, key=lambda r: float(r.get("opportunity_score") or 0), reverse=True)
    lines = ["# Opportunity atlas", "", "This is a compact, evidence-linked view of the existing cross-signal opportunity clusters.", ""]
    for row in rows:
        lines.extend([
            f"## {row.get('cluster_id')} — {row.get('cluster_name')}",
            f"- Score/stage: {row.get('opportunity_score')} / {row.get('funnel_stage')}",
            f"- Buyer: {row.get('target_user')}",
            f"- Problem: {row.get('problem')}",
            f"- Evidence: {row.get('record_count')} records; {row.get('signal_count')} signals; {row.get('unique_authors')} authors; {row.get('unique_domains')} domains.",
            f"- Hypothesis: {row.get('opportunity_hypothesis')}",
            f"- Next experiment: {row.get('next_experiment')}",
            "",
        ])
    return "\n".join(lines)


def lifecycle_summary(rows):
    fields = ("attention", "reselection", "money", "activation", "outcome", "usage", "purchase", "repeat", "friction", "total_signal_volume")
    result = []
    for row in rows:
        result.append({"project_id": row.get("project_id"), "project": row.get("project"), "category": row.get("category"),
                       "opportunity_signal_grade": row.get("opportunity_signal_grade"),
                       **{f: row.get(f) for f in fields}, "source_table": "04_recent_project_feature_scores.csv"})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "knowledge-pack")
    parser.add_argument("--clusters", type=int, default=96)
    args = parser.parse_args()
    if args.clusters < 2:
        raise ValueError("--clusters must be at least 2")
    args.output.mkdir(parents=True, exist_ok=True)
    evidence = read_csv(DATA / "01_deduplicated_evidence.csv")
    opportunities = read_csv(DATA / "02_cross_signal_opportunity_scores.csv")
    lifecycle = read_csv(DATA / "04_recent_project_feature_scores.csv")
    cards, vectorized_records, features = build_evidence_clusters(evidence, args.clusters)
    write_csv(args.output / "evidence-clusters.csv", cards, list(cards[0]) if cards else [])
    (args.output / "opportunity-atlas.md").write_text(opportunity_atlas(opportunities), encoding="utf-8")
    lrows = lifecycle_summary(lifecycle)
    write_csv(args.output / "lifecycle-summary.csv", lrows, list(lrows[0]) if lrows else [])
    manifest = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "method": "exact-key deduplication + multilingual word TF-IDF (1–2 grams) + MiniBatchKMeans + representative evidence selection",
        "inputs": {"deduplicated_evidence": len(evidence), "opportunity_clusters": len(opportunities), "recent_lifecycle_projects": len(lifecycle)},
        "vectorized_unique_evidence": vectorized_records,
        "tfidf_features": features,
        "topic_clusters": len(cards),
        "provenance_rule": "All cluster cards retain IDs, counts, source table and representative titles; verify against the source table before making a claim.",
    }
    (args.output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(args.output), **manifest}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
