# Cross-source evidence correlation

## Purpose

The correlation script creates a review queue of pairs of publications from different publishers that have similar wording and publication times. It is intended to help a researcher notice potentially related reporting across official sources.

## Run

From the repository root:

```bash
python scripts/correlate_evidence.py data/collection/YYYY-MM-DD.json
```

The default output is written beside the input snapshot with the suffix `.correlation.json`. An alternate destination can be supplied with `--output PATH`.

## Candidate rule

A pair is queued only when:

- Both records have an ID, URL, parseable publication timestamp, and usable title/summary text.
- The publishers differ.
- The canonicalized URLs differ.
- Publication timestamps are within 72 hours.
- Jaccard similarity of normalized title/summary tokens is at least 0.45.

The similarity threshold is a retrieval heuristic, not a calibrated probability or evidentiary score. It may miss related reports that use different terminology and may surface unrelated reports that share generic terms.

## Mandatory human review

A candidate means only **possible related publications**. Reviewers must independently establish whether the items concern the same underlying event, whether the publishers relied on independent evidence, whether one source merely repeated another, and whether the publication actually describes an event rather than a warning, exercise, capability, or policy action.

Do not convert a candidate into a confirmed incident, corroboration, attribution, severity judgment, or public alert without separate source review and documented reasoning. Preserve each original publication URL and timestamp. Record contradictory reporting and unresolved questions.

## Known limitations

- The current feed schema does not provide structured incident identifiers or reliable entity extraction.
- Publisher names are used as a coarse independence check; two different publishers may still share a source, and two feeds from one publisher may report distinct material.
- The script compares pairs, not clusters. It does not merge records or infer a common event.
- Only items present in the supplied snapshot are considered.
- Publication time is not event time.
- The script does not assess threat, likelihood, impact, imminence, actor identity, or civilian consequences.
