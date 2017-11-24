# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qrllegacy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import qrl.generated.qrl_pb2 as qrl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qrllegacy.proto',
  package='qrl',
  syntax='proto3',
  serialized_pb=_b('\n\x0fqrllegacy.proto\x12\x03qrl\x1a\tqrl.proto\"\x93\x04\n\rLegacyMessage\x12.\n\tfunc_name\x18\x01 \x01(\x0e\x32\x1b.qrl.LegacyMessage.FuncName\x12\x1d\n\x06noData\x18\x02 \x01(\x0b\x32\x0b.qrl.NoDataH\x00\x12\x1d\n\x06veData\x18\x03 \x01(\x0b\x32\x0b.qrl.VEDataH\x00\x12!\n\x08pongData\x18\x04 \x01(\x0b\x32\r.qrl.PONGDataH\x00\x12\x1d\n\x06mrData\x18\x05 \x01(\x0b\x32\x0b.qrl.MRDataH\x00\x12\x1e\n\x07sfmData\x18\x06 \x01(\x0b\x32\x0b.qrl.MRDataH\x00\x12\x1d\n\x06\x62kData\x18\x07 \x01(\x0b\x32\x0b.qrl.BKDataH\x00\x12\x1d\n\x06\x66\x62\x44\x61ta\x18\x08 \x01(\x0b\x32\x0b.qrl.FBDataH\x00\x12\x1d\n\x06pbData\x18\t \x01(\x0b\x32\x0b.qrl.PBDataH\x00\x12\x1e\n\x07pbbData\x18\n \x01(\x0b\x32\x0b.qrl.PBDataH\x00\x12!\n\x08syncData\x18\x63 \x01(\x0b\x32\r.qrl.SYNCDataH\x00\"\x89\x01\n\x08\x46uncName\x12\x06\n\x02VE\x10\x00\x12\x06\n\x02PL\x10\x01\x12\x08\n\x04PONG\x10\x02\x12\x06\n\x02MR\x10\x03\x12\x07\n\x03SFM\x10\x04\x12\x06\n\x02\x42K\x10\x05\x12\x06\n\x02\x46\x42\x10\x06\x12\x06\n\x02PB\x10\x07\x12\x07\n\x03PBB\x10\x08\x12\x06\n\x02ST\x10\t\x12\x07\n\x03\x44ST\x10\n\x12\x06\n\x02\x44T\x10\x0b\x12\x06\n\x02TX\x10\x0c\x12\x06\n\x02VT\x10\r\x12\x08\n\x04SYNC\x10\x0e\x42\x06\n\x04\x64\x61ta\"\x08\n\x06NoData\"4\n\x06VEData\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x19\n\x11genesis_prev_hash\x18\x02 \x01(\x0c\"\x1a\n\x06PLData\x12\x10\n\x08peer_ips\x18\x01 \x03(\t\"\n\n\x08PONGData\"\x9d\x01\n\x06MRData\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.qrl.LegacyMessage.FuncName\x12\x16\n\x0estake_selector\x18\x03 \x01(\x0c\x12\x14\n\x0c\x62lock_number\x18\x04 \x01(\x04\x12\x17\n\x0fprev_headerhash\x18\x05 \x01(\x0c\x12\x13\n\x0breveal_hash\x18\x06 \x01(\x0c\"@\n\x06\x42KData\x12\x1b\n\x06mrData\x18\x01 \x01(\x0b\x32\x0b.qrl.MRData\x12\x19\n\x05\x62lock\x18\x02 \x01(\x0b\x32\n.qrl.Block\"\x17\n\x06\x46\x42\x44\x61ta\x12\r\n\x05index\x18\x01 \x01(\x04\"2\n\x06PBData\x12\r\n\x05index\x18\x01 \x01(\x04\x12\x19\n\x05\x62lock\x18\x02 \x01(\x0b\x32\n.qrl.Block\"\n\n\x08SYNCDatab\x06proto3')
  ,
  dependencies=[qrl__pb2.DESCRIPTOR,])



_LEGACYMESSAGE_FUNCNAME = _descriptor.EnumDescriptor(
  name='FuncName',
  full_name='qrl.LegacyMessage.FuncName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PONG', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFM', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BK', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FB', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PB', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PBB', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ST', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DST', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TX', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VT', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC', index=14, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=422,
  serialized_end=559,
)
_sym_db.RegisterEnumDescriptor(_LEGACYMESSAGE_FUNCNAME)


