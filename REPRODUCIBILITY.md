# Reproducibility Status

## What this public repository reproduces now

The repository contains a frozen, machine-readable evidence summary, the matched-rival preregistration, the minimum-interface table, conservative scientific decision records, and a validator that checks the central claim boundaries and interface-table shape.

Run:

```bash
python scripts/validate_artifact.py
```

Expected output:

```text
Artifact validation passed.
R12CB budget rows: 12
Claim boundary checks: passed
```

## What is not yet a one-command clean-room reproduction

The full historical pipeline depends on upstream Physical Network data, frozen intermediate tables, source-locked official-solver exports, and large development packages that are deliberately not redistributed in this curated public exhibit.

The public repository therefore makes an **auditable evidence claim**, not a false promise that every upstream experiment can already be rerun from this checkout alone.

## Release rule

A future reproduction release may add source-locked inputs and runners only after redistribution terms, hashes, and environment requirements are audited. Scientific claim boundaries must not be broadened merely because more implementation files become public.
