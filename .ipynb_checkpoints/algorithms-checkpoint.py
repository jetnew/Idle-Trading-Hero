import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Algorithm:
    def __init__(self, indicator, strategy, capital):
        self.indicator = indicator  # e.g. pd.DataFrame, AUD-USD
        self.strategy = strategy  # e.g. Strategy, MACDStrategy
        self.capital = capital  # e.g. 1000
        
    def accept(self, observation):
        # Integrate incoming new data
        self.indicator = self.indicator.append(pd.Series(observation), ignore_index=True)
    
    def balance(self):
        # Compute the balance remaining
        self.indicator['balance_change'] = -1 * self.indicator['action'] * self.indicator['O']
        self.indicator['stock'] = self.indicator['action'].cumsum()
        self.indicator['balance'] = self.capital + self.indicator['balance_change'].cumsum()
    
    def performance(self):
        self.indicator['return'] = self.indicator['balance'] - self.capital
        self.indicator['alpha'] = self.indicator['return'] / self.capital
#         self.indicator['beta'] = 
        self.indicator['sharpe'] = self.indicator['return'].mean() / self.indicator['return'].std()
        self.indicator['annual_sharpe'] = 252**0.5 * self.indicator['sharpe']
        self.indicator['sortino'] = self.indicator['return'].mean() / \
                                    self.indicator[self.indicator['return'] < 0]['return'].std()
        
        
    def act(self, observation):
        self.accept(observation)
        self.strategy.action(self.indicator)
        self.balance()
        self.performance()
        
    def statistics(self, k=100):
        return self.indicator.iloc[-1]
    
    def plot_indicators(self, k=100):
        self.strategy.plot(self.indicator, k=k)
        
    def plot_performance(self, k=100):
        ax1 = plt.axes()
        ax1.plot(self.indicator['O'][-k:], label='O', c='r')
        ax1.set_ylabel("Opening")
        plt.legend(loc='best')
        ax2 = ax1.twinx() 
        ax2.plot(self.indicator['balance'][-k:], label='balance')
        ax2.set_ylabel("balance")
        plt.legend(loc='best')
        plt.show()
        
        
from ta.trend import MACD

class MACDStrategy:
    def __init__(self, parameters):
        self.parameters = parameters  # e.g. Dictionary, {'ema26':26, 'ema12':12, 'ema9':9}
        
    def action(self, indicator):
        # Derive the action based on past data
        # action: 1 means buy, -1 means sell, 0 means do nothing
        close = indicator['C']
        macd = MACD(close=close,
                   n_slow=self.parameters['ema26'],
                   n_fast=self.parameters['ema12'],
                   n_sign=self.parameters['ema9'])
        indicator['trend_macd'] = macd.macd()
        indicator['trend_macd_signal'] = macd.macd_signal()
        indicator['trend_macd_diff'] = macd.macd_diff()
        indicator['trend_macd_diff_prev'] = indicator['trend_macd_diff'].shift(1)
        indicator['action'] = (np.sign(indicator['trend_macd_diff']) \
                                    - np.sign(indicator['trend_macd_diff_prev'])) / 2
        
    def plot(self, indicator, k=100):
        plt.plot(indicator['trend_macd'][-k:], label='trend_macd')
        plt.plot(indicator['trend_macd_diff'][-k:], label='trend_macd_diff')
        plt.plot(indicator['trend_macd_signal'][-k:], label='trend_macd_signal')
        plt.legend(loc='best')
        plt.show()
        
        
from ta.volume import MFIIndicator

class MFIStrategy:
    def __init__(self, parameters):
        self.parameters = parameters  # e.g. Dictionary, {'mfi80':80, 'mfi20':20}
        
    def action(self, indicator):
        # Derive the action based on past data
        # action: 1 means buy, -1 means sell, 0 means do nothing
        high, low, close, volume = indicator['H'], indicator['L'], indicator['C'], indicator['Volume']
        indicator['volume_mfi'] = MFIIndicator(high=high, low=low, close=close, volume=volume).money_flow_index()
        indicator['volume_mfi_prev'] = indicator['volume_mfi'].shift(1)
        
        # If 80 -> 79: Sell, If 19 -> 20: Buy
        indicator['sell'] = ((indicator['volume_mfi_prev'] >= self.parameters['mfi80']) & \
                             (indicator['volume_mfi'] < self.parameters['mfi80'])).astype(int)
        indicator['buy'] = ((indicator['volume_mfi_prev'] < self.parameters['mfi20']) & \
                            (indicator['volume_mfi'] >= self.parameters['mfi20'])).astype(int)
        indicator['action'] = indicator['buy'] - indicator['sell']
        
    def plot(self, indicator, k=100):
        plt.plot(indicator['volume_mfi'][-k:], label='volume_mfi')
        plt.legend(loc='best')
        plt.show()
        
        
from ta.momentum import RSIIndicator

class RSIStrategy:
    def __init__(self, parameters):
        self.parameters = parameters  # e.g. Dictionary, {'rsi70': 70, 'rsi30': 30}
        
    def action(self, indicator):
        # Derive the action based on past data
        # action: 1 means buy, -1 means sell, 0 means do nothing
        close = indicator['C']
        indicator['momentum_rsi'] = RSIIndicator(close=close).rsi()
        indicator['momentum_rsi_prev'] = indicator['momentum_rsi'].shift(1)
        
        # If 69 -> 70: Sell, If 30 -> 29: Buy
        indicator['sell'] = ((indicator['momentum_rsi_prev'] < self.parameters['rsi70']) & \
                             (indicator['momentum_rsi'] >= self.parameters['rsi70'])).astype(int)
        indicator['buy'] = ((indicator['momentum_rsi_prev'] >= self.parameters['rsi30']) & \
                            (indicator['momentum_rsi'] < self.parameters['rsi30'])).astype(int)
        indicator['action'] = indicator['buy'] - indicator['sell']
        
    def plot(self, indicator, k=100):
        plt.plot(indicator['momentum_rsi'][-k:], label='momentum_rsi')
        plt.legend(loc='best')
        plt.show()