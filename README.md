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
Since 23-10-23\:
| council                                                |   count |   average rent |   max rent |   min rent |   average bedrooms |   max bedrooms |   average bathrooms |   max bathrooms |
|--------------------------------------------------------|---------|----------------|------------|------------|--------------------|----------------|---------------------|-----------------|
| Town Of Gawler                                         |       7 |            412 |        460 |        360 |                  3 |              3 |                   1 |               2 |
| City Of Playford                                       |      93 |            490 |        750 |        270 |                  3 |              5 |                   2 |               4 |
| City Of Salisbury                                      |      55 |            510 |        900 |        280 |                  3 |              4 |                   1 |               3 |
| City Of Port Adelaide Enfield & City of Tea Tree Gully |       3 |            517 |        600 |        430 |                  2 |              3 |                   1 |               1 |
| City Of Onkaparinga                                    |      45 |            522 |        680 |        345 |                  3 |              5 |                   1 |               2 |
| City Of Port Adelaide Enfield                          |      88 |            531 |        950 |         50 |                  3 |              4 |                   1 |               3 |
| City Of Tea Tree Gully                                 |      34 |            539 |        850 |        400 |                  3 |              4 |                   1 |               2 |
| City Of West Torrens                                   |      53 |            551 |        900 |        310 |                  3 |              5 |                   1 |               3 |
| City Of Marion                                         |      66 |            562 |       1050 |        250 |                  3 |              8 |                   1 |               2 |
| Mount Barker District Council                          |      22 |            565 |       1200 |        410 |                  3 |              5 |                   2 |               2 |
| Corporation Of The City Of Adelaide                    |      63 |            570 |       1400 |        300 |                  2 |              4 |                   1 |               3 |
| City of Prospect & City Of Port Adelaide Enfield       |      10 |            573 |        700 |        440 |                  3 |              4 |                   2 |               2 |
| City Of Campbelltown                                   |      30 |            583 |        800 |        300 |                  3 |              4 |                   1 |               2 |
| City Of Charles Sturt                                  |      91 |            630 |       1500 |        350 |                  3 |              5 |                   2 |               3 |
| City Of Mitcham                                        |      26 |            638 |       1200 |        370 |                  3 |              6 |                   1 |               3 |
| Light Regional Council                                 |       1 |            650 |        650 |        650 |                  4 |              4 |                   2 |               2 |
| Adelaide Hills Council                                 |      20 |            650 |       1400 |        420 |                  3 |              5 |                   2 |               3 |
| Corporation Of The Town Of Walkerville                 |       5 |            655 |        925 |        480 |                  3 |              4 |                   1 |               3 |
| City Of Norwood Payneham & St Peters                   |      50 |            673 |       3000 |        350 |                  3 |              5 |                   1 |               3 |
| Corporation Of The City Of Unley                       |      41 |            675 |       2000 |        300 |                  3 |              4 |                   1 |               4 |
| City Of Prospect                                       |       4 |            678 |       1200 |        400 |                  2 |              3 |                   2 |               2 |
| City Of Holdfast Bay                                   |      34 |            699 |       1400 |        430 |                  3 |              5 |                   2 |               3 |
| City Of Burnside                                       |      41 |            714 |       2300 |        280 |                  3 |              5 |                   2 |               3 |
## Method

### Coarsened Exact Matching

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

## Conclusions

### Bedrooms

For rental properties in Adelaide, each additional bedroom will add, on average, $98 a week. This estimation is independent of dwelling type, location, bathrooms and parking spaces.