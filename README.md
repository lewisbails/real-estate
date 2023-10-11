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
Since 10-09-23\:
| council                                                |   count |   average rent |   max rent |   min rent |   average bedrooms |   max bedrooms |   average bathrooms |   max bathrooms |
|--------------------------------------------------------|---------|----------------|------------|------------|--------------------|----------------|---------------------|-----------------|
| The Barossa Council                                    |       2 |            328 |        355 |        300 |                  2 |              2 |                   1 |               1 |
| Mid Murray Council                                     |       1 |            380 |        380 |        380 |                  3 |              3 |                   1 |               1 |
| Town Of Gawler                                         |       5 |            476 |        550 |        400 |                  3 |              4 |                   2 |               2 |
| City of Prospect & City Of Port Adelaide Enfield       |      11 |            481 |        650 |        325 |                  2 |              4 |                   1 |               2 |
| City Of Playford                                       |      43 |            486 |        620 |        340 |                  3 |              5 |                   2 |               2 |
| City Of Salisbury                                      |      31 |            488 |        650 |        320 |                  3 |              4 |                   1 |               3 |
| City Of Prospect                                       |       3 |            503 |        550 |        440 |                  2 |              2 |                   1 |               1 |
| Mount Barker District Council                          |      11 |            508 |        670 |        420 |                  3 |              4 |                   2 |               3 |
| City Of Onkaparinga                                    |      21 |            522 |        650 |        420 |                  3 |              4 |                   2 |               2 |
| City Of West Torrens                                   |      16 |            525 |        800 |        360 |                  3 |              4 |                   1 |               2 |
| Corporation Of The City Of Adelaide                    |      33 |            547 |       1300 |        195 |                  2 |              3 |                   1 |               2 |
| City Of Port Adelaide Enfield                          |      43 |            552 |       1000 |        290 |                  3 |              6 |                   2 |               3 |
| City Of Tea Tree Gully                                 |      12 |            570 |        740 |        420 |                  3 |              4 |                   1 |               2 |
| City Of Port Adelaide Enfield & City of Tea Tree Gully |       1 |            575 |        575 |        575 |                  4 |              4 |                   2 |               2 |
| City Of Charles Sturt                                  |      40 |            577 |       1400 |          6 |                  3 |              4 |                   1 |               3 |
| Corporation Of The City Of Unley                       |      23 |            585 |       1080 |        350 |                  2 |              4 |                   1 |               2 |
| City Of Mitcham                                        |      10 |            587 |        820 |        320 |                  3 |              5 |                   2 |               3 |
| City Of Campbelltown                                   |      14 |            618 |        900 |        480 |                  3 |              4 |                   2 |               3 |
| City Of Marion                                         |      29 |            629 |       1250 |        330 |                  3 |              5 |                   2 |               3 |
| Adelaide Hills Council                                 |       6 |            659 |        870 |        495 |                  3 |              4 |                   2 |               2 |
| Corporation Of The Town Of Walkerville                 |       5 |            734 |       1200 |        525 |                  4 |              4 |                   2 |               2 |
| City Of Burnside                                       |      14 |            742 |       1280 |        310 |                  3 |              5 |                   2 |               3 |
| Light Regional Council                                 |       1 |            750 |        750 |        750 |                  5 |              5 |                   3 |               3 |
| City Of Holdfast Bay                                   |      14 |            767 |       1900 |        440 |                  3 |              5 |                   1 |               2 |
| City Of Norwood Payneham & St Peters                   |      20 |            782 |       1800 |        330 |                  3 |              5 |                   2 |               2 |
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
  <th>Dep. Variable:</th>          <td>price</td>      <th>  R-squared:         </th> <td>   0.171</td>
</tr>
<tr>
  <th>Model:</th>                   <td>WLS</td>       <th>  Adj. R-squared:    </th> <td>   0.169</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   82.16</td>
</tr>
<tr>
  <th>Date:</th>             <td>Tue, 10 Oct 2023</td> <th>  Prob (F-statistic):</th> <td>5.77e-18</td>
</tr>
<tr>
  <th>Time:</th>                 <td>08:02:59</td>     <th>  Log-Likelihood:    </th> <td>    -inf</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>   400</td>      <th>  AIC:               </th> <td>     inf</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   398</td>      <th>  BIC:               </th> <td>     inf</td>
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
  <th>constant</th> <td>  275.8905</td> <td>   28.248</td> <td>    9.767</td> <td> 0.000</td> <td>  220.357</td> <td>  331.424</td>
</tr>
<tr>
  <th>bed</th>      <td>   87.1731</td> <td>    9.617</td> <td>    9.064</td> <td> 0.000</td> <td>   68.266</td> <td>  106.080</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>474.359</td> <th>  Durbin-Watson:     </th> <td>   1.953</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td>  <th>  Jarque-Bera (JB):  </th> <td>45603.240</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 5.329</td>  <th>  Prob(JB):          </th> <td>    0.00</td> 
</tr>
<tr>
  <th>Kurtosis:</th>      <td>54.212</td>  <th>  Cond. No.          </th> <td>    14.7</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

</pre>

#### Residuals

...

## Conclusions

### Bedrooms

For rental properties in Adelaide, each additional bedroom will add, on average, $87.17 a week. This estimation is independent of dwelling type, location, bathrooms and parking spaces.