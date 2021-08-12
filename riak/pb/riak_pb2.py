# Copyright 2010-present Basho Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riak.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='riak.proto',
  package='',
  serialized_pb=b'\n\nriak.proto\"/\n\x0cRpbErrorResp\x12\x0e\n\x06\x65rrmsg\x18\x01 \x02(\x0c\x12\x0f\n\x07\x65rrcode\x18\x02 \x02(\r\"<\n\x14RpbGetServerInfoResp\x12\x0c\n\x04node\x18\x01 \x01(\x0c\x12\x16\n\x0eserver_version\x18\x02 \x01(\x0c\"%\n\x07RpbPair\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"/\n\x0fRpbGetBucketReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0c\n\x04type\x18\x02 \x01(\x0c\"2\n\x10RpbGetBucketResp\x12\x1e\n\x05props\x18\x01 \x02(\x0b\x32\x0f.RpbBucketProps\"O\n\x0fRpbSetBucketReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x1e\n\x05props\x18\x02 \x02(\x0b\x32\x0f.RpbBucketProps\x12\x0c\n\x04type\x18\x03 \x01(\x0c\"1\n\x11RpbResetBucketReq\x12\x0e\n\x06\x62ucket\x18\x01 \x02(\x0c\x12\x0c\n\x04type\x18\x02 \x01(\x0c\"#\n\x13RpbGetBucketTypeReq\x12\x0c\n\x04type\x18\x01 \x02(\x0c\"C\n\x13RpbSetBucketTypeReq\x12\x0c\n\x04type\x18\x01 \x02(\x0c\x12\x1e\n\x05props\x18\x02 \x02(\x0b\x32\x0f.RpbBucketProps\"-\n\tRpbModFun\x12\x0e\n\x06module\x18\x01 \x02(\x0c\x12\x10\n\x08\x66unction\x18\x02 \x02(\x0c\"9\n\rRpbCommitHook\x12\x1a\n\x06modfun\x18\x01 \x01(\x0b\x32\n.RpbModFun\x12\x0c\n\x04name\x18\x02 \x01(\x0c\"\xc7\x05\n\x0eRpbBucketProps\x12\r\n\x05n_val\x18\x01 \x01(\r\x12\x12\n\nallow_mult\x18\x02 \x01(\x08\x12\x17\n\x0flast_write_wins\x18\x03 \x01(\x08\x12!\n\tprecommit\x18\x04 \x03(\x0b\x32\x0e.RpbCommitHook\x12\x1c\n\rhas_precommit\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\"\n\npostcommit\x18\x06 \x03(\x0b\x32\x0e.RpbCommitHook\x12\x1d\n\x0ehas_postcommit\x18\x07 \x01(\x08:\x05\x66\x61lse\x12 \n\x0c\x63hash_keyfun\x18\x08 \x01(\x0b\x32\n.RpbModFun\x12\x1b\n\x07linkfun\x18\t \x01(\x0b\x32\n.RpbModFun\x12\x12\n\nold_vclock\x18\n \x01(\r\x12\x14\n\x0cyoung_vclock\x18\x0b \x01(\r\x12\x12\n\nbig_vclock\x18\x0c \x01(\r\x12\x14\n\x0csmall_vclock\x18\r \x01(\r\x12\n\n\x02pr\x18\x0e \x01(\r\x12\t\n\x01r\x18\x0f \x01(\r\x12\t\n\x01w\x18\x10 \x01(\r\x12\n\n\x02pw\x18\x11 \x01(\r\x12\n\n\x02\x64w\x18\x12 \x01(\r\x12\n\n\x02rw\x18\x13 \x01(\r\x12\x14\n\x0c\x62\x61sic_quorum\x18\x14 \x01(\x08\x12\x13\n\x0bnotfound_ok\x18\x15 \x01(\x08\x12\x0f\n\x07\x62\x61\x63kend\x18\x16 \x01(\x0c\x12\x0e\n\x06search\x18\x17 \x01(\x08\x12)\n\x04repl\x18\x18 \x01(\x0e\x32\x1b.RpbBucketProps.RpbReplMode\x12\x14\n\x0csearch_index\x18\x19 \x01(\x0c\x12\x10\n\x08\x64\x61tatype\x18\x1a \x01(\x0c\x12\x12\n\nconsistent\x18\x1b \x01(\x08\x12\x12\n\nwrite_once\x18\x1c \x01(\x08\x12\x15\n\rhll_precision\x18\x1d \x01(\r\">\n\x0bRpbReplMode\x12\t\n\x05\x46\x41LSE\x10\x00\x12\x0c\n\x08REALTIME\x10\x01\x12\x0c\n\x08\x46ULLSYNC\x10\x02\x12\x08\n\x04TRUE\x10\x03\",\n\nRpbAuthReq\x12\x0c\n\x04user\x18\x01 \x02(\x0c\x12\x10\n\x08password\x18\x02 \x02(\x0c\x42!\n\x17\x63om.basho.riak.protobufB\x06RiakPB')



