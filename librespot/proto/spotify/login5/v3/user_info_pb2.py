# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spotify/login5/v3/user_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='spotify/login5/v3/user_info.proto',
    package='spotify.login5.v3',
    syntax='proto3',
    serialized_options=b'\n\024com.spotify.login5v3',
    create_key=_descriptor._internal_create_key,
    serialized_pb=
    b'\n!spotify/login5/v3/user_info.proto\x12\x11spotify.login5.v3\"\x97\x02\n\x08UserInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x16\n\x0e\x65mail_verified\x18\x03 \x01(\x08\x12\x11\n\tbirthdate\x18\x04 \x01(\t\x12\x32\n\x06gender\x18\x05 \x01(\x0e\x32\".spotify.login5.v3.UserInfo.Gender\x12\x14\n\x0cphone_number\x18\x06 \x01(\t\x12\x1d\n\x15phone_number_verified\x18\x07 \x01(\x08\x12 \n\x18\x65mail_already_registered\x18\x08 \x01(\x08\"8\n\x06Gender\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\x12\x0b\n\x07NEUTRAL\x10\x03\x42\x16\n\x14\x63om.spotify.login5v3b\x06proto3'
)

_USERINFO_GENDER = _descriptor.EnumDescriptor(
    name='Gender',
    full_name='spotify.login5.v3.UserInfo.Gender',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNKNOWN',
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='MALE',
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='FEMALE',
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='NEUTRAL',
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=280,
    serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_USERINFO_GENDER)

_USERINFO = _descriptor.Descriptor(
    name='UserInfo',
    full_name='spotify.login5.v3.UserInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='spotify.login5.v3.UserInfo.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='email',
            full_name='spotify.login5.v3.UserInfo.email',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='email_verified',
            full_name='spotify.login5.v3.UserInfo.email_verified',
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='birthdate',
            full_name='spotify.login5.v3.UserInfo.birthdate',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='gender',
            full_name='spotify.login5.v3.UserInfo.gender',
            index=4,
            number=5,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='phone_number',
            full_name='spotify.login5.v3.UserInfo.phone_number',
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='phone_number_verified',
            full_name='spotify.login5.v3.UserInfo.phone_number_verified',
            index=6,
            number=7,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='email_already_registered',
            full_name='spotify.login5.v3.UserInfo.email_already_registered',
            index=7,
            number=8,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _USERINFO_GENDER,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=57,
    serialized_end=336,
)

_USERINFO.fields_by_name['gender'].enum_type = _USERINFO_GENDER
_USERINFO_GENDER.containing_type = _USERINFO
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserInfo = _reflection.GeneratedProtocolMessageType(
    'UserInfo',
    (_message.Message, ),
    {
        'DESCRIPTOR': _USERINFO,
        '__module__': 'spotify.login5.v3.user_info_pb2'
        # @@protoc_insertion_point(class_scope:spotify.login5.v3.UserInfo)
    })
_sym_db.RegisterMessage(UserInfo)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)