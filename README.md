
With `yfinance`, if you do the following:

```
import yfinance as yf

df = yf.download(tickers='^GSPC')
```

you'll download all the data for the S&P 500.

Later on, if you repeat the same steps to get new data, it will download all data again.

With `yfinance_download`, all the data is only downloaded the first time. The data is serialized into a pkl file. Subsequent calls to download the data only request recent data (data since 2nd most recent date).

After running the following:

```
import yfinance_download

df = yfinance_download.update_records('^GSPC')
```

you should have a file `pkl/^GSPC-1d.pkl` which stores the serialized data.

To select a `1mo` interval:

```
df = yfinance_download.update_records('^GSPC', interval='1mo')
```

You should then see a file `pkl/^GSPC-1mo.pkl`
