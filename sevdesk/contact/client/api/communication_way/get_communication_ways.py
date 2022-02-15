from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_communication_ways_main import GetCommunicationWaysMain
from ...models.get_communication_ways_response_200 import (
    GetCommunicationWaysResponse200,
)
from ...models.get_communication_ways_type import GetCommunicationWaysType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    contactid: Union[Unset, None, str] = UNSET,
    contactobject_name: Union[Unset, None, str] = "Contact",
    type: Union[Unset, None, GetCommunicationWaysType] = UNSET,
    main: Union[Unset, None, GetCommunicationWaysMain] = UNSET,
) -> Dict[str, Any]:
    url = "{}/CommunicationWay".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["contact[id]"] = contactid

    params["contact[objectName]"] = contactobject_name

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    json_main: Union[Unset, None, str] = UNSET
    if not isinstance(main, Unset):
        json_main = main.value if main else None

    params["main"] = json_main

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, GetCommunicationWaysResponse200]]:
    if response.status_code == 200:
        response_200 = GetCommunicationWaysResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, GetCommunicationWaysResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    contactid: Union[Unset, None, str] = UNSET,
    contactobject_name: Union[Unset, None, str] = "Contact",
    type: Union[Unset, None, GetCommunicationWaysType] = UNSET,
    main: Union[Unset, None, GetCommunicationWaysMain] = UNSET,
) -> Response[Union[Any, GetCommunicationWaysResponse200]]:
    """Retrieve communication ways

     Returns all communication ways which have been added up until now. Filters can be added.

    Args:
        contactid (Union[Unset, None, str]):
        contactobject_name (Union[Unset, None, str]):  Default: 'Contact'.
        type (Union[Unset, None, GetCommunicationWaysType]):
        main (Union[Unset, None, GetCommunicationWaysMain]):

    Returns:
        Response[Union[Any, GetCommunicationWaysResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        contactid=contactid,
        contactobject_name=contactobject_name,
        type=type,
        main=main,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    contactid: Union[Unset, None, str] = UNSET,
    contactobject_name: Union[Unset, None, str] = "Contact",
    type: Union[Unset, None, GetCommunicationWaysType] = UNSET,
    main: Union[Unset, None, GetCommunicationWaysMain] = UNSET,
) -> Optional[Union[Any, GetCommunicationWaysResponse200]]:
    """Retrieve communication ways

     Returns all communication ways which have been added up until now. Filters can be added.

    Args:
        contactid (Union[Unset, None, str]):
        contactobject_name (Union[Unset, None, str]):  Default: 'Contact'.
        type (Union[Unset, None, GetCommunicationWaysType]):
        main (Union[Unset, None, GetCommunicationWaysMain]):

    Returns:
        Response[Union[Any, GetCommunicationWaysResponse200]]
    """

    return sync_detailed(
        client=client,
        contactid=contactid,
        contactobject_name=contactobject_name,
        type=type,
        main=main,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    contactid: Union[Unset, None, str] = UNSET,
    contactobject_name: Union[Unset, None, str] = "Contact",
    type: Union[Unset, None, GetCommunicationWaysType] = UNSET,
    main: Union[Unset, None, GetCommunicationWaysMain] = UNSET,
) -> Response[Union[Any, GetCommunicationWaysResponse200]]:
    """Retrieve communication ways

     Returns all communication ways which have been added up until now. Filters can be added.

    Args:
        contactid (Union[Unset, None, str]):
        contactobject_name (Union[Unset, None, str]):  Default: 'Contact'.
        type (Union[Unset, None, GetCommunicationWaysType]):
        main (Union[Unset, None, GetCommunicationWaysMain]):

    Returns:
        Response[Union[Any, GetCommunicationWaysResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        contactid=contactid,
        contactobject_name=contactobject_name,
        type=type,
        main=main,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    contactid: Union[Unset, None, str] = UNSET,
    contactobject_name: Union[Unset, None, str] = "Contact",
    type: Union[Unset, None, GetCommunicationWaysType] = UNSET,
    main: Union[Unset, None, GetCommunicationWaysMain] = UNSET,
) -> Optional[Union[Any, GetCommunicationWaysResponse200]]:
    """Retrieve communication ways

     Returns all communication ways which have been added up until now. Filters can be added.

    Args:
        contactid (Union[Unset, None, str]):
        contactobject_name (Union[Unset, None, str]):  Default: 'Contact'.
        type (Union[Unset, None, GetCommunicationWaysType]):
        main (Union[Unset, None, GetCommunicationWaysMain]):

    Returns:
        Response[Union[Any, GetCommunicationWaysResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            contactid=contactid,
            contactobject_name=contactobject_name,
            type=type,
            main=main,
        )
    ).parsed
