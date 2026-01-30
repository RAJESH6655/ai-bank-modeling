import json
import os

def recommend_banks(credit_score):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    rules_path = os.path.join(base_dir, "..", "data", "bank_rules.json")

    with open(rules_path, "r") as f:
        rules = json.load(f)

    for category, details in rules.items():
        min_score, max_score = details["score_range"]
        if min_score <= credit_score <= max_score:
            return category, details["banks"]

    return "Unknown", []
