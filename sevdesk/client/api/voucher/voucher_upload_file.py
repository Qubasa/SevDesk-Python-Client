from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.voucher_upload_file_multipart_data import VoucherUploadFileMultipartData
from ...models.voucher_upload_file_response_201 import VoucherUploadFileResponse201
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: VoucherUploadFileMultipartData,
) -> Dict[str, Any]:
    url = "{}/Voucher/Factory/uploadTempFile".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, VoucherUploadFileResponse201]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = VoucherUploadFileResponse201.from_dict(response.json())

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
) -> Response[Union[Any, VoucherUploadFileResponse201]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: VoucherUploadFileMultipartData,
) -> Response[Union[Any, VoucherUploadFileResponse201]]:
    """Upload voucher file

     To attach a document to a voucher, you will need to upload it first for later use.<br> To do this,
    you can use this request.<br> When you successfully uploaded the file, you will get a sevDesk
    internal filename in the response.<br> The filename will be a hash generated from your uploaded
    file. You will need it in the next request!<br> After you got the just mentioned filename, you can
    enter it as a value for the filename parameter of the saveVoucher request.<br> If you provided all
    necessary parameters and kept all of them in the right order, the file will be attached to your
    voucher.

    Args:
        multipart_data (VoucherUploadFileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VoucherUploadFileResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    multipart_data: VoucherUploadFileMultipartData,
) -> Optional[Union[Any, VoucherUploadFileResponse201]]:
    """Upload voucher file

     To attach a document to a voucher, you will need to upload it first for later use.<br> To do this,
    you can use this request.<br> When you successfully uploaded the file, you will get a sevDesk
    internal filename in the response.<br> The filename will be a hash generated from your uploaded
    file. You will need it in the next request!<br> After you got the just mentioned filename, you can
    enter it as a value for the filename parameter of the saveVoucher request.<br> If you provided all
    necessary parameters and kept all of them in the right order, the file will be attached to your
    voucher.

    Args:
        multipart_data (VoucherUploadFileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VoucherUploadFileResponse201]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: VoucherUploadFileMultipartData,
) -> Response[Union[Any, VoucherUploadFileResponse201]]:
    """Upload voucher file

     To attach a document to a voucher, you will need to upload it first for later use.<br> To do this,
    you can use this request.<br> When you successfully uploaded the file, you will get a sevDesk
    internal filename in the response.<br> The filename will be a hash generated from your uploaded
    file. You will need it in the next request!<br> After you got the just mentioned filename, you can
    enter it as a value for the filename parameter of the saveVoucher request.<br> If you provided all
    necessary parameters and kept all of them in the right order, the file will be attached to your
    voucher.

    Args:
        multipart_data (VoucherUploadFileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VoucherUploadFileResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: VoucherUploadFileMultipartData,
) -> Optional[Union[Any, VoucherUploadFileResponse201]]:
    """Upload voucher file

     To attach a document to a voucher, you will need to upload it first for later use.<br> To do this,
    you can use this request.<br> When you successfully uploaded the file, you will get a sevDesk
    internal filename in the response.<br> The filename will be a hash generated from your uploaded
    file. You will need it in the next request!<br> After you got the just mentioned filename, you can
    enter it as a value for the filename parameter of the saveVoucher request.<br> If you provided all
    necessary parameters and kept all of them in the right order, the file will be attached to your
    voucher.

    Args:
        multipart_data (VoucherUploadFileMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VoucherUploadFileResponse201]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
