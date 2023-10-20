# Causal Inference For Real Estate in Adelaide

![pytest](https://github.com/lewisbails/real-estate/actions/workflows/pytest.yml/badge.svg?event=push&branch=main)
![style](https://github.com/lewisbails/real-estate/actions/workflows/style.yml/badge.svg?event=push&branch=main)

In this study, we aim to estimate the causal effect of the number of bedrooms, number of bathrooms, location, and dwelling type on the weekly rental asking price for properties in Adelaide.

Faced with significant covariate imbalance, simply controlling for confounding variables (e.g. in a OLS regression model) can lead to effect estimates that are sensitive to model specification. Exact matching aims to eliminate this imbalance altogether, but can lead to discarding a large number of observations. This results in not only imprecise treatment effect estimates (larger standard errors), but more importantly in a sample that is not reflective of the population! In this study, we opt for coarsened exact matching, which has the effect of monotonically reducing multidimensional covariate imbalance whilst also maintaining a reasonably-sized and representative sample.

## Setup

```bash
poetry install
```

## Data

An ETL pipeline is run daily to scrape rental listings from various online real estate portals, transform them into a standard `Listing` format, and store them in a NoSQL database (MongoDB).
The pipeline can be ran manually as below:
```bash
poetry run python pipelines/domain_listings.py \
--uri <MONGODB URI> \
--db <DB NAME> \
--collection <COLLECTION NAME> \
--url <DOMAIN URL>
```

## Statistics
Since 20-09-23\:
| council                                                |   count |   average rent |   max rent |   min rent |   average bedrooms |   max bedrooms |   average bathrooms |   max bathrooms |
|--------------------------------------------------------|---------|----------------|------------|------------|--------------------|----------------|---------------------|-----------------|
| Mid Murray Council                                     |       1 |            380 |        380 |        380 |                  3 |              3 |                   1 |               1 |
| The Barossa Council                                    |       4 |            444 |        600 |        300 |                  3 |              4 |                   1 |               2 |
| Town Of Gawler                                         |      10 |            455 |        550 |        400 |                  3 |              4 |                   2 |               3 |
| City Of Playford                                       |      89 |            465 |        620 |        235 |                  3 |              5 |                   2 |               3 |
| City Of Salisbury                                      |      83 |            502 |        850 |        320 |                  3 |              4 |                   1 |               3 |
| City Of Port Adelaide Enfield & City of Tea Tree Gully |       2 |            518 |        575 |        460 |                  4 |              4 |                   2 |               2 |
| City Of Prospect                                       |       6 |            519 |        620 |        405 |                  3 |              5 |                   1 |               3 |
| Mount Barker District Council                          |      27 |            522 |        690 |        340 |                  3 |              4 |                   2 |               3 |
| City Of Onkaparinga                                    |      60 |            528 |        800 |        350 |                  3 |              5 |                   1 |               2 |
| City of Prospect & City Of Port Adelaide Enfield       |      15 |            547 |       1150 |        325 |                  2 |              4 |                   1 |               2 |
| City Of Tea Tree Gully                                 |      37 |            556 |        740 |        390 |                  3 |              4 |                   1 |               2 |
| Corporation Of The City Of Adelaide                    |      62 |            560 |       1300 |        195 |                  2 |              3 |                   1 |               2 |
| City Of West Torrens                                   |      44 |            564 |        850 |        270 |                  3 |              5 |                   1 |               3 |
| City Of Port Adelaide Enfield                          |     103 |            570 |       1600 |        290 |                  3 |              7 |                   2 |               4 |
| Corporation Of The City Of Unley                       |      47 |            578 |       1080 |        340 |                  2 |              4 |                   1 |               2 |
| City Of Charles Sturt                                  |     103 |            595 |       1400 |        195 |                  3 |              4 |                   1 |               3 |
| City Of Campbelltown                                   |      42 |            596 |        900 |        310 |                  3 |              4 |                   2 |               3 |
| City Of Marion                                         |      60 |            610 |       1250 |        330 |                  3 |              5 |                   2 |               3 |
| City Of Mitcham                                        |      26 |            652 |       1980 |        320 |                  3 |              5 |                   2 |               3 |
| Corporation Of The Town Of Walkerville                 |      15 |            667 |       1200 |        420 |                  3 |              4 |                   2 |               3 |
| City Of Holdfast Bay                                   |      27 |            675 |       1900 |        360 |                  3 |              5 |                   1 |               2 |
| Adelaide Hills Council                                 |      20 |            693 |       1400 |        400 |                  3 |              5 |                   1 |               2 |
| City Of Norwood Payneham & St Peters                   |      45 |            693 |       1800 |        330 |                  3 |              5 |                   1 |               2 |
| City Of Burnside                                       |      39 |            708 |       2000 |        310 |                  3 |              6 |                   2 |               4 |
| Light Regional Council                                 |       1 |            750 |        750 |        750 |                  5 |              5 |                   3 |               3 |
## Method

### No Matching

...

### Exact Matching

...

### Coarsened Exact Matching

...

## Results

### Bedrooms

#### Regression

<pre>
<table class="simpletable">
<caption>WLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>          <td>price</td>      <th>  R-squared:         </th> <td>   0.299</td>
</tr>
<tr>
  <th>Model:</th>                   <td>WLS</td>       <th>  Adj. R-squared:    </th> <td>   0.298</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   404.3</td>
</tr>
<tr>
  <th>Date:</th>             <td>Fri, 20 Oct 2023</td> <th>  Prob (F-statistic):</th> <td>3.57e-75</td>
</tr>
<tr>
  <th>Time:</th>                 <td>06:52:28</td>     <th>  Log-Likelihood:    </th> <td>    -inf</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>   950</td>      <th>  AIC:               </th> <td>     inf</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   948</td>      <th>  BIC:               </th> <td>     inf</td>
</tr>
<tr>
  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>     <td> </td>   
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   
</tr>
</table>
<table class="simpletable">
<tr>
      <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>constant</th> <td>  239.9474</td> <td>   14.135</td> <td>   16.976</td> <td> 0.000</td> <td>  212.208</td> <td>  267.687</td>
</tr>
<tr>
  <th>bed</th>      <td>   98.8725</td> <td>    4.917</td> <td>   20.107</td> <td> 0.000</td> <td>   89.223</td> <td>  108.523</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>521.272</td> <th>  Durbin-Watson:     </th> <td>   1.961</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td>  <th>  Jarque-Bera (JB):  </th> <td>20393.910</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 1.842</td>  <th>  Prob(JB):          </th> <td>    0.00</td> 
</tr>
<tr>
  <th>Kurtosis:</th>      <td>25.397</td>  <th>  Cond. No.          </th> <td>    13.2</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
</pre>

#### Residuals

...

## Conclusions

### Bedrooms

For rental properties in Adelaide, each additional bedroom will add, on average, $98 a week. This estimation is independent of dwelling type, location, bathrooms and parking spaces.