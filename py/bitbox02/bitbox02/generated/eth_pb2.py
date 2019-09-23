# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='eth.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\teth.proto\x1a\x0c\x63ommon.proto\"\xb8\x01\n\rETHPubRequest\x12\x0f\n\x07keypath\x18\x01 \x03(\r\x12\x16\n\x04\x63oin\x18\x02 \x01(\x0e\x32\x08.ETHCoin\x12.\n\x0boutput_type\x18\x03 \x01(\x0e\x32\x19.ETHPubRequest.OutputType\x12\x0f\n\x07\x64isplay\x18\x04 \x01(\x08\x12\x18\n\x10\x63ontract_address\x18\x05 \x01(\x0c\"#\n\nOutputType\x12\x0b\n\x07\x41\x44\x44RESS\x10\x00\x12\x08\n\x04XPUB\x10\x01\"\x9e\x01\n\x0e\x45THSignRequest\x12\x16\n\x04\x63oin\x18\x01 \x01(\x0e\x32\x08.ETHCoin\x12\x0f\n\x07keypath\x18\x02 \x03(\r\x12\r\n\x05nonce\x18\x03 \x01(\x0c\x12\x11\n\tgas_price\x18\x04 \x01(\x0c\x12\x11\n\tgas_limit\x18\x05 \x01(\x0c\x12\x11\n\trecipient\x18\x06 \x01(\x0c\x12\r\n\x05value\x18\x07 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x08 \x01(\x0c\"$\n\x0f\x45THSignResponse\x12\x11\n\tsignature\x18\x01 \x01(\x0c\"W\n\nETHRequest\x12\x1d\n\x03pub\x18\x01 \x01(\x0b\x32\x0e.ETHPubRequestH\x00\x12\x1f\n\x04sign\x18\x02 \x01(\x0b\x32\x0f.ETHSignRequestH\x00\x42\t\n\x07request\"X\n\x0b\x45THResponse\x12\x1b\n\x03pub\x18\x01 \x01(\x0b\x32\x0c.PubResponseH\x00\x12 \n\x04sign\x18\x02 \x01(\x0b\x32\x10.ETHSignResponseH\x00\x42\n\n\x08response*2\n\x07\x45THCoin\x12\x07\n\x03\x45TH\x10\x00\x12\x0e\n\nRopstenETH\x10\x01\x12\x0e\n\nRinkebyETH\x10\x02\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_ETHCOIN = _descriptor.EnumDescriptor(
  name='ETHCoin',
  full_name='ETHCoin',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ETH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RopstenETH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RinkebyETH', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=592,
  serialized_end=642,
)
_sym_db.RegisterEnumDescriptor(_ETHCOIN)

ETHCoin = enum_type_wrapper.EnumTypeWrapper(_ETHCOIN)
ETH = 0
RopstenETH = 1
RinkebyETH = 2


_ETHPUBREQUEST_OUTPUTTYPE = _descriptor.EnumDescriptor(
  name='OutputType',
  full_name='ETHPubRequest.OutputType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADDRESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XPUB', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=177,
  serialized_end=212,
)
_sym_db.RegisterEnumDescriptor(_ETHPUBREQUEST_OUTPUTTYPE)


_ETHPUBREQUEST = _descriptor.Descriptor(
  name='ETHPubRequest',
  full_name='ETHPubRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keypath', full_name='ETHPubRequest.keypath', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coin', full_name='ETHPubRequest.coin', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_type', full_name='ETHPubRequest.output_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display', full_name='ETHPubRequest.display', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract_address', full_name='ETHPubRequest.contract_address', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ETHPUBREQUEST_OUTPUTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=212,
)


_ETHSIGNREQUEST = _descriptor.Descriptor(
  name='ETHSignRequest',
  full_name='ETHSignRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin', full_name='ETHSignRequest.coin', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keypath', full_name='ETHSignRequest.keypath', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='ETHSignRequest.nonce', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_price', full_name='ETHSignRequest.gas_price', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_limit', full_name='ETHSignRequest.gas_limit', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='ETHSignRequest.recipient', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ETHSignRequest.value', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='ETHSignRequest.data', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=215,
  serialized_end=373,
)


_ETHSIGNRESPONSE = _descriptor.Descriptor(
  name='ETHSignResponse',
  full_name='ETHSignResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='ETHSignResponse.signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=375,
  serialized_end=411,
)


_ETHREQUEST = _descriptor.Descriptor(
  name='ETHRequest',
  full_name='ETHRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub', full_name='ETHRequest.pub', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign', full_name='ETHRequest.sign', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
      name='request', full_name='ETHRequest.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=413,
  serialized_end=500,
)


