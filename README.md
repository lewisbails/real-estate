# Causal Inference For Real Estate in Adelaide

* How much does the number of bedrooms or bathrooms affect the asking price for rentals in Adelaide? What about the type of dwelling?
* Using coarsened exact match, a matching method for causal inference, we aim to provide answers to such questions.

## Setup

For development:

```bash
poetry install --with dev,test,style
```


## Data Collection

* Data was scraped periodically from various online real estate portals, transformed into a standard format, and loaded into a NoSQL database (MongoDB).

```bash
python pipelines/domain_listings.py
```

## Statistics
As of 05-10-23\:
| council                                          |   count |   average rent |   max rent |   min rent |   average bedrooms |   max bedrooms |   average bathrooms |   max bathrooms |
|--------------------------------------------------|---------|----------------|------------|------------|--------------------|----------------|---------------------|-----------------|
| The Barossa Council                              |       2 |            328 |        355 |        300 |                  2 |              2 |                   1 |               1 |
| Town Of Gawler                                   |       1 |            400 |        400 |        400 |                  3 |              3 |                   1 |               1 |
| City Of Mitcham                                  |       3 |            392 |        485 |        320 |                  2 |              3 |                   1 |               1 |
| City Of Prospect                                 |       3 |            503 |        550 |        440 |                  2 |              2 |                   1 |               1 |
| City Of Playford                                 |      31 |            491 |        620 |        340 |                  3 |              5 |                   2 |               2 |
| City Of Onkaparinga                              |      14 |            517 |        650 |        420 |                  3 |              3 |                   2 |               2 |
| City of Prospect & City Of Port Adelaide Enfield |       6 |            502 |        650 |        340 |                  2 |              4 |                   1 |               2 |
| City Of Salisbury                                |      21 |            494 |        650 |        320 |                  3 |              4 |                   2 |               3 |
| City Of Tea Tree Gully                           |       8 |            550 |        650 |        420 |                  3 |              4 |                   1 |               2 |
| Mount Barker District Council                    |       8 |            523 |        670 |        450 |                  3 |              4 |                   2 |               3 |
| Adelaide Hills Council                           |       3 |            628 |        720 |        495 |                  3 |              4 |                   1 |               2 |
| Light Regional Council                           |       1 |            750 |        750 |        750 |                  5 |              5 |                   3 |               3 |
| City Of Port Adelaide Enfield                    |      29 |            516 |        750 |        290 |                  3 |              3 |                   1 |               3 |
| City Of Marion                                   |      17 |            602 |        790 |        415 |                  3 |              5 |                   2 |               3 |
| City Of West Torrens                             |      10 |            544 |        800 |        370 |                  3 |              4 |                   1 |               2 |
| City Of Charles Sturt                            |      24 |            574 |        900 |        400 |                  3 |              4 |                   1 |               3 |
| City Of Campbelltown                             |      10 |            608 |        900 |        480 |                  3 |              4 |                   2 |               3 |
| Corporation Of The City Of Unley                 |      16 |            633 |       1080 |        395 |                  3 |              4 |                   1 |               2 |
| Corporation Of The City Of Adelaide              |      22 |            564 |       1100 |        200 |                  2 |              3 |                   1 |               2 |
| Corporation Of The Town Of Walkerville           |       5 |            734 |       1200 |        525 |                  4 |              4 |                   2 |               2 |
| City Of Burnside                                 |       9 |            820 |       1280 |        480 |                  3 |              5 |                   2 |               3 |
| City Of Norwood Payneham & St Peters             |      11 |            691 |       1400 |        400 |                  3 |              5 |                   1 |               2 |
| City Of Holdfast Bay                             |       7 |            784 |       1500 |        450 |                  3 |              4 |                   1 |               2 |
## Results

...