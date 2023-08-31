"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import base.usage.v1alpha.usage_pb2
import collections.abc
import grpc
import grpc.aio
import typing

_T = typing.TypeVar('_T')

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta):
    ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore
    ...

class UsageServiceStub:
    """UsageService responds to incoming usage requests."""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Liveness: grpc.UnaryUnaryMultiCallable[
        base.usage.v1alpha.usage_pb2.LivenessRequest,
        base.usage.v1alpha.usage_pb2.LivenessResponse,
    ]
    """Liveness method receives a LivenessRequest message and returns a
    LivenessResponse message.
    See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """
    Readiness: grpc.UnaryUnaryMultiCallable[
        base.usage.v1alpha.usage_pb2.ReadinessRequest,
        base.usage.v1alpha.usage_pb2.ReadinessResponse,
    ]
    """Readiness method receives a ReadinessRequest message and returns a
    ReadinessResponse message.
    See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """
    CreateSession: grpc.UnaryUnaryMultiCallable[
        base.usage.v1alpha.usage_pb2.CreateSessionRequest,
        base.usage.v1alpha.usage_pb2.CreateSessionResponse,
    ]
    """CreateSession method receives a CreateSessionRequest message and returns
    a CreateSessionResponse message.
    """
    SendSessionReport: grpc.UnaryUnaryMultiCallable[
        base.usage.v1alpha.usage_pb2.SendSessionReportRequest,
        base.usage.v1alpha.usage_pb2.SendSessionReportResponse,
    ]
    """SendSessionReport method receives a SendSessionReportRequest message and
    returns a SendSessionReportResponse message.
    """

class UsageServiceAsyncStub:
    """UsageService responds to incoming usage requests."""

    Liveness: grpc.aio.UnaryUnaryMultiCallable[
        base.usage.v1alpha.usage_pb2.LivenessRequest,
        base.usage.v1alpha.usage_pb2.LivenessResponse,
    ]
    """Liveness method receives a LivenessRequest message and returns a
    LivenessResponse message.
    See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """
    Readiness: grpc.aio.UnaryUnaryMultiCallable[
        base.usage.v1alpha.usage_pb2.ReadinessRequest,
        base.usage.v1alpha.usage_pb2.ReadinessResponse,
    ]
    """Readiness method receives a ReadinessRequest message and returns a
    ReadinessResponse message.
    See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
    """
    CreateSession: grpc.aio.UnaryUnaryMultiCallable[
        base.usage.v1alpha.usage_pb2.CreateSessionRequest,
        base.usage.v1alpha.usage_pb2.CreateSessionResponse,
    ]
    """CreateSession method receives a CreateSessionRequest message and returns
    a CreateSessionResponse message.
    """
    SendSessionReport: grpc.aio.UnaryUnaryMultiCallable[
        base.usage.v1alpha.usage_pb2.SendSessionReportRequest,
        base.usage.v1alpha.usage_pb2.SendSessionReportResponse,
    ]
    """SendSessionReport method receives a SendSessionReportRequest message and
    returns a SendSessionReportResponse message.
    """

class UsageServiceServicer(metaclass=abc.ABCMeta):
    """UsageService responds to incoming usage requests."""

    @abc.abstractmethod
    def Liveness(
        self,
        request: base.usage.v1alpha.usage_pb2.LivenessRequest,
        context: _ServicerContext,
    ) -> typing.Union[base.usage.v1alpha.usage_pb2.LivenessResponse, collections.abc.Awaitable[base.usage.v1alpha.usage_pb2.LivenessResponse]]:
        """Liveness method receives a LivenessRequest message and returns a
        LivenessResponse message.
        See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
        """
    @abc.abstractmethod
    def Readiness(
        self,
        request: base.usage.v1alpha.usage_pb2.ReadinessRequest,
        context: _ServicerContext,
    ) -> typing.Union[base.usage.v1alpha.usage_pb2.ReadinessResponse, collections.abc.Awaitable[base.usage.v1alpha.usage_pb2.ReadinessResponse]]:
        """Readiness method receives a ReadinessRequest message and returns a
        ReadinessResponse message.
        See https://github.com/grpc/grpc/blob/master/doc/health-checking.md
        """
    @abc.abstractmethod
    def CreateSession(
        self,
        request: base.usage.v1alpha.usage_pb2.CreateSessionRequest,
        context: _ServicerContext,
    ) -> typing.Union[base.usage.v1alpha.usage_pb2.CreateSessionResponse, collections.abc.Awaitable[base.usage.v1alpha.usage_pb2.CreateSessionResponse]]:
        """CreateSession method receives a CreateSessionRequest message and returns
        a CreateSessionResponse message.
        """
    @abc.abstractmethod
    def SendSessionReport(
        self,
        request: base.usage.v1alpha.usage_pb2.SendSessionReportRequest,
        context: _ServicerContext,
    ) -> typing.Union[base.usage.v1alpha.usage_pb2.SendSessionReportResponse, collections.abc.Awaitable[base.usage.v1alpha.usage_pb2.SendSessionReportResponse]]:
        """SendSessionReport method receives a SendSessionReportRequest message and
        returns a SendSessionReportResponse message.
        """

def add_UsageServiceServicer_to_server(servicer: UsageServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...