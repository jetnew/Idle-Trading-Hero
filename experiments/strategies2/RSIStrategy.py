import pandas as pd

from ta.utils import dropna
from ta.momentum import RSIIndicator

from .Strategy import Strategy

class RSIStrategy(Strategy):
    def __init__(self, capital, candles, overbought=70, oversold=30):
        self.capital = capital
        self.holdings = 0
        self.candles = []
        self.candleDf = None
        self.overbought = overbought
        self.oversold = oversold
        self.addCandles(candles)

    def acceptCandle(self, candle):
        '''
        accepts a candle and updates current state of strategy to determine buy/sell
        '''
        self.addCandle(candle)

        rsi = RSIIndicator(self.candleDf['C'])
        
        prevRsi = rsi.rsi().iloc[-2]
        currentRsi = rsi.rsi().iloc[-1]

        if currentRsi >= self.oversold and prevRsi < self.oversold:
            self.buy(0.05 * self.capital)
        elif currentRsi <= self.overbought and prevRsi > self.overbought:
            self.sell()

    def buy(self, amountToUse):
        '''
        internal function
        deduct from capital and increase holdings
        amountToUse refers to the amount of money used to buy
        therefore the amount to deduct from capital would be <= amountToUse
        '''

        cost = self.candles[-1]['C']
        numberToBuy = amountToUse // cost
        self.capital -= numberToBuy * cost
        self.holdings += numberToBuy


    def sell(self):
        '''
        internal function
        decrease holdings and add earnings to capital
        sells all holding if any
        '''

        cost = self.candles[-1]['C']
        self.capital += self.holdings * cost
        self.holdings -= self.holdings

    def addCandles(self, candles):
        self.candles += candles
        self.candleDf = pd.DataFrame(self.candles)

    def addCandle(self, candle):
        self.candles.append(candle)
        self.candleDf = pd.DataFrame(self.candles)

    def currentState(self):
        return (self.capital, self.holdings)