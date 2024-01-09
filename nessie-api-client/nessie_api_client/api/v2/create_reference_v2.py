from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.branch import Branch
from ...models.detached_commit_hash import DetachedCommitHash
from ...models.tag import Tag
from ...types import UNSET, Response


def _get_kwargs(
    *,
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    name: str,
    type: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["name"] = name

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
        "method": "post",
        "url": "/v2/trees",
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
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
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    name: str,
    type: str,
) -> Response[Any]:
    """Create a new branch or tag

     The name and type query parameters define the kind of reference to be created. The payload object
    defines the new reference's origin in the commit history.
    Only branches and tags can be created by this method, but the payload object may be any valid
    reference, including a detached commit.
    If the payload reference object does not define a commit hash, the HEAD of that reference will be
    used.

    Args:
        name (str):
        type (str):
        json_body (Union['Branch', 'DetachedCommitHash', 'Tag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        name=name,
        type=type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    name: str,
    type: str,
) -> Response[Any]:
    """Create a new branch or tag

     The name and type query parameters define the kind of reference to be created. The payload object
    defines the new reference's origin in the commit history.
    Only branches and tags can be created by this method, but the payload object may be any valid
    reference, including a detached commit.
    If the payload reference object does not define a commit hash, the HEAD of that reference will be
    used.

    Args:
        name (str):
        type (str):
        json_body (Union['Branch', 'DetachedCommitHash', 'Tag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        name=name,
        type=type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
