from typing import Any, Dict

import httpx

from ...client import Client
from ...models.invoice_change_status_json_body import InvoiceChangeStatusJsonBody
from ...types import Response


def _get_kwargs(
    invoice_id: int,
    *,
    client: Client,
    json_body: InvoiceChangeStatusJsonBody,
) -> Dict[str, Any]:
    url = "{}/Invoice/{invoiceId}/changeStatus".format(
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    invoice_id: int,
    *,
    client: Client,
    json_body: InvoiceChangeStatusJsonBody,
) -> Response[Any]:
    """Changed status of invoice if not enshrined

    Args:
        invoice_id (int):
        json_body (InvoiceChangeStatusJsonBody):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    invoice_id: int,
    *,
    client: Client,
    json_body: InvoiceChangeStatusJsonBody,
) -> Response[Any]:
    """Changed status of invoice if not enshrined

    Args:
        invoice_id (int):
        json_body (InvoiceChangeStatusJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
