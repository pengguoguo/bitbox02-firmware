# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: btc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='btc.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tbtc.proto\"\xe1\x01\n\rBTCPubRequest\x12\x0f\n\x07keypath\x18\x01 \x03(\r\x12#\n\x0bscript_type\x18\x02 \x01(\x0e\x32\x0e.BTCScriptType\x12\x16\n\x04\x63oin\x18\x03 \x01(\x0e\x32\x08.BTCCoin\x12.\n\x0boutput_type\x18\x04 \x01(\x0e\x32\x19.BTCPubRequest.OutputType\x12\x0f\n\x07\x64isplay\x18\x05 \x01(\x08\"A\n\nOutputType\x12\x08\n\x04TPUB\x10\x00\x12\x08\n\x04XPUB\x10\x01\x12\x08\n\x04YPUB\x10\x02\x12\x08\n\x04ZPUB\x10\x03\x12\x0b\n\x07\x41\x44\x44RESS\x10\x04\"\xb4\x01\n\x12\x42TCSignInitRequest\x12\x16\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x08.BTCCoin\x12#\n\x0bscript_type\x18\x02 \x01(\x0e\x32\x0e.BTCScriptType\x12\x15\n\rbip44_account\x18\x03 \x01(\r\x12\x0f\n\x07version\x18\x04 \x01(\r\x12\x12\n\nnum_inputs\x18\x05 \x01(\r\x12\x13\n\x0bnum_outputs\x18\x06 \x01(\r\x12\x10\n\x08locktime\x18\x07 \x01(\r\"\xa0\x01\n\x13\x42TCSignNextResponse\x12\'\n\x04type\x18\x01 \x01(\x0e\x32\x19.BTCSignNextResponse.Type\x12\r\n\x05index\x18\x02 \x01(\r\x12\x15\n\rhas_signature\x18\x03 \x01(\x08\x12\x11\n\tsignature\x18\x04 \x01(\x0c\"\'\n\x04Type\x12\t\n\x05INPUT\x10\x00\x12\n\n\x06OUTPUT\x10\x01\x12\x08\n\x04\x44ONE\x10\x02\"y\n\x13\x42TCSignInputRequest\x12\x13\n\x0bprevOutHash\x18\x01 \x01(\x0c\x12\x14\n\x0cprevOutIndex\x18\x02 \x01(\r\x12\x14\n\x0cprevOutValue\x18\x03 \x01(\x04\x12\x10\n\x08sequence\x18\x04 \x01(\r\x12\x0f\n\x07keypath\x18\x06 \x03(\r\"p\n\x14\x42TCSignOutputRequest\x12\x0c\n\x04ours\x18\x01 \x01(\x08\x12\x1c\n\x04type\x18\x02 \x01(\x0e\x32\x0e.BTCOutputType\x12\r\n\x05value\x18\x03 \x01(\x04\x12\x0c\n\x04hash\x18\x04 \x01(\x0c\x12\x0f\n\x07keypath\x18\x05 \x03(\r*/\n\x07\x42TCCoin\x12\x07\n\x03\x42TC\x10\x00\x12\x08\n\x04TBTC\x10\x01\x12\x07\n\x03LTC\x10\x02\x12\x08\n\x04TLTC\x10\x03*`\n\rBTCScriptType\x12\x12\n\x0eSCRIPT_UNKNOWN\x10\x00\x12\x10\n\x0cSCRIPT_P2PKH\x10\x01\x12\x16\n\x12SCRIPT_P2WPKH_P2SH\x10\x02\x12\x11\n\rSCRIPT_P2WPKH\x10\x03*H\n\rBTCOutputType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05P2PKH\x10\x01\x12\x08\n\x04P2SH\x10\x02\x12\n\n\x06P2WPKH\x10\x03\x12\t\n\x05P2WSH\x10\x04\x62\x06proto3')
)

_BTCCOIN = _descriptor.EnumDescriptor(
  name='BTCCoin',
  full_name='BTCCoin',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BTC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TBTC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LTC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TLTC', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=824,
  serialized_end=871,
)
_sym_db.RegisterEnumDescriptor(_BTCCOIN)

