# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/services/ad_group_ad_label_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.resources import ad_group_ad_label_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__ad__label__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/services/ad_group_ad_label_service.proto',
  package='google.ads.googleads.v4.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v4.servicesB\032AdGroupAdLabelServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V4.Services\312\002 Google\\Ads\\GoogleAds\\V4\\Services\352\002$Google::Ads::GoogleAds::V4::Services'),
  serialized_pb=_b('\nFgoogle/ads/googleads_v4/proto/services/ad_group_ad_label_service.proto\x12 google.ads.googleads.v4.services\x1a?google/ads/googleads_v4/proto/resources/ad_group_ad_label.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto\"b\n\x18GetAdGroupAdLabelRequest\x12\x46\n\rresource_name\x18\x01 \x01(\tB/\xe0\x41\x02\xfa\x41)\n\'googleads.googleapis.com/AdGroupAdLabel\"\xbc\x01\n\x1cMutateAdGroupAdLabelsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12R\n\noperations\x18\x02 \x03(\x0b\x32\x39.google.ads.googleads.v4.services.AdGroupAdLabelOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"}\n\x17\x41\x64GroupAdLabelOperation\x12\x43\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x31.google.ads.googleads.v4.resources.AdGroupAdLabelH\x00\x12\x10\n\x06remove\x18\x02 \x01(\tH\x00\x42\x0b\n\toperation\"\xa1\x01\n\x1dMutateAdGroupAdLabelsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12M\n\x07results\x18\x02 \x03(\x0b\x32<.google.ads.googleads.v4.services.MutateAdGroupAdLabelResult\"3\n\x1aMutateAdGroupAdLabelResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xf9\x03\n\x15\x41\x64GroupAdLabelService\x12\xcd\x01\n\x11GetAdGroupAdLabel\x12:.google.ads.googleads.v4.services.GetAdGroupAdLabelRequest\x1a\x31.google.ads.googleads.v4.resources.AdGroupAdLabel\"I\x82\xd3\xe4\x93\x02\x33\x12\x31/v4/{resource_name=customers/*/adGroupAdLabels/*}\xda\x41\rresource_name\x12\xf2\x01\n\x15MutateAdGroupAdLabels\x12>.google.ads.googleads.v4.services.MutateAdGroupAdLabelsRequest\x1a?.google.ads.googleads.v4.services.MutateAdGroupAdLabelsResponse\"X\x82\xd3\xe4\x93\x02\x39\"4/v4/customers/{customer_id=*}/adGroupAdLabels:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x81\x02\n$com.google.ads.googleads.v4.servicesB\x1a\x41\x64GroupAdLabelServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V4.Services\xca\x02 Google\\Ads\\GoogleAds\\V4\\Services\xea\x02$Google::Ads::GoogleAds::V4::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__ad__label__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETADGROUPADLABELREQUEST = _descriptor.Descriptor(
  name='GetAdGroupAdLabelRequest',
  full_name='google.ads.googleads.v4.services.GetAdGroupAdLabelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.GetAdGroupAdLabelRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A)\n\'googleads.googleapis.com/AdGroupAdLabel'), file=DESCRIPTOR),
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
  serialized_start=313,
  serialized_end=411,
)


_MUTATEADGROUPADLABELSREQUEST = _descriptor.Descriptor(
  name='MutateAdGroupAdLabelsRequest',
  full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=414,
  serialized_end=602,
)


_ADGROUPADLABELOPERATION = _descriptor.Descriptor(
  name='AdGroupAdLabelOperation',
  full_name='google.ads.googleads.v4.services.AdGroupAdLabelOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v4.services.AdGroupAdLabelOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v4.services.AdGroupAdLabelOperation.remove', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
      name='operation', full_name='google.ads.googleads.v4.services.AdGroupAdLabelOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=604,
  serialized_end=729,
)


_MUTATEADGROUPADLABELSRESPONSE = _descriptor.Descriptor(
  name='MutateAdGroupAdLabelsResponse',
  full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=732,
  serialized_end=893,
)


_MUTATEADGROUPADLABELRESULT = _descriptor.Descriptor(
  name='MutateAdGroupAdLabelResult',
  full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.MutateAdGroupAdLabelResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=895,
  serialized_end=946,
)

_MUTATEADGROUPADLABELSREQUEST.fields_by_name['operations'].message_type = _ADGROUPADLABELOPERATION
_ADGROUPADLABELOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__ad__label__pb2._ADGROUPADLABEL
_ADGROUPADLABELOPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPADLABELOPERATION.fields_by_name['create'])
_ADGROUPADLABELOPERATION.fields_by_name['create'].containing_oneof = _ADGROUPADLABELOPERATION.oneofs_by_name['operation']
_ADGROUPADLABELOPERATION.oneofs_by_name['operation'].fields.append(
  _ADGROUPADLABELOPERATION.fields_by_name['remove'])
