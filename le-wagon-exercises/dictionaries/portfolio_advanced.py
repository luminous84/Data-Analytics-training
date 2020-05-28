# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

portfolio = {
  "AAPL": {
    "volume": 10,
    "strike": 154.12
  },
  "GOOG": {
    "volume": 2,
    "strike": 812.56
  },
  "TSLA": {
    "volume": 12,
    "strike": 342.12
  },
  "FB": {
    "volume": 18,
    "strike": 209.0
  }
}


market = {
    "AAPL": 198.84 ,
    "GOOG": 1217.93,
    "TSLA": 267.66 ,
    "FB"  : 179.06 
}


print(portfolio['TSLA']['volume'])
print(portfolio['GOOG']['strike'])


pnl = 0
for key, value in portfolio.items():   
    pnl += value["volume"]* (market[key] - portfolio[key]["strike"])
print(round(pnl,1))

