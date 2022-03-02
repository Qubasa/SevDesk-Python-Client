from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_next_credit_note_number_response_200 import (
    GetNextCreditNoteNumberResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    credit_note_type: str,
    use_next_number: bool,
) -> Dict[str, Any]:
    url = "{}/CreditNote/Factory/getNextCreditNoteNumber".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["creditNoteType"] = credit_note_type

    params["useNextNumber"] = use_next_number

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
) -> Optional[Union[Any, GetNextCreditNoteNumberResponse200]]:
    if response.status_code == 200:
        response_200 = GetNextCreditNoteNumberResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetNextCreditNoteNumberResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    credit_note_type: str,
    use_next_number: bool,
) -> Response[Union[Any, GetNextCreditNoteNumberResponse200]]:
    """Get the next credit note number

    Args:
        credit_note_type (str):
        use_next_number (bool):

    Returns:
        Response[Union[Any, GetNextCreditNoteNumberResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        credit_note_type=credit_note_type,
        use_next_number=use_next_number,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    credit_note_type: str,
    use_next_number: bool,
) -> Optional[Union[Any, GetNextCreditNoteNumberResponse200]]:
    """Get the next credit note number

    Args:
        credit_note_type (str):
        use_next_number (bool):

    Returns:
        Response[Union[Any, GetNextCreditNoteNumberResponse200]]
    """

    return sync_detailed(
        client=client,
        credit_note_type=credit_note_type,
        use_next_number=use_next_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    credit_note_type: str,
    use_next_number: bool,
) -> Response[Union[Any, GetNextCreditNoteNumberResponse200]]:
    """Get the next credit note number

    Args:
        credit_note_type (str):
        use_next_number (bool):

    Returns:
        Response[Union[Any, GetNextCreditNoteNumberResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        credit_note_type=credit_note_type,
        use_next_number=use_next_number,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    credit_note_type: str,
    use_next_number: bool,
) -> Optional[Union[Any, GetNextCreditNoteNumberResponse200]]:
    """Get the next credit note number

    Args:
        credit_note_type (str):
        use_next_number (bool):

    Returns:
        Response[Union[Any, GetNextCreditNoteNumberResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            credit_note_type=credit_note_type,
            use_next_number=use_next_number,
        )
    ).parsed
