# POLYBRUTUS 15D — Exact Euclidean labelled metric and ninefold model eigenvalue

## Official verified public release

- **Zenodo DOI:** [10.5281/zenodo.24408887](https://doi.org/10.5281/zenodo.24408887), [public record 24408887](https://zenodo.org/records/24408887), verified by Zenodo REST API.
- **Frozen science source tag:** [`v0.1.0`](https://github.com/Topbrutus/polybrutus-d15/tree/v0.1.0) at commit `680182c69307fe1be8df831cf7b8eacae2f8ff62`.
- **Successful independent CI:** [GitHub Actions D15 run 44843502748](https://github.com/Topbrutus/polybrutus-d15/actions/runs/44843502748); both verifiers pass.
- **Three verified Zenodo files:** immutable tagged source ZIP, mathematical preprint PDF, complete 190-pair JSON certificate.
- **Scientific limits:** exact affine Euclidean metric of rank 15 and hypothetical graph spectrum; no novel universal theorem or physical extra dimension claim.


**Human author and research responsibility:** Gabriel St-Pierre (Topbrutus), independent researcher.  
**Scientific status:** independently reproducible exact computational mathematics; not peer reviewed by independent human researchers.  
**AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted exact symbolic checking, independent rational checking, graph modelling, research drafting and publication workflow. AI is not an author.

## Complete exact results (radius R=1)

- **20 labelled points**, **190 labelled squared distances**, exact minimal Euclidean affine dimension **15**.
- All **171/171** labelled squared distances of published Polybrutus 14D remain unchanged.
- One orthogonal radius-one vector adds **19** squared pair distances, each exactly **2**.
- Eight classes of normalized squared distances `k=4d²/R²`: `{4:6,7:2,8:159,9:3,10:10,12:6,13:2,16:2}`.
- Exact squared-distance sum: `1567R²/4`.
- Coordinate-difference rank **15** and centered squared-distance Gram rank **15**, with exact positive-semidefinite identity `B=(HX)(HX)^T`. Although points are stored in 16 coordinate slots, the old simplex block has one linear relation.
- **Chosen ideal scalar oscillator weighted graph:** with unit scalar masses and `w_ij=R²/d_ij²`, eigenvalue **10** has exact multiplicity **9** and eigenvalue **19/2** has exact multiplicity **4**. No physical resonance has been measured.
- Two independent implementations confirm all **190/190** labelled metric entries and eigenvalue multiplicities; **4/4** deliberately invalid control cases rejected.

## Reproduce

```sh
python -m pip install sympy==1.14.0
python src/verify_d15.py
python tests/independent_d15.py
```

The second program rebuilds 190 exact rational squared distances and verifies Gram rank and spectrum without importing any point-generator code. The immutable predecessor source and all certificate files are preserved in `prior/`.

## Included artifacts

- `src/verify_d15.py` — exact symbolic construction, full metric, rank, Gram factorization, model Laplacian and four negative controls.
- `tests/independent_d15.py` — independent rational-metric and characteristic-polynomial derivative tests.
- `results/certificate_d15.json` — exact distance values for **all 190 labelled pairs**.
- `SPECIFICATION_D15.md`, `PREUVE_D15.md`, `PROVENANCE.md` — geometry, mathematical proof, original-source chain.
- `publication/POLYBRUTUS_15D_NOTE.pdf` and `.md` — unreviewed computational mathematical preprint CC BY 4.0.
- `SHA256SUMS.txt` — frozen Git source blob hash index; source code MIT.

## Provenance and previous DOIs

Canonical seven-point source: https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md

Polybrutus 7D: https://doi.org/10.5281/zenodo.24407952  
Polybrutus 8D: https://doi.org/10.5281/zenodo.24408344  
Polybrutus 9D: https://doi.org/10.5281/zenodo.24408448  
Polybrutus 10D: https://doi.org/10.5281/zenodo.24408569  
Polybrutus 11D: https://doi.org/10.5281/zenodo.24408650  
Polybrutus 12D: https://doi.org/10.5281/zenodo.24408720  
Polybrutus 13D: https://doi.org/10.5281/zenodo.24408769  
Polybrutus 14D: https://doi.org/10.5281/zenodo.24408836

Frozen predecessor tag: `Topbrutus/polybrutus-d14@v0.1.0`, source commit `853687b71dd32b05c807aa47b1c8d7b48d7e97e4`.

**Limits:** Orthogonal Euclidean completion and graph spectral shifts are established techniques. No novel universal mathematical theorem, discovery of fifteen physical dimensions, or empirical finding is claimed.
