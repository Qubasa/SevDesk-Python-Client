from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.create_voucher_by_factory_json_body import CreateVoucherByFactoryJsonBody
from ...models.save_voucher_response import SaveVoucherResponse
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateVoucherByFactoryJsonBody,
) -> Dict[str, Any]:
    url = "{}/Voucher/Factory/saveVoucher".format(client.base_url)

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
) -> Optional[Union[Any, SaveVoucherResponse, ValidationError]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SaveVoucherResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ValidationError.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, SaveVoucherResponse, ValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateVoucherByFactoryJsonBody,
) -> Response[Union[Any, SaveVoucherResponse, ValidationError]]:
    r"""Create a new voucher

     Bundles the creation or updating of voucher and voucher position.<br> The list of parameters starts
    with the voucher array.<br> This array contains all required attributes for a complete voucher.<br>
    Most of the attributes are covered in the voucher attribute list, there are only two parameters
    standing out, namely <b>mapAll</b> and <b>objectName</b>.<br> These are just needed for our system
    and you always need to provide them.<br><br> The list of parameters then continues with the voucher
    position array.<br> With this array you have the possibility to add multiple positions at once.<br>
    In the example it only contains one position, again together with the parameters <b>mapAll</b> and
    <b>objectName</b>, however, you can add more voucher positions by extending the array.<br> So if you
    wanted to add another position, you would add the same list of parameters with an incremented array
    index of \\"1\\" instead of \\"0\\".<br><br> The list ends with the two parameters voucherPosDelete
    and filename.<br> We will shortly explain what they can do.<br> With voucherPosDelete you have to
    option to delete voucher positions as this request can also be used to update vouchers.<br> With
    filename you can attach a file to the voucher.<br> For most of our customers this is a really
    important step, as they need to digitize their receipts.<br> Finally, after covering all parameters,
    they only important information left, is that the order of the last two attributes always needs to
    be kept.

    Args:
        json_body (CreateVoucherByFactoryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SaveVoucherResponse, ValidationError]]
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
    json_body: CreateVoucherByFactoryJsonBody,
) -> Optional[Union[Any, SaveVoucherResponse, ValidationError]]:
    r"""Create a new voucher

     Bundles the creation or updating of voucher and voucher position.<br> The list of parameters starts
    with the voucher array.<br> This array contains all required attributes for a complete voucher.<br>
    Most of the attributes are covered in the voucher attribute list, there are only two parameters
    standing out, namely <b>mapAll</b> and <b>objectName</b>.<br> These are just needed for our system
    and you always need to provide them.<br><br> The list of parameters then continues with the voucher
    position array.<br> With this array you have the possibility to add multiple positions at once.<br>
    In the example it only contains one position, again together with the parameters <b>mapAll</b> and
    <b>objectName</b>, however, you can add more voucher positions by extending the array.<br> So if you
    wanted to add another position, you would add the same list of parameters with an incremented array
    index of \\"1\\" instead of \\"0\\".<br><br> The list ends with the two parameters voucherPosDelete
    and filename.<br> We will shortly explain what they can do.<br> With voucherPosDelete you have to
    option to delete voucher positions as this request can also be used to update vouchers.<br> With
    filename you can attach a file to the voucher.<br> For most of our customers this is a really
    important step, as they need to digitize their receipts.<br> Finally, after covering all parameters,
    they only important information left, is that the order of the last two attributes always needs to
    be kept.

    Args:
        json_body (CreateVoucherByFactoryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SaveVoucherResponse, ValidationError]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateVoucherByFactoryJsonBody,
) -> Response[Union[Any, SaveVoucherResponse, ValidationError]]:
    r"""Create a new voucher

     Bundles the creation or updating of voucher and voucher position.<br> The list of parameters starts
    with the voucher array.<br> This array contains all required attributes for a complete voucher.<br>
    Most of the attributes are covered in the voucher attribute list, there are only two parameters
    standing out, namely <b>mapAll</b> and <b>objectName</b>.<br> These are just needed for our system
    and you always need to provide them.<br><br> The list of parameters then continues with the voucher
    position array.<br> With this array you have the possibility to add multiple positions at once.<br>
    In the example it only contains one position, again together with the parameters <b>mapAll</b> and
    <b>objectName</b>, however, you can add more voucher positions by extending the array.<br> So if you
    wanted to add another position, you would add the same list of parameters with an incremented array
    index of \\"1\\" instead of \\"0\\".<br><br> The list ends with the two parameters voucherPosDelete
    and filename.<br> We will shortly explain what they can do.<br> With voucherPosDelete you have to
    option to delete voucher positions as this request can also be used to update vouchers.<br> With
    filename you can attach a file to the voucher.<br> For most of our customers this is a really
    important step, as they need to digitize their receipts.<br> Finally, after covering all parameters,
    they only important information left, is that the order of the last two attributes always needs to
    be kept.

    Args:
        json_body (CreateVoucherByFactoryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SaveVoucherResponse, ValidationError]]
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
    json_body: CreateVoucherByFactoryJsonBody,
) -> Optional[Union[Any, SaveVoucherResponse, ValidationError]]:
    r"""Create a new voucher

     Bundles the creation or updating of voucher and voucher position.<br> The list of parameters starts
    with the voucher array.<br> This array contains all required attributes for a complete voucher.<br>
    Most of the attributes are covered in the voucher attribute list, there are only two parameters
    standing out, namely <b>mapAll</b> and <b>objectName</b>.<br> These are just needed for our system
    and you always need to provide them.<br><br> The list of parameters then continues with the voucher
    position array.<br> With this array you have the possibility to add multiple positions at once.<br>
    In the example it only contains one position, again together with the parameters <b>mapAll</b> and
    <b>objectName</b>, however, you can add more voucher positions by extending the array.<br> So if you
    wanted to add another position, you would add the same list of parameters with an incremented array
    index of \\"1\\" instead of \\"0\\".<br><br> The list ends with the two parameters voucherPosDelete
    and filename.<br> We will shortly explain what they can do.<br> With voucherPosDelete you have to
    option to delete voucher positions as this request can also be used to update vouchers.<br> With
    filename you can attach a file to the voucher.<br> For most of our customers this is a really
    important step, as they need to digitize their receipts.<br> Finally, after covering all parameters,
    they only important information left, is that the order of the last two attributes always needs to
    be kept.

    Args:
        json_body (CreateVoucherByFactoryJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SaveVoucherResponse, ValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
