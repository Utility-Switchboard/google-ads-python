# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/campaign_group_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import campaign_group_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__group__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/campaign_group_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\nCgoogle/ads/googleads_v0/proto/services/campaign_group_service.proto\x12 google.ads.googleads.v0.services\x1a<google/ads/googleads_v0/proto/resources/campaign_group.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"0\n\x17GetCampaignGroupRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\x80\x01\n\x1bMutateCampaignGroupsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12L\n\noperations\x18\x02 \x03(\x0b\x32\x38.google.ads.googleads.v0.services.CampaignGroupOperation\"\xf0\x01\n\x16\x43\x61mpaignGroupOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x42\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x30.google.ads.googleads.v0.resources.CampaignGroupH\x00\x12\x42\n\x06update\x18\x02 \x01(\x0b\x32\x30.google.ads.googleads.v0.resources.CampaignGroupH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"l\n\x1cMutateCampaignGroupsResponse\x12L\n\x07results\x18\x02 \x03(\x0b\x32;.google.ads.googleads.v0.services.MutateCampaignGroupResult\"2\n\x19MutateCampaignGroupResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xaa\x03\n\x14\x43\x61mpaignGroupService\x12\xb9\x01\n\x10GetCampaignGroup\x12\x39.google.ads.googleads.v0.services.GetCampaignGroupRequest\x1a\x30.google.ads.googleads.v0.resources.CampaignGroup\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/v0/{resource_name=customers/*/campaignGroups/*}\x12\xd5\x01\n\x14MutateCampaignGroups\x12=.google.ads.googleads.v0.services.MutateCampaignGroupsRequest\x1a>.google.ads.googleads.v0.services.MutateCampaignGroupsResponse\">\x82\xd3\xe4\x93\x02\x38\"3/v0/customers/{customer_id=*}/campaignGroups:mutate:\x01*B\xd9\x01\n$com.google.ads.googleads.v0.servicesB\x19\x43\x61mpaignGroupServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__group__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETCAMPAIGNGROUPREQUEST = _descriptor.Descriptor(
  name='GetCampaignGroupRequest',
  full_name='google.ads.googleads.v0.services.GetCampaignGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetCampaignGroupRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=279,
)


_MUTATECAMPAIGNGROUPSREQUEST = _descriptor.Descriptor(
  name='MutateCampaignGroupsRequest',
  full_name='google.ads.googleads.v0.services.MutateCampaignGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateCampaignGroupsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.MutateCampaignGroupsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=410,
)


_CAMPAIGNGROUPOPERATION = _descriptor.Descriptor(
  name='CampaignGroupOperation',
  full_name='google.ads.googleads.v0.services.CampaignGroupOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v0.services.CampaignGroupOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.CampaignGroupOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v0.services.CampaignGroupOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.CampaignGroupOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.CampaignGroupOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=413,
  serialized_end=653,
)


_MUTATECAMPAIGNGROUPSRESPONSE = _descriptor.Descriptor(
  name='MutateCampaignGroupsResponse',
  full_name='google.ads.googleads.v0.services.MutateCampaignGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.MutateCampaignGroupsResponse.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=763,
)


_MUTATECAMPAIGNGROUPRESULT = _descriptor.Descriptor(
  name='MutateCampaignGroupResult',
  full_name='google.ads.googleads.v0.services.MutateCampaignGroupResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateCampaignGroupResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=815,
)

_MUTATECAMPAIGNGROUPSREQUEST.fields_by_name['operations'].message_type = _CAMPAIGNGROUPOPERATION
_CAMPAIGNGROUPOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_CAMPAIGNGROUPOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__group__pb2._CAMPAIGNGROUP
_CAMPAIGNGROUPOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__group__pb2._CAMPAIGNGROUP
_CAMPAIGNGROUPOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNGROUPOPERATION.fields_by_name['create'])
_CAMPAIGNGROUPOPERATION.fields_by_name['create'].containing_oneof = _CAMPAIGNGROUPOPERATION.oneofs_by_name['operation']
_CAMPAIGNGROUPOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNGROUPOPERATION.fields_by_name['update'])
_CAMPAIGNGROUPOPERATION.fields_by_name['update'].containing_oneof = _CAMPAIGNGROUPOPERATION.oneofs_by_name['operation']
_CAMPAIGNGROUPOPERATION.oneofs_by_name['operation'].fields.append(
  _CAMPAIGNGROUPOPERATION.fields_by_name['remove'])