_RPBBUCKETPROPS_RPBREPLMODE = _descriptor.EnumDescriptor(
  name='RpbReplMode',
  full_name='RpbBucketProps.RpbReplMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FALSE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REALTIME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULLSYNC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1259,
  serialized_end=1321,
)


_RPBERRORRESP = _descriptor.Descriptor(
  name='RpbErrorResp',
  full_name='RpbErrorResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='errmsg', full_name='RpbErrorResp.errmsg', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errcode', full_name='RpbErrorResp.errcode', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  serialized_start=14,
  serialized_end=61,
)


_RPBGETSERVERINFORESP = _descriptor.Descriptor(
  name='RpbGetServerInfoResp',
  full_name='RpbGetServerInfoResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='RpbGetServerInfoResp.node', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_version', full_name='RpbGetServerInfoResp.server_version', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=63,
  serialized_end=123,
)


_RPBPAIR = _descriptor.Descriptor(
  name='RpbPair',
  full_name='RpbPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='RpbPair.key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='RpbPair.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=125,
  serialized_end=162,
)


_RPBGETBUCKETREQ = _descriptor.Descriptor(
  name='RpbGetBucketReq',
  full_name='RpbGetBucketReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='RpbGetBucketReq.bucket', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='RpbGetBucketReq.type', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=164,
  serialized_end=211,
)


_RPBGETBUCKETRESP = _descriptor.Descriptor(
  name='RpbGetBucketResp',
  full_name='RpbGetBucketResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='props', full_name='RpbGetBucketResp.props', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=213,
  serialized_end=263,
)


_RPBSETBUCKETREQ = _descriptor.Descriptor(
  name='RpbSetBucketReq',
  full_name='RpbSetBucketReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='RpbSetBucketReq.bucket', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='props', full_name='RpbSetBucketReq.props', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='RpbSetBucketReq.type', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=265,
  serialized_end=344,
)


_RPBRESETBUCKETREQ = _descriptor.Descriptor(
  name='RpbResetBucketReq',
  full_name='RpbResetBucketReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='RpbResetBucketReq.bucket', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='RpbResetBucketReq.type', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=346,
  serialized_end=395,
)


_RPBGETBUCKETTYPEREQ = _descriptor.Descriptor(
  name='RpbGetBucketTypeReq',
  full_name='RpbGetBucketTypeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='RpbGetBucketTypeReq.type', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=397,
  serialized_end=432,
)


_RPBSETBUCKETTYPEREQ = _descriptor.Descriptor(
  name='RpbSetBucketTypeReq',
  full_name='RpbSetBucketTypeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='RpbSetBucketTypeReq.type', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='props', full_name='RpbSetBucketTypeReq.props', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=434,
  serialized_end=501,
)


_RPBMODFUN = _descriptor.Descriptor(
  name='RpbModFun',
  full_name='RpbModFun',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module', full_name='RpbModFun.module', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='function', full_name='RpbModFun.function', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=503,
  serialized_end=548,
)


_RPBCOMMITHOOK = _descriptor.Descriptor(
  name='RpbCommitHook',
  full_name='RpbCommitHook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modfun', full_name='RpbCommitHook.modfun', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='RpbCommitHook.name', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=550,
  serialized_end=607,
)


_RPBBUCKETPROPS = _descriptor.Descriptor(
  name='RpbBucketProps',
  full_name='RpbBucketProps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n_val', full_name='RpbBucketProps.n_val', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allow_mult', full_name='RpbBucketProps.allow_mult', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_write_wins', full_name='RpbBucketProps.last_write_wins', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precommit', full_name='RpbBucketProps.precommit', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_precommit', full_name='RpbBucketProps.has_precommit', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='postcommit', full_name='RpbBucketProps.postcommit', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_postcommit', full_name='RpbBucketProps.has_postcommit', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chash_keyfun', full_name='RpbBucketProps.chash_keyfun', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linkfun', full_name='RpbBucketProps.linkfun', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='old_vclock', full_name='RpbBucketProps.old_vclock', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='young_vclock', full_name='RpbBucketProps.young_vclock', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='big_vclock', full_name='RpbBucketProps.big_vclock', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='small_vclock', full_name='RpbBucketProps.small_vclock', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pr', full_name='RpbBucketProps.pr', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r', full_name='RpbBucketProps.r', index=14,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='w', full_name='RpbBucketProps.w', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pw', full_name='RpbBucketProps.pw', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dw', full_name='RpbBucketProps.dw', index=17,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rw', full_name='RpbBucketProps.rw', index=18,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_quorum', full_name='RpbBucketProps.basic_quorum', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notfound_ok', full_name='RpbBucketProps.notfound_ok', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backend', full_name='RpbBucketProps.backend', index=21,
      number=22, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search', full_name='RpbBucketProps.search', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repl', full_name='RpbBucketProps.repl', index=23,
      number=24, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_index', full_name='RpbBucketProps.search_index', index=24,
      number=25, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datatype', full_name='RpbBucketProps.datatype', index=25,
      number=26, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consistent', full_name='RpbBucketProps.consistent', index=26,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='write_once', full_name='RpbBucketProps.write_once', index=27,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hll_precision', full_name='RpbBucketProps.hll_precision', index=28,
      number=29, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RPBBUCKETPROPS_RPBREPLMODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=610,
  serialized_end=1321,
)


