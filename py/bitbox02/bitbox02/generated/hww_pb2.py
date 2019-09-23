# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hww.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from . import backup_commands_pb2 as backup__commands__pb2
from . import bitbox02_system_pb2 as bitbox02__system__pb2
from . import btc_pb2 as btc__pb2
from . import eth_pb2 as eth__pb2
from . import mnemonic_pb2 as mnemonic__pb2
from . import random_number_pb2 as random__number__pb2
from . import system_pb2 as system__pb2
from . import perform_attestation_pb2 as perform__attestation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hww.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\thww.proto\x1a\x0c\x63ommon.proto\x1a\x15\x62\x61\x63kup_commands.proto\x1a\x15\x62itbox02_system.proto\x1a\tbtc.proto\x1a\teth.proto\x1a\x0emnemonic.proto\x1a\x13random_number.proto\x1a\x0csystem.proto\x1a\x19perform_attestation.proto\"&\n\x05\x45rror\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\t\n\x07Success\"\xac\x08\n\x07Request\x12-\n\rrandom_number\x18\x01 \x01(\x0b\x32\x14.RandomNumberRequestH\x00\x12,\n\x0b\x64\x65vice_name\x18\x02 \x01(\x0b\x32\x15.SetDeviceNameRequestH\x00\x12\x34\n\x0f\x64\x65vice_language\x18\x03 \x01(\x0b\x32\x19.SetDeviceLanguageRequestH\x00\x12)\n\x0b\x64\x65vice_info\x18\x04 \x01(\x0b\x32\x12.DeviceInfoRequestH\x00\x12+\n\x0cset_password\x18\x05 \x01(\x0b\x32\x13.SetPasswordRequestH\x00\x12-\n\rcreate_backup\x18\x06 \x01(\x0b\x32\x14.CreateBackupRequestH\x00\x12-\n\rshow_mnemonic\x18\x07 \x01(\x0b\x32\x14.ShowMnemonicRequestH\x00\x12!\n\x07\x62tc_pub\x18\x08 \x01(\x0b\x32\x0e.BTCPubRequestH\x00\x12,\n\rbtc_sign_init\x18\t \x01(\x0b\x32\x13.BTCSignInitRequestH\x00\x12.\n\x0e\x62tc_sign_input\x18\n \x01(\x0b\x32\x14.BTCSignInputRequestH\x00\x12\x30\n\x0f\x62tc_sign_output\x18\x0b \x01(\x0b\x32\x15.BTCSignOutputRequestH\x00\x12:\n\x14insert_remove_sdcard\x18\x0c \x01(\x0b\x32\x1a.InsertRemoveSDCardRequestH\x00\x12+\n\x0c\x63heck_sdcard\x18\r \x01(\x0b\x32\x13.CheckSDCardRequestH\x00\x12O\n\x1fset_mnemonic_passphrase_enabled\x18\x0e \x01(\x0b\x32$.SetMnemonicPassphraseEnabledRequestH\x00\x12+\n\x0clist_backups\x18\x0f \x01(\x0b\x32\x13.ListBackupsRequestH\x00\x12/\n\x0erestore_backup\x18\x10 \x01(\x0b\x32\x15.RestoreBackupRequestH\x00\x12\x39\n\x13perform_attestation\x18\x11 \x01(\x0b\x32\x1a.PerformAttestationRequestH\x00\x12 \n\x06reboot\x18\x12 \x01(\x0b\x32\x0e.RebootRequestH\x00\x12+\n\x0c\x63heck_backup\x18\x13 \x01(\x0b\x32\x13.CheckBackupRequestH\x00\x12\x1a\n\x03\x65th\x18\x14 \x01(\x0b\x32\x0b.ETHRequestH\x00\x12\x1e\n\x05reset\x18\x15 \x01(\x0b\x32\r.ResetRequestH\x00\x12<\n\x15restore_from_mnemonic\x18\x16 \x01(\x0b\x32\x1b.RestoreFromMnemonicRequestH\x00\x42\t\n\x07request\"\xd7\x03\n\x08Response\x12\x1b\n\x07success\x18\x01 \x01(\x0b\x32\x08.SuccessH\x00\x12\x17\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x06.ErrorH\x00\x12.\n\rrandom_number\x18\x03 \x01(\x0b\x32\x15.RandomNumberResponseH\x00\x12*\n\x0b\x64\x65vice_info\x18\x04 \x01(\x0b\x32\x13.DeviceInfoResponseH\x00\x12\x1b\n\x03pub\x18\x05 \x01(\x0b\x32\x0c.PubResponseH\x00\x12-\n\rbtc_sign_next\x18\x06 \x01(\x0b\x32\x14.BTCSignNextResponseH\x00\x12,\n\x0clist_backups\x18\x07 \x01(\x0b\x32\x14.ListBackupsResponseH\x00\x12,\n\x0c\x63heck_backup\x18\x08 \x01(\x0b\x32\x14.CheckBackupResponseH\x00\x12:\n\x13perform_attestation\x18\t \x01(\x0b\x32\x1b.PerformAttestationResponseH\x00\x12,\n\x0c\x63heck_sdcard\x18\n \x01(\x0b\x32\x14.CheckSDCardResponseH\x00\x12\x1b\n\x03\x65th\x18\x0b \x01(\x0b\x32\x0c.ETHResponseH\x00\x42\n\n\x08responseb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,backup__commands__pb2.DESCRIPTOR,bitbox02__system__pb2.DESCRIPTOR,btc__pb2.DESCRIPTOR,eth__pb2.DESCRIPTOR,mnemonic__pb2.DESCRIPTOR,random__number__pb2.DESCRIPTOR,system__pb2.DESCRIPTOR,perform__attestation__pb2.DESCRIPTOR,])




