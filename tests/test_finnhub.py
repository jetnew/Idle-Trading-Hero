import unittest
from datetime import datetime
from pytz import timezone

from finnhub import Resolution, stock

class TestSum(unittest.TestCase):
    def test_get_candles(self):

        newYorkTz = timezone('America/New_York')

        fromTime = int(datetime(2020, 5, 22, tzinfo=newYorkTz).timestamp())
        toTime = int(datetime(2020, 5, 23, tzinfo=newYorkTz).timestamp())
        json = stock.get_candles('AAPL', Resolution.HOUR1.value, fromTime=fromTime, toTime=toTime)
        self.assertTrue(len(json['c']) == 17)

if __name__ == '__main__':
    unittest.main()