_LEGACYMESSAGE = _descriptor.Descriptor(
  name='LegacyMessage',
  full_name='qrl.LegacyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='func_name', full_name='qrl.LegacyMessage.func_name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='noData', full_name='qrl.LegacyMessage.noData', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='veData', full_name='qrl.LegacyMessage.veData', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pongData', full_name='qrl.LegacyMessage.pongData', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mrData', full_name='qrl.LegacyMessage.mrData', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sfmData', full_name='qrl.LegacyMessage.sfmData', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bkData', full_name='qrl.LegacyMessage.bkData', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fbData', full_name='qrl.LegacyMessage.fbData', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pbData', full_name='qrl.LegacyMessage.pbData', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pbbData', full_name='qrl.LegacyMessage.pbbData', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='syncData', full_name='qrl.LegacyMessage.syncData', index=10,
      number=99, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEGACYMESSAGE_FUNCNAME,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='qrl.LegacyMessage.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=36,
  serialized_end=567,
)


_NODATA = _descriptor.Descriptor(
  name='NoData',
  full_name='qrl.NoData',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=577,
)


_VEDATA = _descriptor.Descriptor(
  name='VEData',
  full_name='qrl.VEData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='qrl.VEData.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genesis_prev_hash', full_name='qrl.VEData.genesis_prev_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=579,
  serialized_end=631,
)


_PLDATA = _descriptor.Descriptor(
  name='PLData',
  full_name='qrl.PLData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer_ips', full_name='qrl.PLData.peer_ips', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=633,
  serialized_end=659,
)


_PONGDATA = _descriptor.Descriptor(
  name='PONGData',
  full_name='qrl.PONGData',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=671,
)


_MRDATA = _descriptor.Descriptor(
  name='MRData',
  full_name='qrl.MRData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='qrl.MRData.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='qrl.MRData.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stake_selector', full_name='qrl.MRData.stake_selector', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block_number', full_name='qrl.MRData.block_number', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev_headerhash', full_name='qrl.MRData.prev_headerhash', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reveal_hash', full_name='qrl.MRData.reveal_hash', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=674,
  serialized_end=831,
)


_BKDATA = _descriptor.Descriptor(
  name='BKData',
  full_name='qrl.BKData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mrData', full_name='qrl.BKData.mrData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='qrl.BKData.block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=833,
  serialized_end=897,
)


_FBDATA = _descriptor.Descriptor(
  name='FBData',
  full_name='qrl.FBData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='qrl.FBData.index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=899,
  serialized_end=922,
)


_PBDATA = _descriptor.Descriptor(
  name='PBData',
  full_name='qrl.PBData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='qrl.PBData.index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block', full_name='qrl.PBData.block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=924,
  serialized_end=974,
)


_SYNCDATA = _descriptor.Descriptor(
  name='SYNCData',
  full_name='qrl.SYNCData',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=976,
  serialized_end=986,
)