_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Error.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='Error.message', index=1,
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
  ],
  serialized_start=173,
  serialized_end=211,
)


_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=213,
  serialized_end=222,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='random_number', full_name='Request.random_number', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='Request.device_name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_language', full_name='Request.device_language', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_info', full_name='Request.device_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_password', full_name='Request.set_password', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_backup', full_name='Request.create_backup', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_mnemonic', full_name='Request.show_mnemonic', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='btc_pub', full_name='Request.btc_pub', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='btc_sign_init', full_name='Request.btc_sign_init', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='btc_sign_input', full_name='Request.btc_sign_input', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='btc_sign_output', full_name='Request.btc_sign_output', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='insert_remove_sdcard', full_name='Request.insert_remove_sdcard', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='check_sdcard', full_name='Request.check_sdcard', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_mnemonic_passphrase_enabled', full_name='Request.set_mnemonic_passphrase_enabled', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_backups', full_name='Request.list_backups', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restore_backup', full_name='Request.restore_backup', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perform_attestation', full_name='Request.perform_attestation', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reboot', full_name='Request.reboot', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='check_backup', full_name='Request.check_backup', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eth', full_name='Request.eth', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset', full_name='Request.reset', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restore_from_mnemonic', full_name='Request.restore_from_mnemonic', index=21,
      number=22, type=11, cpp_type=10, label=1,
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
      name='request', full_name='Request.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=225,
  serialized_end=1293,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='Response.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='Response.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='random_number', full_name='Response.random_number', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_info', full_name='Response.device_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub', full_name='Response.pub', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='btc_sign_next', full_name='Response.btc_sign_next', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_backups', full_name='Response.list_backups', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='check_backup', full_name='Response.check_backup', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perform_attestation', full_name='Response.perform_attestation', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='check_sdcard', full_name='Response.check_sdcard', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eth', full_name='Response.eth', index=10,
      number=11, type=11, cpp_type=10, label=1,
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
      name='response', full_name='Response.response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1296,
  serialized_end=1767,
)

_REQUEST.fields_by_name['random_number'].message_type = random__number__pb2._RANDOMNUMBERREQUEST
_REQUEST.fields_by_name['device_name'].message_type = bitbox02__system__pb2._SETDEVICENAMEREQUEST
_REQUEST.fields_by_name['device_language'].message_type = bitbox02__system__pb2._SETDEVICELANGUAGEREQUEST
_REQUEST.fields_by_name['device_info'].message_type = bitbox02__system__pb2._DEVICEINFOREQUEST
_REQUEST.fields_by_name['set_password'].message_type = bitbox02__system__pb2._SETPASSWORDREQUEST
_REQUEST.fields_by_name['create_backup'].message_type = backup__commands__pb2._CREATEBACKUPREQUEST
_REQUEST.fields_by_name['show_mnemonic'].message_type = mnemonic__pb2._SHOWMNEMONICREQUEST
_REQUEST.fields_by_name['btc_pub'].message_type = btc__pb2._BTCPUBREQUEST
_REQUEST.fields_by_name['btc_sign_init'].message_type = btc__pb2._BTCSIGNINITREQUEST
_REQUEST.fields_by_name['btc_sign_input'].message_type = btc__pb2._BTCSIGNINPUTREQUEST
_REQUEST.fields_by_name['btc_sign_output'].message_type = btc__pb2._BTCSIGNOUTPUTREQUEST
_REQUEST.fields_by_name['insert_remove_sdcard'].message_type = bitbox02__system__pb2._INSERTREMOVESDCARDREQUEST
_REQUEST.fields_by_name['check_sdcard'].message_type = bitbox02__system__pb2._CHECKSDCARDREQUEST
_REQUEST.fields_by_name['set_mnemonic_passphrase_enabled'].message_type = mnemonic__pb2._SETMNEMONICPASSPHRASEENABLEDREQUEST
_REQUEST.fields_by_name['list_backups'].message_type = backup__commands__pb2._LISTBACKUPSREQUEST
_REQUEST.fields_by_name['restore_backup'].message_type = backup__commands__pb2._RESTOREBACKUPREQUEST
_REQUEST.fields_by_name['perform_attestation'].message_type = perform__attestation__pb2._PERFORMATTESTATIONREQUEST
_REQUEST.fields_by_name['reboot'].message_type = system__pb2._REBOOTREQUEST
_REQUEST.fields_by_name['check_backup'].message_type = backup__commands__pb2._CHECKBACKUPREQUEST
_REQUEST.fields_by_name['eth'].message_type = eth__pb2._ETHREQUEST
_REQUEST.fields_by_name['reset'].message_type = bitbox02__system__pb2._RESETREQUEST
_REQUEST.fields_by_name['restore_from_mnemonic'].message_type = mnemonic__pb2._RESTOREFROMMNEMONICREQUEST
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['random_number'])
_REQUEST.fields_by_name['random_number'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['device_name'])
_REQUEST.fields_by_name['device_name'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['device_language'])
_REQUEST.fields_by_name['device_language'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['device_info'])
_REQUEST.fields_by_name['device_info'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['set_password'])
_REQUEST.fields_by_name['set_password'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['create_backup'])
_REQUEST.fields_by_name['create_backup'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['show_mnemonic'])
_REQUEST.fields_by_name['show_mnemonic'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['btc_pub'])
_REQUEST.fields_by_name['btc_pub'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['btc_sign_init'])
_REQUEST.fields_by_name['btc_sign_init'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['btc_sign_input'])
_REQUEST.fields_by_name['btc_sign_input'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['btc_sign_output'])
_REQUEST.fields_by_name['btc_sign_output'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['insert_remove_sdcard'])
_REQUEST.fields_by_name['insert_remove_sdcard'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['check_sdcard'])
_REQUEST.fields_by_name['check_sdcard'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['set_mnemonic_passphrase_enabled'])
_REQUEST.fields_by_name['set_mnemonic_passphrase_enabled'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['list_backups'])
_REQUEST.fields_by_name['list_backups'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['restore_backup'])
_REQUEST.fields_by_name['restore_backup'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['perform_attestation'])
_REQUEST.fields_by_name['perform_attestation'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['reboot'])
_REQUEST.fields_by_name['reboot'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['check_backup'])
_REQUEST.fields_by_name['check_backup'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['eth'])
_REQUEST.fields_by_name['eth'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['reset'])
_REQUEST.fields_by_name['reset'].containing_oneof = _REQUEST.oneofs_by_name['request']
_REQUEST.oneofs_by_name['request'].fields.append(
  _REQUEST.fields_by_name['restore_from_mnemonic'])
