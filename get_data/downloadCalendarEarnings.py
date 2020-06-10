from datetime import datetime
from pytz import timezone
from yahoo_earnings_calendar import YahooEarningsCalendar
import json


newYorkTz = timezone('America/New_York')

symbol = 'AAPL'
fromDate = datetime(2010, 1, 1, tzinfo=newYorkTz)
toDate = datetime(2020, 6, 9, tzinfo=newYorkTz)
fromDateFormat = fromDate.strftime('%Y-%m-%d')
toDateFormat = toDate.strftime('%Y-%m-%d')

yec = YahooEarningsCalendar()

data = yec.get_earnings_of(symbol)

with open(f'./data/data3/earnings/{symbol}.json', 'w') as f:
    json.dump(data, f)
