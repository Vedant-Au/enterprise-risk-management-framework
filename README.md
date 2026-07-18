# Enterprise Risk Management for a Growing Engineering Group

**A proportionate board-to-operations risk model for a £25M multi-jurisdictional engineering group.**

[![Quality checks](https://github.com/Vedant-Au/enterprise-risk-management-framework/actions/workflows/quality.yml/badge.svg)](https://github.com/Vedant-Au/enterprise-risk-management-framework/actions/workflows/quality.yml)

**Role:** Team Lead, MSc client engagement  
**Client context:** WB Alloys Group  
**Core decision:** how to create consistent risk intelligence without importing enterprise-scale bureaucracy

## Recommendation

Adopt ERM in stages. Start with board oversight, appetite, named ownership and a common register; then introduce monthly KRIs and quarterly group reporting. Scenario and Monte Carlo methods should follow only when ownership and data quality are reliable enough to support them.

That sequencing matters. A more sophisticated model would not compensate for fragmented accountability or inconsistent source data.

## What I led

During the engagement I led the translation of ISO 31000 and COSO principles into a three-layer governance model and risk lifecycle for the group. The team used FMEA, Bow-Tie and simulation methods to assess strategic and operational exposure and produced a phased implementation roadmap.

This repository publishes a sanitised, reproducible implementation of the register, scoring, FMEA and KRI components. It deliberately separates client-derived examples from illustrative entries.

## Priority view

The example register brings commodity exposure, equipment downtime, supplier interruption, cyber risk and key-person dependency into one escalation model. Residual risk remains high where control evidence is weak, even when the inherent risk is already understood.

![Residual risk priorities](outputs/figures/residual_risk_priorities.png)

![Risk heat map](outputs/figures/risk_heatmap.png)

| Implemented component | Decision use |
| --- | --- |
| Inherent and residual 5x5 scoring | Distinguish exposure from current control effect |
| RAG escalation and review cadence | Focus management attention and set reporting rhythm |
| Named owners and KRIs | Turn the register into an operating mechanism |
| FMEA Risk Priority Number | Prioritise operational failure modes |
| Evidence-status field | Prevent illustrative scores being mistaken for verified facts |

## Design trade-off

The model favours **governance maturity before analytical complexity**. The first implementation phase can run in a controlled spreadsheet or lightweight register. More advanced scenario modelling is gated behind agreed taxonomies, reliable KRIs and facilitated scoring workshops.

The [implementation roadmap](docs/IMPLEMENTATION.md) sets out the ownership, cadence and maturity sequence. The [methodology](docs/METHODOLOGY.md) documents scoring rules, while [validation](docs/VALIDATION.md) distinguishes reproduced evidence from examples.

## Reproduce the implementation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python analysis.py
python -m unittest discover -s tests -v
```

## Evidence boundary

This is not an official WB Alloys risk register. Organisation-specific tolerances, owners, controls and scores require validation in facilitated workshops. Commercial source material and the submitted MSc report are excluded; see [ASSET_NOTICE.md](ASSET_NOTICE.md).
