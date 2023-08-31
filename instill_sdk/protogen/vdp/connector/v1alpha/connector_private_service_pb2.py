# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vdp/connector/v1alpha/connector_private_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from vdp.connector.v1alpha import connector_pb2 as vdp_dot_connector_dot_v1alpha_dot_connector__pb2
from vdp.connector.v1alpha import connector_definition_pb2 as vdp_dot_connector_dot_v1alpha_dot_connector__definition__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5vdp/connector/v1alpha/connector_private_service.proto\x12\x15vdp.connector.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a%vdp/connector/v1alpha/connector.proto\x1a\x30vdp/connector/v1alpha/connector_definition.proto2\x86\x07\n\x17\x43onnectorPrivateService\x12\xec\x01\n\x1eLookUpConnectorDefinitionAdmin\x12<.vdp.connector.v1alpha.LookUpConnectorDefinitionAdminRequest\x1a=.vdp.connector.v1alpha.LookUpConnectorDefinitionAdminResponse\"M\xda\x41\tpermalink\x82\xd3\xe4\x93\x02;\x12\x39/v1alpha/admin/{permalink=connector-definitions/*}/lookUp\x12\xc0\x01\n\x1bListConnectorResourcesAdmin\x12\x39.vdp.connector.v1alpha.ListConnectorResourcesAdminRequest\x1a:.vdp.connector.v1alpha.ListConnectorResourcesAdminResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/v1alpha/admin/connector-resources\x12\xe4\x01\n\x1cLookUpConnectorResourceAdmin\x12:.vdp.connector.v1alpha.LookUpConnectorResourceAdminRequest\x1a;.vdp.connector.v1alpha.LookUpConnectorResourceAdminResponse\"K\xda\x41\tpermalink\x82\xd3\xe4\x93\x02\x39\x12\x37/v1alpha/admin/{permalink=connector-resources/*}/lookUp\x12\xd1\x01\n\x16\x43heckConnectorResource\x12\x34.vdp.connector.v1alpha.CheckConnectorResourceRequest\x1a\x35.vdp.connector.v1alpha.CheckConnectorResourceResponse\"J\xda\x41\tpermalink\x82\xd3\xe4\x93\x02\x38\x12\x36/v1alpha/admin/{permalink=connector-resources/*}/checkB\xf9\x01\n\x19\x63om.vdp.connector.v1alphaB\x1c\x43onnectorPrivateServiceProtoP\x01ZHgithub.com/instill-ai/protogen-go/vdp/connector/v1alpha;connectorv1alpha\xa2\x02\x03VCX\xaa\x02\x15Vdp.Connector.V1alpha\xca\x02\x15Vdp\\Connector\\V1alpha\xe2\x02!Vdp\\Connector\\V1alpha\\GPBMetadata\xea\x02\x17Vdp::Connector::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vdp.connector.v1alpha.connector_private_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.vdp.connector.v1alphaB\034ConnectorPrivateServiceProtoP\001ZHgithub.com/instill-ai/protogen-go/vdp/connector/v1alpha;connectorv1alpha\242\002\003VCX\252\002\025Vdp.Connector.V1alpha\312\002\025Vdp\\Connector\\V1alpha\342\002!Vdp\\Connector\\V1alpha\\GPBMetadata\352\002\027Vdp::Connector::V1alpha'
  _CONNECTORPRIVATESERVICE.methods_by_name['LookUpConnectorDefinitionAdmin']._options = None
  _CONNECTORPRIVATESERVICE.methods_by_name['LookUpConnectorDefinitionAdmin']._serialized_options = b'\332A\tpermalink\202\323\344\223\002;\0229/v1alpha/admin/{permalink=connector-definitions/*}/lookUp'
  _CONNECTORPRIVATESERVICE.methods_by_name['ListConnectorResourcesAdmin']._options = None
  _CONNECTORPRIVATESERVICE.methods_by_name['ListConnectorResourcesAdmin']._serialized_options = b'\202\323\344\223\002$\022\"/v1alpha/admin/connector-resources'
  _CONNECTORPRIVATESERVICE.methods_by_name['LookUpConnectorResourceAdmin']._options = None
  _CONNECTORPRIVATESERVICE.methods_by_name['LookUpConnectorResourceAdmin']._serialized_options = b'\332A\tpermalink\202\323\344\223\0029\0227/v1alpha/admin/{permalink=connector-resources/*}/lookUp'
  _CONNECTORPRIVATESERVICE.methods_by_name['CheckConnectorResource']._options = None
  _CONNECTORPRIVATESERVICE.methods_by_name['CheckConnectorResource']._serialized_options = b'\332A\tpermalink\202\323\344\223\0028\0226/v1alpha/admin/{permalink=connector-resources/*}/check'
  _globals['_CONNECTORPRIVATESERVICE']._serialized_start=225
  _globals['_CONNECTORPRIVATESERVICE']._serialized_end=1127
# @@protoc_insertion_point(module_scope)