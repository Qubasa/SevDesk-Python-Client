from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_invoices_response_200 import GetInvoicesResponse200
from ...models.get_invoices_status import GetInvoicesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    status: Union[Unset, None, GetInvoicesStatus] = UNSET,
    invoice_number: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, int] = UNSET,
    end_date: Union[Unset, None, int] = UNSET,
    contactid: Union[Unset, None, int] = UNSET,
    contactobject_name: Union[Unset, None, str] = UNSET,
    customer_internal_note: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Invoice".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["invoiceNumber"] = invoice_number

    params["startDate"] = start_date

    params["endDate"] = end_date

    params["contact[id]"] = contactid

    params["contact[objectName]"] = contactobject_name

    params["customerInternalNote"] = customer_internal_note

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
) -> Optional[Union[Any, GetInvoicesResponse200]]:
    if response.status_code == 200:
        response_200 = GetInvoicesResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetInvoicesResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    status: Union[Unset, None, GetInvoicesStatus] = UNSET,
    invoice_number: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, int] = UNSET,
    end_date: Union[Unset, None, int] = UNSET,
    contactid: Union[Unset, None, int] = UNSET,
    contactobject_name: Union[Unset, None, str] = UNSET,
    customer_internal_note: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetInvoicesResponse200]]:
    """Retrieve invoices

     There are a multitude of parameter which can be used to filter. A few of them are attached but
         for a complete list please check out <a
    href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-invoices#filtering'>this</a> list

    Args:
        status (Union[Unset, None, GetInvoicesStatus]):
        invoice_number (Union[Unset, None, str]):
        start_date (Union[Unset, None, int]):
        end_date (Union[Unset, None, int]):
        contactid (Union[Unset, None, int]):
        contactobject_name (Union[Unset, None, str]):
        customer_internal_note (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, GetInvoicesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        status=status,
        invoice_number=invoice_number,
        start_date=start_date,
        end_date=end_date,
        contactid=contactid,
        contactobject_name=contactobject_name,
        customer_internal_note=customer_internal_note,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    status: Union[Unset, None, GetInvoicesStatus] = UNSET,
    invoice_number: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, int] = UNSET,
    end_date: Union[Unset, None, int] = UNSET,
    contactid: Union[Unset, None, int] = UNSET,
    contactobject_name: Union[Unset, None, str] = UNSET,
    customer_internal_note: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetInvoicesResponse200]]:
    """Retrieve invoices

     There are a multitude of parameter which can be used to filter. A few of them are attached but
         for a complete list please check out <a
    href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-invoices#filtering'>this</a> list

    Args:
        status (Union[Unset, None, GetInvoicesStatus]):
        invoice_number (Union[Unset, None, str]):
        start_date (Union[Unset, None, int]):
        end_date (Union[Unset, None, int]):
        contactid (Union[Unset, None, int]):
        contactobject_name (Union[Unset, None, str]):
        customer_internal_note (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, GetInvoicesResponse200]]
    """

    return sync_detailed(
        client=client,
        status=status,
        invoice_number=invoice_number,
        start_date=start_date,
        end_date=end_date,
        contactid=contactid,
        contactobject_name=contactobject_name,
        customer_internal_note=customer_internal_note,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    status: Union[Unset, None, GetInvoicesStatus] = UNSET,
    invoice_number: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, int] = UNSET,
    end_date: Union[Unset, None, int] = UNSET,
    contactid: Union[Unset, None, int] = UNSET,
    contactobject_name: Union[Unset, None, str] = UNSET,
    customer_internal_note: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetInvoicesResponse200]]:
    """Retrieve invoices

     There are a multitude of parameter which can be used to filter. A few of them are attached but
         for a complete list please check out <a
    href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-invoices#filtering'>this</a> list

    Args:
        status (Union[Unset, None, GetInvoicesStatus]):
        invoice_number (Union[Unset, None, str]):
        start_date (Union[Unset, None, int]):
        end_date (Union[Unset, None, int]):
        contactid (Union[Unset, None, int]):
        contactobject_name (Union[Unset, None, str]):
        customer_internal_note (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, GetInvoicesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        status=status,
        invoice_number=invoice_number,
        start_date=start_date,
        end_date=end_date,
        contactid=contactid,
        contactobject_name=contactobject_name,
        customer_internal_note=customer_internal_note,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    status: Union[Unset, None, GetInvoicesStatus] = UNSET,
    invoice_number: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, int] = UNSET,
    end_date: Union[Unset, None, int] = UNSET,
    contactid: Union[Unset, None, int] = UNSET,
    contactobject_name: Union[Unset, None, str] = UNSET,
    customer_internal_note: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetInvoicesResponse200]]:
    """Retrieve invoices

     There are a multitude of parameter which can be used to filter. A few of them are attached but
         for a complete list please check out <a
    href='https://5677.extern.sevdesk.dev/apiOverview/index.html#/doc-invoices#filtering'>this</a> list

    Args:
        status (Union[Unset, None, GetInvoicesStatus]):
        invoice_number (Union[Unset, None, str]):
        start_date (Union[Unset, None, int]):
        end_date (Union[Unset, None, int]):
        contactid (Union[Unset, None, int]):
        contactobject_name (Union[Unset, None, str]):
        customer_internal_note (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, GetInvoicesResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            invoice_number=invoice_number,
            start_date=start_date,
            end_date=end_date,
            contactid=contactid,
            contactobject_name=contactobject_name,
            customer_internal_note=customer_internal_note,
        )
    ).parsed
