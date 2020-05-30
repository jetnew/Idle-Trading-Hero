import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

with open('data/data2/AUD_USD-1588780800-H1-10000.json') as f:
    data = json.load(f)
d = {r: [dic[r] for dic in data] for r in data[0]}
df = pd.DataFrame(d)
#================= TODO: ENABLE CHOICE OF DATASET ===================

import time
import logging
from algorithms import *

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
        self.req_strat = request.Strategy
        self.req_params = request.Parameters
        self.req_capital = request.Capital
        
        self.strategy = Strategies[self.req_strat](parameters=self.req_params)
        self.algorithm = Algorithm(indicator=df.loc[:100],
                                   strategy=self.strategy,
                                   capital=self.req_capital)
        self.algorithm.act(df.loc[100])
        return route_pb2.Statistics(**self.algorithm.statistics())
    
    def GetStatistics(self, request, context):
        return route_pb2.Statistics(**self.algorithm.statistics())
    
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