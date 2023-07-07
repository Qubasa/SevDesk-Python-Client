from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.check_account_model import CheckAccountModel
from ...models.create_check_account_response_201 import CreateCheckAccountResponse201
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CheckAccountModel,
) -> Dict[str, Any]:
    url = "{}/CheckAccount".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, CreateCheckAccountResponse201]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateCheckAccountResponse201.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, CreateCheckAccountResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CheckAccountModel,
) -> Response[Union[Any, CreateCheckAccountResponse201]]:
    """Create a new check account

     Creates a new banking account on which transactions can be created.

    Args:
        json_body (CheckAccountModel): CheckAccount model. Responsible for the payment accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCheckAccountResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CheckAccountModel,
) -> Optional[Union[Any, CreateCheckAccountResponse201]]:
    """Create a new check account

     Creates a new banking account on which transactions can be created.

    Args:
        json_body (CheckAccountModel): CheckAccount model. Responsible for the payment accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCheckAccountResponse201]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CheckAccountModel,
) -> Response[Union[Any, CreateCheckAccountResponse201]]:
    """Create a new check account

     Creates a new banking account on which transactions can be created.

    Args:
        json_body (CheckAccountModel): CheckAccount model. Responsible for the payment accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCheckAccountResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CheckAccountModel,
) -> Optional[Union[Any, CreateCheckAccountResponse201]]:
    """Create a new check account

     Creates a new banking account on which transactions can be created.

    Args:
        json_body (CheckAccountModel): CheckAccount model. Responsible for the payment accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCheckAccountResponse201]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
