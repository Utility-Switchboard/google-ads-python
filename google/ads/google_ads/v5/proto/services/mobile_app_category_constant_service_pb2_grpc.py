# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import mobile_app_category_constant_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_mobile__app__category__constant__pb2
from google.ads.google_ads.v5.proto.services import mobile_app_category_constant_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_mobile__app__category__constant__service__pb2


class MobileAppCategoryConstantServiceStub(object):
    """Service to fetch mobile app category constants.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMobileAppCategoryConstant = channel.unary_unary(
                '/google.ads.googleads.v5.services.MobileAppCategoryConstantService/GetMobileAppCategoryConstant',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_mobile__app__category__constant__service__pb2.GetMobileAppCategoryConstantRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_mobile__app__category__constant__pb2.MobileAppCategoryConstant.FromString,
                )


class MobileAppCategoryConstantServiceServicer(object):
    """Service to fetch mobile app category constants.
    """

    def GetMobileAppCategoryConstant(self, request, context):
        """Returns the requested mobile app category constant.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MobileAppCategoryConstantServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMobileAppCategoryConstant': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMobileAppCategoryConstant,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_mobile__app__category__constant__service__pb2.GetMobileAppCategoryConstantRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_mobile__app__category__constant__pb2.MobileAppCategoryConstant.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.MobileAppCategoryConstantService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MobileAppCategoryConstantService(object):
    """Service to fetch mobile app category constants.
    """

    @staticmethod
    def GetMobileAppCategoryConstant(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.MobileAppCategoryConstantService/GetMobileAppCategoryConstant',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_mobile__app__category__constant__service__pb2.GetMobileAppCategoryConstantRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_mobile__app__category__constant__pb2.MobileAppCategoryConstant.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
