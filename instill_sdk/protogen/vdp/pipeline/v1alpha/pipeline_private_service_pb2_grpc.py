# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vdp.pipeline.v1alpha import operator_definition_pb2 as vdp_dot_pipeline_dot_v1alpha_dot_operator__definition__pb2
from vdp.pipeline.v1alpha import pipeline_pb2 as vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2


class PipelinePrivateServiceStub(object):
    """Pipeline service responds to internal access
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPipelinesAdmin = channel.unary_unary(
                '/vdp.pipeline.v1alpha.PipelinePrivateService/ListPipelinesAdmin',
                request_serializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelinesAdminRequest.SerializeToString,
                response_deserializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelinesAdminResponse.FromString,
                )
        self.LookUpPipelineAdmin = channel.unary_unary(
                '/vdp.pipeline.v1alpha.PipelinePrivateService/LookUpPipelineAdmin',
                request_serializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.LookUpPipelineAdminRequest.SerializeToString,
                response_deserializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.LookUpPipelineAdminResponse.FromString,
                )
        self.LookUpOperatorDefinitionAdmin = channel.unary_unary(
                '/vdp.pipeline.v1alpha.PipelinePrivateService/LookUpOperatorDefinitionAdmin',
                request_serializer=vdp_dot_pipeline_dot_v1alpha_dot_operator__definition__pb2.LookUpOperatorDefinitionAdminRequest.SerializeToString,
                response_deserializer=vdp_dot_pipeline_dot_v1alpha_dot_operator__definition__pb2.LookUpOperatorDefinitionAdminResponse.FromString,
                )
        self.ListPipelineReleasesAdmin = channel.unary_unary(
                '/vdp.pipeline.v1alpha.PipelinePrivateService/ListPipelineReleasesAdmin',
                request_serializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelineReleasesAdminRequest.SerializeToString,
                response_deserializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelineReleasesAdminResponse.FromString,
                )


class PipelinePrivateServiceServicer(object):
    """Pipeline service responds to internal access
    """

    def ListPipelinesAdmin(self, request, context):
        """ListPipelinesAdmin method receives a ListPipelinesAdminRequest message and
        returns a ListPipelinesAdminResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookUpPipelineAdmin(self, request, context):
        """LookUpPipelineAdmin method receives a LookUpPipelineAdminRequest message
        and returns a LookUpPipelineAdminResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookUpOperatorDefinitionAdmin(self, request, context):
        """LookUpOperatorDefinitionAdmin method receives a
        LookUpOperatorDefinitionAdminRequest message and returns a
        LookUpOperatorDefinitionAdminResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPipelineReleasesAdmin(self, request, context):
        """ListPipelineReleasesAdmin method receives a ListPipelineReleasesAdminRequest message and
        returns a ListPipelineReleasesAdminResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PipelinePrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListPipelinesAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPipelinesAdmin,
                    request_deserializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelinesAdminRequest.FromString,
                    response_serializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelinesAdminResponse.SerializeToString,
            ),
            'LookUpPipelineAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.LookUpPipelineAdmin,
                    request_deserializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.LookUpPipelineAdminRequest.FromString,
                    response_serializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.LookUpPipelineAdminResponse.SerializeToString,
            ),
            'LookUpOperatorDefinitionAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.LookUpOperatorDefinitionAdmin,
                    request_deserializer=vdp_dot_pipeline_dot_v1alpha_dot_operator__definition__pb2.LookUpOperatorDefinitionAdminRequest.FromString,
                    response_serializer=vdp_dot_pipeline_dot_v1alpha_dot_operator__definition__pb2.LookUpOperatorDefinitionAdminResponse.SerializeToString,
            ),
            'ListPipelineReleasesAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPipelineReleasesAdmin,
                    request_deserializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelineReleasesAdminRequest.FromString,
                    response_serializer=vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelineReleasesAdminResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vdp.pipeline.v1alpha.PipelinePrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PipelinePrivateService(object):
    """Pipeline service responds to internal access
    """

    @staticmethod
    def ListPipelinesAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.pipeline.v1alpha.PipelinePrivateService/ListPipelinesAdmin',
            vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelinesAdminRequest.SerializeToString,
            vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelinesAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookUpPipelineAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.pipeline.v1alpha.PipelinePrivateService/LookUpPipelineAdmin',
            vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.LookUpPipelineAdminRequest.SerializeToString,
            vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.LookUpPipelineAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookUpOperatorDefinitionAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.pipeline.v1alpha.PipelinePrivateService/LookUpOperatorDefinitionAdmin',
            vdp_dot_pipeline_dot_v1alpha_dot_operator__definition__pb2.LookUpOperatorDefinitionAdminRequest.SerializeToString,
            vdp_dot_pipeline_dot_v1alpha_dot_operator__definition__pb2.LookUpOperatorDefinitionAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPipelineReleasesAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.pipeline.v1alpha.PipelinePrivateService/ListPipelineReleasesAdmin',
            vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelineReleasesAdminRequest.SerializeToString,
            vdp_dot_pipeline_dot_v1alpha_dot_pipeline__pb2.ListPipelineReleasesAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)