_ETHRESPONSE = _descriptor.Descriptor(
  name='ETHResponse',
  full_name='ETHResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub', full_name='ETHResponse.pub', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign', full_name='ETHResponse.sign', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
      name='response', full_name='ETHResponse.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=502,
  serialized_end=590,
)

_ETHPUBREQUEST.fields_by_name['coin'].enum_type = _ETHCOIN
_ETHPUBREQUEST.fields_by_name['output_type'].enum_type = _ETHPUBREQUEST_OUTPUTTYPE
_ETHPUBREQUEST_OUTPUTTYPE.containing_type = _ETHPUBREQUEST
_ETHSIGNREQUEST.fields_by_name['coin'].enum_type = _ETHCOIN
_ETHREQUEST.fields_by_name['pub'].message_type = _ETHPUBREQUEST
_ETHREQUEST.fields_by_name['sign'].message_type = _ETHSIGNREQUEST
_ETHREQUEST.oneofs_by_name['request'].fields.append(
  _ETHREQUEST.fields_by_name['pub'])
_ETHREQUEST.fields_by_name['pub'].containing_oneof = _ETHREQUEST.oneofs_by_name['request']
_ETHREQUEST.oneofs_by_name['request'].fields.append(
  _ETHREQUEST.fields_by_name['sign'])
_ETHREQUEST.fields_by_name['sign'].containing_oneof = _ETHREQUEST.oneofs_by_name['request']
_ETHRESPONSE.fields_by_name['pub'].message_type = common__pb2._PUBRESPONSE
_ETHRESPONSE.fields_by_name['sign'].message_type = _ETHSIGNRESPONSE
_ETHRESPONSE.oneofs_by_name['response'].fields.append(
  _ETHRESPONSE.fields_by_name['pub'])
_ETHRESPONSE.fields_by_name['pub'].containing_oneof = _ETHRESPONSE.oneofs_by_name['response']
_ETHRESPONSE.oneofs_by_name['response'].fields.append(
  _ETHRESPONSE.fields_by_name['sign'])
_ETHRESPONSE.fields_by_name['sign'].containing_oneof = _ETHRESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['ETHPubRequest'] = _ETHPUBREQUEST
DESCRIPTOR.message_types_by_name['ETHSignRequest'] = _ETHSIGNREQUEST
DESCRIPTOR.message_types_by_name['ETHSignResponse'] = _ETHSIGNRESPONSE
DESCRIPTOR.message_types_by_name['ETHRequest'] = _ETHREQUEST
DESCRIPTOR.message_types_by_name['ETHResponse'] = _ETHRESPONSE
DESCRIPTOR.enum_types_by_name['ETHCoin'] = _ETHCOIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ETHPubRequest = _reflection.GeneratedProtocolMessageType('ETHPubRequest', (_message.Message,), dict(
  DESCRIPTOR = _ETHPUBREQUEST,
  __module__ = 'eth_pb2'
  # @@protoc_insertion_point(class_scope:ETHPubRequest)
  ))
_sym_db.RegisterMessage(ETHPubRequest)

ETHSignRequest = _reflection.GeneratedProtocolMessageType('ETHSignRequest', (_message.Message,), dict(
  DESCRIPTOR = _ETHSIGNREQUEST,
  __module__ = 'eth_pb2'
  # @@protoc_insertion_point(class_scope:ETHSignRequest)
  ))
_sym_db.RegisterMessage(ETHSignRequest)

ETHSignResponse = _reflection.GeneratedProtocolMessageType('ETHSignResponse', (_message.Message,), dict(
  DESCRIPTOR = _ETHSIGNRESPONSE,
  __module__ = 'eth_pb2'
  # @@protoc_insertion_point(class_scope:ETHSignResponse)
  ))
_sym_db.RegisterMessage(ETHSignResponse)

ETHRequest = _reflection.GeneratedProtocolMessageType('ETHRequest', (_message.Message,), dict(
  DESCRIPTOR = _ETHREQUEST,
  __module__ = 'eth_pb2'
  # @@protoc_insertion_point(class_scope:ETHRequest)
  ))
_sym_db.RegisterMessage(ETHRequest)

ETHResponse = _reflection.GeneratedProtocolMessageType('ETHResponse', (_message.Message,), dict(
  DESCRIPTOR = _ETHRESPONSE,
  __module__ = 'eth_pb2'
  # @@protoc_insertion_point(class_scope:ETHResponse)
  ))
_sym_db.RegisterMessage(ETHResponse)


# @@protoc_insertion_point(module_scope)
