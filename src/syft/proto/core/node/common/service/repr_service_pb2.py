# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/common/service/repr_service.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/node/common/service/repr_service.proto",
    package="syft.core.node.common.service",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n1proto/core/node/common/service/repr_service.proto\x12\x1dsyft.core.node.common.service\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\\\n\x0bReprMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address"\x9b\x01\n\x0f\x43reateVMMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x10\n\x08settings\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\xb1\x01\n\x17\x43reateVMResponseMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12)\n\nvm_address\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x04 \x01(\x08\x12\x0b\n\x03msg\x18\x05 \x01(\t"\x9f\x01\n\x13\x43reateWorkerMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x10\n\x08settings\x18\x03 \x01(\t\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\xb5\x01\n\x1b\x43reateWorkerResponseMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12)\n\nvm_address\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x04 \x01(\x08\x12\x0b\n\x03msg\x18\x05 \x01(\tb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_REPRMESSAGE = _descriptor.Descriptor(
    name="ReprMessage",
    full_name="syft.core.node.common.service.ReprMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.ReprMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.ReprMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=152,
    serialized_end=244,
)


_CREATEVMMESSAGE = _descriptor.Descriptor(
    name="CreateVMMessage",
    full_name="syft.core.node.common.service.CreateVMMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.CreateVMMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.CreateVMMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="settings",
            full_name="syft.core.node.common.service.CreateVMMessage.settings",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.core.node.common.service.CreateVMMessage.reply_to",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=247,
    serialized_end=402,
)


_CREATEVMRESPONSEMESSAGE = _descriptor.Descriptor(
    name="CreateVMResponseMessage",
    full_name="syft.core.node.common.service.CreateVMResponseMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.CreateVMResponseMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.CreateVMResponseMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="vm_address",
            full_name="syft.core.node.common.service.CreateVMResponseMessage.vm_address",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.core.node.common.service.CreateVMResponseMessage.success",
            index=3,
            number=4,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="syft.core.node.common.service.CreateVMResponseMessage.msg",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=405,
    serialized_end=582,
)


_CREATEWORKERMESSAGE = _descriptor.Descriptor(
    name="CreateWorkerMessage",
    full_name="syft.core.node.common.service.CreateWorkerMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.CreateWorkerMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.CreateWorkerMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="settings",
            full_name="syft.core.node.common.service.CreateWorkerMessage.settings",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.core.node.common.service.CreateWorkerMessage.reply_to",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=585,
    serialized_end=744,
)


_CREATEWORKERRESPONSEMESSAGE = _descriptor.Descriptor(
    name="CreateWorkerResponseMessage",
    full_name="syft.core.node.common.service.CreateWorkerResponseMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.CreateWorkerResponseMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.CreateWorkerResponseMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="vm_address",
            full_name="syft.core.node.common.service.CreateWorkerResponseMessage.vm_address",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.core.node.common.service.CreateWorkerResponseMessage.success",
            index=3,
            number=4,
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
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="syft.core.node.common.service.CreateWorkerResponseMessage.msg",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=747,
    serialized_end=928,
)

_REPRMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_REPRMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEVMMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEVMMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEVMMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEVMRESPONSEMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEVMRESPONSEMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEVMRESPONSEMESSAGE.fields_by_name[
    "vm_address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEWORKERMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEWORKERMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEWORKERMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEWORKERRESPONSEMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEWORKERRESPONSEMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEWORKERRESPONSEMESSAGE.fields_by_name[
    "vm_address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name["ReprMessage"] = _REPRMESSAGE
DESCRIPTOR.message_types_by_name["CreateVMMessage"] = _CREATEVMMESSAGE
DESCRIPTOR.message_types_by_name["CreateVMResponseMessage"] = _CREATEVMRESPONSEMESSAGE
DESCRIPTOR.message_types_by_name["CreateWorkerMessage"] = _CREATEWORKERMESSAGE
DESCRIPTOR.message_types_by_name[
    "CreateWorkerResponseMessage"
] = _CREATEWORKERRESPONSEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReprMessage = _reflection.GeneratedProtocolMessageType(
    "ReprMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _REPRMESSAGE,
        "__module__": "proto.core.node.common.service.repr_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.ReprMessage)
    },
)
_sym_db.RegisterMessage(ReprMessage)

CreateVMMessage = _reflection.GeneratedProtocolMessageType(
    "CreateVMMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEVMMESSAGE,
        "__module__": "proto.core.node.common.service.repr_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.CreateVMMessage)
    },
)
_sym_db.RegisterMessage(CreateVMMessage)

CreateVMResponseMessage = _reflection.GeneratedProtocolMessageType(
    "CreateVMResponseMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEVMRESPONSEMESSAGE,
        "__module__": "proto.core.node.common.service.repr_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.CreateVMResponseMessage)
    },
)
_sym_db.RegisterMessage(CreateVMResponseMessage)

CreateWorkerMessage = _reflection.GeneratedProtocolMessageType(
    "CreateWorkerMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEWORKERMESSAGE,
        "__module__": "proto.core.node.common.service.repr_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.CreateWorkerMessage)
    },
)
_sym_db.RegisterMessage(CreateWorkerMessage)

CreateWorkerResponseMessage = _reflection.GeneratedProtocolMessageType(
    "CreateWorkerResponseMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEWORKERRESPONSEMESSAGE,
        "__module__": "proto.core.node.common.service.repr_service_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.CreateWorkerResponseMessage)
    },
)
_sym_db.RegisterMessage(CreateWorkerResponseMessage)


# @@protoc_insertion_point(module_scope)
