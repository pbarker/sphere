# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1alpha/sphere.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1alpha/sphere.proto',
  package='sphere.api.v1alpha',
  syntax='proto3',
  serialized_options=_b('Z\rspherev1alpha'),
  serialized_pb=_b('\n\x14v1alpha/sphere.proto\x12\x12sphere.api.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"C\n\x15RegisterServerRequest\x12*\n\x06server\x18\x01 \x01(\x0b\x32\x1a.sphere.api.v1alpha.Server\"D\n\x16RegisterServerResponse\x12*\n\x06server\x18\x01 \x01(\x0b\x32\x1a.sphere.api.v1alpha.Server\"\x1e\n\x10GetServerRequest\x12\n\n\x02id\x18\x01 \x01(\t\"?\n\x11GetServerResponse\x12*\n\x06server\x18\x01 \x01(\x0b\x32\x1a.sphere.api.v1alpha.Server\"\x13\n\x11ListServerRequest\"A\n\x12ListServerResponse\x12+\n\x07servers\x18\x01 \x03(\x0b\x32\x1a.sphere.api.v1alpha.Server\"%\n\x17UnregisterServerRequest\x12\n\n\x02id\x18\x01 \x01(\t\"+\n\x18UnregisterServerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"z\n\x06Server\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x30\n\x0c\x63reated_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\n\n\x02id\x18\x05 \x01(\t2\x92\x04\n\tSphereAPI\x12\x84\x01\n\x0eRegisterServer\x12).sphere.api.v1alpha.RegisterServerRequest\x1a*.sphere.api.v1alpha.RegisterServerResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1alpha/servers:\x01*\x12w\n\tGetServer\x12$.sphere.api.v1alpha.GetServerRequest\x1a%.sphere.api.v1alpha.GetServerResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1alpha/servers/{id}\x12v\n\x0bListServers\x12%.sphere.api.v1alpha.ListServerRequest\x1a&.sphere.api.v1alpha.ListServerResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1alpha/servers\x12\x8c\x01\n\x10UnregisterServer\x12+.sphere.api.v1alpha.UnregisterServerRequest\x1a,.sphere.api.v1alpha.UnregisterServerResponse\"\x1d\x82\xd3\xe4\x93\x02\x17*\x15/v1alpha/servers/{id}B\x0fZ\rspherev1alphab\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_REGISTERSERVERREQUEST = _descriptor.Descriptor(
  name='RegisterServerRequest',
  full_name='sphere.api.v1alpha.RegisterServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='sphere.api.v1alpha.RegisterServerRequest.server', index=0,
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
  ],
  serialized_start=107,
  serialized_end=174,
)


_REGISTERSERVERRESPONSE = _descriptor.Descriptor(
  name='RegisterServerResponse',
  full_name='sphere.api.v1alpha.RegisterServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='sphere.api.v1alpha.RegisterServerResponse.server', index=0,
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
  ],
  serialized_start=176,
  serialized_end=244,
)


_GETSERVERREQUEST = _descriptor.Descriptor(
  name='GetServerRequest',
  full_name='sphere.api.v1alpha.GetServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sphere.api.v1alpha.GetServerRequest.id', index=0,
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
  serialized_start=246,
  serialized_end=276,
)


_GETSERVERRESPONSE = _descriptor.Descriptor(
  name='GetServerResponse',
  full_name='sphere.api.v1alpha.GetServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='sphere.api.v1alpha.GetServerResponse.server', index=0,
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
  ],
  serialized_start=278,
  serialized_end=341,
)


_LISTSERVERREQUEST = _descriptor.Descriptor(
  name='ListServerRequest',
  full_name='sphere.api.v1alpha.ListServerRequest',
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
  serialized_start=343,
  serialized_end=362,
)


_LISTSERVERRESPONSE = _descriptor.Descriptor(
  name='ListServerResponse',
  full_name='sphere.api.v1alpha.ListServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servers', full_name='sphere.api.v1alpha.ListServerResponse.servers', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=364,
  serialized_end=429,
)


_UNREGISTERSERVERREQUEST = _descriptor.Descriptor(
  name='UnregisterServerRequest',
  full_name='sphere.api.v1alpha.UnregisterServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sphere.api.v1alpha.UnregisterServerRequest.id', index=0,
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
  serialized_start=431,
  serialized_end=468,
)


_UNREGISTERSERVERRESPONSE = _descriptor.Descriptor(
  name='UnregisterServerResponse',
  full_name='sphere.api.v1alpha.UnregisterServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='sphere.api.v1alpha.UnregisterServerResponse.message', index=0,
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
  serialized_start=470,
  serialized_end=513,
)


_SERVER = _descriptor.Descriptor(
  name='Server',
  full_name='sphere.api.v1alpha.Server',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sphere.api.v1alpha.Server.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='sphere.api.v1alpha.Server.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='sphere.api.v1alpha.Server.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_time', full_name='sphere.api.v1alpha.Server.created_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='sphere.api.v1alpha.Server.id', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=515,
  serialized_end=637,
)

