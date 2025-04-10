# stock-sim

Takes in data from several different "joke" indicators (i.e Nancy Pelosi Tracker, Inverse Cramer, Donald Trump's Truth Social posts, etc.) and uses this to "buy" specific indexes, stocks, bonds, etc. and record the potential gains from such purchases. Also tracks more standard investments, the US Dollar, and other indexes as well as stock market data at large and then compares results over a period of 10 trading days to see how each index performs against the "regular" stock market.

## Strategy:
- Pull stock market data from yfinance on top indexes (S&P 500, Dow Jones Industrial Average, VTI, the US Dollar, etc.) and a selection of high-performing stocks.
- Using scrapers and/or APIs pull data from Truth Social, Twitter/X, and Capitol Trades and then using this pull stock market data from yfinance based on this.
- Record and store prices of stocks and indexes at the time of them being mentioned on any of the above platforms. (Simulate "buying")
- monitor trends in those prices over a period of 10 trading days.
- Record and store price of above stocks and indexes at market close on the 10th day of tracking (Simulate "selling")
- Analyze % Change and $ Change over the period as well as relative minimum, maximum, mean and median values for each.
- Compare the above to % Change and $ Change in stock market at large.
- Create visualizations based on the above to show how well "joke" indexes/indicators perform in relation to the stock market at large.

## Hypothesis:
- "Joke" indexes/indicators will outperform the stock market at large in the short term.
 
## Potential Other Factors:

There is an irregular amount of uncertainty in the stock market (and economy at large) in both the US and the world right now due to actions taken by the federal government as well as various other factors occuring in the world right now which may cause the stock market, the economy, "stable" and/or "safe" funds/indexes to perform unpredictably as well as potentially causing things like "joke" indexes to perform better than expected.

As this is a very short-term experiment, this data may not be reflective of how these funds will fare in the long term and the results gathered here may not accurately reflect long term market situations and data.


# DISCLAIMER
*NONE OF THE ABOVE IS INVESTMENT OR FINANCIAL ADVICE. THIS SIMULATION IS MADE AS A SHORT TERM EXPERIMENT AND EXCERSIZE IN DATA ANALYSIS. USE THE ABOVE DATA AND METHODS AT YOUR OWN RISK.*
