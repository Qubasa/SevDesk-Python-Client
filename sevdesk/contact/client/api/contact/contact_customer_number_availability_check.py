from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.contact_customer_number_availability_check_response_200 import (
    ContactCustomerNumberAvailabilityCheckResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    customer_number: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Contact/Mapper/checkCustomerNumberAvailability".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["customerNumber"] = customer_number

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
) -> Optional[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]:
    if response.status_code == 200:
        response_200 = ContactCustomerNumberAvailabilityCheckResponse200.from_dict(
            response.json()
        )

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
) -> Response[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    customer_number: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]:
    """Check if a customer number is available

     Checks if a given customer number is available or already used.

    Args:
        customer_number (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        customer_number=customer_number,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    customer_number: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]:
    """Check if a customer number is available

     Checks if a given customer number is available or already used.

    Args:
        customer_number (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]
    """

    return sync_detailed(
        client=client,
        customer_number=customer_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    customer_number: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]:
    """Check if a customer number is available

     Checks if a given customer number is available or already used.

    Args:
        customer_number (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        customer_number=customer_number,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    customer_number: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]:
    """Check if a customer number is available

     Checks if a given customer number is available or already used.

    Args:
        customer_number (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ContactCustomerNumberAvailabilityCheckResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            customer_number=customer_number,
        )
    ).parsed
