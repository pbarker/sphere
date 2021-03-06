# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import env_pb2 as env__pb2


class EnvironmentAPIStub(object):
  """The Environment API.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Info = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/Info',
        request_serializer=env__pb2.Empty.SerializeToString,
        response_deserializer=env__pb2.InfoResponse.FromString,
        )
    self.CreateEnv = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/CreateEnv',
        request_serializer=env__pb2.CreateEnvRequest.SerializeToString,
        response_deserializer=env__pb2.CreateEnvResponse.FromString,
        )
    self.ListEnvs = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/ListEnvs',
        request_serializer=env__pb2.ListEnvRequest.SerializeToString,
        response_deserializer=env__pb2.ListEnvResponse.FromString,
        )
    self.ListModels = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/ListModels',
        request_serializer=env__pb2.ListModelsRequest.SerializeToString,
        response_deserializer=env__pb2.ListModelsResponse.FromString,
        )
    self.GetEnv = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/GetEnv',
        request_serializer=env__pb2.GetEnvRequest.SerializeToString,
        response_deserializer=env__pb2.GetEnvResponse.FromString,
        )
    self.ResetEnv = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/ResetEnv',
        request_serializer=env__pb2.ResetEnvRequest.SerializeToString,
        response_deserializer=env__pb2.ResetEnvResponse.FromString,
        )
    self.StepEnv = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/StepEnv',
        request_serializer=env__pb2.StepEnvRequest.SerializeToString,
        response_deserializer=env__pb2.StepEnvResponse.FromString,
        )
    self.SampleAction = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/SampleAction',
        request_serializer=env__pb2.SampleActionRequest.SerializeToString,
        response_deserializer=env__pb2.SampleActionResponse.FromString,
        )
    self.RenderEnv = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/RenderEnv',
        request_serializer=env__pb2.RenderEnvRequest.SerializeToString,
        response_deserializer=env__pb2.RenderEnvResponse.FromString,
        )
    self.StartRecordEnv = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/StartRecordEnv',
        request_serializer=env__pb2.StartRecordEnvRequest.SerializeToString,
        response_deserializer=env__pb2.StartRecordEnvResponse.FromString,
        )
    self.StopRecordEnv = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/StopRecordEnv',
        request_serializer=env__pb2.StopRecordEnvRequest.SerializeToString,
        response_deserializer=env__pb2.StopRecordEnvResponse.FromString,
        )
    self.Results = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/Results',
        request_serializer=env__pb2.ResultsRequest.SerializeToString,
        response_deserializer=env__pb2.ResultsResponse.FromString,
        )
    self.GetVideo = channel.unary_stream(
        '/sphere.api.v1alpha.EnvironmentAPI/GetVideo',
        request_serializer=env__pb2.GetVideoRequest.SerializeToString,
        response_deserializer=env__pb2.GetVideoResponse.FromString,
        )
    self.DeleteVideo = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/DeleteVideo',
        request_serializer=env__pb2.DeleteVideoRequest.SerializeToString,
        response_deserializer=env__pb2.DeleteVideoResponse.FromString,
        )
    self.DeleteEnv = channel.unary_unary(
        '/sphere.api.v1alpha.EnvironmentAPI/DeleteEnv',
        request_serializer=env__pb2.DeleteEnvRequest.SerializeToString,
        response_deserializer=env__pb2.DeleteEnvResponse.FromString,
        )


class EnvironmentAPIServicer(object):
  """The Environment API.
  """

  def Info(self, request, context):
    """Info about the environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateEnv(self, request, context):
    """Create an environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListEnvs(self, request, context):
    """List all environments.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListModels(self, request, context):
    """List all environment models that can be created.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetEnv(self, request, context):
    """Gen an environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetEnv(self, request, context):
    """Reset an environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StepEnv(self, request, context):
    """Step through an environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SampleAction(self, request, context):
    """Get a sample action for the environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RenderEnv(self, request, context):
    """RenderEnv the current environment state.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartRecordEnv(self, request, context):
    """Start recording an environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopRecordEnv(self, request, context):
    """Stop recording an environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Results(self, request, context):
    """Results from the environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetVideo(self, request, context):
    """Stream result video.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteVideo(self, request, context):
    """Delete a result video.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteEnv(self, request, context):
    """Delete an environment.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EnvironmentAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Info': grpc.unary_unary_rpc_method_handler(
          servicer.Info,
          request_deserializer=env__pb2.Empty.FromString,
          response_serializer=env__pb2.InfoResponse.SerializeToString,
      ),
      'CreateEnv': grpc.unary_unary_rpc_method_handler(
          servicer.CreateEnv,
          request_deserializer=env__pb2.CreateEnvRequest.FromString,
          response_serializer=env__pb2.CreateEnvResponse.SerializeToString,
      ),
      'ListEnvs': grpc.unary_unary_rpc_method_handler(
          servicer.ListEnvs,
          request_deserializer=env__pb2.ListEnvRequest.FromString,
          response_serializer=env__pb2.ListEnvResponse.SerializeToString,
      ),
      'ListModels': grpc.unary_unary_rpc_method_handler(
          servicer.ListModels,
          request_deserializer=env__pb2.ListModelsRequest.FromString,
          response_serializer=env__pb2.ListModelsResponse.SerializeToString,
      ),
      'GetEnv': grpc.unary_unary_rpc_method_handler(
          servicer.GetEnv,
          request_deserializer=env__pb2.GetEnvRequest.FromString,
          response_serializer=env__pb2.GetEnvResponse.SerializeToString,
      ),
      'ResetEnv': grpc.unary_unary_rpc_method_handler(
          servicer.ResetEnv,
          request_deserializer=env__pb2.ResetEnvRequest.FromString,
          response_serializer=env__pb2.ResetEnvResponse.SerializeToString,
      ),
      'StepEnv': grpc.unary_unary_rpc_method_handler(
          servicer.StepEnv,
          request_deserializer=env__pb2.StepEnvRequest.FromString,
          response_serializer=env__pb2.StepEnvResponse.SerializeToString,
      ),
      'SampleAction': grpc.unary_unary_rpc_method_handler(
          servicer.SampleAction,
          request_deserializer=env__pb2.SampleActionRequest.FromString,
          response_serializer=env__pb2.SampleActionResponse.SerializeToString,
      ),
      'RenderEnv': grpc.unary_unary_rpc_method_handler(
          servicer.RenderEnv,
          request_deserializer=env__pb2.RenderEnvRequest.FromString,
          response_serializer=env__pb2.RenderEnvResponse.SerializeToString,
      ),
      'StartRecordEnv': grpc.unary_unary_rpc_method_handler(
          servicer.StartRecordEnv,
          request_deserializer=env__pb2.StartRecordEnvRequest.FromString,
          response_serializer=env__pb2.StartRecordEnvResponse.SerializeToString,
      ),
      'StopRecordEnv': grpc.unary_unary_rpc_method_handler(
          servicer.StopRecordEnv,
          request_deserializer=env__pb2.StopRecordEnvRequest.FromString,
          response_serializer=env__pb2.StopRecordEnvResponse.SerializeToString,
      ),
      'Results': grpc.unary_unary_rpc_method_handler(
          servicer.Results,
          request_deserializer=env__pb2.ResultsRequest.FromString,
          response_serializer=env__pb2.ResultsResponse.SerializeToString,
      ),
      'GetVideo': grpc.unary_stream_rpc_method_handler(
          servicer.GetVideo,
          request_deserializer=env__pb2.GetVideoRequest.FromString,
          response_serializer=env__pb2.GetVideoResponse.SerializeToString,
      ),
      'DeleteVideo': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteVideo,
          request_deserializer=env__pb2.DeleteVideoRequest.FromString,
          response_serializer=env__pb2.DeleteVideoResponse.SerializeToString,
      ),
      'DeleteEnv': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteEnv,
          request_deserializer=env__pb2.DeleteEnvRequest.FromString,
          response_serializer=env__pb2.DeleteEnvResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sphere.api.v1alpha.EnvironmentAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
