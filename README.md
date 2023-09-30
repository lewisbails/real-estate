# Causal Inference For Real Estate in Adelaide

* Data was scraped periodically from various online real estate portals and sorted in a NoSQL database.
* Coarsened Exact Matching was used to reduce multidimensional covariate imbalance between the treated and control groups.
* We look into the possible treatment effect of an extra bedroom or bathroom, or the kind of dwelling.

## Data Collection

* Extract HTML, transform into a standardised `Listing` format, and load into a MongoDB collection.
* This script was run every day on the most recent listings page.

```bash
python pipelines/domain_listings.py
```

## Data Exploration

...

## Modelling

...

## Results

...

## Conclusions

...