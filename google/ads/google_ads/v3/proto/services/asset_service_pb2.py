# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/services/asset_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.resources import asset_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_asset__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/services/asset_service.proto',
  package='google.ads.googleads.v3.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v3.servicesB\021AssetServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V3.Services\312\002 Google\\Ads\\GoogleAds\\V3\\Services\352\002$Google::Ads::GoogleAds::V3::Services'),
  serialized_pb=_b('\n:google/ads/googleads_v3/proto/services/asset_service.proto\x12 google.ads.googleads.v3.services\x1a\x33google/ads/googleads_v3/proto/resources/asset.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"P\n\x0fGetAssetRequest\x12=\n\rresource_name\x18\x01 \x01(\tB&\xe0\x41\x02\xfa\x41 \n\x1egoogleads.googleapis.com/Asset\"z\n\x13MutateAssetsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12I\n\noperations\x18\x02 \x03(\x0b\x32\x30.google.ads.googleads.v3.services.AssetOperationB\x03\xe0\x41\x02\"Y\n\x0e\x41ssetOperation\x12:\n\x06\x63reate\x18\x01 \x01(\x0b\x32(.google.ads.googleads.v3.resources.AssetH\x00\x42\x0b\n\toperation\"\\\n\x14MutateAssetsResponse\x12\x44\n\x07results\x18\x02 \x03(\x0b\x32\x33.google.ads.googleads.v3.services.MutateAssetResult\"*\n\x11MutateAssetResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xa8\x03\n\x0c\x41ssetService\x12\xa9\x01\n\x08GetAsset\x12\x31.google.ads.googleads.v3.services.GetAssetRequest\x1a(.google.ads.googleads.v3.resources.Asset\"@\x82\xd3\xe4\x93\x02*\x12(/v3/{resource_name=customers/*/assets/*}\xda\x41\rresource_name\x12\xce\x01\n\x0cMutateAssets\x12\x35.google.ads.googleads.v3.services.MutateAssetsRequest\x1a\x36.google.ads.googleads.v3.services.MutateAssetsResponse\"O\x82\xd3\xe4\x93\x02\x30\"+/v3/customers/{customer_id=*}/assets:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xf8\x01\n$com.google.ads.googleads.v3.servicesB\x11\x41ssetServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V3.Services\xca\x02 Google\\Ads\\GoogleAds\\V3\\Services\xea\x02$Google::Ads::GoogleAds::V3::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_asset__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETASSETREQUEST = _descriptor.Descriptor(
  name='GetAssetRequest',
  full_name='google.ads.googleads.v3.services.GetAssetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.GetAssetRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A \n\036googleads.googleapis.com/Asset'), file=DESCRIPTOR),
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
  serialized_start=264,
  serialized_end=344,
)


_MUTATEASSETSREQUEST = _descriptor.Descriptor(
  name='MutateAssetsRequest',
  full_name='google.ads.googleads.v3.services.MutateAssetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v3.services.MutateAssetsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v3.services.MutateAssetsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
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
  serialized_start=346,
  serialized_end=468,
)


_ASSETOPERATION = _descriptor.Descriptor(
  name='AssetOperation',
  full_name='google.ads.googleads.v3.services.AssetOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v3.services.AssetOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='operation', full_name='google.ads.googleads.v3.services.AssetOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=470,
  serialized_end=559,
)


_MUTATEASSETSRESPONSE = _descriptor.Descriptor(
  name='MutateAssetsResponse',
  full_name='google.ads.googleads.v3.services.MutateAssetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v3.services.MutateAssetsResponse.results', index=0,
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
  serialized_start=561,
  serialized_end=653,
)


_MUTATEASSETRESULT = _descriptor.Descriptor(
  name='MutateAssetResult',
  full_name='google.ads.googleads.v3.services.MutateAssetResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.MutateAssetResult.resource_name', index=0,
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
  serialized_start=655,
  serialized_end=697,
)

_MUTATEASSETSREQUEST.fields_by_name['operations'].message_type = _ASSETOPERATION
_ASSETOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_asset__pb2._ASSET
_ASSETOPERATION.oneofs_by_name['operation'].fields.append(
  _ASSETOPERATION.fields_by_name['create'])
