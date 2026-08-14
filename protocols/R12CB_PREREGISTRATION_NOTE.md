# R12C-B preregistration — Matched-rival interface sufficiency

## Primary matched pair

```text
M_weighted_equilibrium
M_developmental_matched_endpoint
```

Both mechanisms use the exact same rho- and boundary-dependent weighted-equilibrium junction endpoint. This is deliberate: the benchmark asks whether one low-order transition law can hide distinct path-generating structures.

## Rendering tracks

### Common rendering

Both mechanisms use identical straight centerlines. Every measured feature must match. Classification above chance is a leakage or implementation failure.

### Native morphology

The weighted world remains straight. The developmental world uses persistent main-axis continuation tangents and smooth Bezier paths while preserving the same junction, terminals, radii, branch chord lengths and full-axis angles.

Interfaces J0-J2 must remain matched. J3/J4 may expose curvature and local tangent history.

## Boundary split

```text
development: frozen nine-point R12B planar grid
final: 12 fixed-seed Latin-hypercube boundaries inside the declared R12B box
```

Final boundaries are not used to set any generator or interface parameter.

## Trajectory budgets

```text
T1_static: rho = 0.90
T3_sparse: rho = {0.30, 0.90, 1.60}
T9_full: all nine frozen rho values
```

## Replicate budgets

```text
1, 3, 10, 100
```

The same noise realization is paired across mechanisms at each boundary/rho/replicate.

## Nested interfaces

```text
J0 radius multiset
J1 unordered chord lengths and full-axis pair angles
J2 role-aware rho, Omega and branch-length contrasts
J3 sampled skeleton shape, curvature and local tangents
J4 exact full geometry and terminal-boundary metadata
```

## Decoder

A standardized nearest-centroid classifier is frozen for every cell.

## Identification gate

Pairwise identification requires:

```text
mean final-boundary accuracy >= 0.70
95% boundary-bootstrap lower bound > 0.55
```

The low-order match gate requires maximum weighted/developmental difference at J0-J2 to be at most `1e-10`.

## Null-calibrated readability

A rho response is readable only when its 95% lower slope bound exceeds the 95th-percentile absolute null slope plus a practical margin of `0.02`.

## Surface position

Exact surface remains available only at the canonical boundary. Noncanonical surface cells remain computationally unresolved and are not imputed.

## Claim ceiling

This phase establishes a synthetic identifiability boundary for a deliberately matched pair. It does not identify mechanisms in real networks.
