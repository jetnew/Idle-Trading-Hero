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

Selection = route_pb2.Selection(Asset='AAPL',
                                 Strategy='MACD',
                                 Parameters=params,
                                 Capital=1000)
statistics = stub.InitialiseAlgorithm(Selection)
print(statistics)

HistoryLength = route_pb2.HistoryLength(Length=10)
history = stub.GetHistory(HistoryLength)
print(history)