_ASSETOPERATION.fields_by_name['create'].containing_oneof = _ASSETOPERATION.oneofs_by_name['operation']
_MUTATEASSETSRESPONSE.fields_by_name['results'].message_type = _MUTATEASSETRESULT
DESCRIPTOR.message_types_by_name['GetAssetRequest'] = _GETASSETREQUEST
DESCRIPTOR.message_types_by_name['MutateAssetsRequest'] = _MUTATEASSETSREQUEST
DESCRIPTOR.message_types_by_name['AssetOperation'] = _ASSETOPERATION
DESCRIPTOR.message_types_by_name['MutateAssetsResponse'] = _MUTATEASSETSRESPONSE
DESCRIPTOR.message_types_by_name['MutateAssetResult'] = _MUTATEASSETRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAssetRequest = _reflection.GeneratedProtocolMessageType('GetAssetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETASSETREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.asset_service_pb2'
  ,
  __doc__ = """Request message for
  [AssetService.GetAsset][google.ads.googleads.v3.services.AssetService.GetAsset]
  
  
  Attributes:
      resource_name:
          Required. The resource name of the asset to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.GetAssetRequest)
  ))
_sym_db.RegisterMessage(GetAssetRequest)

MutateAssetsRequest = _reflection.GeneratedProtocolMessageType('MutateAssetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEASSETSREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.asset_service_pb2'
  ,
  __doc__ = """Request message for
  [AssetService.MutateAssets][google.ads.googleads.v3.services.AssetService.MutateAssets]
  
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose assets are being
          modified.
      operations:
          Required. The list of operations to perform on individual
          assets.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateAssetsRequest)
  ))
_sym_db.RegisterMessage(MutateAssetsRequest)

AssetOperation = _reflection.GeneratedProtocolMessageType('AssetOperation', (_message.Message,), dict(
  DESCRIPTOR = _ASSETOPERATION,
  __module__ = 'google.ads.googleads_v3.proto.services.asset_service_pb2'
  ,
  __doc__ = """A single operation to create an asset. Supported asset types are
  YoutubeVideoAsset, MediaBundleAsset, ImageAsset, and LeadFormAsset.
  TextAsset should be created with Ad inline.
  
  
  Attributes:
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          asset.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.AssetOperation)
  ))
_sym_db.RegisterMessage(AssetOperation)

MutateAssetsResponse = _reflection.GeneratedProtocolMessageType('MutateAssetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEASSETSRESPONSE,
  __module__ = 'google.ads.googleads_v3.proto.services.asset_service_pb2'
  ,
  __doc__ = """Response message for an asset mutate.
  
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateAssetsResponse)
  ))
_sym_db.RegisterMessage(MutateAssetsResponse)

MutateAssetResult = _reflection.GeneratedProtocolMessageType('MutateAssetResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEASSETRESULT,
  __module__ = 'google.ads.googleads_v3.proto.services.asset_service_pb2'
  ,
  __doc__ = """The result for the asset mutate.
  
  
  Attributes:
      resource_name:
          The resource name returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.MutateAssetResult)
  ))
_sym_db.RegisterMessage(MutateAssetResult)


DESCRIPTOR._options = None
_GETASSETREQUEST.fields_by_name['resource_name']._options = None
_MUTATEASSETSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEASSETSREQUEST.fields_by_name['operations']._options = None

_ASSETSERVICE = _descriptor.ServiceDescriptor(
  name='AssetService',
  full_name='google.ads.googleads.v3.services.AssetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=700,
  serialized_end=1124,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAsset',
    full_name='google.ads.googleads.v3.services.AssetService.GetAsset',
    index=0,
    containing_service=None,
    input_type=_GETASSETREQUEST,
    output_type=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_asset__pb2._ASSET,
    serialized_options=_b('\202\323\344\223\002*\022(/v3/{resource_name=customers/*/assets/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateAssets',
    full_name='google.ads.googleads.v3.services.AssetService.MutateAssets',
    index=1,
    containing_service=None,
    input_type=_MUTATEASSETSREQUEST,
    output_type=_MUTATEASSETSRESPONSE,
    serialized_options=_b('\202\323\344\223\0020\"+/v3/customers/{customer_id=*}/assets:mutate:\001*\332A\026customer_id,operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_ASSETSERVICE)

DESCRIPTOR.services_by_name['AssetService'] = _ASSETSERVICE

# @@protoc_insertion_point(module_scope)