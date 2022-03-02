from __future__ import annotations

from collections import UserDict, namedtuple
from enum import Enum
from typing import Dict, Union

import attrs
import cattrs
import requests

from .. import UNSET, Client, Unset
from .borg import Borg

ApiObjectTypeHelper = namedtuple("ApiObjectType", ["url", "object_type", "key"])


class ApiObjectType(Enum):
    """
    API-Objects available trough the SevDesk API
    The Enum-Type contains specific helpers to access the SevDesk API (url-fragment, object-type, sort key)
    """

    COUNTRY = ApiObjectTypeHelper("StaticCountry", UNSET, "code")
    ADDRESS_CATEGORIES = ApiObjectTypeHelper(
        "Category", "ContactAddress", "translationCode"
    )
    COMMUNICATION_WAY_KEY = ApiObjectTypeHelper(
        "CommunicationWayKey", UNSET, "translationCode"
    )
    UNITY = ApiObjectTypeHelper("Unity", UNSET, "translationCode")


@attrs.define()
class ApiObject:
    """
    A SevDesk API-Object
    """

    id: str
    objectName: str
    name: str
    translationCode: str
    code: Union[Unset, str] = UNSET

    @staticmethod
    def from_dict(item: Dict) -> ApiObject:
        return cattrs.structure(item, ApiObject)


class ApiObjects(UserDict):
    def __init__(self, client: Client, api_type: ApiObjectType) -> None:
        super().__init__()

        url = f"{client.base_url}/{api_type.value.url}"

        params = {"limit": 1000}
        if api_type.value.object_type:
            params.update({"objectType": api_type.value.object_type})

        request = requests.get(url=url, headers=client.get_headers(), params=params)
        request.raise_for_status()

        objects = request.json()["objects"]

        for item in objects:
            api_object = ApiObject.from_dict(item)
            self.update({getattr(api_object, api_type.value.key): api_object})

    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    def __delitem__(self, key):
        raise RuntimeError("Deletion not allowed")

    def sort_by_id(self):
        sorted = {}
        for object in self.data.values():
            sorted.update({object.id: object})

        return sorted


class ApiObjectCache(Borg):
    def __init__(self, client: Union[Unset, Client] = UNSET) -> None:
        Borg.__init__(self)

        if not hasattr(self, "cache"):
            self.cache = dict[ApiObjectType, ApiObjects]()

        if not hasattr(self, "client") and not client:
            raise ValueError("Client not intialised.")

        if client:
            self.client = client

    def get(self, api_type: ApiObjectType) -> ApiObjects:
        if not api_type in self.cache:
            self.cache[api_type] = ApiObjects(self.client, api_type)

        return self.cache[api_type]
