import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import asyncio

df_aapl = pd.read_json("data/data3/candles/AAPL-20000103-20200525.json")
df_googl = pd.read_json("data/data3/candles/GOOGL-20040819-20200525.json")
df_spy = pd.read_json("data/data3/candles/SPY-20000103-20200525.json")
df_voo = pd.read_json("data/data3/candles/VOO-20100909-20200525.json")

import time
import logging
from algorithms import *

import yaml
import oandapyV20

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
access_token = config["access_token"]
accountID = config["accountID"]

from oanda import Oanda

oanda = Oanda(accountID, access_token)

from concurrent import futures
import grpc
import strategy_pb2
import strategy_pb2_grpc

Strategies = {
    "macd": MACDStrategy,
    "mfi": MFIStrategy,
    "rsi": RSIStrategy,
}

import threading


def runAlgorithm(algorithm):
    while algorithm.is_active:
        algorithm.act()
        time.sleep(5)


class StrategyService(strategy_pb2_grpc.StrategyServiceServicer):
    def __init__(self):
        self.algorithm_dict = {}
        self.oanda = Oanda(accountID, access_token)

    def InitialiseAlgorithm(self, request, context):
        strategy_id = request.ID
        # asset = request.Asset
        strategy_type = request.Strategy
        strategy_params = request.Parameters
        capital = request.Capital
        instrument = request.Instrument
        granularity = request.Granularity

        strategy = Strategies[strategy_type](parameters=strategy_params)

        algorithm = Algorithm(
            strategy_id=strategy_id,
            oanda=self.oanda,
            instrument=instrument,
            granularity=granularity,
            strategy=strategy,
            capital=capital,
        )

        self.algorithm_dict[strategy_id] = algorithm

        return strategy_pb2.Statistics(**algorithm.statistics())

    def StartAlgorithm(self, request, context):
        strategy_id = request.ID

        algorithm = self.algorithm_dict[strategy_id]

        if algorithm.is_active:
            return

        print(f"Creating thread for strategy {algorithm.id}")
        algoThread = threading.Thread(target=runAlgorithm, args=(algorithm,))
        print(f"Starting strategy {algorithm.id}")

        try:
            algorithm.is_active = True
            algoThread.start()
        except e:
            return strategy_pb2.StartAlgorithmResponse(Error=str(e))

        return strategy_pb2.StartAlgorithmResponse(Error=None)

    def StopAlgorithm(self, request, context):
        strategy_id = request.ID

        algorithm = self.algorithm_dict[strategy_id]

        algorithm.is_active = False

        return strategy_pb2.StopAlgorithmResponse(Error=None)

    def Act(self, request, context):
        strategy_id = request.ID

        algorithm = self.algorithm_dict[strategy_id]
        algorithm.act()

        return strategy_pb2.Statistics(**algorithm.statistics())

    def GetStatistics(self, request, context):
        strategy_id = request.ID

        algorithm = self.algorithm_dict[strategy_id]

        return strategy_pb2.Statistics(**algorithm.statistics())

    def GetData(self, request, context):
        strategy_id = request.ID
        k = request.Length

        algorithm = self.algorithm_dict[strategy_id]

        columns = algorithm.data_col
        matrix = algorithm.indicator[columns].values[-k:, :].T.tolist()
        TS = [
            strategy_pb2.TimeSeries(Key=columns[i], Value=matrix[i])
            for i in range(len(columns))
        ]
        return strategy_pb2.History(TS=TS)

    def GetIndicators(self, request, context):
        strategy_id = request.ID
        k = request.Length

        algorithm = self.algorithm_dict[strategy_id]

        columns = algorithm.strategy.indicator_col[:]
        columns.append("t")
        matrix = algorithm.indicator[columns].values[-k:, :].T.tolist()
        TS = [
            strategy_pb2.TimeSeries(Key=columns[i], Value=matrix[i])
            for i in range(len(columns))
        ]
        return strategy_pb2.History(TS=TS)

    def GetPerformances(self, request, context):
        """Get performance history"""
        strategy_id = request.ID
        k = request.Length

        algorithm = self.algorithm_dict[strategy_id]

        columns = algorithm.performance_col[:]
        print(k, columns)
        columns.append("t")
        matrix = algorithm.indicator[columns].values[-k:, :].T.tolist()
        print(matrix)
        TS = [
            strategy_pb2.TimeSeries(Key=columns[i], Value=matrix[i])
            for i in range(len(columns))
        ]
        print(TS)
        return strategy_pb2.History(TS=TS)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    strategy_pb2_grpc.add_StrategyServiceServicer_to_server(StrategyService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("started")

    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print()
    finally:
        loop.close()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
