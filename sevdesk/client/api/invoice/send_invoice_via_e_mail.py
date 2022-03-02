from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.send_invoice_via_e_mail_json_body import SendInvoiceViaEMailJsonBody
from ...models.send_invoice_via_e_mail_response_201 import (
    SendInvoiceViaEMailResponse201,
)
from ...types import Response


def _get_kwargs(
    document_id: int,
    *,
    client: Client,
    json_body: SendInvoiceViaEMailJsonBody,
) -> Dict[str, Any]:
    url = "{}/Invoice/{DocumentId}/sendViaEmail".format(
        client.base_url, DocumentId=document_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, SendInvoiceViaEMailResponse201]]:
    if response.status_code == 201:
        response_201 = SendInvoiceViaEMailResponse201.from_dict(response.json())

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
) -> Response[Union[Any, SendInvoiceViaEMailResponse201]]:
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
    json_body: SendInvoiceViaEMailJsonBody,
) -> Response[Union[Any, SendInvoiceViaEMailResponse201]]:
    """Send invoice via email

     This endpoint sends the specified invoice to a customer via email. This will automatically mark the
    invoice as sent. Please note, that in production an invoice is not allowed to be changed after this
    happened!

    Args:
        document_id (int):
        json_body (SendInvoiceViaEMailJsonBody):

    Returns:
        Response[Union[Any, SendInvoiceViaEMailResponse201]]
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
    json_body: SendInvoiceViaEMailJsonBody,
) -> Optional[Union[Any, SendInvoiceViaEMailResponse201]]:
    """Send invoice via email

     This endpoint sends the specified invoice to a customer via email. This will automatically mark the
    invoice as sent. Please note, that in production an invoice is not allowed to be changed after this
    happened!

    Args:
        document_id (int):
        json_body (SendInvoiceViaEMailJsonBody):

    Returns:
        Response[Union[Any, SendInvoiceViaEMailResponse201]]
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
    json_body: SendInvoiceViaEMailJsonBody,
) -> Response[Union[Any, SendInvoiceViaEMailResponse201]]:
    """Send invoice via email

     This endpoint sends the specified invoice to a customer via email. This will automatically mark the
    invoice as sent. Please note, that in production an invoice is not allowed to be changed after this
    happened!

    Args:
        document_id (int):
        json_body (SendInvoiceViaEMailJsonBody):

    Returns:
        Response[Union[Any, SendInvoiceViaEMailResponse201]]
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
    json_body: SendInvoiceViaEMailJsonBody,
) -> Optional[Union[Any, SendInvoiceViaEMailResponse201]]:
    """Send invoice via email

     This endpoint sends the specified invoice to a customer via email. This will automatically mark the
    invoice as sent. Please note, that in production an invoice is not allowed to be changed after this
    happened!

    Args:
        document_id (int):
        json_body (SendInvoiceViaEMailJsonBody):

    Returns:
        Response[Union[Any, SendInvoiceViaEMailResponse201]]
    """

    return (
        await asyncio_detailed(
            document_id=document_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
