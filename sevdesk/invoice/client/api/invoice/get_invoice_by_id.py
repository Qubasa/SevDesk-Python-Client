from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_invoice_by_id_response_200 import GetInvoiceByIdResponse200
from ...types import Response


def _get_kwargs(
    invoice_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/Invoice/{invoiceId}".format(client.base_url, invoiceId=invoice_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, GetInvoiceByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetInvoiceByIdResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetInvoiceByIdResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    invoice_id: int,
    *,
    client: Client,
) -> Response[Union[Any, GetInvoiceByIdResponse200]]:
    """Find invoice by ID

     Returns a single invoice

    Args:
        invoice_id (int):

    Returns:
        Response[Union[Any, GetInvoiceByIdResponse200]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    invoice_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, GetInvoiceByIdResponse200]]:
    """Find invoice by ID

     Returns a single invoice

    Args:
        invoice_id (int):

    Returns:
        Response[Union[Any, GetInvoiceByIdResponse200]]
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invoice_id: int,
    *,
    client: Client,
) -> Response[Union[Any, GetInvoiceByIdResponse200]]:
    """Find invoice by ID

     Returns a single invoice

    Args:
        invoice_id (int):

    Returns:
        Response[Union[Any, GetInvoiceByIdResponse200]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    invoice_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, GetInvoiceByIdResponse200]]:
    """Find invoice by ID

     Returns a single invoice

    Args:
        invoice_id (int):

    Returns:
        Response[Union[Any, GetInvoiceByIdResponse200]]
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
