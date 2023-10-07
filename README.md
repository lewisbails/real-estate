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
## Method

### No Matching

...

### Exact Matching

...

### Coarsened Exact Matching

...

#### Council

...

#### Bathrooms

...

#### Parking

...

## Results

### Bedrooms

<pre>
<table class="simpletable">
<caption>WLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>          <td>price</td>      <th>  R-squared:         </th> <td>   0.086</td>
</tr>
<tr>
  <th>Model:</th>                   <td>WLS</td>       <th>  Adj. R-squared:    </th> <td>   0.083</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   27.68</td>
</tr>
<tr>
  <th>Date:</th>             <td>Sat, 07 Oct 2023</td> <th>  Prob (F-statistic):</th> <td>2.76e-07</td>
</tr>
<tr>
  <th>Time:</th>                 <td>21:03:26</td>     <th>  Log-Likelihood:    </th> <td>    -inf</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>   297</td>      <th>  AIC:               </th> <td>     inf</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   295</td>      <th>  BIC:               </th> <td>     inf</td>
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
  <th>constant</th> <td>  370.5619</td> <td>   39.460</td> <td>    9.391</td> <td> 0.000</td> <td>  292.904</td> <td>  448.220</td>
</tr>
<tr>
  <th>bed</th>      <td>   71.3951</td> <td>   13.570</td> <td>    5.261</td> <td> 0.000</td> <td>   44.688</td> <td>   98.102</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>408.078</td> <th>  Durbin-Watson:     </th> <td>   1.982</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td>  <th>  Jarque-Bera (JB):  </th> <td>68528.996</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 6.288</td>  <th>  Prob(JB):          </th> <td>    0.00</td> 
</tr>
<tr>
  <th>Kurtosis:</th>      <td>76.345</td>  <th>  Cond. No.          </th> <td>    14.4</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
</pre>

## Conclusions

### Bedrooms

For rental properties in Adelaide, each additional bedroom will add, on average, $71.39 a week. This controls for dwelling type, location, bathrooms and parking spaces.

### Council

...

### Bathrooms

...

### Parking

...