import os
from enum import Enum

from sevdesk import Client, __version__, UNSET
from sevdesk.common import ApiObjectCache, ApiObjectType
from sevdesk.contact.address import AddressCategory
from sevdesk.accounting import Unity


def test_version():
    assert __version__ == "0.1.0"


def test_api_object_cache():
    token = os.environ["SEVDESKTOKEN"]

    client = Client(base_url="https://my.sevdesk.de/api/v1", token=token)
    cache_1 = ApiObjectCache(client=client)

    # Test communication ways
    comm_ways = cache_1.get(ApiObjectType.COMMUNICATION_WAY_KEY)
    assert len(comm_ways) != 0

    # Countries should be sorted by country short-code, test for Austria
    countries = cache_1.get(ApiObjectType.COUNTRY)
    assert "at" in countries

    # This should not throw
    addr_catg = cache_1.get(ApiObjectType.ADDRESS_CATEGORIES)
    addr_catg[AddressCategory.CATEGORY_DELIVERY_ADDRESS]
    assert len(addr_catg) != 0

    # Get Unities
    unity = cache_1.get(ApiObjectType.UNITY)
    unity[Unity.BLANKET]

    # Test Borg-Pattern
    cache_2 = ApiObjectCache()
    assert cache_2.client is not UNSET
    assert len(cache_2.cache) != 0
