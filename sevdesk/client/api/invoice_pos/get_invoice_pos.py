from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_invoice_pos_response_200 import GetInvoicePosResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    invoiceobject_name: str,
    invoiceid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/InvoicePos".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["invoice[objectName]"] = invoiceobject_name

    params["invoice[id]"] = invoiceid

    params["limit"] = limit

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
) -> Optional[Union[Any, GetInvoicePosResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetInvoicePosResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetInvoicePosResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    invoiceobject_name: str,
    invoiceid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetInvoicePosResponse200]]:
    """Get invoice positions

     Get all positions corresponding to an invoice

    Args:
        invoiceobject_name (str):
        invoiceid (int):
        limit (Union[Unset, None, int]):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetInvoicePosResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        invoiceobject_name=invoiceobject_name,
        invoiceid=invoiceid,
        limit=limit,
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
    invoiceobject_name: str,
    invoiceid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetInvoicePosResponse200]]:
    """Get invoice positions

     Get all positions corresponding to an invoice

    Args:
        invoiceobject_name (str):
        invoiceid (int):
        limit (Union[Unset, None, int]):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetInvoicePosResponse200]
    """

    return sync_detailed(
        client=client,
        invoiceobject_name=invoiceobject_name,
        invoiceid=invoiceid,
        limit=limit,
        embed=embed,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    invoiceobject_name: str,
    invoiceid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetInvoicePosResponse200]]:
    """Get invoice positions

     Get all positions corresponding to an invoice

    Args:
        invoiceobject_name (str):
        invoiceid (int):
        limit (Union[Unset, None, int]):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetInvoicePosResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        invoiceobject_name=invoiceobject_name,
        invoiceid=invoiceid,
        limit=limit,
        embed=embed,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    invoiceobject_name: str,
    invoiceid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetInvoicePosResponse200]]:
    """Get invoice positions

     Get all positions corresponding to an invoice

    Args:
        invoiceobject_name (str):
        invoiceid (int):
        limit (Union[Unset, None, int]):
        embed (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetInvoicePosResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            invoiceobject_name=invoiceobject_name,
            invoiceid=invoiceid,
            limit=limit,
            embed=embed,
        )
    ).parsed
