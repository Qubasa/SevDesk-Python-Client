from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
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
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, GetCommunicationWaysResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCommunicationWaysResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, GetCommunicationWaysResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

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

    return _build_response(client=client, response=response)


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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetCommunicationWaysResponse200]
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

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

    return _build_response(client=client, response=response)


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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetCommunicationWaysResponse200]
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
