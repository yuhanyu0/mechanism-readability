# Data and Source Provenance

## Physical Network data

- Catalog: `https://physical.network/`
- Zenodo record: `17154400`
- DOI: `10.5281/zenodo.17154400`
- Historical frozen package noted in the research audit: `physical.network.zip`

The held-out object split reported in this artifact comes from the **same upstream Physical Network dataset**. It is a frozen held-out evaluation split, not an independent external-dataset replication.

The public artifact does not redistribute the full upstream archive by default.

## Surface-minimization solver

- Upstream repository: `https://github.com/Barabasi-Lab/min-surf-netw`
- Locked commit used for the exact-payload / canonical-trajectory work: `dcd0ca4490540af8b5e374550f2380055a613955`
- The canonical trajectory used in the comparison was extracted from source-verified saved solver states rather than digitized from a paper figure.

The locked-commit value is recorded in the R10B0-C preregistration and reused by later exact-surface work.

## Associated paper

X. Meng et al., *Surface optimization governs the local design of physical networks*, Nature 649, 315–322 (2026). DOI: `10.1038/s41586-025-09784-4`.

## Release rule

Every future public release should record exact upstream versions/hashes before adding new scientific claims.
