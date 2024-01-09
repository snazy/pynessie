from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.branch import Branch
from ...models.detached_commit_hash import DetachedCommitHash
from ...models.reference_type import ReferenceType
from ...models.tag import Tag
from ...types import UNSET, Response


def _get_kwargs(
    reference_type: ReferenceType,
    reference_name: str,
    *,
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    expected_hash: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["expectedHash"] = expected_hash

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
        "url": "/v1/trees/{referenceType}/{referenceName}".format(
            referenceType=reference_type,
            referenceName=reference_name,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
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
    reference_type: ReferenceType,
    reference_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    expected_hash: str,
) -> Response[Any]:
    """Set a named reference to a specific hash via a named-reference.

     This operation takes the name of the named reference to reassign and the hash and the name of a
    named-reference via which the caller has access to that hash.

    Args:
        reference_type (ReferenceType):
        reference_name (str):
        expected_hash (str):
        json_body (Union['Branch', 'DetachedCommitHash', 'Tag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        reference_type=reference_type,
        reference_name=reference_name,
        json_body=json_body,
        expected_hash=expected_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    reference_type: ReferenceType,
    reference_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    expected_hash: str,
) -> Response[Any]:
    """Set a named reference to a specific hash via a named-reference.

     This operation takes the name of the named reference to reassign and the hash and the name of a
    named-reference via which the caller has access to that hash.

    Args:
        reference_type (ReferenceType):
        reference_name (str):
        expected_hash (str):
        json_body (Union['Branch', 'DetachedCommitHash', 'Tag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        reference_type=reference_type,
        reference_name=reference_name,
        json_body=json_body,
        expected_hash=expected_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)