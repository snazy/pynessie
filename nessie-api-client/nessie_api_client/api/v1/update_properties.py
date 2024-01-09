from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.namespace import Namespace
from ...models.namespace_update import NamespaceUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: str,
    name: "Namespace",
    *,
    json_body: NamespaceUpdate,
    hash_on_ref: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["hashOnRef"] = hash_on_ref

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v1/namespaces/namespace/{ref}/{name}".format(
            ref=ref,
            name=name,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ref: str,
    name: "Namespace",
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NamespaceUpdate,
    hash_on_ref: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        ref (str):
        name (Namespace):
        hash_on_ref (Union[Unset, None, str]):
        json_body (NamespaceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        name=name,
        json_body=json_body,
        hash_on_ref=hash_on_ref,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ref: str,
    name: "Namespace",
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NamespaceUpdate,
    hash_on_ref: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        ref (str):
        name (Namespace):
        hash_on_ref (Union[Unset, None, str]):
        json_body (NamespaceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        name=name,
        json_body=json_body,
        hash_on_ref=hash_on_ref,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
