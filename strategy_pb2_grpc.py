# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import strategy_pb2 as strategy__pb2


class StrategyServiceStub(object):
    """Template
    rpc Function(Request) returns (Message) {}
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitialiseAlgorithm = channel.unary_unary(
                '/strategy_proto.StrategyService/InitialiseAlgorithm',
                request_serializer=strategy__pb2.Selection.SerializeToString,
                response_deserializer=strategy__pb2.Statistics.FromString,
                )
        self.StartAlgorithm = channel.unary_unary(
                '/strategy_proto.StrategyService/StartAlgorithm',
                request_serializer=strategy__pb2.StartAlgorithmParam.SerializeToString,
                response_deserializer=strategy__pb2.StartAlgorithmResponse.FromString,
                )
        self.StopAlgorithm = channel.unary_unary(
                '/strategy_proto.StrategyService/StopAlgorithm',
                request_serializer=strategy__pb2.StopAlgorithmParam.SerializeToString,
                response_deserializer=strategy__pb2.StopAlgorithmResponse.FromString,
                )
        self.Act = channel.unary_unary(
                '/strategy_proto.StrategyService/Act',
                request_serializer=strategy__pb2.Tmp.SerializeToString,
                response_deserializer=strategy__pb2.Statistics.FromString,
                )
        self.GetStatistics = channel.unary_unary(
                '/strategy_proto.StrategyService/GetStatistics',
                request_serializer=strategy__pb2.Tmp.SerializeToString,
                response_deserializer=strategy__pb2.Statistics.FromString,
                )
        self.GetData = channel.unary_unary(
                '/strategy_proto.StrategyService/GetData',
                request_serializer=strategy__pb2.HistoryParams.SerializeToString,
                response_deserializer=strategy__pb2.History.FromString,
                )
        self.GetIndicators = channel.unary_unary(
                '/strategy_proto.StrategyService/GetIndicators',
                request_serializer=strategy__pb2.HistoryParams.SerializeToString,
                response_deserializer=strategy__pb2.History.FromString,
                )
        self.GetPerformances = channel.unary_unary(
                '/strategy_proto.StrategyService/GetPerformances',
                request_serializer=strategy__pb2.HistoryParams.SerializeToString,
                response_deserializer=strategy__pb2.History.FromString,
                )


class StrategyServiceServicer(object):
    """Template
    rpc Function(Request) returns (Message) {}
    """

    def InitialiseAlgorithm(self, request, context):
        """Initialise indicator, strategy, parameters
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartAlgorithm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopAlgorithm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Act(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatistics(self, request, context):
        """Get statistics
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetData(self, request, context):
        """Get past data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIndicators(self, request, context):
        """Get past indicators
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPerformances(self, request, context):
        """Get past performances
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StrategyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitialiseAlgorithm': grpc.unary_unary_rpc_method_handler(
                    servicer.InitialiseAlgorithm,
                    request_deserializer=strategy__pb2.Selection.FromString,
                    response_serializer=strategy__pb2.Statistics.SerializeToString,
            ),
            'StartAlgorithm': grpc.unary_unary_rpc_method_handler(
                    servicer.StartAlgorithm,
                    request_deserializer=strategy__pb2.StartAlgorithmParam.FromString,
                    response_serializer=strategy__pb2.StartAlgorithmResponse.SerializeToString,
            ),
            'StopAlgorithm': grpc.unary_unary_rpc_method_handler(
                    servicer.StopAlgorithm,
                    request_deserializer=strategy__pb2.StopAlgorithmParam.FromString,
                    response_serializer=strategy__pb2.StopAlgorithmResponse.SerializeToString,
            ),
            'Act': grpc.unary_unary_rpc_method_handler(
                    servicer.Act,
                    request_deserializer=strategy__pb2.Tmp.FromString,
                    response_serializer=strategy__pb2.Statistics.SerializeToString,
            ),
            'GetStatistics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatistics,
                    request_deserializer=strategy__pb2.Tmp.FromString,
                    response_serializer=strategy__pb2.Statistics.SerializeToString,
            ),
            'GetData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=strategy__pb2.HistoryParams.FromString,
                    response_serializer=strategy__pb2.History.SerializeToString,
            ),
            'GetIndicators': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIndicators,
                    request_deserializer=strategy__pb2.HistoryParams.FromString,
                    response_serializer=strategy__pb2.History.SerializeToString,
            ),
            'GetPerformances': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPerformances,
                    request_deserializer=strategy__pb2.HistoryParams.FromString,
                    response_serializer=strategy__pb2.History.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'strategy_proto.StrategyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StrategyService(object):
    """Template
    rpc Function(Request) returns (Message) {}
    """

    @staticmethod
    def InitialiseAlgorithm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strategy_proto.StrategyService/InitialiseAlgorithm',
            strategy__pb2.Selection.SerializeToString,
            strategy__pb2.Statistics.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartAlgorithm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strategy_proto.StrategyService/StartAlgorithm',
            strategy__pb2.StartAlgorithmParam.SerializeToString,
            strategy__pb2.StartAlgorithmResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopAlgorithm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strategy_proto.StrategyService/StopAlgorithm',
            strategy__pb2.StopAlgorithmParam.SerializeToString,
            strategy__pb2.StopAlgorithmResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Act(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strategy_proto.StrategyService/Act',
            strategy__pb2.Tmp.SerializeToString,
            strategy__pb2.Statistics.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatistics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strategy_proto.StrategyService/GetStatistics',
            strategy__pb2.Tmp.SerializeToString,
            strategy__pb2.Statistics.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strategy_proto.StrategyService/GetData',
            strategy__pb2.HistoryParams.SerializeToString,
            strategy__pb2.History.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIndicators(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strategy_proto.StrategyService/GetIndicators',
            strategy__pb2.HistoryParams.SerializeToString,
            strategy__pb2.History.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPerformances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/strategy_proto.StrategyService/GetPerformances',
            strategy__pb2.HistoryParams.SerializeToString,
            strategy__pb2.History.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
