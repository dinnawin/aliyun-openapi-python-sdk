# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvcs.endpoint import endpoint_data

class ListEventAlgorithmDetailsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'ListEventAlgorithmDetails','vcs')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SourceId(self):
		return self.get_body_params().get('SourceId')

	def set_SourceId(self,SourceId):
		self.add_body_params('SourceId', SourceId)

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_ExtendValue(self):
		return self.get_body_params().get('ExtendValue')

	def set_ExtendValue(self,ExtendValue):
		self.add_body_params('ExtendValue', ExtendValue)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_RecordId(self):
		return self.get_body_params().get('RecordId')

	def set_RecordId(self,RecordId):
		self.add_body_params('RecordId', RecordId)

	def get_EventValue(self):
		return self.get_body_params().get('EventValue')

	def set_EventValue(self,EventValue):
		self.add_body_params('EventValue', EventValue)

	def get_DataSourceId(self):
		return self.get_body_params().get('DataSourceId')

	def set_DataSourceId(self,DataSourceId):
		self.add_body_params('DataSourceId', DataSourceId)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_EventType(self):
		return self.get_body_params().get('EventType')

	def set_EventType(self,EventType):
		self.add_body_params('EventType', EventType)