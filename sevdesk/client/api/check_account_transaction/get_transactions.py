import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_transactions_response_200 import GetTransactionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    offset: int = 0,
    check_accountid: Union[Unset, None, int] = UNSET,
    check_accountobject_name: Union[Unset, None, str] = UNSET,
    is_booked: Union[Unset, None, bool] = UNSET,
    paymt_purpose: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    payee_payer_name: Union[Unset, None, str] = UNSET,
    only_credit: Union[Unset, None, bool] = UNSET,
    only_debit: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/CheckAccountTransaction".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["checkAccount[id]"] = check_accountid

    params["checkAccount[objectName]"] = check_accountobject_name

    params["isBooked"] = is_booked

    params["paymtPurpose"] = paymt_purpose

    params["offset"] = offset

    json_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat() if start_date else None

    params["startDate"] = json_start_date

    json_end_date: Union[Unset, None, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat() if end_date else None

    params["endDate"] = json_end_date

    params["payeePayerName"] = payee_payer_name

    params["onlyCredit"] = only_credit

    params["onlyDebit"] = only_debit

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
) -> Optional[Union[Any, GetTransactionsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTransactionsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetTransactionsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    offset: int,
    check_accountid: Union[Unset, None, int] = UNSET,
    check_accountobject_name: Union[Unset, None, str] = UNSET,
    is_booked: Union[Unset, None, bool] = UNSET,
    paymt_purpose: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    payee_payer_name: Union[Unset, None, str] = UNSET,
    only_credit: Union[Unset, None, bool] = UNSET,
    only_debit: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, GetTransactionsResponse200]]:
    """Retrieve transactions

     Retrieve all transactions depending on the filters defined in the query.

    Args:
        check_accountid (Union[Unset, None, int]):
        check_accountobject_name (Union[Unset, None, str]):
        is_booked (Union[Unset, None, bool]):
        paymt_purpose (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        payee_payer_name (Union[Unset, None, str]):
        only_credit (Union[Unset, None, bool]):
        only_debit (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTransactionsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        check_accountid=check_accountid,
        check_accountobject_name=check_accountobject_name,
        is_booked=is_booked,
        paymt_purpose=paymt_purpose,
        start_date=start_date,
        end_date=end_date,
        payee_payer_name=payee_payer_name,
        only_credit=only_credit,
        only_debit=only_debit,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    offset: int = 0,
    check_accountid: Union[Unset, None, int] = UNSET,
    check_accountobject_name: Union[Unset, None, str] = UNSET,
    is_booked: Union[Unset, None, bool] = UNSET,
    paymt_purpose: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    payee_payer_name: Union[Unset, None, str] = UNSET,
    only_credit: Union[Unset, None, bool] = UNSET,
    only_debit: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, GetTransactionsResponse200]]:
    """Retrieve transactions

     Retrieve all transactions depending on the filters defined in the query.

    Args:
        check_accountid (Union[Unset, None, int]):
        check_accountobject_name (Union[Unset, None, str]):
        is_booked (Union[Unset, None, bool]):
        paymt_purpose (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        payee_payer_name (Union[Unset, None, str]):
        only_credit (Union[Unset, None, bool]):
        only_debit (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetTransactionsResponse200]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        check_accountid=check_accountid,
        check_accountobject_name=check_accountobject_name,
        is_booked=is_booked,
        paymt_purpose=paymt_purpose,
        start_date=start_date,
        end_date=end_date,
        payee_payer_name=payee_payer_name,
        only_credit=only_credit,
        only_debit=only_debit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    check_accountid: Union[Unset, None, int] = UNSET,
    check_accountobject_name: Union[Unset, None, str] = UNSET,
    is_booked: Union[Unset, None, bool] = UNSET,
    paymt_purpose: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    payee_payer_name: Union[Unset, None, str] = UNSET,
    only_credit: Union[Unset, None, bool] = UNSET,
    only_debit: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, GetTransactionsResponse200]]:
    """Retrieve transactions

     Retrieve all transactions depending on the filters defined in the query.

    Args:
        check_accountid (Union[Unset, None, int]):
        check_accountobject_name (Union[Unset, None, str]):
        is_booked (Union[Unset, None, bool]):
        paymt_purpose (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        payee_payer_name (Union[Unset, None, str]):
        only_credit (Union[Unset, None, bool]):
        only_debit (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTransactionsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        check_accountid=check_accountid,
        check_accountobject_name=check_accountobject_name,
        is_booked=is_booked,
        paymt_purpose=paymt_purpose,
        start_date=start_date,
        end_date=end_date,
        payee_payer_name=payee_payer_name,
        only_credit=only_credit,
        only_debit=only_debit,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    check_accountid: Union[Unset, None, int] = UNSET,
    check_accountobject_name: Union[Unset, None, str] = UNSET,
    is_booked: Union[Unset, None, bool] = UNSET,
    paymt_purpose: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    payee_payer_name: Union[Unset, None, str] = UNSET,
    only_credit: Union[Unset, None, bool] = UNSET,
    only_debit: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, GetTransactionsResponse200]]:
    """Retrieve transactions

     Retrieve all transactions depending on the filters defined in the query.

    Args:
        check_accountid (Union[Unset, None, int]):
        check_accountobject_name (Union[Unset, None, str]):
        is_booked (Union[Unset, None, bool]):
        paymt_purpose (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        payee_payer_name (Union[Unset, None, str]):
        only_credit (Union[Unset, None, bool]):
        only_debit (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetTransactionsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            check_accountid=check_accountid,
            check_accountobject_name=check_accountobject_name,
            is_booked=is_booked,
            paymt_purpose=paymt_purpose,
            start_date=start_date,
            end_date=end_date,
            payee_payer_name=payee_payer_name,
            only_credit=only_credit,
            only_debit=only_debit,
        )
    ).parsed
