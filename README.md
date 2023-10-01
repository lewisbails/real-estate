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

## Data Exploration

...

## Modelling

...

## Results

...

## Conclusions

...