_RPBAUTHREQ = _descriptor.Descriptor(
  name='RpbAuthReq',
  full_name='RpbAuthReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='RpbAuthReq.user', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='RpbAuthReq.password', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=1323,
  serialized_end=1367,
)

_RPBGETBUCKETRESP.fields_by_name['props'].message_type = _RPBBUCKETPROPS
_RPBSETBUCKETREQ.fields_by_name['props'].message_type = _RPBBUCKETPROPS
_RPBSETBUCKETTYPEREQ.fields_by_name['props'].message_type = _RPBBUCKETPROPS
_RPBCOMMITHOOK.fields_by_name['modfun'].message_type = _RPBMODFUN
_RPBBUCKETPROPS.fields_by_name['precommit'].message_type = _RPBCOMMITHOOK
_RPBBUCKETPROPS.fields_by_name['postcommit'].message_type = _RPBCOMMITHOOK
_RPBBUCKETPROPS.fields_by_name['chash_keyfun'].message_type = _RPBMODFUN
_RPBBUCKETPROPS.fields_by_name['linkfun'].message_type = _RPBMODFUN
_RPBBUCKETPROPS.fields_by_name['repl'].enum_type = _RPBBUCKETPROPS_RPBREPLMODE
_RPBBUCKETPROPS_RPBREPLMODE.containing_type = _RPBBUCKETPROPS;
DESCRIPTOR.message_types_by_name['RpbErrorResp'] = _RPBERRORRESP
DESCRIPTOR.message_types_by_name['RpbGetServerInfoResp'] = _RPBGETSERVERINFORESP
DESCRIPTOR.message_types_by_name['RpbPair'] = _RPBPAIR
DESCRIPTOR.message_types_by_name['RpbGetBucketReq'] = _RPBGETBUCKETREQ
DESCRIPTOR.message_types_by_name['RpbGetBucketResp'] = _RPBGETBUCKETRESP
DESCRIPTOR.message_types_by_name['RpbSetBucketReq'] = _RPBSETBUCKETREQ
DESCRIPTOR.message_types_by_name['RpbResetBucketReq'] = _RPBRESETBUCKETREQ
DESCRIPTOR.message_types_by_name['RpbGetBucketTypeReq'] = _RPBGETBUCKETTYPEREQ
DESCRIPTOR.message_types_by_name['RpbSetBucketTypeReq'] = _RPBSETBUCKETTYPEREQ
DESCRIPTOR.message_types_by_name['RpbModFun'] = _RPBMODFUN
DESCRIPTOR.message_types_by_name['RpbCommitHook'] = _RPBCOMMITHOOK
DESCRIPTOR.message_types_by_name['RpbBucketProps'] = _RPBBUCKETPROPS
DESCRIPTOR.message_types_by_name['RpbAuthReq'] = _RPBAUTHREQ

class RpbErrorResp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBERRORRESP

  # @@protoc_insertion_point(class_scope:RpbErrorResp)

class RpbGetServerInfoResp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBGETSERVERINFORESP

  # @@protoc_insertion_point(class_scope:RpbGetServerInfoResp)

class RpbPair(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBPAIR

  # @@protoc_insertion_point(class_scope:RpbPair)

class RpbGetBucketReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBGETBUCKETREQ

  # @@protoc_insertion_point(class_scope:RpbGetBucketReq)

class RpbGetBucketResp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBGETBUCKETRESP

  # @@protoc_insertion_point(class_scope:RpbGetBucketResp)

class RpbSetBucketReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBSETBUCKETREQ

  # @@protoc_insertion_point(class_scope:RpbSetBucketReq)

class RpbResetBucketReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBRESETBUCKETREQ

  # @@protoc_insertion_point(class_scope:RpbResetBucketReq)

class RpbGetBucketTypeReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBGETBUCKETTYPEREQ

  # @@protoc_insertion_point(class_scope:RpbGetBucketTypeReq)

class RpbSetBucketTypeReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBSETBUCKETTYPEREQ

  # @@protoc_insertion_point(class_scope:RpbSetBucketTypeReq)

class RpbModFun(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBMODFUN

  # @@protoc_insertion_point(class_scope:RpbModFun)

class RpbCommitHook(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBCOMMITHOOK

  # @@protoc_insertion_point(class_scope:RpbCommitHook)

class RpbBucketProps(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBBUCKETPROPS

  # @@protoc_insertion_point(class_scope:RpbBucketProps)

class RpbAuthReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPBAUTHREQ

  # @@protoc_insertion_point(class_scope:RpbAuthReq)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\027com.basho.riak.protobufB\006RiakPB')
# @@protoc_insertion_point(module_scope)
