import unittest
from datetime import datetime
from pytz import timezone
import json

from finnhub import Resolution, stock

newYorkTz = timezone('America/New_York')

symbol = 'AMZN'
fromDate = datetime(2000, 1, 3, tzinfo=newYorkTz)
toDate = datetime(2020, 5, 25, tzinfo=newYorkTz)
fromDateUnix = int(fromDate.timestamp())
toDateUnix = int(toDate.timestamp())
data = stock.get_candles(symbol, Resolution.HOUR1.value, fromTime=fromDateUnix, toTime=toDateUnix)

fromDateString = fromDate.strftime('%Y%m%d')
toDateString = toDate.strftime('%Y%m%d')
with open(f'./data/data3/candles/{symbol}-{fromDateString}-{toDateString}.json', 'w') as f:
    json.dump(data, f)