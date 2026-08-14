# R9 Conservative Scientific Review

## Uploaded automatic decision

`PASS_R9_MOTIF_INTERFACE_RESTORES_READABILITY_AND_TRANSPORT`

## Conservative decision

`PARTIAL_R9_MOTIF_INTERFACE_REVEALS_A_TRANSPORTABLE_TRIAD_RELATION; FOURARM_TRANSITION_INCONCLUSIVE`

## Strongest supported result

The degree-3 triad interface reveals a robust pooled relation between the radius ratio proxy `rho_proxy` and the steering-angle proxy `Omega`:

- challenge hinge R2: 0.293811
- external-final hinge R2: 0.327889
- external-final gain over constant: 0.330131
- external object-bootstrap gain 95% interval: 0.237221 to 0.422327

However, the hinge model improves only modestly over the linear model:

- challenge incremental R2 over linear: 0.010731
- external-final incremental R2 over linear: 0.015761

Therefore the robust result is a transferable monotonic `rho_proxy -> Omega` association. Evidence for a sharp threshold/regime boundary is positive but modest.

## Four-arm result

The frozen `chi_proxy -> merged degree-4` model is not robust across frozen splits:

- development log-loss gain: +0.026338
- challenge log-loss gain: -0.040334; AUC 0.422008
- external-final log-loss gain: +0.016352; AUC 0.688320

Domain-level signs are heterogeneous, and the relation is construction-adjacent because `chi_proxy` contains central radius while merged state is defined by node degree. It is not currently a transported topology-transition law.

## Readability geometry

R9 motif fingerprints have effective rank 2.802 (bootstrap 95% interval 2.744 to 2.985), compared with the frozen R7 edge-level value 1.158. This is promising but not a clean causal comparison because R7 and R9 use different query sets and different fingerprint scaling. A matched cross-interface normalization is required before attributing the entire rank increase to the motif observation unit.

The four R3 geometry candidates remain highly query-equivalent in motif space (absolute pairwise cosine roughly 0.884 to 0.986). The R4 degree-radius relation is more distinct (absolute cosine roughly 0.506 to 0.661). Thus R9 supports at least two broad response families rather than five independent mechanism directions:

1. a main-path versus third-branch geometry response family;
2. a topology-thickness response family.

## Query adequacy caveat

The oracle classification is 55/55, but the oracle candidate bundles are direct noisy copies of the same target variables queried by the fingerprint panel. This validates implementation plumbing and gross axis separability, not discrimination among realistic rival mechanisms.

## Surface-minimization claim

R9 is compatible with a surface-minimization-style triad relation, but it does not uniquely identify surface minimization. Developmental main-path continuation, flow-weighted branching, and growth-guidance mechanisms remain viable rivals. All R9 variables are same-source SWC-derived proxies, not exact circumference/surface quantities or physical interventions.

## Next scientific step

Do not create another adaptive internal stage. Freeze the R9 triad law and test it in one of two genuinely confirmatory settings:

1. official simulator trajectories with known parameters and rival objectives; or
2. a wholly new object/data cohort with a preregistered balance criterion and independent thickness/surface measurements.

The four-arm law should remain inconclusive until a new-data or simulator confirmation succeeds across both challenge-like and final-like environments.
