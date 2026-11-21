# Polybrutus D15 — Exact 20-point Euclidean configuration

**Frozen parent:** `Topbrutus/polybrutus-d14@v0.1.0`, commit `853687b71dd32b05c807aa47b1c8d7b48d7e97e4`, DOI `10.5281/zenodo.24408836`.

Normalize `R=1`. Let `p1,...,p19` be the 19 exact D14 unit vectors represented in 15 storage-coordinate slots (one zero-sum relation constrains the five-simplex block).

Embed all old points by `q_i=(p_i,0)` for `i=1,...,19`. Append `q20=e16=(0,...,0,1)`, the new orthogonal unit vector in the sixteenth slot.

Every earlier labelled pair distance is identical. For every old index `i`,
```
||q20-q_i||²=||q20||²+||q_i||²-2<q20,q_i>=2.
```

For arbitrary radius `R>0`, all distances squared scale by `R²`.

- Number of vertices: **20**; unordered labelled pairs: **190**.
- Previous distances conserved: **171/171**. New squared distances: **19 × 2R²**.
- Minimal affine dimension **15**, with **16** storage coordinates and one linear constraint.
- Normalized family histogram `k=4d²/R²`: `{4:6,7:2,8:159,9:3,10:10,12:6,13:2,16:2}`.
- Squared-distance sum `sum(d²)=1567R²/4`.
- At R=1 the exact storage-coordinate centroid is `(0,0,1/40,0,0,0,0,0,1/20,1/20,1/20,1/20,1/20,1/20,1/20,1/20)`.

## The chosen ideal oscillator graph

For equal unit masses and weights `w_ij=R²/d_ij²`, a new graph vertex is joined with weight 1/2 to each of the 19 former vertices:

```
L15 = [ L14 + (1/2)I19    -(1/2)1 ]
      [ -(1/2)1ᵀ             19/2 ].
```

The full exact characteristic polynomial obeys
```
chi20(z) = z(z-10)*chi19(z-1/2)/(z-1/2)
         = z(z-10)^9(z-19/2)^4 f6(z-13/2),
f6(z)=chiP7(z)/z.
```

Eigenvalue 10 has multiplicity 9 and eigenvalue 19/2 multiplicity 4. These are properties of this **chosen graph model**, not measured frequencies or new physics.
