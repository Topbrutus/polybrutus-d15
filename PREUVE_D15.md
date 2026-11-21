# Mathematical certificate — Polybrutus 15D

## A. Labelled distance preservation

From the frozen Polybrutus 14D set `{p1,...,p19}` of radius-one vectors, embed `q_i=(p_i,0)` and adjoin `q20=e16`, orthogonal to every old vector. The old 171 labelled squared distances are exactly unchanged. Since `||q20||²=||q_i||²=1` and `<q20,q_i>=0`, each new squared distance equals 2. Thus there are `171+19=C(20,2)=190` labelled pairs, with normalized histogram `k=4d²` equal to `{4:6,7:2,8:159,9:3,10:10,12:6,13:2,16:2}`. Their total squared length is `1567/4`.

## B. Exact minimal affine rank

Let `X` be the full 20-by-16 coordinate matrix, `D` the 20-by-20 squared-distance matrix, and `H=I-11ᵀ/20` the centering matrix. The exact symbolic verifier proves
```
rank([q2-q1,...,q20-q1]) = 15
rank(B) = 15
B=-H D H / 2 = (H X)(H X)^T
```

The final identity proves `B` positive semidefinite without numerical approximations. Any Euclidean realization of the same 190 *labelled* squared distances has the same centered Gram matrix and therefore affine rank **exactly fifteen**. The 16th storage slot is not a 16th independent affine direction because the embedded five-simplex block satisfies one linear relation.

## C. Exact spectrum of a chosen ideal weighted graph

Choose complete-graph scalar oscillators with equal unit masses and couplings `w_ij=1/d_ij²` at unit radius. The new point couples to each of the 19 former points with weight 1/2, so
```
L15=[ L14+(1/2)I19   -(1/2)1 ]
    [ -(1/2)1ᵀ           19/2 ].
```

The eigenmodes split into old nonuniform modes shifted by 1/2, the global uniform zero mode, and a new intergroup mode at `20/2=10`. For the monic characteristic polynomials,
```
chi20(z)=z(z-10) chi19(z-1/2)/(z-1/2).
```

The frozen parent has `chi19(z)=z(z-19/2)^8(z-9)^4 f6(z-6)`, where `f6(z)=chiP7(z)/z` contains the nonzero modes of the original seven-point graph. Substitution yields
```
chi20(z)=z(z-10)^9(z-19/2)^4 f6(z-13/2).
```

The source computes the entire 20-by-20 exact characteristic polynomial and checks the factorization. Its nonvanishing checks `f6(7/2) != 0` and `f6(3) != 0` establish that the indicated multiplicities are **exactly 9** at eigenvalue 10 and **exactly 4** at eigenvalue 19/2.

An independently written rational metric program verifies **all 190** entries, the rank-15 centered Gram, and both spectral multiplicities by direct polynomial derivatives without importing the primary generator.

## D. Adversarial controls and limits

Four negative controls catch altered squared distances, duplicated new vertices, nonorthogonal additions, and relabelings that preserve unlabelled histograms but violate the labelled metric. The construction uses known Euclidean orthogonal joins and uniformly joined graph Laplacians. It does not establish novel physical dimensions or a universal new theorem, and has not been independently human peer reviewed.
