from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.contact_address import ContactAddress
from ...models.update_contact_address_response_200 import (
    UpdateContactAddressResponse200,
)
from ...types import Response


def _get_kwargs(
    contact_address_id: int,
    *,
    client: Client,
    json_body: ContactAddress,
) -> Dict[str, Any]:
    url = "{}/ContactAddress/{contactAddressId}".format(
        client.base_url, contactAddressId=contact_address_id
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
) -> Optional[UpdateContactAddressResponse200]:
    if response.status_code == 200:
        response_200 = UpdateContactAddressResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[UpdateContactAddressResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    contact_address_id: int,
    *,
    client: Client,
    json_body: ContactAddress,
) -> Response[UpdateContactAddressResponse200]:
    """Update an existing contact address

     Update a contact address

    Args:
        contact_address_id (int):
        json_body (ContactAddress): ContactAddress model

    Returns:
        Response[UpdateContactAddressResponse200]
    """

    kwargs = _get_kwargs(
        contact_address_id=contact_address_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    contact_address_id: int,
    *,
    client: Client,
    json_body: ContactAddress,
) -> Optional[UpdateContactAddressResponse200]:
    """Update an existing contact address

     Update a contact address

    Args:
        contact_address_id (int):
        json_body (ContactAddress): ContactAddress model

    Returns:
        Response[UpdateContactAddressResponse200]
    """

    return sync_detailed(
        contact_address_id=contact_address_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    contact_address_id: int,
    *,
    client: Client,
    json_body: ContactAddress,
) -> Response[UpdateContactAddressResponse200]:
    """Update an existing contact address

     Update a contact address

    Args:
        contact_address_id (int):
        json_body (ContactAddress): ContactAddress model

    Returns:
        Response[UpdateContactAddressResponse200]
    """

    kwargs = _get_kwargs(
        contact_address_id=contact_address_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    contact_address_id: int,
    *,
    client: Client,
    json_body: ContactAddress,
) -> Optional[UpdateContactAddressResponse200]:
    """Update an existing contact address

     Update a contact address

    Args:
        contact_address_id (int):
        json_body (ContactAddress): ContactAddress model

    Returns:
        Response[UpdateContactAddressResponse200]
    """

    return (
        await asyncio_detailed(
            contact_address_id=contact_address_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