BTCCoin = enum_type_wrapper.EnumTypeWrapper(_BTCCOIN)
_BTCSCRIPTTYPE = _descriptor.EnumDescriptor(
  name='BTCScriptType',
  full_name='BTCScriptType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCRIPT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCRIPT_P2PKH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCRIPT_P2WPKH_P2SH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCRIPT_P2WPKH', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=873,
  serialized_end=969,
)
_sym_db.RegisterEnumDescriptor(_BTCSCRIPTTYPE)

BTCScriptType = enum_type_wrapper.EnumTypeWrapper(_BTCSCRIPTTYPE)
_BTCOUTPUTTYPE = _descriptor.EnumDescriptor(
  name='BTCOutputType',
  full_name='BTCOutputType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2PKH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2SH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2WPKH', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='P2WSH', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=971,
  serialized_end=1043,
)
_sym_db.RegisterEnumDescriptor(_BTCOUTPUTTYPE)

BTCOutputType = enum_type_wrapper.EnumTypeWrapper(_BTCOUTPUTTYPE)
BTC = 0
TBTC = 1
LTC = 2
TLTC = 3
SCRIPT_UNKNOWN = 0
SCRIPT_P2PKH = 1
SCRIPT_P2WPKH_P2SH = 2
SCRIPT_P2WPKH = 3
UNKNOWN = 0
P2PKH = 1
P2SH = 2
P2WPKH = 3
P2WSH = 4


_BTCPUBREQUEST_OUTPUTTYPE = _descriptor.EnumDescriptor(
  name='OutputType',
  full_name='BTCPubRequest.OutputType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TPUB', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XPUB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YPUB', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZPUB', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=174,
  serialized_end=239,
)
_sym_db.RegisterEnumDescriptor(_BTCPUBREQUEST_OUTPUTTYPE)

_BTCSIGNNEXTRESPONSE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='BTCSignNextResponse.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INPUT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=546,
  serialized_end=585,
)
_sym_db.RegisterEnumDescriptor(_BTCSIGNNEXTRESPONSE_TYPE)


_BTCPUBREQUEST = _descriptor.Descriptor(
  name='BTCPubRequest',
  full_name='BTCPubRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keypath', full_name='BTCPubRequest.keypath', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script_type', full_name='BTCPubRequest.script_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coin', full_name='BTCPubRequest.coin', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_type', full_name='BTCPubRequest.output_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display', full_name='BTCPubRequest.display', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BTCPUBREQUEST_OUTPUTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=239,
)


_BTCSIGNINITREQUEST = _descriptor.Descriptor(
  name='BTCSignInitRequest',
  full_name='BTCSignInitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin', full_name='BTCSignInitRequest.coin', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='script_type', full_name='BTCSignInitRequest.script_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bip44_account', full_name='BTCSignInitRequest.bip44_account', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='BTCSignInitRequest.version', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_inputs', full_name='BTCSignInitRequest.num_inputs', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_outputs', full_name='BTCSignInitRequest.num_outputs', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locktime', full_name='BTCSignInitRequest.locktime', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=242,
  serialized_end=422,
)


_BTCSIGNNEXTRESPONSE = _descriptor.Descriptor(
  name='BTCSignNextResponse',
  full_name='BTCSignNextResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='BTCSignNextResponse.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='BTCSignNextResponse.index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_signature', full_name='BTCSignNextResponse.has_signature', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='BTCSignNextResponse.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BTCSIGNNEXTRESPONSE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=585,
)


_BTCSIGNINPUTREQUEST = _descriptor.Descriptor(
  name='BTCSignInputRequest',
  full_name='BTCSignInputRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prevOutHash', full_name='BTCSignInputRequest.prevOutHash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevOutIndex', full_name='BTCSignInputRequest.prevOutIndex', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prevOutValue', full_name='BTCSignInputRequest.prevOutValue', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='BTCSignInputRequest.sequence', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keypath', full_name='BTCSignInputRequest.keypath', index=4,
      number=6, type=13, cpp_type=3, label=3,
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
  serialized_start=587,
  serialized_end=708,
)


