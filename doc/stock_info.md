# Sources of stock information

Finding free stock information is hard since Yahoo and Google Finance APIs died. Free sources tend to be limited to current and historical stock info so we will need separate sources for company profiles, dividend distribution data, etc.

## Free APIs

If you have an account at any financial trading institution, you probably have free API access through your account.

### E*Trade

If you have an E*Trade account (doesn't need to be funded), you can get free access to their APIs. See instruction under "Requesting keys" on [this page](https://developer.etrade.com/ctnt/dev-portal/getArticleByCategory?category=Documentation)

### [Alpha Vantage](https://www.alphavantage.co/)

**API Key**: [Free](https://www.alphavantage.co/support/#api-key)
**Attribution**: ???

* Focuses on Stock time series, Foreign Exchange, Cryptocurrencies, and provides many technical indicators.
* Python library [doc](https://alpha-vantage.readthedocs.io/en/latest/source/alpha_vantage.html)

TIME_SERIES_DAILY_ADJUSTED provides dividend and split info, but the dividend info is only available on the dividend issue date - we would need a source for that info.

```
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=ctl&apikey=YOUR_KEY

"2018-08-30": {
    "1. open": "21.8300",
    "2. high": "21.8900",
    "3. low": "21.3500",
    "4. close": "21.6800",
    "5. adjusted close": "21.6800",
    "6. volume": "13840811",
    "7. dividend amount": "0.5400",
    "8. split coefficient": "1.0000"
},
```

Notes:

* [Dividends and Adjuted close](https://www.alpha-vantage.community/post/adjusted-close-and-dividends-9732269)

### [IEX Trading](https://iextrading.com/)

**API Key**: None
**Attribution**: Required if you redistribute API data: See [Attribution here](https://iextrading.com/developer/docs/#terms).

They have a dedicated dividends API, but when I checked (url below), it was 2 quarters behind.

Example GET `https://api.iextrading.com/1.0/stock/aapl/dividends/1y`
Developer site is [here](https://iextrading.com/developer/)


### [Quantopian](https://www.quantopian.com/)

Focuses on quantitative stock analysis, let's you develop stragies and try to partner with Quantopian by them funding your algorithms and paying a royalty on your IP - and they also provide 56 free data feeds.

Data set list is [here](https://www.quantopian.com/data)

### [Barchart OnDemand](https://www.barchart.com/ondemand/api)

Free data signup is [here](https://www.barchart.com/ondemand/free-market-data-api)

From [https://www.barchart.com/ondemand/free-market-data-api/faq](https://www.barchart.com/ondemand/free-market-data-api/faq), extracted:

> Barchart’s free market data API only allows for both getQuote and getHistory APIs. Any additional APIs require a paid subscription to Barchart OnDemand. For pricing, please contact solutions@barchart.com
>
> The free market data API includes data from AMEX, NYSE, NASDAQ in end of day frequency. Cboe BZX Exchange equity and Forex data is included on a 15-minute delay.
> 
> You are limited to end of day US stocks and futures with the free market data API.
> 
> No indices, mutual funds, futures, equity options
> 
> Every user is able to make 400 getQuote queries and 150 getHistory queries per day.

Looks like they have a robust dividend api - but only on a paid subscription.

### [Quandl](https://www.quandl.com/)

An information broker with many [free sources](https://www.quandl.com/search?filters=%5B%22United%20States%22%2C%22Free%22%5D) focusing on financial research but including diverse topics like Fed economic data, US and BP energy production/consumption, World bank gender stats, international tourism, etc.

### [Intrinio](https://intrinio.com/)

**API Key**: Developer program provides six months free data

Intrinio provides info for US Public Companies (11.5K), Securities (10K), and data tags like rations, metrics, properties (4K).


### Lists

Lists of stock api providers:

* From Feb 2018 - [a list of 10](https://www.quantshare.com/sa-620-10-new-ways-to-download-historical-stock-quotes-for-free).
* From 2013 - [96 Stocks APIs (world)](https://www.programmableweb.com/news/96-stocks-apis-bloomberg-nasdaq-and-etrade/2013/05/22). Many are no longer available and the new ones are not listed.



