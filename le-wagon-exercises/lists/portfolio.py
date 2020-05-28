# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]

fb_stock_count = portfolio[3][0]
print(fb_stock_count)

#            AAPL     GOOG    TSLA      FB
market = [ 198.84, 1217.93, 267.66, 179.06 ]
    

# 1st try
pnl = 0
counter = 0
for volume, strike_price in portfolio:
    pnl = pnl + ((volume*market[counter])-(volume*strike_price))
    counter += 1
print(round(pnl,1))


# Better:
pnl2 = 0
for index, value in enumerate(portfolio):
    pnl2 += portfolio[index][0]* (market[index] - portfolio[index][1])
print(round(pnl2,1))

