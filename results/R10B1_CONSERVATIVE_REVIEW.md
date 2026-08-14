# R10B1 Conservative Scientific Review

## Revised scientific decision

`CANONICAL_SURFACE_CURVE_NOT_PREFERRED; THICKNESS-CONDITIONED_STEERING_REMAINS_SUPPORTED`

The automatic decision, `RIVAL_TRAJECTORY_PREFERRED_OVER_OFFICIAL_SURFACE`, is directionally correct but
should not be read as falsifying all forms of surface optimization.

## Frozen primary analysis

- main-pair balance threshold: `0.90`
- external-final motifs: 5,995
- external-final objects: 163
- domains: 6
- empirical rho support: 0.300–1.600

## External-final model ranking

| model_id            |     rmse |         r2 |   correlation |   median_object_rmse |
|:--------------------|---------:|-----------:|--------------:|---------------------:|
| weighted_p_free     | 0.83804  |  0.154647  |     0.405509  |             0.65057  |
| developmental_hinge | 0.838622 |  0.153471  |     0.403818  |             0.650851 |
| linear_logrho       | 0.83931  |  0.152082  |     0.403576  |             0.676125 |
| weighted_p1         | 0.851808 |  0.126642  |     0.370266  |             0.634674 |
| official_surface    | 0.864104 |  0.101245  |     0.337499  |             0.656944 |
| weighted_p2         | 0.875442 |  0.0775049 |     0.295721  |             0.670877 |
| constant_null       | 0.916226 | -0.0104481 |     0.0685322 |             0.781169 |

## Pairwise object-bootstrap results versus the official surface curve

| rival_model_id      |   mean_rival_minus_surface_mse |      ci_low |     ci_high |   surface_better_probability |
|:--------------------|-------------------------------:|------------:|------------:|-----------------------------:|
| constant_null       |                      0.0927938 |  0.0302504  |  0.150671   |                       0.997  |
| developmental_hinge |                     -0.0433889 | -0.0754654  | -0.0155379  |                       0.0015 |
| linear_logrho       |                     -0.0422343 | -0.0890002  | -0.00030076 |                       0.0245 |
| weighted_p1         |                     -0.0210993 | -0.0335568  | -0.0107591  |                       0      |
| weighted_p2         |                      0.0197234 |  0.00101807 |  0.0374168  |                       0.9795 |
| weighted_p_free     |                     -0.0443657 | -0.0792845  | -0.0143896  |                       0.0025 |

Positive `rival-minus-surface MSE` means the official surface curve is better.
Negative values mean the rival is better.

## What is supported

1. A rho-dependent steering relation is real at the motif level.
2. The exact official surface curve is better than a rho-independent null.
3. The exact official surface curve is better than the tested p=2
   area-weighted cylindrical/volume-like response.
4. A fixed p=1 weighted-length law, a shallow development-fitted weighted law,
   a main-path/side-sprout hinge, and a generic log-rho law all outperform the
   canonical official surface curve on external-final objects.
5. The ranking is stable across main-pair balance thresholds 0.80, 0.90 and
   0.95.

## What the result most likely means

The empirical response is shallower than the single canonical
`min-surf-netw` bimodal curve. The surface basis retains a positive coefficient
and meaningful predictive value, but its high-rho curvature is too strong as a
universal skeleton-level law.

This does not by itself falsify local surface optimization. The official curve
is generated for a specific terminal geometry and boundary condition, whereas
the empirical motifs mix domains, terminal layouts, planarity, developmental
states and functional constraints. Marginalizing a family of
boundary-conditioned surface trajectories could produce a shallower effective
curve.

## Four-arm result

The four-arm secondary track has essentially no explanatory power:
external-final R2 = 0.000839.
It cannot support a real-network chi-to-lambda transition claim.

## Claim boundary

Allowed:

> Frozen empirical triads support a thickness-conditioned steering law, but
> the single canonical official surface-minimization trajectory is not the
> best predictor among the tested low-capacity response laws.

Not allowed:

- surface minimization has been falsified in all boundary conditions;
- the developmental or flow rival has been causally established;
- a real physical intervention has been performed;
- the four-arm topology transition has been validated in real networks.

## Recommended next action

Do not create another result-rescue phase before outreach. Send a short
technical note to Xiangyi Meng asking whether the canonical bimodal trajectory
was intended as a universal curve across arbitrary terminal geometry, and
whether a boundary-condition ensemble can be generated from the official
simulator.
