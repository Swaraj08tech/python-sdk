# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/usage/v1alpha/usage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base.mgmt.v1alpha import metric_pb2 as base_dot_mgmt_dot_v1alpha_dot_metric__pb2
from base.mgmt.v1alpha import mgmt_pb2 as base_dot_mgmt_dot_v1alpha_dot_mgmt__pb2
from common.healthcheck.v1alpha import healthcheck_pb2 as common_dot_healthcheck_dot_v1alpha_dot_healthcheck__pb2
from common.task.v1alpha import task_pb2 as common_dot_task_dot_v1alpha_dot_task__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x62\x61se/usage/v1alpha/usage.proto\x12\x12\x62\x61se.usage.v1alpha\x1a\x1e\x62\x61se/mgmt/v1alpha/metric.proto\x1a\x1c\x62\x61se/mgmt/v1alpha/mgmt.proto\x1a,common/healthcheck/v1alpha/healthcheck.proto\x1a\x1e\x63ommon/task/v1alpha/task.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x97\x01\n\x0fLivenessRequest\x12k\n\x14health_check_request\x18\x01 \x01(\x0b\x32..common.healthcheck.v1alpha.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"w\n\x10LivenessResponse\x12\x63\n\x15health_check_response\x18\x01 \x01(\x0b\x32/.common.healthcheck.v1alpha.HealthCheckResponseR\x13healthCheckResponse\"\x98\x01\n\x10ReadinessRequest\x12k\n\x14health_check_request\x18\x01 \x01(\x0b\x32..common.healthcheck.v1alpha.HealthCheckRequestB\x04\xe2\x41\x01\x01H\x00R\x12healthCheckRequest\x88\x01\x01\x42\x17\n\x15_health_check_request\"x\n\x11ReadinessResponse\x12\x63\n\x15health_check_response\x18\x01 \x01(\x0b\x32/.common.healthcheck.v1alpha.HealthCheckResponseR\x13healthCheckResponse\"\xbf\x05\n\x07Session\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12\x16\n\x03uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03R\x03uid\x12\x43\n\x07service\x18\x03 \x01(\x0e\x32#.base.usage.v1alpha.Session.ServiceB\x04\xe2\x41\x01\x02R\x07service\x12\x1e\n\x07\x65\x64ition\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02R\x07\x65\x64ition\x12\x1e\n\x07version\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02R\x07version\x12\x18\n\x04\x61rch\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\x04\x61rch\x12\x14\n\x02os\x18\x07 \x01(\tB\x04\xe2\x41\x01\x02R\x02os\x12\x1c\n\x06uptime\x18\x08 \x01(\x03\x42\x04\xe2\x41\x01\x02R\x06uptime\x12\x41\n\x0breport_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\nreportTime\x12\x1a\n\x05token\x18\n \x01(\tB\x04\xe2\x41\x01\x03R\x05token\x12\x41\n\x0b\x63reate_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12!\n\towner_uid\x18\r \x01(\tB\x04\xe2\x41\x01\x02R\x08ownerUid\"t\n\x07Service\x12\x17\n\x13SERVICE_UNSPECIFIED\x10\x00\x12\x10\n\x0cSERVICE_MGMT\x10\x01\x12\x15\n\x11SERVICE_CONNECTOR\x10\x02\x12\x11\n\rSERVICE_MODEL\x10\x03\x12\x14\n\x10SERVICE_PIPELINE\x10\x04:1\xea\x41.\n\x18\x61pi.instill.tech/Session\x12\x12sessions/{session}\"@\n\rMgmtUsageData\x12/\n\x06usages\x18\x01 \x03(\x0b\x32\x17.base.mgmt.v1alpha.UserR\x06usages\"\xc6\x04\n\x12\x43onnectorUsageData\x12L\n\x06usages\x18\x01 \x03(\x0b\x32\x34.base.usage.v1alpha.ConnectorUsageData.UserUsageDataR\x06usages\x1a\xe1\x03\n\rUserUsageData\x12\x1f\n\x08user_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x07userUid\x12\x85\x01\n\x16\x63onnector_execute_data\x18\x02 \x03(\x0b\x32I.base.usage.v1alpha.ConnectorUsageData.UserUsageData.ConnectorExecuteDataB\x04\xe2\x41\x01\x02R\x14\x63onnectorExecuteData\x1a\xa6\x02\n\x14\x43onnectorExecuteData\x12)\n\rconnector_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0c\x63onnectorUid\x12%\n\x0b\x65xecute_uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\nexecuteUid\x12\x43\n\x0c\x65xecute_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\x0b\x65xecuteTime\x12>\n\x18\x63onnector_definition_uid\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02R\x16\x63onnectorDefinitionUid\x12\x37\n\x06status\x18\x05 \x01(\x0e\x32\x19.base.mgmt.v1alpha.StatusB\x04\xe2\x41\x01\x02R\x06status\"\xd9\x04\n\x0eModelUsageData\x12H\n\x06usages\x18\x01 \x03(\x0b\x32\x30.base.usage.v1alpha.ModelUsageData.UserUsageDataR\x06usages\x1a\xfc\x03\n\rUserUsageData\x12\x1f\n\x08user_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x07userUid\x12u\n\x12model_trigger_data\x18\x02 \x03(\x0b\x32\x41.base.usage.v1alpha.ModelUsageData.UserUsageData.ModelTriggerDataB\x04\xe2\x41\x01\x02R\x10modelTriggerData\x1a\xd2\x02\n\x10ModelTriggerData\x12!\n\tmodel_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08modelUid\x12%\n\x0btrigger_uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\ntriggerUid\x12\x43\n\x0ctrigger_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\x0btriggerTime\x12\x36\n\x14model_definition_uid\x18\x04 \x01(\tB\x04\xe2\x41\x01\x02R\x12modelDefinitionUid\x12>\n\nmodel_task\x18\x05 \x01(\x0e\x32\x19.common.task.v1alpha.TaskB\x04\xe2\x41\x01\x02R\tmodelTask\x12\x37\n\x06status\x18\x06 \x01(\x0e\x32\x19.base.mgmt.v1alpha.StatusB\x04\xe2\x41\x01\x02R\x06status\"\xbf\x04\n\x11PipelineUsageData\x12K\n\x06usages\x18\x01 \x03(\x0b\x32\x33.base.usage.v1alpha.PipelineUsageData.UserUsageDataR\x06usages\x1a\xdc\x03\n\rUserUsageData\x12\x1f\n\x08user_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x07userUid\x12\x81\x01\n\x15pipeline_trigger_data\x18\x02 \x03(\x0b\x32G.base.usage.v1alpha.PipelineUsageData.UserUsageData.PipelineTriggerDataB\x04\xe2\x41\x01\x02R\x13pipelineTriggerData\x1a\xa5\x02\n\x13PipelineTriggerData\x12\'\n\x0cpipeline_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0bpipelineUid\x12%\n\x0btrigger_uid\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\ntriggerUid\x12\x43\n\x0ctrigger_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02R\x0btriggerTime\x12@\n\x0ctrigger_mode\x18\x04 \x01(\x0e\x32\x17.base.mgmt.v1alpha.ModeB\x04\xe2\x41\x01\x02R\x0btriggerMode\x12\x37\n\x06status\x18\x05 \x01(\x0e\x32\x19.base.mgmt.v1alpha.StatusB\x04\xe2\x41\x01\x02R\x06status\"\x87\x04\n\rSessionReport\x12%\n\x0bsession_uid\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\nsessionUid\x12\x1a\n\x05token\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x05token\x12\x16\n\x03pow\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x03pow\x12;\n\x07session\x18\x04 \x01(\x0b\x32\x1b.base.usage.v1alpha.SessionB\x04\xe2\x41\x01\x02R\x07session\x12K\n\x0fmgmt_usage_data\x18\x05 \x01(\x0b\x32!.base.usage.v1alpha.MgmtUsageDataH\x00R\rmgmtUsageData\x12Z\n\x14\x63onnector_usage_data\x18\x06 \x01(\x0b\x32&.base.usage.v1alpha.ConnectorUsageDataH\x00R\x12\x63onnectorUsageData\x12N\n\x10model_usage_data\x18\x07 \x01(\x0b\x32\".base.usage.v1alpha.ModelUsageDataH\x00R\x0emodelUsageData\x12W\n\x13pipeline_usage_data\x18\x08 \x01(\x0b\x32%.base.usage.v1alpha.PipelineUsageDataH\x00R\x11pipelineUsageDataB\x0c\n\nusage_data\"S\n\x14\x43reateSessionRequest\x12;\n\x07session\x18\x01 \x01(\x0b\x32\x1b.base.usage.v1alpha.SessionB\x04\xe2\x41\x01\x02R\x07session\"N\n\x15\x43reateSessionResponse\x12\x35\n\x07session\x18\x01 \x01(\x0b\x32\x1b.base.usage.v1alpha.SessionR\x07session\"[\n\x18SendSessionReportRequest\x12?\n\x06report\x18\x01 \x01(\x0b\x32!.base.usage.v1alpha.SessionReportB\x04\xe2\x41\x01\x02R\x06report\"\x1b\n\x19SendSessionReportResponseB\xd1\x01\n\x16\x63om.base.usage.v1alphaB\nUsageProtoP\x01ZAgithub.com/instill-ai/protogen-go/base/usage/v1alpha;usagev1alpha\xa2\x02\x03\x42UX\xaa\x02\x12\x42\x61se.Usage.V1alpha\xca\x02\x12\x42\x61se\\Usage\\V1alpha\xe2\x02\x1e\x42\x61se\\Usage\\V1alpha\\GPBMetadata\xea\x02\x14\x42\x61se::Usage::V1alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.usage.v1alpha.usage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.base.usage.v1alphaB\nUsageProtoP\001ZAgithub.com/instill-ai/protogen-go/base/usage/v1alpha;usagev1alpha\242\002\003BUX\252\002\022Base.Usage.V1alpha\312\002\022Base\\Usage\\V1alpha\342\002\036Base\\Usage\\V1alpha\\GPBMetadata\352\002\024Base::Usage::V1alpha'
  _LIVENESSREQUEST.fields_by_name['health_check_request']._options = None
  _LIVENESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _READINESSREQUEST.fields_by_name['health_check_request']._options = None
  _READINESSREQUEST.fields_by_name['health_check_request']._serialized_options = b'\342A\001\001'
  _SESSION.fields_by_name['name']._options = None
  _SESSION.fields_by_name['name']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['uid']._options = None
  _SESSION.fields_by_name['uid']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['service']._options = None
  _SESSION.fields_by_name['service']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['edition']._options = None
  _SESSION.fields_by_name['edition']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['version']._options = None
  _SESSION.fields_by_name['version']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['arch']._options = None
  _SESSION.fields_by_name['arch']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['os']._options = None
  _SESSION.fields_by_name['os']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['uptime']._options = None
  _SESSION.fields_by_name['uptime']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['report_time']._options = None
  _SESSION.fields_by_name['report_time']._serialized_options = b'\342A\001\002'
  _SESSION.fields_by_name['token']._options = None
  _SESSION.fields_by_name['token']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['create_time']._options = None
  _SESSION.fields_by_name['create_time']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['update_time']._options = None
  _SESSION.fields_by_name['update_time']._serialized_options = b'\342A\001\003'
  _SESSION.fields_by_name['owner_uid']._options = None
  _SESSION.fields_by_name['owner_uid']._serialized_options = b'\342A\001\002'
  _SESSION._options = None
  _SESSION._serialized_options = b'\352A.\n\030api.instill.tech/Session\022\022sessions/{session}'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['connector_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['connector_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['execute_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['execute_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['execute_time']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['execute_time']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['connector_definition_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['connector_definition_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['status']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA.fields_by_name['status']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['user_uid']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['user_uid']._serialized_options = b'\342A\001\002'
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['connector_execute_data']._options = None
  _CONNECTORUSAGEDATA_USERUSAGEDATA.fields_by_name['connector_execute_data']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['trigger_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['trigger_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['trigger_time']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['trigger_time']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_definition_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_definition_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_task']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['model_task']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['status']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA.fields_by_name['status']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['user_uid']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['user_uid']._serialized_options = b'\342A\001\002'
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['model_trigger_data']._options = None
  _MODELUSAGEDATA_USERUSAGEDATA.fields_by_name['model_trigger_data']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_uid']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['pipeline_uid']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_uid']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_uid']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_time']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_time']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_mode']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['trigger_mode']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['status']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA.fields_by_name['status']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['user_uid']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['user_uid']._serialized_options = b'\342A\001\002'
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['pipeline_trigger_data']._options = None
  _PIPELINEUSAGEDATA_USERUSAGEDATA.fields_by_name['pipeline_trigger_data']._serialized_options = b'\342A\001\002'
  _SESSIONREPORT.fields_by_name['session_uid']._options = None
  _SESSIONREPORT.fields_by_name['session_uid']._serialized_options = b'\342A\001\002'
  _SESSIONREPORT.fields_by_name['token']._options = None
  _SESSIONREPORT.fields_by_name['token']._serialized_options = b'\342A\001\002'
  _SESSIONREPORT.fields_by_name['pow']._options = None
  _SESSIONREPORT.fields_by_name['pow']._serialized_options = b'\342A\001\002'
  _SESSIONREPORT.fields_by_name['session']._options = None
  _SESSIONREPORT.fields_by_name['session']._serialized_options = b'\342A\001\002'
  _CREATESESSIONREQUEST.fields_by_name['session']._options = None
  _CREATESESSIONREQUEST.fields_by_name['session']._serialized_options = b'\342A\001\002'
  _SENDSESSIONREPORTREQUEST.fields_by_name['report']._options = None
  _SENDSESSIONREPORTREQUEST.fields_by_name['report']._serialized_options = b'\342A\001\002'
  _globals['_LIVENESSREQUEST']._serialized_start=288
  _globals['_LIVENESSREQUEST']._serialized_end=439
  _globals['_LIVENESSRESPONSE']._serialized_start=441
  _globals['_LIVENESSRESPONSE']._serialized_end=560
  _globals['_READINESSREQUEST']._serialized_start=563
  _globals['_READINESSREQUEST']._serialized_end=715
  _globals['_READINESSRESPONSE']._serialized_start=717
  _globals['_READINESSRESPONSE']._serialized_end=837
  _globals['_SESSION']._serialized_start=840
  _globals['_SESSION']._serialized_end=1543
  _globals['_SESSION_SERVICE']._serialized_start=1376
  _globals['_SESSION_SERVICE']._serialized_end=1492
  _globals['_MGMTUSAGEDATA']._serialized_start=1545
  _globals['_MGMTUSAGEDATA']._serialized_end=1609
  _globals['_CONNECTORUSAGEDATA']._serialized_start=1612
  _globals['_CONNECTORUSAGEDATA']._serialized_end=2194
  _globals['_CONNECTORUSAGEDATA_USERUSAGEDATA']._serialized_start=1713
  _globals['_CONNECTORUSAGEDATA_USERUSAGEDATA']._serialized_end=2194
  _globals['_CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA']._serialized_start=1900
  _globals['_CONNECTORUSAGEDATA_USERUSAGEDATA_CONNECTOREXECUTEDATA']._serialized_end=2194
  _globals['_MODELUSAGEDATA']._serialized_start=2197
  _globals['_MODELUSAGEDATA']._serialized_end=2798
  _globals['_MODELUSAGEDATA_USERUSAGEDATA']._serialized_start=2290
  _globals['_MODELUSAGEDATA_USERUSAGEDATA']._serialized_end=2798
  _globals['_MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA']._serialized_start=2460
  _globals['_MODELUSAGEDATA_USERUSAGEDATA_MODELTRIGGERDATA']._serialized_end=2798
  _globals['_PIPELINEUSAGEDATA']._serialized_start=2801
  _globals['_PIPELINEUSAGEDATA']._serialized_end=3376
  _globals['_PIPELINEUSAGEDATA_USERUSAGEDATA']._serialized_start=2900
  _globals['_PIPELINEUSAGEDATA_USERUSAGEDATA']._serialized_end=3376
  _globals['_PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA']._serialized_start=3083
  _globals['_PIPELINEUSAGEDATA_USERUSAGEDATA_PIPELINETRIGGERDATA']._serialized_end=3376
  _globals['_SESSIONREPORT']._serialized_start=3379
  _globals['_SESSIONREPORT']._serialized_end=3898
  _globals['_CREATESESSIONREQUEST']._serialized_start=3900
  _globals['_CREATESESSIONREQUEST']._serialized_end=3983
  _globals['_CREATESESSIONRESPONSE']._serialized_start=3985
  _globals['_CREATESESSIONRESPONSE']._serialized_end=4063
  _globals['_SENDSESSIONREPORTREQUEST']._serialized_start=4065
  _globals['_SENDSESSIONREPORTREQUEST']._serialized_end=4156
  _globals['_SENDSESSIONREPORTRESPONSE']._serialized_start=4158
  _globals['_SENDSESSIONREPORTRESPONSE']._serialized_end=4185
# @@protoc_insertion_point(module_scope)