from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_credit_note_pos_response_200 import GetCreditNotePosResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    credit_noteobject_name: str,
    credit_noteid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/CreditNotePos".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["creditNote[objectName]"] = credit_noteobject_name

    params["creditNote[id]"] = credit_noteid

    params["limit"] = limit

    params["embed"] = embed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, GetCreditNotePosResponse200]]:
    if response.status_code == 200:
        response_200 = GetCreditNotePosResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetCreditNotePosResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    credit_noteobject_name: str,
    credit_noteid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetCreditNotePosResponse200]]:
    """Get credit note positions

     Get all positions corresponding to a credit note

    Args:
        credit_noteobject_name (str):
        credit_noteid (int):
        limit (Union[Unset, None, int]):
        embed (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, GetCreditNotePosResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        credit_noteobject_name=credit_noteobject_name,
        credit_noteid=credit_noteid,
        limit=limit,
        embed=embed,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    credit_noteobject_name: str,
    credit_noteid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetCreditNotePosResponse200]]:
    """Get credit note positions

     Get all positions corresponding to a credit note

    Args:
        credit_noteobject_name (str):
        credit_noteid (int):
        limit (Union[Unset, None, int]):
        embed (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, GetCreditNotePosResponse200]]
    """

    return sync_detailed(
        client=client,
        credit_noteobject_name=credit_noteobject_name,
        credit_noteid=credit_noteid,
        limit=limit,
        embed=embed,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    credit_noteobject_name: str,
    credit_noteid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetCreditNotePosResponse200]]:
    """Get credit note positions

     Get all positions corresponding to a credit note

    Args:
        credit_noteobject_name (str):
        credit_noteid (int):
        limit (Union[Unset, None, int]):
        embed (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, GetCreditNotePosResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        credit_noteobject_name=credit_noteobject_name,
        credit_noteid=credit_noteid,
        limit=limit,
        embed=embed,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    credit_noteobject_name: str,
    credit_noteid: int,
    limit: Union[Unset, None, int] = UNSET,
    embed: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetCreditNotePosResponse200]]:
    """Get credit note positions

     Get all positions corresponding to a credit note

    Args:
        credit_noteobject_name (str):
        credit_noteid (int):
        limit (Union[Unset, None, int]):
        embed (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, GetCreditNotePosResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            credit_noteobject_name=credit_noteobject_name,
            credit_noteid=credit_noteid,
            limit=limit,
            embed=embed,
        )
    ).parsed
