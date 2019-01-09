# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/geo_target_constant_suggestion_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/geo_target_constant_suggestion_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\nOgoogle/ads/googleads_v0/proto/errors/geo_target_constant_suggestion_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xd8\x01\n$GeoTargetConstantSuggestionErrorEnum\"\xaf\x01\n GeoTargetConstantSuggestionError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1c\n\x18LOCATION_NAME_SIZE_LIMIT\x10\x02\x12\x17\n\x13LOCATION_NAME_LIMIT\x10\x03\x12\x18\n\x14INVALID_COUNTRY_CODE\x10\x04\x12\x1c\n\x18REQUEST_PARAMETERS_UNSET\x10\x05\x42\xdb\x01\n\"com.google.ads.googleads.v0.errorsB%GeoTargetConstantSuggestionErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_GEOTARGETCONSTANTSUGGESTIONERRORENUM_GEOTARGETCONSTANTSUGGESTIONERROR = _descriptor.EnumDescriptor(
  name='GeoTargetConstantSuggestionError',
  full_name='google.ads.googleads.v0.errors.GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_NAME_SIZE_LIMIT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_NAME_LIMIT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_COUNTRY_CODE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_PARAMETERS_UNSET', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=157,
  serialized_end=332,
)
_sym_db.RegisterEnumDescriptor(_GEOTARGETCONSTANTSUGGESTIONERRORENUM_GEOTARGETCONSTANTSUGGESTIONERROR)


_GEOTARGETCONSTANTSUGGESTIONERRORENUM = _descriptor.Descriptor(
  name='GeoTargetConstantSuggestionErrorEnum',
  full_name='google.ads.googleads.v0.errors.GeoTargetConstantSuggestionErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GEOTARGETCONSTANTSUGGESTIONERRORENUM_GEOTARGETCONSTANTSUGGESTIONERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=332,
)

_GEOTARGETCONSTANTSUGGESTIONERRORENUM_GEOTARGETCONSTANTSUGGESTIONERROR.containing_type = _GEOTARGETCONSTANTSUGGESTIONERRORENUM
DESCRIPTOR.message_types_by_name['GeoTargetConstantSuggestionErrorEnum'] = _GEOTARGETCONSTANTSUGGESTIONERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeoTargetConstantSuggestionErrorEnum = _reflection.GeneratedProtocolMessageType('GeoTargetConstantSuggestionErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _GEOTARGETCONSTANTSUGGESTIONERRORENUM,
  __module__ = 'google.ads.google_ads.v0.proto.errors.geo_target_constant_suggestion_error_pb2'
  ,
  __doc__ = """Container for enum describing possible geo target constant suggestion
  errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.GeoTargetConstantSuggestionErrorEnum)
  ))
_sym_db.RegisterMessage(GeoTargetConstantSuggestionErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB%GeoTargetConstantSuggestionErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)