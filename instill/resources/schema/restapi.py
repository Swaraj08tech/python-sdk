# generated by datamodel-codegen:
#   filename:  restapi_definitions.json

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Union


@dataclass
class NoAuth:
    """
    Authentication method to use for the REST API
    """

    auth_type: str


@dataclass
class BasicAuth:
    """
    Authentication method to use for the REST API
    """

    auth_type: str
    password: str
    username: str


class WhereToAddAPIKeyTo(Enum):
    """
    Add the API key to the header or query params
    """

    header = 'header'
    query = 'query'


@dataclass
class APIKey:
    """
    Authentication method to use for the REST API
    """

    auth_location: WhereToAddAPIKeyTo
    auth_type: str
    key: str
    value: str


@dataclass
class BearerToken:
    """
    Authentication method to use for the REST API
    """

    auth_type: str
    token: str


@dataclass
class RESTAPIConnectorSpec:
    authentication: Union[NoAuth, BasicAuth, APIKey, BearerToken]
    base_url: str
