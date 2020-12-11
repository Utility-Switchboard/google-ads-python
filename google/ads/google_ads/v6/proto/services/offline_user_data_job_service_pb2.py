# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/services/offline_user_data_job_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.common import offline_user_data_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_offline__user__data__pb2
from google.ads.google_ads.v6.proto.resources import offline_user_data_job_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_offline__user__data__job__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/services/offline_user_data_job_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB\036OfflineUserDataJobServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nJgoogle/ads/googleads_v6/proto/services/offline_user_data_job_service.proto\x12 google.ads.googleads.v6.services\x1a<google/ads/googleads_v6/proto/common/offline_user_data.proto\x1a\x43google/ads/googleads_v6/proto/resources/offline_user_data_job.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x17google/rpc/status.proto\"\x84\x01\n\x1f\x43reateOfflineUserDataJobRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12G\n\x03job\x18\x02 \x01(\x0b\x32\x35.google.ads.googleads.v6.resources.OfflineUserDataJobB\x03\xe0\x41\x02\"9\n CreateOfflineUserDataJobResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\"j\n\x1cGetOfflineUserDataJobRequest\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+googleads.googleapis.com/OfflineUserDataJob\"j\n\x1cRunOfflineUserDataJobRequest\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+googleads.googleapis.com/OfflineUserDataJob\"\x8c\x02\n&AddOfflineUserDataJobOperationsRequest\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+googleads.googleapis.com/OfflineUserDataJob\x12#\n\x16\x65nable_partial_failure\x18\x04 \x01(\x08H\x00\x88\x01\x01\x12V\n\noperations\x18\x03 \x03(\x0b\x32=.google.ads.googleads.v6.services.OfflineUserDataJobOperationB\x03\xe0\x41\x02\x42\x19\n\x17_enable_partial_failure\"\xb8\x01\n\x1bOfflineUserDataJobOperation\x12:\n\x06\x63reate\x18\x01 \x01(\x0b\x32(.google.ads.googleads.v6.common.UserDataH\x00\x12:\n\x06remove\x18\x02 \x01(\x0b\x32(.google.ads.googleads.v6.common.UserDataH\x00\x12\x14\n\nremove_all\x18\x03 \x01(\x08H\x00\x42\x0b\n\toperation\"\\\n\'AddOfflineUserDataJobOperationsResponse\x12\x31\n\x15partial_failure_error\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status2\xb8\x08\n\x19OfflineUserDataJobService\x12\xf8\x01\n\x18\x43reateOfflineUserDataJob\x12\x41.google.ads.googleads.v6.services.CreateOfflineUserDataJobRequest\x1a\x42.google.ads.googleads.v6.services.CreateOfflineUserDataJobResponse\"U\x82\xd3\xe4\x93\x02=\"8/v6/customers/{customer_id=*}/offlineUserDataJobs:create:\x01*\xda\x41\x0f\x63ustomer_id,job\x12\xdd\x01\n\x15GetOfflineUserDataJob\x12>.google.ads.googleads.v6.services.GetOfflineUserDataJobRequest\x1a\x35.google.ads.googleads.v6.resources.OfflineUserDataJob\"M\x82\xd3\xe4\x93\x02\x37\x12\x35/v6/{resource_name=customers/*/offlineUserDataJobs/*}\xda\x41\rresource_name\x12\xa1\x02\n\x1f\x41\x64\x64OfflineUserDataJobOperations\x12H.google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsRequest\x1aI.google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsResponse\"i\x82\xd3\xe4\x93\x02H\"C/v6/{resource_name=customers/*/offlineUserDataJobs/*}:addOperations:\x01*\xda\x41\x18resource_name,operations\x12\xfe\x01\n\x15RunOfflineUserDataJob\x12>.google.ads.googleads.v6.services.RunOfflineUserDataJobRequest\x1a\x1d.google.longrunning.Operation\"\x85\x01\x82\xd3\xe4\x93\x02>\"9/v6/{resource_name=customers/*/offlineUserDataJobs/*}:run:\x01*\xda\x41\rresource_name\xca\x41.\n\x15google.protobuf.Empty\x12\x15google.protobuf.Empty\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x85\x02\n$com.google.ads.googleads.v6.servicesB\x1eOfflineUserDataJobServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_offline__user__data__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_offline__user__data__job__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_CREATEOFFLINEUSERDATAJOBREQUEST = _descriptor.Descriptor(
  name='CreateOfflineUserDataJobRequest',
  full_name='google.ads.googleads.v6.services.CreateOfflineUserDataJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.CreateOfflineUserDataJobRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job', full_name='google.ads.googleads.v6.services.CreateOfflineUserDataJobRequest.job', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=421,
  serialized_end=553,
)


