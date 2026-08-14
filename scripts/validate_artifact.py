from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCKED_SOLVER_SHA = "dcd0ca4490540af8b5e374550f2380055a613955"


def main() -> int:
    required = [
        "README.md",
        "CLAIM_BOUNDARY.md",
        "REPRODUCIBILITY.md",
        "DATA_PROVENANCE.md",
        "figures/mechanism_readability_overview.svg",
        "figures/held_out_model_ranking.svg",
        "results/frozen_summary.json",
        "results/R12CB_PRIMARY_MINIMUM_INTERFACE_TABLE.csv",
        "protocols/R12CB_PREREGISTRATION_NOTE.md",
        ".github/workflows/validate-artifact.yml",
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    if missing:
        print("Missing required artifact files:")
        for path in missing:
            print(f"- {path}")
        return 1

    summary = json.loads((ROOT / "results/frozen_summary.json").read_text(encoding="utf-8"))
    assert summary["r12cb_matched_pair"]["max_declared_low_order_difference"] == 0.0
    assert summary["r12cb_matched_pair"]["max_native_j0_j2_accuracy"] == 0.5
    assert summary["claim_boundary"]["empirical_generator_identified"] is False
    assert summary["claim_boundary"]["surface_optimization_generally_falsified"] is False

    with (ROOT / "results/R12CB_PRIMARY_MINIMUM_INTERFACE_TABLE.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 12:
        raise AssertionError(f"Expected 12 R12CB budget rows, found {len(rows)}")

    provenance = (ROOT / "DATA_PROVENANCE.md").read_text(encoding="utf-8")
    if LOCKED_SOLVER_SHA not in provenance:
        raise AssertionError("Locked solver commit SHA is missing from DATA_PROVENANCE.md")

    boundary = (ROOT / "CLAIM_BOUNDARY.md").read_text(encoding="utf-8").lower()
    if "independent external-dataset replication" not in boundary:
        raise AssertionError("Independent-replication boundary is missing from CLAIM_BOUNDARY.md")

    print("Artifact validation passed.")
    print(f"R12CB budget rows: {len(rows)}")
    print("Claim boundary checks: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
