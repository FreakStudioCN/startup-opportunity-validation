#!/usr/bin/env python3
"""Optional local-LLM second pass over distilled cluster cards."""
import argparse
import csv
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYSTEM = """You are a research distillation assistant. Return valid JSON only.
Summarize the supplied evidence cluster without adding facts, URLs, counts, buyers,
or citations absent from it. Separate evidence from inference. Use Chinese keys:
claim, evidence_summary, inference, counterevidence_or_unknown, confidence.
Confidence must be low, medium, or high."""

def prompt(card):
    return SYSTEM + "\nINPUT:\n" + json.dumps(card, ensure_ascii=False) + "\nJSON:"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--llama-cli", type=Path, required=True)
    parser.add_argument("--model-arg", action="append", default=[], help="Additional llama-cli arguments, repeated as needed")
    parser.add_argument("--input", type=Path, default=ROOT / "knowledge-pack" / "evidence-clusters.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "knowledge-pack" / "llm-cluster-cards.jsonl")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    rows = list(csv.DictReader(args.input.open(encoding="utf-8")))[:args.limit]
    with args.output.open("w", encoding="utf-8") as handle:
        for card in rows:
            command = [str(args.llama_cli), *args.model_arg, "-n", "350", "-p", prompt(card)]
            result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=300, check=True)
            raw = result.stdout.strip()
            first, last = raw.find("{"), raw.rfind("}")
            if first < 0 or last < first:
                raise ValueError(f"No JSON received for {card['cluster_id']}")
            summary = json.loads(raw[first:last + 1])
            handle.write(json.dumps({"cluster_id": card["cluster_id"], "source_card": card, "summary": summary}, ensure_ascii=False) + "\n")
    print(args.output)

if __name__ == "__main__":
    main()