_CREATEOFFLINEUSERDATAJOBRESPONSE = _descriptor.Descriptor(
  name='CreateOfflineUserDataJobResponse',
  full_name='google.ads.googleads.v6.services.CreateOfflineUserDataJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.CreateOfflineUserDataJobResponse.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=555,
  serialized_end=612,
)


_GETOFFLINEUSERDATAJOBREQUEST = _descriptor.Descriptor(
  name='GetOfflineUserDataJobRequest',
  full_name='google.ads.googleads.v6.services.GetOfflineUserDataJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.GetOfflineUserDataJobRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A-\n+googleads.googleapis.com/OfflineUserDataJob', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=614,
  serialized_end=720,
)


_RUNOFFLINEUSERDATAJOBREQUEST = _descriptor.Descriptor(
  name='RunOfflineUserDataJobRequest',
  full_name='google.ads.googleads.v6.services.RunOfflineUserDataJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.RunOfflineUserDataJobRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A-\n+googleads.googleapis.com/OfflineUserDataJob', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=722,
  serialized_end=828,
)


_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST = _descriptor.Descriptor(
  name='AddOfflineUserDataJobOperationsRequest',
  full_name='google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A-\n+googleads.googleapis.com/OfflineUserDataJob', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_partial_failure', full_name='google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsRequest.enable_partial_failure', index=1,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsRequest.operations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_enable_partial_failure', full_name='google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsRequest._enable_partial_failure',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=831,
  serialized_end=1099,
)


_OFFLINEUSERDATAJOBOPERATION = _descriptor.Descriptor(
  name='OfflineUserDataJobOperation',
  full_name='google.ads.googleads.v6.services.OfflineUserDataJobOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v6.services.OfflineUserDataJobOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v6.services.OfflineUserDataJobOperation.remove', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove_all', full_name='google.ads.googleads.v6.services.OfflineUserDataJobOperation.remove_all', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v6.services.OfflineUserDataJobOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1102,
  serialized_end=1286,
)


_ADDOFFLINEUSERDATAJOBOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='AddOfflineUserDataJobOperationsResponse',
  full_name='google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsResponse.partial_failure_error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1288,
  serialized_end=1380,
)

