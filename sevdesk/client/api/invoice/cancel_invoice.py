from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.cancel_invoice_response_201 import CancelInvoiceResponse201
from ...types import Response


def _get_kwargs(
    document_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/Invoice/{DocumentId}/cancelInvoice".format(
        client.base_url, DocumentId=document_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, CancelInvoiceResponse201]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CancelInvoiceResponse201.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, CancelInvoiceResponse201]]:
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
) -> Response[Union[Any, CancelInvoiceResponse201]]:
    """Cancel an invoice / Create cancellation invoice

     This endpoint will cancel the specified invoice therefor creating a cancellation invoice. The
    cancellation invoice will be automatically paid and the source invoices status will change to
    'cancelled'.

    Args:
        document_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CancelInvoiceResponse201]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
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
) -> Optional[Union[Any, CancelInvoiceResponse201]]:
    """Cancel an invoice / Create cancellation invoice

     This endpoint will cancel the specified invoice therefor creating a cancellation invoice. The
    cancellation invoice will be automatically paid and the source invoices status will change to
    'cancelled'.

    Args:
        document_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CancelInvoiceResponse201]
    """

    return sync_detailed(
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    document_id: int,
    *,
    client: Client,
) -> Response[Union[Any, CancelInvoiceResponse201]]:
    """Cancel an invoice / Create cancellation invoice

     This endpoint will cancel the specified invoice therefor creating a cancellation invoice. The
    cancellation invoice will be automatically paid and the source invoices status will change to
    'cancelled'.

    Args:
        document_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CancelInvoiceResponse201]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    document_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, CancelInvoiceResponse201]]:
    """Cancel an invoice / Create cancellation invoice

     This endpoint will cancel the specified invoice therefor creating a cancellation invoice. The
    cancellation invoice will be automatically paid and the source invoices status will change to
    'cancelled'.

    Args:
        document_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CancelInvoiceResponse201]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
        )
    ).parsed