_CAMPAIGNGROUPOPERATION.fields_by_name['remove'].containing_oneof = _CAMPAIGNGROUPOPERATION.oneofs_by_name['operation']
_MUTATECAMPAIGNGROUPSRESPONSE.fields_by_name['results'].message_type = _MUTATECAMPAIGNGROUPRESULT
DESCRIPTOR.message_types_by_name['GetCampaignGroupRequest'] = _GETCAMPAIGNGROUPREQUEST
DESCRIPTOR.message_types_by_name['MutateCampaignGroupsRequest'] = _MUTATECAMPAIGNGROUPSREQUEST
DESCRIPTOR.message_types_by_name['CampaignGroupOperation'] = _CAMPAIGNGROUPOPERATION
DESCRIPTOR.message_types_by_name['MutateCampaignGroupsResponse'] = _MUTATECAMPAIGNGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['MutateCampaignGroupResult'] = _MUTATECAMPAIGNGROUPRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCampaignGroupRequest = _reflection.GeneratedProtocolMessageType('GetCampaignGroupRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCAMPAIGNGROUPREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.campaign_group_service_pb2'
  ,
  __doc__ = """Request message for
  [CampaignGroupService.GetCampaignGroup][google.ads.googleads.v0.services.CampaignGroupService.GetCampaignGroup].
  
  
  Attributes:
      resource_name:
          The resource name of the campaign group to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetCampaignGroupRequest)
  ))
_sym_db.RegisterMessage(GetCampaignGroupRequest)

MutateCampaignGroupsRequest = _reflection.GeneratedProtocolMessageType('MutateCampaignGroupsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNGROUPSREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.campaign_group_service_pb2'
  ,
  __doc__ = """Request message for
  [CampaignGroupService.MutateCampaignGroups][google.ads.googleads.v0.services.CampaignGroupService.MutateCampaignGroups].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose campaign groups are being
          modified.
      operations:
          The list of operations to perform on individual campaign
          groups.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCampaignGroupsRequest)
  ))
_sym_db.RegisterMessage(MutateCampaignGroupsRequest)

CampaignGroupOperation = _reflection.GeneratedProtocolMessageType('CampaignGroupOperation', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNGROUPOPERATION,
  __module__ = 'google.ads.googleads_v0.proto.services.campaign_group_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on a campaign group.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          campaign group.
      update:
          Update operation: The campaign group is expected to have a
          valid resource name.
      remove:
          Remove operation: A resource name for the removed campaign
          group is expected, in this format:
          ``customers/{customer_id}/campaignGroups/{campaign_group_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.CampaignGroupOperation)
  ))
_sym_db.RegisterMessage(CampaignGroupOperation)

MutateCampaignGroupsResponse = _reflection.GeneratedProtocolMessageType('MutateCampaignGroupsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNGROUPSRESPONSE,
  __module__ = 'google.ads.googleads_v0.proto.services.campaign_group_service_pb2'
  ,
  __doc__ = """Response message for campaign group mutate.
  
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCampaignGroupsResponse)
  ))
_sym_db.RegisterMessage(MutateCampaignGroupsResponse)

MutateCampaignGroupResult = _reflection.GeneratedProtocolMessageType('MutateCampaignGroupResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECAMPAIGNGROUPRESULT,
  __module__ = 'google.ads.googleads_v0.proto.services.campaign_group_service_pb2'
  ,
  __doc__ = """The result for the campaign group mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCampaignGroupResult)
  ))
_sym_db.RegisterMessage(MutateCampaignGroupResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\031CampaignGroupServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_CAMPAIGNGROUPSERVICE = _descriptor.ServiceDescriptor(
  name='CampaignGroupService',
  full_name='google.ads.googleads.v0.services.CampaignGroupService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=818,
  serialized_end=1244,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCampaignGroup',
    full_name='google.ads.googleads.v0.services.CampaignGroupService.GetCampaignGroup',
    index=0,
    containing_service=None,
    input_type=_GETCAMPAIGNGROUPREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__group__pb2._CAMPAIGNGROUP,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0022\0220/v0/{resource_name=customers/*/campaignGroups/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='MutateCampaignGroups',
    full_name='google.ads.googleads.v0.services.CampaignGroupService.MutateCampaignGroups',
    index=1,
    containing_service=None,
    input_type=_MUTATECAMPAIGNGROUPSREQUEST,
    output_type=_MUTATECAMPAIGNGROUPSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0028\"3/v0/customers/{customer_id=*}/campaignGroups:mutate:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CAMPAIGNGROUPSERVICE)

DESCRIPTOR.services_by_name['CampaignGroupService'] = _CAMPAIGNGROUPSERVICE

# @@protoc_insertion_point(module_scope)