_CREATEOFFLINEUSERDATAJOBREQUEST.fields_by_name['job'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_offline__user__data__job__pb2._OFFLINEUSERDATAJOB
_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST.fields_by_name['operations'].message_type = _OFFLINEUSERDATAJOBOPERATION
_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST.oneofs_by_name['_enable_partial_failure'].fields.append(
  _ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST.fields_by_name['enable_partial_failure'])
_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST.fields_by_name['enable_partial_failure'].containing_oneof = _ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST.oneofs_by_name['_enable_partial_failure']
_OFFLINEUSERDATAJOBOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_offline__user__data__pb2._USERDATA
_OFFLINEUSERDATAJOBOPERATION.fields_by_name['remove'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_offline__user__data__pb2._USERDATA
_OFFLINEUSERDATAJOBOPERATION.oneofs_by_name['operation'].fields.append(
  _OFFLINEUSERDATAJOBOPERATION.fields_by_name['create'])
_OFFLINEUSERDATAJOBOPERATION.fields_by_name['create'].containing_oneof = _OFFLINEUSERDATAJOBOPERATION.oneofs_by_name['operation']
_OFFLINEUSERDATAJOBOPERATION.oneofs_by_name['operation'].fields.append(
  _OFFLINEUSERDATAJOBOPERATION.fields_by_name['remove'])
_OFFLINEUSERDATAJOBOPERATION.fields_by_name['remove'].containing_oneof = _OFFLINEUSERDATAJOBOPERATION.oneofs_by_name['operation']
_OFFLINEUSERDATAJOBOPERATION.oneofs_by_name['operation'].fields.append(
  _OFFLINEUSERDATAJOBOPERATION.fields_by_name['remove_all'])
_OFFLINEUSERDATAJOBOPERATION.fields_by_name['remove_all'].containing_oneof = _OFFLINEUSERDATAJOBOPERATION.oneofs_by_name['operation']
_ADDOFFLINEUSERDATAJOBOPERATIONSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['CreateOfflineUserDataJobRequest'] = _CREATEOFFLINEUSERDATAJOBREQUEST
DESCRIPTOR.message_types_by_name['CreateOfflineUserDataJobResponse'] = _CREATEOFFLINEUSERDATAJOBRESPONSE
DESCRIPTOR.message_types_by_name['GetOfflineUserDataJobRequest'] = _GETOFFLINEUSERDATAJOBREQUEST
DESCRIPTOR.message_types_by_name['RunOfflineUserDataJobRequest'] = _RUNOFFLINEUSERDATAJOBREQUEST
DESCRIPTOR.message_types_by_name['AddOfflineUserDataJobOperationsRequest'] = _ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['OfflineUserDataJobOperation'] = _OFFLINEUSERDATAJOBOPERATION
DESCRIPTOR.message_types_by_name['AddOfflineUserDataJobOperationsResponse'] = _ADDOFFLINEUSERDATAJOBOPERATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateOfflineUserDataJobRequest = _reflection.GeneratedProtocolMessageType('CreateOfflineUserDataJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEOFFLINEUSERDATAJOBREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.offline_user_data_job_service_pb2'
  ,
  '__doc__': """Request message for [OfflineUserDataJobService.CreateOfflineUserDataJo
  b][google.ads.googleads.v6.services.OfflineUserDataJobService.CreateOf
  flineUserDataJob].
  
  Attributes:
      customer_id:
          Required. The ID of the customer for which to create an
          offline user data job.
      job:
          Required. The offline user data job to be created.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.CreateOfflineUserDataJobRequest)
  })
_sym_db.RegisterMessage(CreateOfflineUserDataJobRequest)

CreateOfflineUserDataJobResponse = _reflection.GeneratedProtocolMessageType('CreateOfflineUserDataJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEOFFLINEUSERDATAJOBRESPONSE,
  '__module__' : 'google.ads.googleads_v6.proto.services.offline_user_data_job_service_pb2'
  ,
  '__doc__': """Response message for [OfflineUserDataJobService.CreateOfflineUserDataJ
  ob][google.ads.googleads.v6.services.OfflineUserDataJobService.CreateO
  fflineUserDataJob].
  
  Attributes:
      resource_name:
          The resource name of the OfflineUserDataJob.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.CreateOfflineUserDataJobResponse)
  })
_sym_db.RegisterMessage(CreateOfflineUserDataJobResponse)

GetOfflineUserDataJobRequest = _reflection.GeneratedProtocolMessageType('GetOfflineUserDataJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOFFLINEUSERDATAJOBREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.offline_user_data_job_service_pb2'
  ,
  '__doc__': """Request message for [OfflineUserDataJobService.GetOfflineUserDataJob][
  google.ads.googleads.v6.services.OfflineUserDataJobService.GetOfflineU
  serDataJob].
  
  Attributes:
      resource_name:
          Required. The resource name of the OfflineUserDataJob to get.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.GetOfflineUserDataJobRequest)
  })
_sym_db.RegisterMessage(GetOfflineUserDataJobRequest)

RunOfflineUserDataJobRequest = _reflection.GeneratedProtocolMessageType('RunOfflineUserDataJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNOFFLINEUSERDATAJOBREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.offline_user_data_job_service_pb2'
  ,
  '__doc__': """Request message for [OfflineUserDataJobService.RunOfflineUserDataJob][
  google.ads.googleads.v6.services.OfflineUserDataJobService.RunOfflineU
  serDataJob].
  
  Attributes:
      resource_name:
          Required. The resource name of the OfflineUserDataJob to run.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.RunOfflineUserDataJobRequest)
  })
_sym_db.RegisterMessage(RunOfflineUserDataJobRequest)

AddOfflineUserDataJobOperationsRequest = _reflection.GeneratedProtocolMessageType('AddOfflineUserDataJobOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST,
  '__module__' : 'google.ads.googleads_v6.proto.services.offline_user_data_job_service_pb2'
  ,
  '__doc__': """Request message for [OfflineUserDataJobService.AddOfflineUserDataJobOp
  erations][google.ads.googleads.v6.services.OfflineUserDataJobService.A
  ddOfflineUserDataJobOperations].
  
  Attributes:
      resource_name:
          Required. The resource name of the OfflineUserDataJob.
      enable_partial_failure:
          True to enable partial failure for the offline user data job.
      operations:
          Required. The list of operations to be done.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsRequest)
  })
_sym_db.RegisterMessage(AddOfflineUserDataJobOperationsRequest)

OfflineUserDataJobOperation = _reflection.GeneratedProtocolMessageType('OfflineUserDataJobOperation', (_message.Message,), {
  'DESCRIPTOR' : _OFFLINEUSERDATAJOBOPERATION,
  '__module__' : 'google.ads.googleads_v6.proto.services.offline_user_data_job_service_pb2'
  ,
  '__doc__': """Operation to be made for the AddOfflineUserDataJobOperationsRequest.
  
  Attributes:
      operation:
          Operation to be made for the
          AddOfflineUserDataJobOperationsRequest.
      create:
          Add the provided data to the transaction. Data cannot be
          retrieved after being uploaded.
      remove:
          Remove the provided data from the transaction. Data cannot be
          retrieved after being uploaded.
      remove_all:
          Remove all previously provided data. This is only supported
          for Customer Match.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.OfflineUserDataJobOperation)
  })