_ADGROUPADLABELOPERATION.fields_by_name['remove'].containing_oneof = _ADGROUPADLABELOPERATION.oneofs_by_name['operation']
_MUTATEADGROUPADLABELSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEADGROUPADLABELSRESPONSE.fields_by_name['results'].message_type = _MUTATEADGROUPADLABELRESULT
DESCRIPTOR.message_types_by_name['GetAdGroupAdLabelRequest'] = _GETADGROUPADLABELREQUEST
DESCRIPTOR.message_types_by_name['MutateAdGroupAdLabelsRequest'] = _MUTATEADGROUPADLABELSREQUEST
DESCRIPTOR.message_types_by_name['AdGroupAdLabelOperation'] = _ADGROUPADLABELOPERATION
DESCRIPTOR.message_types_by_name['MutateAdGroupAdLabelsResponse'] = _MUTATEADGROUPADLABELSRESPONSE
DESCRIPTOR.message_types_by_name['MutateAdGroupAdLabelResult'] = _MUTATEADGROUPADLABELRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdGroupAdLabelRequest = _reflection.GeneratedProtocolMessageType('GetAdGroupAdLabelRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETADGROUPADLABELREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_group_ad_label_service_pb2'
  ,
  __doc__ = """Request message for
  [AdGroupAdLabelService.GetAdGroupAdLabel][google.ads.googleads.v4.services.AdGroupAdLabelService.GetAdGroupAdLabel].
  
  
  Attributes:
      resource_name:
          Required. The resource name of the ad group ad label to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.GetAdGroupAdLabelRequest)
  ))
_sym_db.RegisterMessage(GetAdGroupAdLabelRequest)

MutateAdGroupAdLabelsRequest = _reflection.GeneratedProtocolMessageType('MutateAdGroupAdLabelsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPADLABELSREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_group_ad_label_service_pb2'
  ,
  __doc__ = """Request message for
  [AdGroupAdLabelService.MutateAdGroupAdLabels][google.ads.googleads.v4.services.AdGroupAdLabelService.MutateAdGroupAdLabels].
  
  
  Attributes:
      customer_id:
          Required. ID of the customer whose ad group ad labels are
          being modified.
      operations:
          Required. The list of operations to perform on ad group ad
          labels.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateAdGroupAdLabelsRequest)
  ))
_sym_db.RegisterMessage(MutateAdGroupAdLabelsRequest)

AdGroupAdLabelOperation = _reflection.GeneratedProtocolMessageType('AdGroupAdLabelOperation', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPADLABELOPERATION,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_group_ad_label_service_pb2'
  ,
  __doc__ = """A single operation (create, remove) on an ad group ad label.
  
  
  Attributes:
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new ad
          group ad label.
      remove:
          Remove operation: A resource name for the ad group ad label
          being removed, in this format:  ``customers/{customer_id}/adGr
          oupAdLabels/{ad_group_id}~{ad_id} _{label_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.AdGroupAdLabelOperation)
  ))
_sym_db.RegisterMessage(AdGroupAdLabelOperation)

MutateAdGroupAdLabelsResponse = _reflection.GeneratedProtocolMessageType('MutateAdGroupAdLabelsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPADLABELSRESPONSE,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_group_ad_label_service_pb2'
  ,
  __doc__ = """Response message for an ad group ad labels mutate.
  
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateAdGroupAdLabelsResponse)
  ))
_sym_db.RegisterMessage(MutateAdGroupAdLabelsResponse)

MutateAdGroupAdLabelResult = _reflection.GeneratedProtocolMessageType('MutateAdGroupAdLabelResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEADGROUPADLABELRESULT,
  __module__ = 'google.ads.googleads_v4.proto.services.ad_group_ad_label_service_pb2'
  ,
  __doc__ = """The result for an ad group ad label mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateAdGroupAdLabelResult)
  ))
_sym_db.RegisterMessage(MutateAdGroupAdLabelResult)


DESCRIPTOR._options = None
_GETADGROUPADLABELREQUEST.fields_by_name['resource_name']._options = None
_MUTATEADGROUPADLABELSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEADGROUPADLABELSREQUEST.fields_by_name['operations']._options = None

_ADGROUPADLABELSERVICE = _descriptor.ServiceDescriptor(
  name='AdGroupAdLabelService',
  full_name='google.ads.googleads.v4.services.AdGroupAdLabelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=949,
  serialized_end=1454,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAdGroupAdLabel',
    full_name='google.ads.googleads.v4.services.AdGroupAdLabelService.GetAdGroupAdLabel',
    index=0,
    containing_service=None,
    input_type=_GETADGROUPADLABELREQUEST,
    output_type=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_ad__group__ad__label__pb2._ADGROUPADLABEL,
    serialized_options=_b('\202\323\344\223\0023\0221/v4/{resource_name=customers/*/adGroupAdLabels/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateAdGroupAdLabels',
    full_name='google.ads.googleads.v4.services.AdGroupAdLabelService.MutateAdGroupAdLabels',
    index=1,
    containing_service=None,
    input_type=_MUTATEADGROUPADLABELSREQUEST,
    output_type=_MUTATEADGROUPADLABELSRESPONSE,
    serialized_options=_b('\202\323\344\223\0029\"4/v4/customers/{customer_id=*}/adGroupAdLabels:mutate:\001*\332A\026customer_id,operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_ADGROUPADLABELSERVICE)

DESCRIPTOR.services_by_name['AdGroupAdLabelService'] = _ADGROUPADLABELSERVICE

# @@protoc_insertion_point(module_scope)
