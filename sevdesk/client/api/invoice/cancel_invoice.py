from typing import Any, Dict, Optional, Union, cast

import httpx

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
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, CancelInvoiceResponse201]]:
    if response.status_code == 201:
        response_201 = CancelInvoiceResponse201.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, CancelInvoiceResponse201]]:
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
) -> Response[Union[Any, CancelInvoiceResponse201]]:
    """Cancel an invoice / Create cancellation invoice

     This endpoint will cancel the specified invoice therefor creating a cancellation invoice. The
    cancellation invoice will be automatically paid and the source invoices status will change to
    'cancelled'.

    Args:
        document_id (int):

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

    return _build_response(response=response)


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

    Returns:
        Response[Union[Any, CancelInvoiceResponse201]]
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

    Returns:
        Response[Union[Any, CancelInvoiceResponse201]]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


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

    Returns:
        Response[Union[Any, CancelInvoiceResponse201]]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
        )
    ).parsed
