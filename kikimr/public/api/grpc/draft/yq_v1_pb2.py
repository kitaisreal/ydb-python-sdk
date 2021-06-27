# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kikimr/public/api/grpc/draft/yq_v1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kikimr.public.api.protos.draft import yq_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kikimr/public/api/grpc/draft/yq_v1.proto',
  package='YandexQuery.V1',
  syntax='proto3',
  serialized_pb=_b('\n(kikimr/public/api/grpc/draft/yq_v1.proto\x12\x0eYandexQuery.V1\x1a\'kikimr/public/api/protos/draft/yq.proto2\xdd\x0b\n\x12YandexQueryService\x12J\n\tCreateJob\x12\x1d.YandexQuery.CreateJobRequest\x1a\x1e.YandexQuery.CreateJobResponse\x12G\n\x08ListJobs\x12\x1c.YandexQuery.ListJobsRequest\x1a\x1d.YandexQuery.ListJobsResponse\x12P\n\x0b\x44\x65scribeJob\x12\x1f.YandexQuery.DescribeJobRequest\x1a .YandexQuery.DescribeJobResponse\x12J\n\tModifyJob\x12\x1d.YandexQuery.ModifyJobRequest\x1a\x1e.YandexQuery.ModifyJobResponse\x12J\n\tDeleteJob\x12\x1d.YandexQuery.DeleteJobRequest\x1a\x1e.YandexQuery.DeleteJobResponse\x12M\n\nControlJob\x12\x1e.YandexQuery.ControlJobRequest\x1a\x1f.YandexQuery.ControlJobResponse\x12V\n\rGetResultData\x12!.YandexQuery.GetResultDataRequest\x1a\".YandexQuery.GetResultDataResponse\x12_\n\x10\x43reateConnection\x12$.YandexQuery.CreateConnectionRequest\x1a%.YandexQuery.CreateConnectionResponse\x12\\\n\x0fListConnections\x12#.YandexQuery.ListConnectionsRequest\x1a$.YandexQuery.ListConnectionsResponse\x12\x65\n\x12\x44\x65scribeConnection\x12&.YandexQuery.DescribeConnectionRequest\x1a\'.YandexQuery.DescribeConnectionResponse\x12_\n\x10ModifyConnection\x12$.YandexQuery.ModifyConnectionRequest\x1a%.YandexQuery.ModifyConnectionResponse\x12_\n\x10\x44\x65leteConnection\x12$.YandexQuery.DeleteConnectionRequest\x1a%.YandexQuery.DeleteConnectionResponse\x12V\n\rCreateBinding\x12!.YandexQuery.CreateBindingRequest\x1a\".YandexQuery.CreateBindingResponse\x12S\n\x0cListBindings\x12 .YandexQuery.ListBindingsRequest\x1a!.YandexQuery.ListBindingsResponse\x12\\\n\x0f\x44\x65scribeBinding\x12#.YandexQuery.DescribeBindingRequest\x1a$.YandexQuery.DescribeBindingResponse\x12V\n\rModifyBinding\x12!.YandexQuery.ModifyBindingRequest\x1a\".YandexQuery.ModifyBindingResponse\x12V\n\rDeleteBinding\x12!.YandexQuery.DeleteBindingRequest\x1a\".YandexQuery.DeleteBindingResponseB\x15\n\x13\x63om.yandex.query.v1b\x06proto3')
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.yandex.query.v1'))

_YANDEXQUERYSERVICE = _descriptor.ServiceDescriptor(
  name='YandexQueryService',
  full_name='YandexQuery.V1.YandexQueryService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=102,
  serialized_end=1603,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateJob',
    full_name='YandexQuery.V1.YandexQueryService.CreateJob',
    index=0,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._CREATEJOBREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._CREATEJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListJobs',
    full_name='YandexQuery.V1.YandexQueryService.ListJobs',
    index=1,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._LISTJOBSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._LISTJOBSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeJob',
    full_name='YandexQuery.V1.YandexQueryService.DescribeJob',
    index=2,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DESCRIBEJOBREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DESCRIBEJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyJob',
    full_name='YandexQuery.V1.YandexQueryService.ModifyJob',
    index=3,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._MODIFYJOBREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._MODIFYJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteJob',
    full_name='YandexQuery.V1.YandexQueryService.DeleteJob',
    index=4,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DELETEJOBREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DELETEJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ControlJob',
    full_name='YandexQuery.V1.YandexQueryService.ControlJob',
    index=5,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._CONTROLJOBREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._CONTROLJOBRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetResultData',
    full_name='YandexQuery.V1.YandexQueryService.GetResultData',
    index=6,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._GETRESULTDATAREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._GETRESULTDATARESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateConnection',
    full_name='YandexQuery.V1.YandexQueryService.CreateConnection',
    index=7,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._CREATECONNECTIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._CREATECONNECTIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListConnections',
    full_name='YandexQuery.V1.YandexQueryService.ListConnections',
    index=8,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._LISTCONNECTIONSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._LISTCONNECTIONSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeConnection',
    full_name='YandexQuery.V1.YandexQueryService.DescribeConnection',
    index=9,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DESCRIBECONNECTIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DESCRIBECONNECTIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyConnection',
    full_name='YandexQuery.V1.YandexQueryService.ModifyConnection',
    index=10,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._MODIFYCONNECTIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._MODIFYCONNECTIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteConnection',
    full_name='YandexQuery.V1.YandexQueryService.DeleteConnection',
    index=11,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DELETECONNECTIONREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DELETECONNECTIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateBinding',
    full_name='YandexQuery.V1.YandexQueryService.CreateBinding',
    index=12,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._CREATEBINDINGREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._CREATEBINDINGRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListBindings',
    full_name='YandexQuery.V1.YandexQueryService.ListBindings',
    index=13,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._LISTBINDINGSREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._LISTBINDINGSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeBinding',
    full_name='YandexQuery.V1.YandexQueryService.DescribeBinding',
    index=14,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DESCRIBEBINDINGREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DESCRIBEBINDINGRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ModifyBinding',
    full_name='YandexQuery.V1.YandexQueryService.ModifyBinding',
    index=15,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._MODIFYBINDINGREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._MODIFYBINDINGRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBinding',
    full_name='YandexQuery.V1.YandexQueryService.DeleteBinding',
    index=16,
    containing_service=None,
    input_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DELETEBINDINGREQUEST,
    output_type=kikimr_dot_public_dot_api_dot_protos_dot_draft_dot_yq__pb2._DELETEBINDINGRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_YANDEXQUERYSERVICE)

DESCRIPTOR.services_by_name['YandexQueryService'] = _YANDEXQUERYSERVICE

# @@protoc_insertion_point(module_scope)