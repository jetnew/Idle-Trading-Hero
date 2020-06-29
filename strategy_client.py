import time
import threading

import grpc

import strategy_pb2
import strategy_pb2_grpc

from google.protobuf.struct_pb2 import Struct


def testRunStrategy(strategy_id):

    channel = grpc.insecure_channel("localhost:50051")
    stub = strategy_pb2_grpc.StrategyServiceStub(channel)

    params = Struct()
    params.update(
        {"ema26": 26, "ema12": 12, "ema9": 9,}
    )

    selection = strategy_pb2.Selection(
        ID=strategy_id,
        Instrument="AUD_USD",
        Granularity="S5",
        Strategy="MACD",
        Parameters=params,
        Capital=1000,
    )
    statistics = stub.InitialiseAlgorithm(selection)
    print(strategy_id, statistics)

    tmp = strategy_pb2.Tmp(ID=strategy_id, tmp=1)
    # stub.Act(tmp)  # MUST RUN ACT BEFORE CALLING GET FUNCTIONS

    start_algo_param = strategy_pb2.StartAlgorithmParam(ID=strategy_id)

    start_algo_res = stub.Start(start_algo_param)

    if start_algo_res.Error != "":
        print(strategy_id, "failed to start", start_algo_res.Error)

    time.sleep(30)

    stop_algo_param = strategy_pb2.StopAlgorithmParam(ID=strategy_id)

    stop_algo_res = stub.Stop(stop_algo_param)

    if stop_algo_res.Error != "":
        print(strategy_id, "failed to stop", stop_algo_res.Error)
        return

    history_params = strategy_pb2.HistoryParams(ID=strategy_id, Length=10)
    data = stub.GetData(history_params)
    indicators = stub.GetIndicators(history_params)
    performances = stub.GetPerformances(history_params)
    statistics = stub.GetStatistics(tmp)

    print(strategy_id, data)
    print(strategy_id, indicators)
    print(strategy_id, performances)
    print(strategy_id, statistics)


if __name__ == "__main__":
    t1 = threading.Thread(target=testRunStrategy, args=("test1",))
    t1.start()
    time.sleep(2)
    t2 = threading.Thread(target=testRunStrategy, args=("test2",))
    t2.start()
