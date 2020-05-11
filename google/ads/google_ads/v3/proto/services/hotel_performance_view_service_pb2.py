# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/services/hotel_performance_view_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.resources import hotel_performance_view_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_hotel__performance__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/services/hotel_performance_view_service.proto',
  package='google.ads.googleads.v3.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v3.servicesB HotelPerformanceViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V3.Services\312\002 Google\\Ads\\GoogleAds\\V3\\Services\352\002$Google::Ads::GoogleAds::V3::Services'),
  serialized_pb=_b('\nKgoogle/ads/googleads_v3/proto/services/hotel_performance_view_service.proto\x12 google.ads.googleads.v3.services\x1a\x44google/ads/googleads_v3/proto/resources/hotel_performance_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"n\n\x1eGetHotelPerformanceViewRequest\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0\x41\x02\xfa\x41/\n-googleads.googleapis.com/HotelPerformanceView2\x9f\x02\n\x1bHotelPerformanceViewService\x12\xe2\x01\n\x17GetHotelPerformanceView\x12@.google.ads.googleads.v3.services.GetHotelPerformanceViewRequest\x1a\x37.google.ads.googleads.v3.resources.HotelPerformanceView\"L\x82\xd3\xe4\x93\x02\x36\x12\x34/v3/{resource_name=customers/*/hotelPerformanceView}\xda\x41\rresource_name\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x87\x02\n$com.google.ads.googleads.v3.servicesB HotelPerformanceViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V3.Services\xca\x02 Google\\Ads\\GoogleAds\\V3\\Services\xea\x02$Google::Ads::GoogleAds::V3::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_hotel__performance__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETHOTELPERFORMANCEVIEWREQUEST = _descriptor.Descriptor(
  name='GetHotelPerformanceViewRequest',
  full_name='google.ads.googleads.v3.services.GetHotelPerformanceViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.GetHotelPerformanceViewRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A/\n-googleads.googleapis.com/HotelPerformanceView'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=408,
)

DESCRIPTOR.message_types_by_name['GetHotelPerformanceViewRequest'] = _GETHOTELPERFORMANCEVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetHotelPerformanceViewRequest = _reflection.GeneratedProtocolMessageType('GetHotelPerformanceViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETHOTELPERFORMANCEVIEWREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.hotel_performance_view_service_pb2'
  ,
  __doc__ = """Request message for
  [HotelPerformanceViewService.GetHotelPerformanceView][google.ads.googleads.v3.services.HotelPerformanceViewService.GetHotelPerformanceView].
  
  
  Attributes:
      resource_name:
          Required. Resource name of the Hotel Performance View to
          fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.GetHotelPerformanceViewRequest)
  ))
_sym_db.RegisterMessage(GetHotelPerformanceViewRequest)


DESCRIPTOR._options = None
_GETHOTELPERFORMANCEVIEWREQUEST.fields_by_name['resource_name']._options = None

_HOTELPERFORMANCEVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='HotelPerformanceViewService',
  full_name='google.ads.googleads.v3.services.HotelPerformanceViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=411,
  serialized_end=698,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetHotelPerformanceView',
    full_name='google.ads.googleads.v3.services.HotelPerformanceViewService.GetHotelPerformanceView',
    index=0,
    containing_service=None,
    input_type=_GETHOTELPERFORMANCEVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_hotel__performance__view__pb2._HOTELPERFORMANCEVIEW,
    serialized_options=_b('\202\323\344\223\0026\0224/v3/{resource_name=customers/*/hotelPerformanceView}\332A\rresource_name'),
  ),
])
_sym_db.RegisterServiceDescriptor(_HOTELPERFORMANCEVIEWSERVICE)

DESCRIPTOR.services_by_name['HotelPerformanceViewService'] = _HOTELPERFORMANCEVIEWSERVICE

# @@protoc_insertion_point(module_scope)