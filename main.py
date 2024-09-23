### INF601 - Advanced Programming in Python
### Angel Escalera
### Mini Project 1

import pprint
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import copy
import os


os.makedirs("charts", exist_ok=True)


#Get today's date
today = datetime.now()
#Calculate the date 10 days ago
ten_days_ago = today - timedelta(days=15)

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]



mytickers.sort ()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(start = ten_days_ago, end = today)
    last10days = []
    for date in hist['Close'][:10]:
        last10days.append(date)
    if len(last10days) == 10:

        # maxlist = copy.copy(last10days)
        # maxlist.sort()
        # max_price = maxlist[-1]+10
        # min_price = maxlist[0]-10
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)


        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((10, 1, min_price, max_price ))
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.savefig(f"charts/{ticker}.png")

    else:
        print(f"Failed to download 10 days of data. There are {len(last10days)} days.")