_LEGACYMESSAGE.fields_by_name['func_name'].enum_type = _LEGACYMESSAGE_FUNCNAME
_LEGACYMESSAGE.fields_by_name['noData'].message_type = _NODATA
_LEGACYMESSAGE.fields_by_name['veData'].message_type = _VEDATA
_LEGACYMESSAGE.fields_by_name['pongData'].message_type = _PONGDATA
_LEGACYMESSAGE.fields_by_name['mrData'].message_type = _MRDATA
_LEGACYMESSAGE.fields_by_name['sfmData'].message_type = _MRDATA
_LEGACYMESSAGE.fields_by_name['bkData'].message_type = _BKDATA
_LEGACYMESSAGE.fields_by_name['fbData'].message_type = _FBDATA
_LEGACYMESSAGE.fields_by_name['pbData'].message_type = _PBDATA
_LEGACYMESSAGE.fields_by_name['pbbData'].message_type = _PBDATA
_LEGACYMESSAGE.fields_by_name['syncData'].message_type = _SYNCDATA
_LEGACYMESSAGE_FUNCNAME.containing_type = _LEGACYMESSAGE
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['noData'])
_LEGACYMESSAGE.fields_by_name['noData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['veData'])
_LEGACYMESSAGE.fields_by_name['veData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['pongData'])
_LEGACYMESSAGE.fields_by_name['pongData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['mrData'])
_LEGACYMESSAGE.fields_by_name['mrData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['sfmData'])
_LEGACYMESSAGE.fields_by_name['sfmData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['bkData'])
_LEGACYMESSAGE.fields_by_name['bkData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['fbData'])
_LEGACYMESSAGE.fields_by_name['fbData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['pbData'])
_LEGACYMESSAGE.fields_by_name['pbData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['pbbData'])
_LEGACYMESSAGE.fields_by_name['pbbData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_LEGACYMESSAGE.oneofs_by_name['data'].fields.append(
  _LEGACYMESSAGE.fields_by_name['syncData'])
_LEGACYMESSAGE.fields_by_name['syncData'].containing_oneof = _LEGACYMESSAGE.oneofs_by_name['data']
_MRDATA.fields_by_name['type'].enum_type = _LEGACYMESSAGE_FUNCNAME
_BKDATA.fields_by_name['mrData'].message_type = _MRDATA
_BKDATA.fields_by_name['block'].message_type = qrl__pb2._BLOCK
_PBDATA.fields_by_name['block'].message_type = qrl__pb2._BLOCK
DESCRIPTOR.message_types_by_name['LegacyMessage'] = _LEGACYMESSAGE
DESCRIPTOR.message_types_by_name['NoData'] = _NODATA
DESCRIPTOR.message_types_by_name['VEData'] = _VEDATA
DESCRIPTOR.message_types_by_name['PLData'] = _PLDATA
DESCRIPTOR.message_types_by_name['PONGData'] = _PONGDATA
DESCRIPTOR.message_types_by_name['MRData'] = _MRDATA
DESCRIPTOR.message_types_by_name['BKData'] = _BKDATA
DESCRIPTOR.message_types_by_name['FBData'] = _FBDATA
DESCRIPTOR.message_types_by_name['PBData'] = _PBDATA
DESCRIPTOR.message_types_by_name['SYNCData'] = _SYNCDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LegacyMessage = _reflection.GeneratedProtocolMessageType('LegacyMessage', (_message.Message,), dict(
  DESCRIPTOR = _LEGACYMESSAGE,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.LegacyMessage)
  ))
_sym_db.RegisterMessage(LegacyMessage)

NoData = _reflection.GeneratedProtocolMessageType('NoData', (_message.Message,), dict(
  DESCRIPTOR = _NODATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.NoData)
  ))
_sym_db.RegisterMessage(NoData)

VEData = _reflection.GeneratedProtocolMessageType('VEData', (_message.Message,), dict(
  DESCRIPTOR = _VEDATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.VEData)
  ))
_sym_db.RegisterMessage(VEData)

PLData = _reflection.GeneratedProtocolMessageType('PLData', (_message.Message,), dict(
  DESCRIPTOR = _PLDATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.PLData)
  ))
_sym_db.RegisterMessage(PLData)

PONGData = _reflection.GeneratedProtocolMessageType('PONGData', (_message.Message,), dict(
  DESCRIPTOR = _PONGDATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.PONGData)
  ))
_sym_db.RegisterMessage(PONGData)

MRData = _reflection.GeneratedProtocolMessageType('MRData', (_message.Message,), dict(
  DESCRIPTOR = _MRDATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.MRData)
  ))
_sym_db.RegisterMessage(MRData)

BKData = _reflection.GeneratedProtocolMessageType('BKData', (_message.Message,), dict(
  DESCRIPTOR = _BKDATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.BKData)
  ))
_sym_db.RegisterMessage(BKData)

FBData = _reflection.GeneratedProtocolMessageType('FBData', (_message.Message,), dict(
  DESCRIPTOR = _FBDATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.FBData)
  ))
_sym_db.RegisterMessage(FBData)

PBData = _reflection.GeneratedProtocolMessageType('PBData', (_message.Message,), dict(
  DESCRIPTOR = _PBDATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.PBData)
  ))
_sym_db.RegisterMessage(PBData)

SYNCData = _reflection.GeneratedProtocolMessageType('SYNCData', (_message.Message,), dict(
  DESCRIPTOR = _SYNCDATA,
  __module__ = 'qrllegacy_pb2'
  # @@protoc_insertion_point(class_scope:qrl.SYNCData)
  ))
_sym_db.RegisterMessage(SYNCData)


# @@protoc_insertion_point(module_scope)
