from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
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
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, BookInvoiceResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BookInvoiceResponse200.from_dict(response.json())

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
) -> Response[Union[Any, BookInvoiceResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

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

    return _build_response(client=client, response=response)


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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BookInvoiceResponse200]
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

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

    return _build_response(client=client, response=response)


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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BookInvoiceResponse200]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
