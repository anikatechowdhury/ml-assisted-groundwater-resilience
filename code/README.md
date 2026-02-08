# Code Overview

This directory contains **generic Python scripts** demonstrating the
machine-learning–assisted Groundwater Resilience Index (GRI) methodology.

The scripts are **illustrative templates only** and are intentionally
location-agnostic. Users are expected to adapt the code to their own
datasets and hydrogeological settings.

No region-specific data, results, or case-study outputs are included.

---

## Workflow Summary
1. Normalize groundwater-related parameters
2. Construct a manually weighted GRI
3. Perform random sampling of parameter values
4. Train a Random Forest model
5. Extract feature importance
6. Generate an ML-assisted GRI (RF-GRI)
7. Translate index outputs into WASH-relevant decision categories
