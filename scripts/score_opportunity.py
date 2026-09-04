#!/usr/bin/env python3
"""Calculate transparent Opportunity Pre-Screen arithmetic from reviewed inputs."""
import argparse
import json
from pathlib import Path

FIELDS = ("demand_behavior", "opportunity_structure", "lifecycle_hardness", "experimentability", "commercialization")

def number(value, field):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    if not 0 <= value <= 20:
        raise ValueError(f"{field} must be between 0 and 20")
    return value

def decision(score):
    if score >= 80: return "Immediate 3–7 day experiment"
    if score >= 65: return "Customer discovery or quote test"
    if score >= 50: return "Gather decisive desktop evidence"
    if score >= 35: return "Watchlist"
    return "Kill unless new evidence appears"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path, help="JSON with five 0–20 fields, anti_pattern_penalty 0–50, evidence, and unknowns")
    args = p.parse_args()
    item = json.loads(args.input.read_text(encoding="utf-8"))
    positive = {field: number(item.get(field), field) for field in FIELDS}
    penalty = item.get("anti_pattern_penalty", 0)
    if isinstance(penalty, bool) or not isinstance(penalty, (int, float)) or not 0 <= penalty <= 50:
        raise ValueError("anti_pattern_penalty must be between 0 and 50")
    score = round(sum(positive.values()) - penalty, 1)
    print(json.dumps({"score": score, "decision": decision(score), "components": positive,
                      "anti_pattern_penalty": penalty, "evidence": item.get("evidence", []),
                      "unknowns": item.get("unknowns", []),
                      "warning": "Pre-screen only; not a success, revenue, or investment prediction."},
                     ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
