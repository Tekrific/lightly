# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
try:
    # Pydantic >=v1.10.17
    from pydantic.v1 import BaseModel, Field
except ImportError:
    # Pydantic v1
    from pydantic import BaseModel, Field
from lightly.openapi_generated.swagger_client.models.docker_worker_config_v3_lightly import DockerWorkerConfigV3Lightly
from lightly.openapi_generated.swagger_client.models.docker_worker_config_v4_docker import DockerWorkerConfigV4Docker
from lightly.openapi_generated.swagger_client.models.docker_worker_type import DockerWorkerType
from lightly.openapi_generated.swagger_client.models.selection_config_v4 import SelectionConfigV4

class DockerWorkerConfigV4(BaseModel):
    """
    DockerWorkerConfigV4
    """
    worker_type: DockerWorkerType = Field(..., alias="workerType")
    docker: Optional[DockerWorkerConfigV4Docker] = None
    lightly: Optional[DockerWorkerConfigV3Lightly] = None
    selection: Optional[SelectionConfigV4] = None
    __properties = ["workerType", "docker", "lightly", "selection"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True
        use_enum_values = True
        extra = "forbid"

    def to_str(self, by_alias: bool = False) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.dict(by_alias=by_alias))

    def to_json(self, by_alias: bool = False) -> str:
        """Returns the JSON representation of the model"""
        return json.dumps(self.to_dict(by_alias=by_alias))

    @classmethod
    def from_json(cls, json_str: str) -> DockerWorkerConfigV4:
        """Create an instance of DockerWorkerConfigV4 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, by_alias: bool = False):
        """Returns the dictionary representation of the model"""
        _dict = self.dict(by_alias=by_alias,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of docker
        if self.docker:
            _dict['docker' if by_alias else 'docker'] = self.docker.to_dict(by_alias=by_alias)
        # override the default output from pydantic by calling `to_dict()` of lightly
        if self.lightly:
            _dict['lightly' if by_alias else 'lightly'] = self.lightly.to_dict(by_alias=by_alias)
        # override the default output from pydantic by calling `to_dict()` of selection
        if self.selection:
            _dict['selection' if by_alias else 'selection'] = self.selection.to_dict(by_alias=by_alias)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DockerWorkerConfigV4:
        """Create an instance of DockerWorkerConfigV4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DockerWorkerConfigV4.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in DockerWorkerConfigV4) in the input: " + str(obj))

        _obj = DockerWorkerConfigV4.parse_obj({
            "worker_type": obj.get("workerType"),
            "docker": DockerWorkerConfigV4Docker.from_dict(obj.get("docker")) if obj.get("docker") is not None else None,
            "lightly": DockerWorkerConfigV3Lightly.from_dict(obj.get("lightly")) if obj.get("lightly") is not None else None,
            "selection": SelectionConfigV4.from_dict(obj.get("selection")) if obj.get("selection") is not None else None
        })
        return _obj

