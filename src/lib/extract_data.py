"File used for extracting stock market information from yfinance"

import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft.info)