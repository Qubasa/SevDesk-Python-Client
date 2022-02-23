from enum import Enum

from .. import Client
from ..common import ApiObject, ApiObjectCache, ApiObjectType
from .client.models import InvoicePositionModelUnity


class Unity(str, Enum):
    PIECE = "UNITY_PIECE"
    SQUARE_METER = "UNITY_SQUARE_METER"
    METER = "UNITY_METER"
    KILOGRAM = "UNITY_KILOGRAM"
    TON = "UNITY_TON"
    RUNNING_METER = "UNITY_RUNNING_METER"
    BLANKET = "UNITY_BLANKET"
    CUBIC_METER = "UNITY_CUBIC_METER"
    HOUR = "UNITY_HOUR"
    KILOMETER = "UNITY_KILOMETER"
    PERCENT = "UNITY_PERCENT"
    DAYS = "UNITY_DAYS"
    L = "UNITY_L"
    EMPTY = "UNITY_EMPTY"

    def _get_api_model(self, client: Client) -> InvoicePositionModelUnity:
        """
        Get the API-Model for the given Unity
        """
        cache = ApiObjectCache(client=client)
        item: ApiObject = cache.get(ApiObjectType.UNITY)[self]

        return InvoicePositionModelUnity(item.id, "Unity")
