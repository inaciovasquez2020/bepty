# Contributing to BEpTy

## Contribution classes

### 1. Documentation improvements

- clarify repository status
- improve onboarding and quickstart text
- add navigation help across theory/status files

### 2. Test and verifier hardening

- add regression tests
- tighten verifier-facing documentation
- improve artifact-surface checks

### 3. Semantic or theorem-surface changes

These require explicit justification.

- changing defined comparison classes
- changing valuation statements
- expanding proved-scope language

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run tests before commit:

```bash
python3 -m pytest -q
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- expanding proved-scope language without synchronized status updates
