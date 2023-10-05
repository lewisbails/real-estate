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
| council                                          |   average rent |   max rent |   min rent |   average bedrooms |   max bedrooms |   average bathrooms |   max bathrooms |
|--------------------------------------------------|----------------|------------|------------|--------------------|----------------|---------------------|-----------------|
| The Barossa Council                              |            328 |        355 |        300 |                  2 |              2 |                   1 |               1 |
| Town Of Gawler                                   |            400 |        400 |        400 |                  3 |              3 |                   1 |               1 |
| City Of Mitcham                                  |            392 |        485 |        320 |                  2 |              3 |                   1 |               1 |
| City Of Prospect                                 |            503 |        550 |        440 |                  2 |              2 |                   1 |               1 |
| City Of Playford                                 |            491 |        620 |        340 |                  3 |              5 |                   2 |               2 |
| City Of Salisbury                                |            494 |        650 |        320 |                  3 |              4 |                   2 |               3 |
| City of Prospect & City Of Port Adelaide Enfield |            502 |        650 |        340 |                  2 |              4 |                   1 |               2 |
| City Of Onkaparinga                              |            517 |        650 |        420 |                  3 |              3 |                   2 |               2 |
| City Of Tea Tree Gully                           |            550 |        650 |        420 |                  3 |              4 |                   1 |               2 |
| Mount Barker District Council                    |            523 |        670 |        450 |                  3 |              4 |                   2 |               3 |
| Corporation Of The Town Of Walkerville           |            494 |        695 |          1 |                  4 |              4 |                   2 |               2 |
| Adelaide Hills Council                           |            628 |        720 |        495 |                  3 |              4 |                   1 |               2 |
| Light Regional Council                           |            750 |        750 |        750 |                  5 |              5 |                   3 |               3 |
| City Of Port Adelaide Enfield                    |            516 |        750 |        290 |                  3 |              3 |                   1 |               3 |
| City Of Marion                                   |            602 |        790 |        415 |                  3 |              5 |                   2 |               3 |
| City Of West Torrens                             |            544 |        800 |        370 |                  3 |              4 |                   1 |               2 |
| City Of Campbelltown                             |            608 |        900 |        480 |                  3 |              4 |                   2 |               3 |
| City Of Charles Sturt                            |            574 |        900 |        400 |                  3 |              4 |                   1 |               3 |
| City Of Norwood Payneham & St Peters             |            564 |        950 |          1 |                  3 |              5 |                   1 |               2 |
| Corporation Of The City Of Unley                 |            633 |       1080 |        395 |                  3 |              4 |                   1 |               2 |
| Corporation Of The City Of Adelaide              |            519 |       1100 |          1 |                  2 |              3 |                   1 |               2 |
| City Of Burnside                                 |            678 |       1200 |          1 |                  3 |              5 |                   2 |               3 |
| City Of Holdfast Bay                             |            784 |       1500 |        450 |                  3 |              4 |                   1 |               2 |
## Results

...