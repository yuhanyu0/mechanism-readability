# Reproducibility Status

## What this public repository checks now

The repository contains a frozen, machine-readable evidence summary, the matched-rival preregistration, the minimum-interface table, conservative scientific decision records, and a validator that checks the central claim boundaries and artifact structure.

Run locally:

```bash
python scripts/validate_artifact.py
```

Expected output:

```text
Artifact validation passed.
R12CB budget rows: 12
Claim boundary checks: passed
```

The same command runs automatically on every push and pull request through `.github/workflows/validate-artifact.yml`.

## What is not yet a one-command clean-room reproduction

The full historical pipeline depends on upstream Physical Network data, frozen intermediate tables, source-locked official-solver exports, and large development packages that are deliberately not redistributed in this curated public exhibit.

The canonical solver work is tied to `Barabasi-Lab/min-surf-netw` commit `dcd0ca4490540af8b5e374550f2380055a613955`.

The public repository therefore makes an **auditable evidence-summary claim**, not a promise that every upstream experiment can already be rerun from this checkout alone.

## Held-out-data boundary

The reported held-out-object evaluation uses a frozen split from the same upstream Physical Network dataset. It is not an independent external-dataset replication.

## Release rule

A future reproduction release may add source-locked inputs and runners only after redistribution terms, hashes, and environment requirements are audited. Scientific claim boundaries must not be broadened merely because more implementation files become public.
