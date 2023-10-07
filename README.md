# Causal Inference For Real Estate in Adelaide

![pytest](https://github.com/lewisbails/real-estate/actions/workflows/pytest.yml/badge.svg?event=push&branch=main)
![style](https://github.com/lewisbails/real-estate/actions/workflows/style.yml/badge.svg?event=push&branch=main)

In this study, we aim to estimate the causal effect of the number of bedrooms, number of bathrooms, location, and dwelling type on the weekly rental asking price for properties in Adelaide.
We use coarsened exact matching to reduce the sensitivity of such treatment effect estimates to model specification.

## Setup

```bash
poetry install
```

## Data

An ETL pipeline is run daily to scrape rental listings from various online real estate portals, transform them into a standard `Listing` format, and store them in a NoSQL database (MongoDB).
The pipeline for this can be ran manually as below:
```bash
poetry run python pipelines/domain_listings.py \
--uri <MONGODB URI> \
--db <DB NAME> \
--collection <COLLECTION NAME> \
--url <DOMAIN URL>
```

## Statistics
Since 07-09-23\:
| council                                                |   count |   average rent |   max rent |   min rent |   average bedrooms |   max bedrooms |   average bathrooms |   max bathrooms |
|--------------------------------------------------------|---------|----------------|------------|------------|--------------------|----------------|---------------------|-----------------|
| The Barossa Council                                    |       2 |            328 |        355 |        300 |                  2 |              2 |                   1 |               1 |
| Town Of Gawler                                         |       2 |            440 |        480 |        400 |                  3 |              3 |                   1 |               1 |
| City Of Salisbury                                      |      24 |            483 |        650 |        320 |                  3 |              4 |                   2 |               3 |
| City Of Playford                                       |      35 |            489 |        620 |        340 |                  3 |              5 |                   2 |               2 |
| City Of Mitcham                                        |       6 |            492 |        630 |        320 |                  3 |              5 |                   1 |               3 |
| City of Prospect & City Of Port Adelaide Enfield       |       8 |            494 |        650 |        340 |                  2 |              4 |                   1 |               2 |
| City Of Prospect                                       |       3 |            503 |        550 |        440 |                  2 |              2 |                   1 |               1 |
| Mount Barker District Council                          |       9 |            512 |        670 |        420 |                  3 |              4 |                   2 |               3 |
| City Of Onkaparinga                                    |      16 |            525 |        650 |        420 |                  3 |              3 |                   2 |               2 |
| City Of West Torrens                                   |      11 |            529 |        800 |        370 |                  3 |              4 |                   1 |               2 |
| City Of Port Adelaide Enfield                          |      34 |            532 |        750 |        290 |                  3 |              6 |                   2 |               3 |
| City Of Tea Tree Gully                                 |      10 |            545 |        650 |        420 |                  3 |              4 |                   1 |               2 |
| City Of Charles Sturt                                  |      28 |            553 |        900 |          6 |                  3 |              4 |                   1 |               3 |
| Corporation Of The City Of Adelaide                    |      24 |            563 |       1100 |        200 |                  2 |              3 |                   1 |               2 |
| City Of Port Adelaide Enfield & City of Tea Tree Gully |       1 |            575 |        575 |        575 |                  4 |              4 |                   2 |               2 |
| Corporation Of The City Of Unley                       |      19 |            599 |       1080 |        350 |                  3 |              4 |                   1 |               2 |
| City Of Marion                                         |      18 |            601 |        790 |        415 |                  3 |              5 |                   2 |               3 |
| City Of Campbelltown                                   |      12 |            617 |        900 |        480 |                  3 |              4 |                   2 |               3 |
| Adelaide Hills Council                                 |       3 |            628 |        720 |        495 |                  3 |              4 |                   1 |               2 |
| City Of Norwood Payneham & St Peters                   |      13 |            711 |       1400 |        400 |                  3 |              5 |                   1 |               2 |
| Corporation Of The Town Of Walkerville                 |       5 |            734 |       1200 |        525 |                  4 |              4 |                   2 |               2 |
| Light Regional Council                                 |       1 |            750 |        750 |        750 |                  5 |              5 |                   3 |               3 |
| City Of Burnside                                       |      10 |            769 |       1280 |        310 |                  3 |              5 |                   2 |               3 |
| City Of Holdfast Bay                                   |      11 |            841 |       1900 |        450 |                  3 |              5 |                   1 |               2 |
## Conclusions
...
