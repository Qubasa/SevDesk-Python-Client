from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.book_invoice_json_body import BookInvoiceJsonBody
from ...models.book_invoice_response_200 import BookInvoiceResponse200
from ...types import Response


def _get_kwargs(
    document_id: int,
    *,
    client: Client,
    json_body: BookInvoiceJsonBody,
) -> Dict[str, Any]:
    url = "{}/Invoice/{DocumentId}/bookAmount".format(
        client.base_url, DocumentId=document_id
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
) -> Optional[Union[Any, BookInvoiceResponse200]]:
    if response.status_code == 200:
        response_200 = BookInvoiceResponse200.from_dict(response.json())

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
) -> Response[Union[Any, BookInvoiceResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    document_id: int,
    *,
    client: Client,
    json_body: BookInvoiceJsonBody,
) -> Response[Union[Any, BookInvoiceResponse200]]:
    """Book an invoice

     This endpoint can be used to book invoices. Invoices are booked on payment accounts where (bank)
    transactions are located and might be linked to the transactions by using this endpoint. For more
    detailed information about booking invoices, please refer to docs.

    Args:
        document_id (int):
        json_body (BookInvoiceJsonBody):

    Returns:
        Response[Union[Any, BookInvoiceResponse200]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    document_id: int,
    *,
    client: Client,
    json_body: BookInvoiceJsonBody,
) -> Optional[Union[Any, BookInvoiceResponse200]]:
    """Book an invoice

     This endpoint can be used to book invoices. Invoices are booked on payment accounts where (bank)
    transactions are located and might be linked to the transactions by using this endpoint. For more
    detailed information about booking invoices, please refer to docs.

    Args:
        document_id (int):
        json_body (BookInvoiceJsonBody):

    Returns:
        Response[Union[Any, BookInvoiceResponse200]]
    """

    return sync_detailed(
        document_id=document_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    document_id: int,
    *,
    client: Client,
    json_body: BookInvoiceJsonBody,
) -> Response[Union[Any, BookInvoiceResponse200]]:
    """Book an invoice

     This endpoint can be used to book invoices. Invoices are booked on payment accounts where (bank)
    transactions are located and might be linked to the transactions by using this endpoint. For more
    detailed information about booking invoices, please refer to docs.

    Args:
        document_id (int):
        json_body (BookInvoiceJsonBody):

    Returns:
        Response[Union[Any, BookInvoiceResponse200]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    document_id: int,
    *,
    client: Client,
    json_body: BookInvoiceJsonBody,
) -> Optional[Union[Any, BookInvoiceResponse200]]:
    """Book an invoice

     This endpoint can be used to book invoices. Invoices are booked on payment accounts where (bank)
    transactions are located and might be linked to the transactions by using this endpoint. For more
    detailed information about booking invoices, please refer to docs.

    Args:
        document_id (int):
        json_body (BookInvoiceJsonBody):

    Returns:
        Response[Union[Any, BookInvoiceResponse200]]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
