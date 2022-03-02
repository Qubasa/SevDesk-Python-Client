from typing import Any, Dict

import httpx

from ...client import Client
from ...models.credit_note_change_status_json_body import CreditNoteChangeStatusJsonBody
from ...types import Response


def _get_kwargs(
    document_id: int,
    *,
    client: Client,
    json_body: CreditNoteChangeStatusJsonBody,
) -> Dict[str, Any]:
    url = "{}/CreditNote/{DocumentId}/changeStatus".format(
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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    document_id: int,
    *,
    client: Client,
    json_body: CreditNoteChangeStatusJsonBody,
) -> Response[Any]:
    """Changed status of invoice if not enshrined

    Args:
        document_id (int):
        json_body (CreditNoteChangeStatusJsonBody):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    document_id: int,
    *,
    client: Client,
    json_body: CreditNoteChangeStatusJsonBody,
) -> Response[Any]:
    """Changed status of invoice if not enshrined

    Args:
        document_id (int):
        json_body (CreditNoteChangeStatusJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        document_id=document_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