_REGISTERSERVERREQUEST.fields_by_name['server'].message_type = _SERVER
_REGISTERSERVERRESPONSE.fields_by_name['server'].message_type = _SERVER
_GETSERVERRESPONSE.fields_by_name['server'].message_type = _SERVER
_LISTSERVERRESPONSE.fields_by_name['servers'].message_type = _SERVER
_SERVER.fields_by_name['created_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['RegisterServerRequest'] = _REGISTERSERVERREQUEST
DESCRIPTOR.message_types_by_name['RegisterServerResponse'] = _REGISTERSERVERRESPONSE
DESCRIPTOR.message_types_by_name['GetServerRequest'] = _GETSERVERREQUEST
DESCRIPTOR.message_types_by_name['GetServerResponse'] = _GETSERVERRESPONSE
DESCRIPTOR.message_types_by_name['ListServerRequest'] = _LISTSERVERREQUEST
DESCRIPTOR.message_types_by_name['ListServerResponse'] = _LISTSERVERRESPONSE
DESCRIPTOR.message_types_by_name['UnregisterServerRequest'] = _UNREGISTERSERVERREQUEST
DESCRIPTOR.message_types_by_name['UnregisterServerResponse'] = _UNREGISTERSERVERRESPONSE
DESCRIPTOR.message_types_by_name['Server'] = _SERVER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterServerRequest = _reflection.GeneratedProtocolMessageType('RegisterServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERSERVERREQUEST,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.RegisterServerRequest)
  })
_sym_db.RegisterMessage(RegisterServerRequest)

RegisterServerResponse = _reflection.GeneratedProtocolMessageType('RegisterServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERSERVERRESPONSE,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.RegisterServerResponse)
  })
_sym_db.RegisterMessage(RegisterServerResponse)

GetServerRequest = _reflection.GeneratedProtocolMessageType('GetServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERREQUEST,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.GetServerRequest)
  })
_sym_db.RegisterMessage(GetServerRequest)

GetServerResponse = _reflection.GeneratedProtocolMessageType('GetServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERRESPONSE,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.GetServerResponse)
  })
_sym_db.RegisterMessage(GetServerResponse)

ListServerRequest = _reflection.GeneratedProtocolMessageType('ListServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVERREQUEST,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.ListServerRequest)
  })
_sym_db.RegisterMessage(ListServerRequest)

ListServerResponse = _reflection.GeneratedProtocolMessageType('ListServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVERRESPONSE,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.ListServerResponse)
  })
_sym_db.RegisterMessage(ListServerResponse)

UnregisterServerRequest = _reflection.GeneratedProtocolMessageType('UnregisterServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNREGISTERSERVERREQUEST,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.UnregisterServerRequest)
  })
_sym_db.RegisterMessage(UnregisterServerRequest)

UnregisterServerResponse = _reflection.GeneratedProtocolMessageType('UnregisterServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNREGISTERSERVERRESPONSE,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.UnregisterServerResponse)
  })
_sym_db.RegisterMessage(UnregisterServerResponse)

Server = _reflection.GeneratedProtocolMessageType('Server', (_message.Message,), {
  'DESCRIPTOR' : _SERVER,
  '__module__' : 'v1alpha.sphere_pb2'
  # @@protoc_insertion_point(class_scope:sphere.api.v1alpha.Server)
  })
_sym_db.RegisterMessage(Server)


DESCRIPTOR._options = None

_SPHEREAPI = _descriptor.ServiceDescriptor(
  name='SphereAPI',
  full_name='sphere.api.v1alpha.SphereAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=640,
  serialized_end=1170,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterServer',
    full_name='sphere.api.v1alpha.SphereAPI.RegisterServer',
    index=0,
    containing_service=None,
    input_type=_REGISTERSERVERREQUEST,
    output_type=_REGISTERSERVERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\025\"\020/v1alpha/servers:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetServer',
    full_name='sphere.api.v1alpha.SphereAPI.GetServer',
    index=1,
    containing_service=None,
    input_type=_GETSERVERREQUEST,
    output_type=_GETSERVERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\022\025/v1alpha/servers/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='ListServers',
    full_name='sphere.api.v1alpha.SphereAPI.ListServers',
    index=2,
    containing_service=None,
    input_type=_LISTSERVERREQUEST,
    output_type=_LISTSERVERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\022\022\020/v1alpha/servers'),
  ),
  _descriptor.MethodDescriptor(
    name='UnregisterServer',
    full_name='sphere.api.v1alpha.SphereAPI.UnregisterServer',
    index=3,
    containing_service=None,
    input_type=_UNREGISTERSERVERREQUEST,
    output_type=_UNREGISTERSERVERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027*\025/v1alpha/servers/{id}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_SPHEREAPI)

DESCRIPTOR.services_by_name['SphereAPI'] = _SPHEREAPI

# @@protoc_insertion_point(module_scope)
