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
    *,
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    source_ref_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["sourceRefName"] = source_ref_name

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
        "url": "/v1/trees/tree",
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
    source_ref_name: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    r"""Create a new reference

     The type of 'refObj', which can be either a 'Branch' or 'Tag', determines the type of the reference
    to be created.

    'Reference.name' defines the the name of the reference to be created,'Reference.hash' is the hash of
    the created reference, the HEAD of the created reference. 'sourceRefName' is the name of the
    reference which contains 'Reference.hash', and must be present if 'Reference.hash' is present.

    Specifying no 'Reference.hash' means that the new reference will be created \"at the beginning of
    time\".

    Args:
        source_ref_name (Union[Unset, None, str]):
        json_body (Union['Branch', 'DetachedCommitHash', 'Tag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        source_ref_name=source_ref_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Union["Branch", "DetachedCommitHash", "Tag"],
    source_ref_name: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    r"""Create a new reference

     The type of 'refObj', which can be either a 'Branch' or 'Tag', determines the type of the reference
    to be created.

    'Reference.name' defines the the name of the reference to be created,'Reference.hash' is the hash of
    the created reference, the HEAD of the created reference. 'sourceRefName' is the name of the
    reference which contains 'Reference.hash', and must be present if 'Reference.hash' is present.

    Specifying no 'Reference.hash' means that the new reference will be created \"at the beginning of
    time\".

    Args:
        source_ref_name (Union[Unset, None, str]):
        json_body (Union['Branch', 'DetachedCommitHash', 'Tag']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        source_ref_name=source_ref_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
