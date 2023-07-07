import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_balance_at_date_response_200 import GetBalanceAtDateResponse200
from ...types import UNSET, Response


def _get_kwargs(
    check_account_id: int,
    *,
    client: Client,
    date: datetime.date,
) -> Dict[str, Any]:
    url = "{}/CheckAccount/{checkAccountId}/getBalanceAtDate".format(
        client.base_url, checkAccountId=check_account_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, GetBalanceAtDateResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetBalanceAtDateResponse200.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, GetBalanceAtDateResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    check_account_id: int,
    *,
    client: Client,
    date: datetime.date,
) -> Response[Union[Any, GetBalanceAtDateResponse200]]:
    """Get the balance at a given date

     Get the balance, calculated as the sum of all transactions sevDesk knows, up to and including the
    given date. Note that this balance does not have to be the actual bank account balance, e.g. if
    sevDesk did not import old transactions.

    Args:
        check_account_id (int):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetBalanceAtDateResponse200]]
    """

    kwargs = _get_kwargs(
        check_account_id=check_account_id,
        client=client,
        date=date,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    check_account_id: int,
    *,
    client: Client,
    date: datetime.date,
) -> Optional[Union[Any, GetBalanceAtDateResponse200]]:
    """Get the balance at a given date

     Get the balance, calculated as the sum of all transactions sevDesk knows, up to and including the
    given date. Note that this balance does not have to be the actual bank account balance, e.g. if
    sevDesk did not import old transactions.

    Args:
        check_account_id (int):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetBalanceAtDateResponse200]
    """

    return sync_detailed(
        check_account_id=check_account_id,
        client=client,
        date=date,
    ).parsed


async def asyncio_detailed(
    check_account_id: int,
    *,
    client: Client,
    date: datetime.date,
) -> Response[Union[Any, GetBalanceAtDateResponse200]]:
    """Get the balance at a given date

     Get the balance, calculated as the sum of all transactions sevDesk knows, up to and including the
    given date. Note that this balance does not have to be the actual bank account balance, e.g. if
    sevDesk did not import old transactions.

    Args:
        check_account_id (int):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetBalanceAtDateResponse200]]
    """

    kwargs = _get_kwargs(
        check_account_id=check_account_id,
        client=client,
        date=date,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    check_account_id: int,
    *,
    client: Client,
    date: datetime.date,
) -> Optional[Union[Any, GetBalanceAtDateResponse200]]:
    """Get the balance at a given date

     Get the balance, calculated as the sum of all transactions sevDesk knows, up to and including the
    given date. Note that this balance does not have to be the actual bank account balance, e.g. if
    sevDesk did not import old transactions.

    Args:
        check_account_id (int):
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetBalanceAtDateResponse200]
    """

    return (
        await asyncio_detailed(
            check_account_id=check_account_id,
            client=client,
            date=date,
        )
    ).parsed
