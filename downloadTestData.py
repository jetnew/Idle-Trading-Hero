from datetime import datetime
from pytz import timezone
import os
import json
import logging

from finnhub import Resolution, stock_price

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LogLevel", "INFO"))

def prependCandleDicts(cd1, cd2):
    '''
        preoend cd2 to cd1
    '''
    cd1['c'] = cd2['c'] + cd1['c']
    cd1['h'] = cd2['h'] + cd1['h']
    cd1['l'] = cd2['l'] + cd1['l']
    cd1['o'] = cd2['o'] + cd1['o']
    cd1['t'] = cd2['t'] + cd1['t']
    cd1['v'] = cd2['v'] + cd1['v']

def downloadStock(symbol, resolution, fromDateTime, toDateTime):
    dateFormat = '%Y%m%d'
    fromDateString = fromDateTime.strftime(dateFormat)
    toDateString = toDateTime.strftime(dateFormat)
    log.info(f'downloading {symbol}, resolution: {resolution.name}, from: {fromDateString}, to: {toDateString}')

    fromTime = int(fromDateTime.timestamp())
    toTime = int(toDateTime.timestamp())

    log.info(f'getting {fromTime} - {toTime}')
    stockJson = stock_price.getCandles(symbol, resolution.value, fromTime=fromTime, toTime=toTime)

    toTime2 = None

    while stockJson['t'][0] > fromTime:
        toTime2 = stockJson['t'][0]
        log.info(f'getting {fromTime} - {toTime2}')
        nextStockJson = stock_price.getCandles(symbol, Resolution.HOUR1.value, fromTime=fromTime, toTime=toTime2)
        if len(nextStockJson['t']) < 1:
            break

        if stockJson['t'][0] == nextStockJson['t'][-1]:
            nextStockJson['c'].pop()
            nextStockJson['h'].pop()
            nextStockJson['l'].pop()
            nextStockJson['o'].pop()
            nextStockJson['t'].pop()
            nextStockJson['v'].pop()
        
        prependCandleDicts(stockJson, nextStockJson)

    log.info(f'Stopped at {toTime2}')

    finalFromDateString = fromDateString

    if toTime2 != toTime:
        log.warning(f'Incomplete time period')
        finalFromDateString = datetime.fromtimestamp(toTime2, tz=toDateTime.tzinfo).strftime(dateFormat)


    filepath = f'data/{symbol}-{finalFromDateString}-{toDateString}.json'
    log.info(f'dumping to {filepath}')
    with open(filepath, 'w') as stockFile:
        json.dump(stockJson, stockFile)

if __name__ == "__main__":
    newYorkTz = timezone('America/New_York')

    fromDateTime = datetime(2000, 1, 3, tzinfo=newYorkTz)
    toDateTime = datetime(2020, 5, 25, tzinfo=newYorkTz)

    # downloadStock('AAPL', Resolution.HOUR1, fromDateTime, toDateTime)
    # downloadStock('VOO', Resolution.HOUR1, fromDateTime, toDateTime)
    # downloadStock('SPY', Resolution.HOUR1, fromDateTime, toDateTime)
    # downloadStock('GOOGL', Resolution.HOUR1, fromDateTime, toDateTime)