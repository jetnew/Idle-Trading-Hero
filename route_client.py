import grpc

import route_pb2
import route_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = route_pb2_grpc.RouteStub(channel)

from google.protobuf.struct_pb2 import Struct
params = Struct()
params.update({
    'ema26': 26,
    'ema12': 12,
    'ema9': 9,
})

Selection = route_pb2.Selection(Instrument='AUD_USD',
                                Granularity='S5',
                                 Strategy='MACD',
                                 Parameters=params,
                                 Capital=1000,
                                 ID="1")
statistics = stub.InitialiseAlgorithm(Selection)
print(statistics)

Tmp = route_pb2.Tmp(tmp=1)
stub.Act(Tmp)  # MUST RUN ACT BEFORE CALLING GET FUNCTIONS

Length = route_pb2.Length(Length=10,
                          ID="1")
data = stub.GetData(Length)
indicators = stub.GetIndicators(Length)
performances = stub.GetPerformances(Length)

statistics = stub.GetStatistics(Tmp)
print(data)
print(indicators)
print(performances)
print(statistics)