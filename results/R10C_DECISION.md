# R10C decision

**R10C_OBSERVER_ATTENUATION_PARTIAL**

Conservative reading:

`PLAUSIBLE_OBSERVER_ATTENUATION_INSUFFICIENT; EXTREME_DEGRADATION_CAN_MIMIC_THE_SHALLOW_CLASS`

The exact official observer has effective exponent `p = 1.26`. Merely
shortening the centreline window to 12.5% changes it to approximately `p =
1.05`, still far above the frozen
R10B1 empirical interval `[0.35, 0.45]`.

No structural-only, low-noise, or moderate-noise condition passes the strict
sufficiency rule. Two severe conditions reach the empirical interval, but both
require `log-radius noise SD = 0.20` with R9-style role inference. Their median
role accuracy is about 0.5, retained rho coverage is about 0.4, their exponent
intervals span nearly the entire search grid, and median shape R2 is about
0.63.

Therefore ordinary skeleton-window compression and low measurement noise do
not plausibly explain why real motifs prefer a shallow response. Severe
measurement degradation can manufacture a shallow exponent, but only while
destroying the motif identity needed for the claim.

R10C does not adjudicate boundary-condition heterogeneity. The next permitted
scientific step is a prospectively specified official-simulator boundary
ensemble, not further tuning of the observation operator.
