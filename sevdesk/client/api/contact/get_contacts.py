from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_contacts_depth import GetContactsDepth
from ...models.get_contacts_response_200 import GetContactsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    depth: Union[Unset, None, GetContactsDepth] = UNSET,
    customer_number: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Contact".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_depth: Union[Unset, None, str] = UNSET
    if not isinstance(depth, Unset):
        json_depth = depth.value if depth else None

    params["depth"] = json_depth

    params["customerNumber"] = customer_number

    params["name"] = name

    params["embed"] = embed

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
) -> Optional[Union[Any, GetContactsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetContactsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetContactsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    depth: Union[Unset, None, GetContactsDepth] = UNSET,
    customer_number: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetContactsResponse200]]:
    """Retrieve contacts

     There are a multitude of parameter which can be used to filter.<br>
         A few of them are attached but
         for a complete list please check out <a
    href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-contacts#filtering'>this</a> list

    Args:
        depth (Union[Unset, None, GetContactsDepth]):
        customer_number (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetContactsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        depth=depth,
        customer_number=customer_number,
        name=name,
        embed=embed,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    depth: Union[Unset, None, GetContactsDepth] = UNSET,
    customer_number: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetContactsResponse200]]:
    """Retrieve contacts

     There are a multitude of parameter which can be used to filter.<br>
         A few of them are attached but
         for a complete list please check out <a
    href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-contacts#filtering'>this</a> list

    Args:
        depth (Union[Unset, None, GetContactsDepth]):
        customer_number (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetContactsResponse200]
    """

    return sync_detailed(
        client=client,
        depth=depth,
        customer_number=customer_number,
        name=name,
        embed=embed,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    depth: Union[Unset, None, GetContactsDepth] = UNSET,
    customer_number: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetContactsResponse200]]:
    """Retrieve contacts

     There are a multitude of parameter which can be used to filter.<br>
         A few of them are attached but
         for a complete list please check out <a
    href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-contacts#filtering'>this</a> list

    Args:
        depth (Union[Unset, None, GetContactsDepth]):
        customer_number (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetContactsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        depth=depth,
        customer_number=customer_number,
        name=name,
        embed=embed,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    depth: Union[Unset, None, GetContactsDepth] = UNSET,
    customer_number: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetContactsResponse200]]:
    """Retrieve contacts

     There are a multitude of parameter which can be used to filter.<br>
         A few of them are attached but
         for a complete list please check out <a
    href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-contacts#filtering'>this</a> list

    Args:
        depth (Union[Unset, None, GetContactsDepth]):
        customer_number (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetContactsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            depth=depth,
            customer_number=customer_number,
            name=name,
            embed=embed,
        )
    ).parsed
