from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_namespaces_response_v1 import GetNamespacesResponseV1
from ...models.namespace import Namespace
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: str,
    *,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, "Namespace"] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["hashOnRef"] = hash_on_ref

    json_name: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(name, Unset):
        json_name = name.to_dict() if name else None

    if not isinstance(json_name, Unset) and json_name is not None:
        params.update(json_name)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/namespaces/{ref}".format(
            ref=ref,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetNamespacesResponseV1]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetNamespacesResponseV1.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetNamespacesResponseV1]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hash_on_ref: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, "Namespace"] = UNSET,
) -> Response[Union[Any, GetNamespacesResponseV1]]:
    """
    Args:
        ref (str):
        hash_on_ref (Union[Unset, None, str]):
        name (Union[Unset, None, Namespace]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetNamespacesResponseV1]]
    """

    kwargs = _get_kwargs(
        ref=ref,
        hash_on_ref=hash_on_ref,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hash_on_ref: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, "Namespace"] = UNSET,
) -> Optional[Union[Any, GetNamespacesResponseV1]]:
    """
    Args:
        ref (str):
        hash_on_ref (Union[Unset, None, str]):
        name (Union[Unset, None, Namespace]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetNamespacesResponseV1]
    """

    return sync_detailed(
        ref=ref,
        client=client,
        hash_on_ref=hash_on_ref,
        name=name,
    ).parsed


async def asyncio_detailed(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hash_on_ref: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, "Namespace"] = UNSET,
) -> Response[Union[Any, GetNamespacesResponseV1]]:
    """
    Args:
        ref (str):
        hash_on_ref (Union[Unset, None, str]):
        name (Union[Unset, None, Namespace]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetNamespacesResponseV1]]
    """

    kwargs = _get_kwargs(
        ref=ref,
        hash_on_ref=hash_on_ref,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    hash_on_ref: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, "Namespace"] = UNSET,
) -> Optional[Union[Any, GetNamespacesResponseV1]]:
    """
    Args:
        ref (str):
        hash_on_ref (Union[Unset, None, str]):
        name (Union[Unset, None, Namespace]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetNamespacesResponseV1]
    """

    return (
        await asyncio_detailed(
            ref=ref,
            client=client,
            hash_on_ref=hash_on_ref,
            name=name,
        )
    ).parsed
