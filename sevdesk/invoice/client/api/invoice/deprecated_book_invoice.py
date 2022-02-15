from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.deprecated_book_invoice_json_body import DeprecatedBookInvoiceJsonBody
from ...models.deprecated_book_invoice_response_200 import (
    DeprecatedBookInvoiceResponse200,
)
from ...types import Response


def _get_kwargs(
    invoice_id: int,
    *,
    client: Client,
    json_body: DeprecatedBookInvoiceJsonBody,
) -> Dict[str, Any]:
    url = "{}/Invoice/{invoiceId}/bookAmmount".format(
        client.base_url, invoiceId=invoice_id
    )

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
) -> Optional[Union[Any, DeprecatedBookInvoiceResponse200]]:
    if response.status_code == 200:
        response_200 = DeprecatedBookInvoiceResponse200.from_dict(response.json())

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
) -> Response[Union[Any, DeprecatedBookInvoiceResponse200]]:
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
    json_body: DeprecatedBookInvoiceJsonBody,
) -> Response[Union[Any, DeprecatedBookInvoiceResponse200]]:
    """Book an invoice

     This endpoint can be used to book invoices.<br>
         Invoices are booked on payment accounts where (bank) transactions are located and might be
    linked to the transactions
         by using this endpoint.<br>
         For more detailed information about booking invoices, please refer to
         <a href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-vouchers#booking'>this</a>
    section of our API-Overview.<br>
         Be aware, that this endpoint is deprecated and the new endpoint 'bookAmount' should be used
    instead.

    Args:
        invoice_id (int):
        json_body (DeprecatedBookInvoiceJsonBody):

    Returns:
        Response[Union[Any, DeprecatedBookInvoiceResponse200]]
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
    json_body: DeprecatedBookInvoiceJsonBody,
) -> Optional[Union[Any, DeprecatedBookInvoiceResponse200]]:
    """Book an invoice

     This endpoint can be used to book invoices.<br>
         Invoices are booked on payment accounts where (bank) transactions are located and might be
    linked to the transactions
         by using this endpoint.<br>
         For more detailed information about booking invoices, please refer to
         <a href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-vouchers#booking'>this</a>
    section of our API-Overview.<br>
         Be aware, that this endpoint is deprecated and the new endpoint 'bookAmount' should be used
    instead.

    Args:
        invoice_id (int):
        json_body (DeprecatedBookInvoiceJsonBody):

    Returns:
        Response[Union[Any, DeprecatedBookInvoiceResponse200]]
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
    json_body: DeprecatedBookInvoiceJsonBody,
) -> Response[Union[Any, DeprecatedBookInvoiceResponse200]]:
    """Book an invoice

     This endpoint can be used to book invoices.<br>
         Invoices are booked on payment accounts where (bank) transactions are located and might be
    linked to the transactions
         by using this endpoint.<br>
         For more detailed information about booking invoices, please refer to
         <a href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-vouchers#booking'>this</a>
    section of our API-Overview.<br>
         Be aware, that this endpoint is deprecated and the new endpoint 'bookAmount' should be used
    instead.

    Args:
        invoice_id (int):
        json_body (DeprecatedBookInvoiceJsonBody):

    Returns:
        Response[Union[Any, DeprecatedBookInvoiceResponse200]]
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
    json_body: DeprecatedBookInvoiceJsonBody,
) -> Optional[Union[Any, DeprecatedBookInvoiceResponse200]]:
    """Book an invoice

     This endpoint can be used to book invoices.<br>
         Invoices are booked on payment accounts where (bank) transactions are located and might be
    linked to the transactions
         by using this endpoint.<br>
         For more detailed information about booking invoices, please refer to
         <a href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-vouchers#booking'>this</a>
    section of our API-Overview.<br>
         Be aware, that this endpoint is deprecated and the new endpoint 'bookAmount' should be used
    instead.

    Args:
        invoice_id (int):
        json_body (DeprecatedBookInvoiceJsonBody):

    Returns:
        Response[Union[Any, DeprecatedBookInvoiceResponse200]]
    """

    return (
        await asyncio_detailed(
            invoice_id=invoice_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
