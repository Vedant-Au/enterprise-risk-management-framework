# Enterprise Risk Management Framework

**A board-to-operations risk register, scoring engine and governance roadmap for a multi-jurisdictional engineering SME.**

[![Quality checks](https://github.com/Vedant-Au/enterprise-risk-management-framework/actions/workflows/quality.yml/badge.svg)](https://github.com/Vedant-Au/enterprise-risk-management-framework/actions/workflows/quality.yml)

**Portfolio:** [Digital inclusion](https://github.com/Vedant-Au/ons-census-2031-digital-inclusion-risk) · [Accessibility business case](https://github.com/Vedant-Au/accessible-employee-services-business-case) · [Carbon modelling](https://github.com/Vedant-Au/offshore-wind-carbon-footprint-model) · [Workflow automation](https://github.com/Vedant-Au/vfx-workflow-automation-decision-model)

> Portfolio context: this repository develops an MSc group consulting case for WB Alloys Group into a reusable analytical framework. It is not an official WB Alloys risk register, and all example scores require validation in facilitated risk workshops.

## Recruiter quick scan

| Lens | Evidence |
| --- | --- |
| Executive problem | Fragmented risk ownership and inconsistent escalation across a growing group |
| Analysis | Inherent/residual scoring, FMEA, heat maps, KRIs and control ownership |
| Recommendation | Staged ERM operating model with proportionate governance |
| Assurance | Reproducible scoring, validation rules and automated tests |

**Contribution and provenance:** the source was an MSc group consulting case. This repository is an individual portfolio reconstruction of the analytical model, governance design and implementation roadmap. Example risks and scores are workshop inputs, not verified company facts.

## Decision question

How can a growing industrial group move from fragmented, reactive controls to consistent enterprise-wide risk intelligence without imposing an enterprise-scale bureaucracy?

## Recommendation

Adopt a staged ERM operating model aligned with ISO 31000 and COSO principles:

1. Establish board oversight, risk appetite and named ownership.
2. Launch a central register and common 5x5 scoring method.
3. Add monthly KRIs and quarterly group reporting for red and amber risks.
4. Introduce scenario and Monte Carlo methods only after data quality is reliable.

The example register highlights commodity exposure, equipment downtime, supply interruption, cyber risk and key-person dependency as cross-functional priorities.

![Residual risk priorities](outputs/figures/residual_risk_priorities.png)

![Risk heat map](outputs/figures/risk_heatmap.png)

## Analytical toolkit

- 5x5 likelihood-impact scoring and RAG escalation
- Inherent versus residual risk comparison
- Risk taxonomy and ownership fields
- FMEA Risk Priority Numbers for operational failure modes
- KRI definitions and review cadence
- Three-layer governance and four-phase implementation roadmap

## Skills demonstrated

- Enterprise-risk diagnosis and governance design
- Risk-register data modelling
- Heat-map and residual-risk prioritisation
- FMEA, bow-tie and KRI integration
- Executive controls, accountability and maturity planning

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python analysis.py
python -m unittest discover -s tests -v
```

See [methodology](docs/METHODOLOGY.md), [implementation roadmap](docs/IMPLEMENTATION.md), [validation status](docs/VALIDATION.md), and [asset notice](ASSET_NOTICE.md).
