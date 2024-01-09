from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: Any,
    *,
    type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["type"] = type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": "/v2/trees/{ref}".format(
            ref=ref,
        ),
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.CONFLICT:
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
    ref: Any,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Delete a reference

     The 'ref' parameter identifies the branch or tag to be deleted.
    The 'ref' parameter may contain a hash qualifier. That hash as well as the optional 'type' parameter
    may be used to ensure the operation is performed on the same object that the user expects.

    Only branches and tags can be deleted. However, deleting the default branch may be restricted.

    Args:
        ref (Any):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ref: Any,
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Delete a reference

     The 'ref' parameter identifies the branch or tag to be deleted.
    The 'ref' parameter may contain a hash qualifier. That hash as well as the optional 'type' parameter
    may be used to ensure the operation is performed on the same object that the user expects.

    Only branches and tags can be deleted. However, deleting the default branch may be restricted.

    Args:
        ref (Any):
        type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
