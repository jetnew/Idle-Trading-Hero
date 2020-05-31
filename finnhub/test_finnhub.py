from datetime import datetime
from pytz import timezone

from finnhub import Resolution, stock_price

newYorkTz = timezone('America/New_York')

fromTime = int(datetime(2020, 5, 22, tzinfo=newYorkTz).timestamp())
toTime = int(datetime(2020, 5, 23, tzinfo=newYorkTz).timestamp())
json = stock_price.getCandles('AAPL', Resolution.HOUR1.value, fromTime=fromTime, toTime=toTime)
assert len(json['c']) == 16