_BTCSIGNOUTPUTREQUEST = _descriptor.Descriptor(
  name='BTCSignOutputRequest',
  full_name='BTCSignOutputRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ours', full_name='BTCSignOutputRequest.ours', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='BTCSignOutputRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='BTCSignOutputRequest.value', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='BTCSignOutputRequest.hash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keypath', full_name='BTCSignOutputRequest.keypath', index=4,
      number=5, type=13, cpp_type=3, label=3,
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
  serialized_start=710,
  serialized_end=822,
)

_BTCPUBREQUEST.fields_by_name['script_type'].enum_type = _BTCSCRIPTTYPE
_BTCPUBREQUEST.fields_by_name['coin'].enum_type = _BTCCOIN
_BTCPUBREQUEST.fields_by_name['output_type'].enum_type = _BTCPUBREQUEST_OUTPUTTYPE
_BTCPUBREQUEST_OUTPUTTYPE.containing_type = _BTCPUBREQUEST
_BTCSIGNINITREQUEST.fields_by_name['coin'].enum_type = _BTCCOIN
_BTCSIGNINITREQUEST.fields_by_name['script_type'].enum_type = _BTCSCRIPTTYPE
_BTCSIGNNEXTRESPONSE.fields_by_name['type'].enum_type = _BTCSIGNNEXTRESPONSE_TYPE
_BTCSIGNNEXTRESPONSE_TYPE.containing_type = _BTCSIGNNEXTRESPONSE
_BTCSIGNOUTPUTREQUEST.fields_by_name['type'].enum_type = _BTCOUTPUTTYPE
DESCRIPTOR.message_types_by_name['BTCPubRequest'] = _BTCPUBREQUEST
DESCRIPTOR.message_types_by_name['BTCSignInitRequest'] = _BTCSIGNINITREQUEST
DESCRIPTOR.message_types_by_name['BTCSignNextResponse'] = _BTCSIGNNEXTRESPONSE
DESCRIPTOR.message_types_by_name['BTCSignInputRequest'] = _BTCSIGNINPUTREQUEST
DESCRIPTOR.message_types_by_name['BTCSignOutputRequest'] = _BTCSIGNOUTPUTREQUEST
DESCRIPTOR.enum_types_by_name['BTCCoin'] = _BTCCOIN
DESCRIPTOR.enum_types_by_name['BTCScriptType'] = _BTCSCRIPTTYPE
DESCRIPTOR.enum_types_by_name['BTCOutputType'] = _BTCOUTPUTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BTCPubRequest = _reflection.GeneratedProtocolMessageType('BTCPubRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCPUBREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:BTCPubRequest)
  ))
_sym_db.RegisterMessage(BTCPubRequest)

BTCSignInitRequest = _reflection.GeneratedProtocolMessageType('BTCSignInitRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCSIGNINITREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:BTCSignInitRequest)
  ))
_sym_db.RegisterMessage(BTCSignInitRequest)

BTCSignNextResponse = _reflection.GeneratedProtocolMessageType('BTCSignNextResponse', (_message.Message,), dict(
  DESCRIPTOR = _BTCSIGNNEXTRESPONSE,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:BTCSignNextResponse)
  ))
_sym_db.RegisterMessage(BTCSignNextResponse)

BTCSignInputRequest = _reflection.GeneratedProtocolMessageType('BTCSignInputRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCSIGNINPUTREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:BTCSignInputRequest)
  ))
_sym_db.RegisterMessage(BTCSignInputRequest)

BTCSignOutputRequest = _reflection.GeneratedProtocolMessageType('BTCSignOutputRequest', (_message.Message,), dict(
  DESCRIPTOR = _BTCSIGNOUTPUTREQUEST,
  __module__ = 'btc_pb2'
  # @@protoc_insertion_point(class_scope:BTCSignOutputRequest)
  ))
_sym_db.RegisterMessage(BTCSignOutputRequest)


# @@protoc_insertion_point(module_scope)
