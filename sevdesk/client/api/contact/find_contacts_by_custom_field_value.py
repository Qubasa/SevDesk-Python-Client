from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.find_contacts_by_custom_field_value_response_200 import (
    FindContactsByCustomFieldValueResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    value: str,
    custom_field_settingid: Union[Unset, None, str] = UNSET,
    custom_field_settingobject_name: Union[Unset, None, str] = UNSET,
    custom_field_name: str,
) -> Dict[str, Any]:
    url = "{}/Contact/Factory/findContactsByCustomFieldValue".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["value"] = value

    params["customFieldSetting[id]"] = custom_field_settingid

    params["customFieldSetting[objectName]"] = custom_field_settingobject_name

    params["customFieldName"] = custom_field_name

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
) -> Optional[Union[Any, FindContactsByCustomFieldValueResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FindContactsByCustomFieldValueResponse200.from_dict(
            response.json()
        )

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
) -> Response[Union[Any, FindContactsByCustomFieldValueResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    value: str,
    custom_field_settingid: Union[Unset, None, str] = UNSET,
    custom_field_settingobject_name: Union[Unset, None, str] = UNSET,
    custom_field_name: str,
) -> Response[Union[Any, FindContactsByCustomFieldValueResponse200]]:
    """Find contacts by custom field value

     Returns an array of contacts having a certain custom field value set.

    Args:
        value (str):
        custom_field_settingid (Union[Unset, None, str]):
        custom_field_settingobject_name (Union[Unset, None, str]):  Example:
            ContactCustomFieldSetting.
        custom_field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FindContactsByCustomFieldValueResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        value=value,
        custom_field_settingid=custom_field_settingid,
        custom_field_settingobject_name=custom_field_settingobject_name,
        custom_field_name=custom_field_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    value: str,
    custom_field_settingid: Union[Unset, None, str] = UNSET,
    custom_field_settingobject_name: Union[Unset, None, str] = UNSET,
    custom_field_name: str,
) -> Optional[Union[Any, FindContactsByCustomFieldValueResponse200]]:
    """Find contacts by custom field value

     Returns an array of contacts having a certain custom field value set.

    Args:
        value (str):
        custom_field_settingid (Union[Unset, None, str]):
        custom_field_settingobject_name (Union[Unset, None, str]):  Example:
            ContactCustomFieldSetting.
        custom_field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FindContactsByCustomFieldValueResponse200]
    """

    return sync_detailed(
        client=client,
        value=value,
        custom_field_settingid=custom_field_settingid,
        custom_field_settingobject_name=custom_field_settingobject_name,
        custom_field_name=custom_field_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    value: str,
    custom_field_settingid: Union[Unset, None, str] = UNSET,
    custom_field_settingobject_name: Union[Unset, None, str] = UNSET,
    custom_field_name: str,
) -> Response[Union[Any, FindContactsByCustomFieldValueResponse200]]:
    """Find contacts by custom field value

     Returns an array of contacts having a certain custom field value set.

    Args:
        value (str):
        custom_field_settingid (Union[Unset, None, str]):
        custom_field_settingobject_name (Union[Unset, None, str]):  Example:
            ContactCustomFieldSetting.
        custom_field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FindContactsByCustomFieldValueResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        value=value,
        custom_field_settingid=custom_field_settingid,
        custom_field_settingobject_name=custom_field_settingobject_name,
        custom_field_name=custom_field_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    value: str,
    custom_field_settingid: Union[Unset, None, str] = UNSET,
    custom_field_settingobject_name: Union[Unset, None, str] = UNSET,
    custom_field_name: str,
) -> Optional[Union[Any, FindContactsByCustomFieldValueResponse200]]:
    """Find contacts by custom field value

     Returns an array of contacts having a certain custom field value set.

    Args:
        value (str):
        custom_field_settingid (Union[Unset, None, str]):
        custom_field_settingobject_name (Union[Unset, None, str]):  Example:
            ContactCustomFieldSetting.
        custom_field_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FindContactsByCustomFieldValueResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            value=value,
            custom_field_settingid=custom_field_settingid,
            custom_field_settingobject_name=custom_field_settingobject_name,
            custom_field_name=custom_field_name,
        )
    ).parsed
