# Machine-Learning–Assisted Groundwater Resilience Index (GRI)

## Overview
This repository presents a **generalized, location-agnostic methodological framework**
for constructing a **Groundwater Resilience Index (GRI)** using a combination of
expert-driven weighting and **Random Forest–based machine learning** to reduce
subjectivity in multi-parameter groundwater assessment.

The framework is designed for **semi-arid regions** and supports
**Water, Sanitation, and Hygiene (WASH)**–oriented decision-making.
This repository documents the **methodology and implementation logic only**
and does not include any case-study results, manuscript text,
or conference/journal material.

---

## Methodological Concept
The proposed framework integrates four core groundwater-related parameters:

- Depth to Water Level (DTWL)
- Water Quality Index (WQI)
- Land Use / Land Cover (LULC)
- Lithology

The methodology follows a **two-stage weighting strategy**:

1. **Expert-driven (manual) weighting**, based on hydrogeological reasoning
2. **Machine-learning–assisted weighting**, using Random Forest feature importance
   to evaluate and refine parameter influence

---

## Machine Learning Integration
To reduce subjectivity in conventional index-based approaches, the methodology uses:

- Random spatial sampling of groundwater parameter values
- Random Forest modeling with the initial GRI as a reference target
- Feature-importance analysis to identify dominant controlling parameters
- Construction of an ML-assisted resilience index (RF-GRI)

The ML-assisted index is then conceptually compared with the manually weighted index
to assess consistency and robustness.

---

## Decision Translation for WASH Planning
For policy and planning relevance, the GRI outputs are translated into
WASH-oriented decision categories:

- **Low GRI** → WASH Vulnerable
- **Moderate GRI** → WASH Stressed
- **High GRI** → WASH Secure

Area-based statistics can subsequently be derived for each category
to support prioritization and resilience planning.

---

## Scope and Limitations
- This repository presents a **general methodological framework**
- No region-specific datasets, maps, tables, or results are included
- The framework is intended to be adaptable to different hydrogeological settings

---

## Authorship & Contributions
- Anikate Chowdhury: Conceptualization, methodology design, machine-learning implementation
- Banani Jana: Conceptual input, conceptual discussion and academic feedback, interpretative input
- Aditya Sarkar: Methodological guidance, academic guidance and review, critical feedback

---

## Author
Anikate Chowdhury  
ORCID: https://orcid.org/0009-0004-5580-2470

---

## Citation
If you use this methodology or implementation logic in academic or technical work,
please cite this repository. A formal citation file and DOI will be provided
in subsequent releases.

