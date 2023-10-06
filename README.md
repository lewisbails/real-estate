# Causal Inference For Real Estate in Adelaide

![pytest](https://github.com/lewisbails/real-estate/actions/workflows/pytest.yml/badge.svg?event=push&branch=main)
![style](https://github.com/lewisbails/real-estate/actions/workflows/style.yml/badge.svg?event=push&branch=main)

In this study, we aim to estimate the causal effect of the number of bedrooms, number of bathrooms, location, and dwelling type on the weekly rental asking price for properties in Adelaide.
We employ causal exact matching to reduce the sensitivity of such treatment effect estimates to model specification.

## Data

Rental listings have been periodically scraped from various online real estate portals, transformed into a standard `Listing` format, and loaded into a NoSQL database (MongoDB).
The pipeline for this can be ran manually as below:
```bash
python pipelines/domain_listings.py
```

## Statistics
Since 06-09-23\:
| council                                          |   count |   average rent |   max rent |   min rent |   average bedrooms |   max bedrooms |   average bathrooms |   max bathrooms |
|--------------------------------------------------|---------|----------------|------------|------------|--------------------|----------------|---------------------|-----------------|
| The Barossa Council                              |       2 |            328 |        355 |        300 |                  2 |              2 |                   1 |               1 |
| Town Of Gawler                                   |       1 |            400 |        400 |        400 |                  3 |              3 |                   1 |               1 |
| City Of Mitcham                                  |       5 |            464 |        600 |        320 |                  3 |              4 |                   1 |               1 |
| City Of Playford                                 |      32 |            489 |        620 |        340 |                  3 |              5 |                   2 |               2 |
| City Of Salisbury                                |      22 |            492 |        650 |        320 |                  3 |              4 |                   2 |               3 |
| City of Prospect & City Of Port Adelaide Enfield |       6 |            502 |        650 |        340 |                  2 |              4 |                   1 |               2 |
| City Of Prospect                                 |       3 |            503 |        550 |        440 |                  2 |              2 |                   1 |               1 |
| Mount Barker District Council                    |       9 |            512 |        670 |        420 |                  3 |              4 |                   2 |               3 |
| City Of Onkaparinga                              |      15 |            521 |        650 |        420 |                  3 |              3 |                   1 |               2 |
| City Of Port Adelaide Enfield                    |      33 |            531 |        750 |        290 |                  3 |              6 |                   2 |               3 |
| City Of West Torrens                             |      10 |            544 |        800 |        370 |                  3 |              4 |                   1 |               2 |
| City Of Tea Tree Gully                           |       9 |            550 |        650 |        420 |                  3 |              4 |                   1 |               2 |
| City Of Charles Sturt                            |      27 |            555 |        900 |          6 |                  3 |              4 |                   1 |               3 |
| Corporation Of The City Of Adelaide              |      22 |            564 |       1100 |        200 |                  2 |              3 |                   1 |               2 |
| City Of Marion                                   |      18 |            601 |        790 |        415 |                  3 |              5 |                   2 |               3 |
| City Of Campbelltown                             |      10 |            608 |        900 |        480 |                  3 |              4 |                   2 |               3 |
| Adelaide Hills Council                           |       3 |            628 |        720 |        495 |                  3 |              4 |                   1 |               2 |
| Corporation Of The City Of Unley                 |      16 |            633 |       1080 |        395 |                  3 |              4 |                   1 |               2 |
| City Of Norwood Payneham & St Peters             |      13 |            711 |       1400 |        400 |                  3 |              5 |                   1 |               2 |
| Corporation Of The Town Of Walkerville           |       5 |            734 |       1200 |        525 |                  4 |              4 |                   2 |               2 |
| City Of Holdfast Bay                             |       9 |            741 |       1500 |        450 |                  3 |              4 |                   1 |               2 |
| Light Regional Council                           |       1 |            750 |        750 |        750 |                  5 |              5 |                   3 |               3 |
| City Of Burnside                                 |      10 |            769 |       1280 |        310 |                  3 |              5 |                   2 |               3 |
## Conclusions
...
