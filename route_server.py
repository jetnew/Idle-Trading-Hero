import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

df_aapl = pd.read_json('data/data3/candles/AAPL-20000103-20200525.json')
df_googl = pd.read_json('data/data3/candles/GOOGL-20040819-20200525.json')
df_spy = pd.read_json('data/data3/candles/SPY-20000103-20200525.json')
df_voo = pd.read_json('data/data3/candles/VOO-20100909-20200525.json')

import time
import logging
from algorithms import *

import yaml
import oandapyV20
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
access_token = config['access_token']
accountID = config['accountID']

from oanda import Oanda
oanda = Oanda(accountID, access_token)

from concurrent import futures
import grpc
import route_pb2
import route_pb2_grpc

Strategies = {
    'MACD': MACDStrategy,
    'MFI': MFIStrategy,
    'RSI': RSIStrategy,
}

class RouteServicer(route_pb2_grpc.RouteServicer):
    def InitialiseAlgorithm(self, request, context):
        self.req_asset = request.Asset
        self.req_strat = request.Strategy
        self.req_params = request.Parameters
        self.req_capital = request.Capital
        self.req_instrument = request.Instrument
        self.req_granularity = request.Granularity
        
        self.strategy = Strategies[self.req_strat](parameters=self.req_params)
        self.oanda = Oanda(accountID, access_token)
        self.algorithm = Algorithm(
            oanda=oanda,
            instrument=self.req_instrument,
            granularity=self.req_granularity,
            strategy=self.strategy,
            capital=self.req_capital)
        return route_pb2.Statistics(**self.algorithm.statistics())
    
    def Act(self, request, context):
        self.algorithm.act()
        return route_pb2.Statistics(**self.algorithm.statistics())
    
    def GetStatistics(self, request, context):
        return route_pb2.Statistics(**self.algorithm.statistics())
    
    def GetData(self, request, context):
        k = request.Length
        columns = self.algorithm.data_col
        matrix = self.algorithm.indicator[columns].values[-k:,:].T.tolist()
        TS = [route_pb2.TimeSeries(Key=columns[i],
                                   Value=matrix[i])
              for i in range(len(columns))]
        return route_pb2.History(TS=TS) 
    
    def GetIndicators(self, request, context):
        k = request.Length
        columns = self.algorithm.strategy.indicator_col
        matrix = self.algorithm.indicator[columns].values[-k:,:].T.tolist()
        TS = [route_pb2.TimeSeries(Key=columns[i],
                                   Value=matrix[i])
              for i in range(len(columns))]
        return route_pb2.History(TS=TS)
    
    def GetPerformances(self, request, context):
        """Get performance history"""
        k = request.Length
        columns = self.algorithm.performance_col
        matrix = self.algorithm.indicator[columns].values[-k:,:].T.tolist()
        TS = [route_pb2.TimeSeries(Key=columns[i],
                                   Value=matrix[i])
              for i in range(len(columns))]
        return route_pb2.History(TS=TS)
        
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_pb2_grpc.add_RouteServicer_to_server(
        RouteServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    time.sleep(1000)
    
    
if __name__ == "__main__":
    logging.basicConfig()
    serve()