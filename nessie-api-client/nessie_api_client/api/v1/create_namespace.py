from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.namespace import Namespace
from ...models.namespace_v1 import NamespaceV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: str,
    name: "Namespace",
    *,
    json_body: Namespace,
    hash_on_ref: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["hashOnRef"] = hash_on_ref

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/v1/namespaces/namespace/{ref}/{name}".format(
            ref=ref,
            name=name,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NamespaceV1]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NamespaceV1.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NamespaceV1]]:
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
    json_body: Namespace,
    hash_on_ref: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, NamespaceV1]]:
    """Creates a Namespace

    Args:
        ref (str):
        name (Namespace):
        hash_on_ref (Union[Unset, None, str]):
        json_body (Namespace):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NamespaceV1]]
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


def sync(
    ref: str,
    name: "Namespace",
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Namespace,
    hash_on_ref: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, NamespaceV1]]:
    """Creates a Namespace

    Args:
        ref (str):
        name (Namespace):
        hash_on_ref (Union[Unset, None, str]):
        json_body (Namespace):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NamespaceV1]
    """

    return sync_detailed(
        ref=ref,
        name=name,
        client=client,
        json_body=json_body,
        hash_on_ref=hash_on_ref,
    ).parsed


async def asyncio_detailed(
    ref: str,
    name: "Namespace",
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Namespace,
    hash_on_ref: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, NamespaceV1]]:
    """Creates a Namespace

    Args:
        ref (str):
        name (Namespace):
        hash_on_ref (Union[Unset, None, str]):
        json_body (Namespace):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NamespaceV1]]
    """

    kwargs = _get_kwargs(
        ref=ref,
        name=name,
        json_body=json_body,
        hash_on_ref=hash_on_ref,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ref: str,
    name: "Namespace",
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Namespace,
    hash_on_ref: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, NamespaceV1]]:
    """Creates a Namespace

    Args:
        ref (str):
        name (Namespace):
        hash_on_ref (Union[Unset, None, str]):
        json_body (Namespace):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NamespaceV1]
    """

    return (
        await asyncio_detailed(
            ref=ref,
            name=name,
            client=client,
            json_body=json_body,
            hash_on_ref=hash_on_ref,
        )
    ).parsed
