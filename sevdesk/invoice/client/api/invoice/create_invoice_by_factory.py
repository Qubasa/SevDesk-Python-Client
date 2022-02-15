from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.create_invoice_by_factory_json_body import CreateInvoiceByFactoryJsonBody
from ...models.create_invoice_by_factory_response_201 import (
    CreateInvoiceByFactoryResponse201,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateInvoiceByFactoryJsonBody,
) -> Dict[str, Any]:
    url = "{}/Invoice/Factory/saveInvoice".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, CreateInvoiceByFactoryResponse201]]:
    if response.status_code == 201:
        response_201 = CreateInvoiceByFactoryResponse201.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, CreateInvoiceByFactoryResponse201]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateInvoiceByFactoryJsonBody,
) -> Response[Union[Any, CreateInvoiceByFactoryResponse201]]:
    """Create a new invoice

     This endpoint offers you the following functionality.
         <ul>
            <li>Create invoices together with positions and discounts</li>
            <li>Delete positions while adding new ones</li>
            <li>Delete or add discounts, or both at the same time</li>
            <li>Automatically fill the address of the supplied contact into the invoice address</li>
         </ul>
         To make your own request sample slimmer, you can omit all parameters which are not required and
    nullable.
         However, for a valid and logical bookkeeping document, you will also need some of them to
    ensure that all the necessary data is in the invoice.

    Args:
        json_body (CreateInvoiceByFactoryJsonBody):

    Returns:
        Response[Union[Any, CreateInvoiceByFactoryResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CreateInvoiceByFactoryJsonBody,
) -> Optional[Union[Any, CreateInvoiceByFactoryResponse201]]:
    """Create a new invoice

     This endpoint offers you the following functionality.
         <ul>
            <li>Create invoices together with positions and discounts</li>
            <li>Delete positions while adding new ones</li>
            <li>Delete or add discounts, or both at the same time</li>
            <li>Automatically fill the address of the supplied contact into the invoice address</li>
         </ul>
         To make your own request sample slimmer, you can omit all parameters which are not required and
    nullable.
         However, for a valid and logical bookkeeping document, you will also need some of them to
    ensure that all the necessary data is in the invoice.

    Args:
        json_body (CreateInvoiceByFactoryJsonBody):

    Returns:
        Response[Union[Any, CreateInvoiceByFactoryResponse201]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateInvoiceByFactoryJsonBody,
) -> Response[Union[Any, CreateInvoiceByFactoryResponse201]]:
    """Create a new invoice

     This endpoint offers you the following functionality.
         <ul>
            <li>Create invoices together with positions and discounts</li>
            <li>Delete positions while adding new ones</li>
            <li>Delete or add discounts, or both at the same time</li>
            <li>Automatically fill the address of the supplied contact into the invoice address</li>
         </ul>
         To make your own request sample slimmer, you can omit all parameters which are not required and
    nullable.
         However, for a valid and logical bookkeeping document, you will also need some of them to
    ensure that all the necessary data is in the invoice.

    Args:
        json_body (CreateInvoiceByFactoryJsonBody):

    Returns:
        Response[Union[Any, CreateInvoiceByFactoryResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateInvoiceByFactoryJsonBody,
) -> Optional[Union[Any, CreateInvoiceByFactoryResponse201]]:
    """Create a new invoice

     This endpoint offers you the following functionality.
         <ul>
            <li>Create invoices together with positions and discounts</li>
            <li>Delete positions while adding new ones</li>
            <li>Delete or add discounts, or both at the same time</li>
            <li>Automatically fill the address of the supplied contact into the invoice address</li>
         </ul>
         To make your own request sample slimmer, you can omit all parameters which are not required and
    nullable.
         However, for a valid and logical bookkeeping document, you will also need some of them to
    ensure that all the necessary data is in the invoice.

    Args:
        json_body (CreateInvoiceByFactoryJsonBody):

    Returns:
        Response[Union[Any, CreateInvoiceByFactoryResponse201]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
