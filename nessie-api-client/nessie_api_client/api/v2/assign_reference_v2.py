from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.branch import Branch
from ...models.detached_commit_hash import DetachedCommitHash
from ...models.tag import Tag
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: Any,
    *,
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["type"] = type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body: Dict[str, Any]

    if isinstance(json_body, Branch):
        json_json_body = json_body.to_dict()

    elif isinstance(json_body, Tag):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/v2/trees/{ref}".format(
            ref=ref,
        ),
        "json": json_json_body,
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
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    type: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Set a named reference to a specific hash via another reference.

     The 'ref' parameter identifies the branch or tag to be reassigned.
    The 'ref' parameter may contain a hash qualifier. That hash as well as the optional 'type' parameter
    may be used to ensure the operation is performed on the same object that the user expects.

    Only branches and tags may be reassigned.
    The payload object identifies any reference visible to the current user whose 'hash' will be used to
    define the new HEAD of the reference being reassigned. Detached hashes may be used in the payload.

    Args:
        ref (Any):
        type (Union[Unset, None, str]):
        json_body (Union['Branch', 'DetachedCommitHash', 'Tag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        json_body=json_body,
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
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    type: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Set a named reference to a specific hash via another reference.

     The 'ref' parameter identifies the branch or tag to be reassigned.
    The 'ref' parameter may contain a hash qualifier. That hash as well as the optional 'type' parameter
    may be used to ensure the operation is performed on the same object that the user expects.

    Only branches and tags may be reassigned.
    The payload object identifies any reference visible to the current user whose 'hash' will be used to
    define the new HEAD of the reference being reassigned. Detached hashes may be used in the payload.

    Args:
        ref (Any):
        type (Union[Unset, None, str]):
        json_body (Union['Branch', 'DetachedCommitHash', 'Tag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        json_body=json_body,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
