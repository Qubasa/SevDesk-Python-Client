from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.create_credit_note_by_factory_json_body import (
    CreateCreditNoteByFactoryJsonBody,
)
from ...models.create_credit_note_by_factory_response_201 import (
    CreateCreditNoteByFactoryResponse201,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateCreditNoteByFactoryJsonBody,
) -> Dict[str, Any]:
    url = "{}/CreditNote/Factory/saveCreditNote".format(client.base_url)

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
) -> Optional[Union[Any, CreateCreditNoteByFactoryResponse201]]:
    if response.status_code == 201:
        response_201 = CreateCreditNoteByFactoryResponse201.from_dict(response.json())

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
) -> Response[Union[Any, CreateCreditNoteByFactoryResponse201]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateCreditNoteByFactoryJsonBody,
) -> Response[Union[Any, CreateCreditNoteByFactoryResponse201]]:
    """Create a new creditNote

    Args:
        json_body (CreateCreditNoteByFactoryJsonBody):

    Returns:
        Response[Union[Any, CreateCreditNoteByFactoryResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CreateCreditNoteByFactoryJsonBody,
) -> Optional[Union[Any, CreateCreditNoteByFactoryResponse201]]:
    """Create a new creditNote

    Args:
        json_body (CreateCreditNoteByFactoryJsonBody):

    Returns:
        Response[Union[Any, CreateCreditNoteByFactoryResponse201]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateCreditNoteByFactoryJsonBody,
) -> Response[Union[Any, CreateCreditNoteByFactoryResponse201]]:
    """Create a new creditNote

    Args:
        json_body (CreateCreditNoteByFactoryJsonBody):

    Returns:
        Response[Union[Any, CreateCreditNoteByFactoryResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateCreditNoteByFactoryJsonBody,
) -> Optional[Union[Any, CreateCreditNoteByFactoryResponse201]]:
    """Create a new creditNote

    Args:
        json_body (CreateCreditNoteByFactoryJsonBody):

    Returns:
        Response[Union[Any, CreateCreditNoteByFactoryResponse201]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
