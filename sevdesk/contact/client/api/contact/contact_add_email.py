from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contact_add_email_json_body import ContactAddEmailJsonBody
from ...models.contact_add_email_response_200 import ContactAddEmailResponse200
from ...types import Response


def _get_kwargs(
    contact_id: int,
    *,
    client: Client,
    json_body: ContactAddEmailJsonBody,
) -> Dict[str, Any]:
    url = "{}/Contact/{contactId}/addEmail".format(
        client.base_url, contactId=contact_id
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
) -> Optional[Union[Any, ContactAddEmailResponse200]]:
    if response.status_code == 200:
        response_200 = ContactAddEmailResponse200.from_dict(response.json())

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
) -> Response[Union[Any, ContactAddEmailResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    contact_id: int,
    *,
    client: Client,
    json_body: ContactAddEmailJsonBody,
) -> Response[Union[Any, ContactAddEmailResponse200]]:
    """Add email to contact

     Adds an email to a contact.

    Args:
        contact_id (int):
        json_body (ContactAddEmailJsonBody):

    Returns:
        Response[Union[Any, ContactAddEmailResponse200]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    contact_id: int,
    *,
    client: Client,
    json_body: ContactAddEmailJsonBody,
) -> Optional[Union[Any, ContactAddEmailResponse200]]:
    """Add email to contact

     Adds an email to a contact.

    Args:
        contact_id (int):
        json_body (ContactAddEmailJsonBody):

    Returns:
        Response[Union[Any, ContactAddEmailResponse200]]
    """

    return sync_detailed(
        contact_id=contact_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    contact_id: int,
    *,
    client: Client,
    json_body: ContactAddEmailJsonBody,
) -> Response[Union[Any, ContactAddEmailResponse200]]:
    """Add email to contact

     Adds an email to a contact.

    Args:
        contact_id (int):
        json_body (ContactAddEmailJsonBody):

    Returns:
        Response[Union[Any, ContactAddEmailResponse200]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    contact_id: int,
    *,
    client: Client,
    json_body: ContactAddEmailJsonBody,
) -> Optional[Union[Any, ContactAddEmailResponse200]]:
    """Add email to contact

     Adds an email to a contact.

    Args:
        contact_id (int):
        json_body (ContactAddEmailJsonBody):

    Returns:
        Response[Union[Any, ContactAddEmailResponse200]]
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
