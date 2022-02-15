from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.invoice_model import InvoiceModel
from ...models.update_invoice_response_200 import UpdateInvoiceResponse200
from ...types import Response


def _get_kwargs(
    invoice_id: int,
    *,
    client: Client,
    json_body: InvoiceModel,
) -> Dict[str, Any]:
    url = "{}/Invoice/{invoiceId}".format(client.base_url, invoiceId=invoice_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, UpdateInvoiceResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateInvoiceResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateInvoiceResponse200]]:
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
    json_body: InvoiceModel,
) -> Response[Union[Any, UpdateInvoiceResponse200]]:
    """Update an existing invoice

     Update an invoice

    Args:
        invoice_id (int):
        json_body (InvoiceModel): Invoice model

    Returns:
        Response[Union[Any, UpdateInvoiceResponse200]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
        json_body=json_body,
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
    json_body: InvoiceModel,
) -> Optional[Union[Any, UpdateInvoiceResponse200]]:
    """Update an existing invoice

     Update an invoice

    Args:
        invoice_id (int):
        json_body (InvoiceModel): Invoice model

    Returns:
        Response[Union[Any, UpdateInvoiceResponse200]]
    """

    return sync_detailed(
        invoice_id=invoice_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    invoice_id: int,
    *,
    client: Client,
    json_body: InvoiceModel,
) -> Response[Union[Any, UpdateInvoiceResponse200]]:
    """Update an existing invoice

     Update an invoice

    Args:
        invoice_id (int):
        json_body (InvoiceModel): Invoice model

    Returns:
        Response[Union[Any, UpdateInvoiceResponse200]]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    invoice_id: int,
    *,
    client: Client,
    json_body: InvoiceModel,
) -> Optional[Union[Any, UpdateInvoiceResponse200]]:
    """Update an existing invoice

     Update an invoice

    Args:
        invoice_id (int):
        json_body (InvoiceModel): Invoice model

    Returns:
        Response[Union[Any, UpdateInvoiceResponse200]]
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
