# Polybrutus D15 — archival release procedure

This is an unreviewed exact mathematical case study with AI assistance explicitly disclosed. No new physical dimension or mathematical universal novelty is claimed.

1. Run both exact and independently coded verifier programs.
2. Create a **private** GitHub source repository, add CI and require a successful run.
3. Freeze the successful source commit with tag `v0.1.0`.
4. Produce source ZIP **from `git archive v0.1.0`**, not the working directory. Record SHA-256 and size of ZIP, scientific PDF and JSON certificate.
5. Stage or reuse **one** Zenodo draft via the user's previously authorized secure local credential loader. Verify author, license, AI disclosure, predecessor DOI, pinned GitHub source and remote file checksums.
6. Make GitHub public. Check tag SHA through public API. Publish the same Zenodo draft and verify the DOI and all files via public API.
7. Record DOI in README, CITATION.cff, manifest and Memoria; preserve immutable source tag.

Avoid simultaneous automated Zenodo harvesting of GitHub archive releases, which would generate duplicates. Do not publish secrets, private files or unrelated conversation data.
