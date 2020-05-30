import os
from enum import Enum

BASE_URL = 'https://finnhub.io/api/v1'
token = os.getenv('FinnhubApiKey')

class Resolution(Enum):
    MIN1 = '1'
    MIN5 = '5'
    MIN15 = '15'
    MIN30 = '30'
    HOUR1 = '60'
    DAY = 'D'
    WEEK = 'W'
    MONTH = 'M'

def addToken(url, isFirst=False):
    if isFirst: 
        return f'{url}?token={token}'
    
    return f'{url}&token={token}'

def fillNoDataCandles(data):
    data['c'] = []
    data['h'] = []
    data['l'] = []
    data['o'] = []
    data['t'] = []
    data['v'] = []