_sym_db.RegisterMessage(OfflineUserDataJobOperation)

AddOfflineUserDataJobOperationsResponse = _reflection.GeneratedProtocolMessageType('AddOfflineUserDataJobOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDOFFLINEUSERDATAJOBOPERATIONSRESPONSE,
  '__module__' : 'google.ads.googleads_v6.proto.services.offline_user_data_job_service_pb2'
  ,
  '__doc__': """Response message for [OfflineUserDataJobService.AddOfflineUserDataJobO
  perations][google.ads.googleads.v6.services.OfflineUserDataJobService.
  AddOfflineUserDataJobOperations].
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.AddOfflineUserDataJobOperationsResponse)
  })
_sym_db.RegisterMessage(AddOfflineUserDataJobOperationsResponse)


DESCRIPTOR._options = None
_CREATEOFFLINEUSERDATAJOBREQUEST.fields_by_name['customer_id']._options = None
_CREATEOFFLINEUSERDATAJOBREQUEST.fields_by_name['job']._options = None
_GETOFFLINEUSERDATAJOBREQUEST.fields_by_name['resource_name']._options = None
_RUNOFFLINEUSERDATAJOBREQUEST.fields_by_name['resource_name']._options = None
_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST.fields_by_name['resource_name']._options = None
_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST.fields_by_name['operations']._options = None

_OFFLINEUSERDATAJOBSERVICE = _descriptor.ServiceDescriptor(
  name='OfflineUserDataJobService',
  full_name='google.ads.googleads.v6.services.OfflineUserDataJobService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1383,
  serialized_end=2463,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateOfflineUserDataJob',
    full_name='google.ads.googleads.v6.services.OfflineUserDataJobService.CreateOfflineUserDataJob',
    index=0,
    containing_service=None,
    input_type=_CREATEOFFLINEUSERDATAJOBREQUEST,
    output_type=_CREATEOFFLINEUSERDATAJOBRESPONSE,
    serialized_options=b'\202\323\344\223\002=\"8/v6/customers/{customer_id=*}/offlineUserDataJobs:create:\001*\332A\017customer_id,job',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOfflineUserDataJob',
    full_name='google.ads.googleads.v6.services.OfflineUserDataJobService.GetOfflineUserDataJob',
    index=1,
    containing_service=None,
    input_type=_GETOFFLINEUSERDATAJOBREQUEST,
    output_type=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_offline__user__data__job__pb2._OFFLINEUSERDATAJOB,
    serialized_options=b'\202\323\344\223\0027\0225/v6/{resource_name=customers/*/offlineUserDataJobs/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddOfflineUserDataJobOperations',
    full_name='google.ads.googleads.v6.services.OfflineUserDataJobService.AddOfflineUserDataJobOperations',
    index=2,
    containing_service=None,
    input_type=_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST,
    output_type=_ADDOFFLINEUSERDATAJOBOPERATIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002H\"C/v6/{resource_name=customers/*/offlineUserDataJobs/*}:addOperations:\001*\332A\030resource_name,operations',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunOfflineUserDataJob',
    full_name='google.ads.googleads.v6.services.OfflineUserDataJobService.RunOfflineUserDataJob',
    index=3,
    containing_service=None,
    input_type=_RUNOFFLINEUSERDATAJOBREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002>\"9/v6/{resource_name=customers/*/offlineUserDataJobs/*}:run:\001*\332A\rresource_name\312A.\n\025google.protobuf.Empty\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OFFLINEUSERDATAJOBSERVICE)

DESCRIPTOR.services_by_name['OfflineUserDataJobService'] = _OFFLINEUSERDATAJOBSERVICE

# @@protoc_insertion_point(module_scope)