_REQUEST.fields_by_name['restore_from_mnemonic'].containing_oneof = _REQUEST.oneofs_by_name['request']
_RESPONSE.fields_by_name['success'].message_type = _SUCCESS
_RESPONSE.fields_by_name['error'].message_type = _ERROR
_RESPONSE.fields_by_name['random_number'].message_type = random__number__pb2._RANDOMNUMBERRESPONSE
_RESPONSE.fields_by_name['device_info'].message_type = bitbox02__system__pb2._DEVICEINFORESPONSE
_RESPONSE.fields_by_name['pub'].message_type = common__pb2._PUBRESPONSE
_RESPONSE.fields_by_name['btc_sign_next'].message_type = btc__pb2._BTCSIGNNEXTRESPONSE
_RESPONSE.fields_by_name['list_backups'].message_type = backup__commands__pb2._LISTBACKUPSRESPONSE
_RESPONSE.fields_by_name['check_backup'].message_type = backup__commands__pb2._CHECKBACKUPRESPONSE
_RESPONSE.fields_by_name['perform_attestation'].message_type = perform__attestation__pb2._PERFORMATTESTATIONRESPONSE
_RESPONSE.fields_by_name['check_sdcard'].message_type = bitbox02__system__pb2._CHECKSDCARDRESPONSE
_RESPONSE.fields_by_name['eth'].message_type = eth__pb2._ETHRESPONSE
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['success'])
_RESPONSE.fields_by_name['success'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['error'])
_RESPONSE.fields_by_name['error'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['random_number'])
_RESPONSE.fields_by_name['random_number'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['device_info'])
_RESPONSE.fields_by_name['device_info'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['pub'])
_RESPONSE.fields_by_name['pub'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['btc_sign_next'])
_RESPONSE.fields_by_name['btc_sign_next'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['list_backups'])
_RESPONSE.fields_by_name['list_backups'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['check_backup'])
_RESPONSE.fields_by_name['check_backup'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['perform_attestation'])
_RESPONSE.fields_by_name['perform_attestation'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['check_sdcard'])
_RESPONSE.fields_by_name['check_sdcard'].containing_oneof = _RESPONSE.oneofs_by_name['response']
_RESPONSE.oneofs_by_name['response'].fields.append(
  _RESPONSE.fields_by_name['eth'])
_RESPONSE.fields_by_name['eth'].containing_oneof = _RESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'hww_pb2'
  # @@protoc_insertion_point(class_scope:Error)
  ))
_sym_db.RegisterMessage(Error)

Success = _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), dict(
  DESCRIPTOR = _SUCCESS,
  __module__ = 'hww_pb2'
  # @@protoc_insertion_point(class_scope:Success)
  ))
_sym_db.RegisterMessage(Success)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'hww_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'hww_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
