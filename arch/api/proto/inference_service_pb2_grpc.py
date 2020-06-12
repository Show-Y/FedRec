#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import inference_service_pb2 as inference__service__pb2


class InferenceServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.inference = channel.unary_unary(
        '/com.webank.ai.fate.api.serving.InferenceService/inference',
        request_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
        response_deserializer=inference__service__pb2.InferenceMessage.FromString,
        )
    self.startInferenceJob = channel.unary_unary(
        '/com.webank.ai.fate.api.serving.InferenceService/startInferenceJob',
        request_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
        response_deserializer=inference__service__pb2.InferenceMessage.FromString,
        )
    self.getInferenceResult = channel.unary_unary(
        '/com.webank.ai.fate.api.serving.InferenceService/getInferenceResult',
        request_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
        response_deserializer=inference__service__pb2.InferenceMessage.FromString,
        )


class InferenceServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def inference(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def startInferenceJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getInferenceResult(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InferenceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'inference': grpc.unary_unary_rpc_method_handler(
          servicer.inference,
          request_deserializer=inference__service__pb2.InferenceMessage.FromString,
          response_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
      ),
      'startInferenceJob': grpc.unary_unary_rpc_method_handler(
          servicer.startInferenceJob,
          request_deserializer=inference__service__pb2.InferenceMessage.FromString,
          response_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
      ),
      'getInferenceResult': grpc.unary_unary_rpc_method_handler(
          servicer.getInferenceResult,
          request_deserializer=inference__service__pb2.InferenceMessage.FromString,
          response_serializer=inference__service__pb2.InferenceMessage.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.ai.fate.api.serving.InferenceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
