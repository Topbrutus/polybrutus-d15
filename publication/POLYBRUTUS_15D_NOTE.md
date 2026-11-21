# Polybrutus 15D: Exact Conservative Euclidean Completion and a Ninefold Weighted-Graph Mode

**Research author:** Gabriel St-Pierre  
**Affiliation:** Independent researcher  
**Project:** Polybrutus-X72  
**Date:** 20 November 2026  
**Version:** 0.1.0  
**Status:** Reproducible computational mathematics preprint; not independently peer reviewed  
**Preceding research:** [Polybrutus 14D, DOI 10.5281/zenodo.24408836](https://doi.org/10.5281/zenodo.24408836)  
**Frozen source:** [Topbrutus/polybrutus-d15@v0.1.0](https://github.com/Topbrutus/polybrutus-d15/tree/v0.1.0) (upon public release)

## Abstract

We construct a **twenty-point labelled Euclidean distance configuration** whose minimal affine embedding dimension is **exactly fifteen**, conservatively preserving all **171 pairwise squared distances** of the previously archived Polybrutus 14D. Adding one orthogonal radius-one point produces **19 new pairwise squared distances of value 2R²**, yielding **190 labelled pair distances** distributed among eight exact normalized distance families. We certify the exact coordinate-difference rank and the rank of the centered Euclidean distance Gram matrix, and give an exact positive-semidefinite Gram factorization. An independently implemented rational-arithmetic checker reconstructs all 190 labelled squared distances without importing the primary geometric source.

For an expressly **chosen theoretical complete weighted-graph scalar-oscillator model**, using weights `w_ij=R²/d_ij²` and equal scalar masses, the exact characteristic polynomial has a **ninefold eigenvalue at 10** and a **fourfold eigenvalue at 19/2**. A second checker independently verifies both root multiplicities. These results describe a specific mathematical configuration and a model graph, **not a physical fifteen-dimensional spacetime, measured frequency, or novel universal theorem**.

## 1. Frozen scientific lineage

Polybrutus originates in seven analytically specified points on a sphere in Euclidean three-space. The initial published seven-dimensional metric was a conservative twelve-point completion: five regular-simplex vertices in a four-dimensional subspace orthogonal to the original three-dimensional geometry, preserving the canonical seven-point distances while establishing minimum affine dimension seven. This work was archived as [10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952).

Subsequent dimension-specific verified case studies were: 8D, 13 vertices and 78 pair distances ([DOI 10.5281/zenodo.24408344](https://doi.org/10.5281/zenodo.24408344)); 9D, 14 vertices and 91 pairs ([10.5281/zenodo.24408448](https://doi.org/10.5281/zenodo.24408448)); 10D, 15 vertices and 105 pairs ([10.5281/zenodo.24408569](https://doi.org/10.5281/zenodo.24408569)); 11D, 16 vertices and 120 pairs ([10.5281/zenodo.24408650](https://doi.org/10.5281/zenodo.24408650)); 12D, 17 vertices and 136 pairs ([10.5281/zenodo.24408720](https://doi.org/10.5281/zenodo.24408720)); 13D, 18 vertices and 153 pairs ([10.5281/zenodo.24408769](https://doi.org/10.5281/zenodo.24408769)); and 14D, 19 vertices and 171 pairs ([10.5281/zenodo.24408836](https://doi.org/10.5281/zenodo.24408836)).

The present 15D case **starts from the immutable 14D scientific source tag** `Topbrutus/polybrutus-d14@v0.1.0`, commit `853687b71dd32b05c807aa47b1c8d7b48d7e97e4`. The full source and certificates needed for its 8D-14D computational ancestry are copied unchanged into the `prior/` directory of the current research archive. The previously published labelled metric is not modified.

## 2. Exact twenty-vertex metric

At normalized radius `R=1`, let `p1,...,p19` denote the exact predecessor 14D vectors represented in fifteen storage coordinates. Within these coordinates the older five-simplex point block occupies a four-dimensional centered hyperplane and enforces one linear constraint.

Embed each predecessor point into sixteen storage coordinates by appending a zero:

```
q_i = (p_i,0),           i=1,...,19.
```

Adjoin the twentieth point as the new orthogonal unit basis vector:

```
q20 = e16 = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1).
```

All twenty points have unit norm, and the new point is orthogonal to every predecessor point. Therefore all **171 existing pair distances are identical**, and for every old index:

```
||q20-q_i||² = ||q20||²+||q_i||²-2<q20,q_i> = 2.
```

There are `171+19=C(20,2)=190` unordered labelled pairs. For a general radius `R>0`, multiply all points by `R`: the newly introduced squared distances become `2R²`.

Using the exact normalized squared-distance family parameter `k=4d²/R²`, the complete histogram is:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 6 | 2 | **159** | 3 | 10 | 6 | 2 | 2 |

These eight multiplicities sum to **190**. The exact total of squared pair distances satisfies

```
sum_{i<j}(d_ij²/R²) = 1567/4.
```

At normalized radius the centroid in sixteen storage slots is

```
G = (0,0,1/40,0,0,0,0,0,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20).
```

This construction's *intrinsic affine dimension* is **fifteen**, not sixteen. The sixteenth storage slot is a convenient representation; the centered old five-simplex block retains one exact coordinate dependence.

## 3. Exact certificate of minimum affine dimension 15

Let `X` be the exact **20-by-16** array of rowwise point coordinates. Let `D` be the exact **20-by-20** matrix of **squared Euclidean distances between labelled points**. Set `H=I-11ᵀ/20`, the centered projection, and define the Euclidean distance Gram matrix

```
B = -1/2 H D H.
```

The primary symbolic program establishes three exact statements without floating-point approximation:

```
rank([q2-q1,...,q20-q1]) = 15;
rank(B) = 15;
B = (H X)(H X)^T.
```

The last identity is an explicit **positive-semidefinite factorization**. For a complete labelled Euclidean distance matrix, the centered Gram matrix is uniquely determined. Therefore every Euclidean realization of this **same exact set of 190 labelled squared distances** has affine dimension fifteen. This is a testable rank statement, **not** evidence for extra dimensions in experimental spacetime physics.

The independently written verifier reconstructs all 190 squared distances from rational coefficients of the original seven canonical points, the known squared distance `5/2` among five simplex vertices, and the fact that the remaining appended orthogonal-radius-one vertices are mutually orthogonal to one another and to the two initial blocks. It reproduces **190/190** labelled distances, confirms that **171/171** correspond to the immutable 14D source and recomputes the centered distance Gram rank **15**.

## 4. Ninefold ideal weighted-graph mode

To study a selected mathematical dynamical analogy, assign each point a unit-mass scalar oscillator and choose complete-graph pair weights `w_ij=R²/d_ij²`. This is a **model definition**, not a measurement or property automatically derived from physical apparatus.

Because the new point lies at squared distance 2 from all 19 old points at normalized radius, its coupling to each old oscillator has weight `1/2`. Let `L14` denote the previous **19-by-19** graph Laplacian, and `L15` the **20-by-20** new graph Laplacian. They obey exactly:

```
L15 = [ L14 + (1/2) I19      -(1/2) 1 ]
      [ -(1/2) 1ᵀ                19/2 ].
```

The old nonuniform graph modes shift upward by `1/2`, the uniform zero mode remains zero, and the new differential mode between the old vertex group and the new point appears at eigenvalue **10**. Writing `chi19(z)=det(zI-L14)` and `chi20(z)=det(zI-L15)`, the exact recurrence is

```
chi20(z) = z(z-10) chi19(z-1/2)/(z-1/2).
```

The frozen 14D source contains the factored characteristic polynomial:

```
chi19(z) = z(z-19/2)^8(z-9)^4 f6(z-6),
f6(z) = chiP7(z)/z,
```

where `chiP7` is the canonical seven-point weighted-graph characteristic polynomial and `f6` its six-nonzero-mode factor. Substitution yields the closed form:

```
chi20(z) = z(z-10)^9(z-19/2)^4 f6(z-13/2).
```

The primary verifier computes the **complete 20-by-20 exact characteristic polynomial** and checks equality to both the recurrence and this closed form. The exact nonvanishing tests `f6(7/2) != 0` and `f6(3) != 0` rule out accidental additional factors at the named eigenvalues. The mode multiplicities are therefore **exactly nine at 10** and **exactly four at 19/2**.

The independent verifier computes all twenty-vertex weighted couplings from its separately derived rational labelled distance matrix and certifies the same exact multiplicities using vanishing and nonvanishing derivatives of the full characteristic polynomial. These eigenvalues are dimensionless after our chosen normalization. They are **not** measured oscillator frequencies in hertz.

## 5. Reproduce and falsify

The GitHub scientific source archive contains the exact primary source `src/verify_d15.py`, an independently coded rational checker `tests/independent_d15.py`, the full **190-pair JSON certificate** `results/certificate_d15.json`, immutable predecessor materials in `prior/`, this note, the mathematical specification, provenance, GitHub Actions verification and a tagged Git-source SHA-256 integrity index.

Run both tests:

```sh
python -m pip install sympy==1.14.0
python src/verify_d15.py
python tests/independent_d15.py
```

Both programs must report PASS and the same SHA-256 for the exact JSON certificate. Four intentionally invalid configurations are used as negative controls: one modified distance entry, a repeated new point which loses the new affine direction, a unit point tilted toward the old space, and a permutation of labels that retains the unlabelled distance histogram but violates the labelled metric.

The separately archived Zenodo release contains the immutable source Git-tag ZIP, the scientific PDF, and the full exact JSON labelled metric certificate. File hashes and the pinned parent version support an auditable chain of reconstruction.

## 6. Scientific precedence and interpretative limits

Adding a unit point in an orthogonal Euclidean direction and then computing the complete labelled distance matrix is an established type of geometric operation; likewise a uniformly attached weighted graph has a known spectral recurrence. The specific **15D Polybrutus instance** provides an exact reproducible certificate but does **not** establish a novel universal geometric theorem.

The fifteen-dimensional number is the minimum affine dimension of these **twenty mathematical points**, not an experimentally observed dimensionality of the physical universe. The graph weights are modelling assumptions, so no new elementary particle, Higgs interaction, measured resonance or physical frequency is claimed. Independent human mathematical peer review remains outstanding.

## 7. Authorship, AI disclosure and licensing

**Research author and scientifically responsible investigator:** Gabriel St-Pierre, independent researcher. He originated the underlying Polybrutus programme, determines the staged dimensional publication workflow and is responsible for this deposit.

**Generative AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted source auditing, mathematical derivation and checking, primary source programming, implementation of a separately derived rational verifier, ideal weighted-graph spectral calculations, reproducibility verification, writing and publication preparation. The AI is not listed as a human research author. No human independent peer review is claimed.

**Licenses:** scientific report and narrative documentation CC BY 4.0; source programs MIT.

**References:** Canonical seven-point Polybrutus https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md ; 7D https://doi.org/10.5281/zenodo.24407952 ; 8D https://doi.org/10.5281/zenodo.24408344 ; 9D https://doi.org/10.5281/zenodo.24408448 ; 10D https://doi.org/10.5281/zenodo.24408569 ; 11D https://doi.org/10.5281/zenodo.24408650 ; 12D https://doi.org/10.5281/zenodo.24408720 ; 13D https://doi.org/10.5281/zenodo.24408769 ; 14D https://doi.org/10.5281/zenodo.24408836 ; frozen 14D source https://github.com/Topbrutus/polybrutus-d14/tree/v0.1.0 .
