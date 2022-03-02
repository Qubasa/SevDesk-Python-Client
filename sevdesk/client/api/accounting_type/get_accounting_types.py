from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_accounting_types_response_200 import GetAccountingTypesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
    use_client_accounting_chart: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    only_own: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/AccountingType".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["embed"] = embed

    params["useClientAccountingChart"] = use_client_accounting_chart

    params["limit"] = limit

    params["onlyOwn"] = only_own

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
) -> Optional[Union[Any, GetAccountingTypesResponse200]]:
    if response.status_code == 200:
        response_200 = GetAccountingTypesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetAccountingTypesResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
    use_client_accounting_chart: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    only_own: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, GetAccountingTypesResponse200]]:
    """Get available accounting types

    Args:
        embed (Union[Unset, None, str]):
        use_client_accounting_chart (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        only_own (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, GetAccountingTypesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        embed=embed,
        use_client_accounting_chart=use_client_accounting_chart,
        limit=limit,
        only_own=only_own,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
    use_client_accounting_chart: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    only_own: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, GetAccountingTypesResponse200]]:
    """Get available accounting types

    Args:
        embed (Union[Unset, None, str]):
        use_client_accounting_chart (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        only_own (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, GetAccountingTypesResponse200]]
    """

    return sync_detailed(
        client=client,
        embed=embed,
        use_client_accounting_chart=use_client_accounting_chart,
        limit=limit,
        only_own=only_own,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
    use_client_accounting_chart: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    only_own: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, GetAccountingTypesResponse200]]:
    """Get available accounting types

    Args:
        embed (Union[Unset, None, str]):
        use_client_accounting_chart (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        only_own (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, GetAccountingTypesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        embed=embed,
        use_client_accounting_chart=use_client_accounting_chart,
        limit=limit,
        only_own=only_own,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    embed: Union[Unset, None, str] = UNSET,
    use_client_accounting_chart: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    only_own: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, GetAccountingTypesResponse200]]:
    """Get available accounting types

    Args:
        embed (Union[Unset, None, str]):
        use_client_accounting_chart (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):
        only_own (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, GetAccountingTypesResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            embed=embed,
            use_client_accounting_chart=use_client_accounting_chart,
            limit=limit,
            only_own=only_own,
        )
    ).parsed
