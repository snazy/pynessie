from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.merge_operation import MergeOperation
from ...types import UNSET, Response


def _get_kwargs(
    branch_name: str,
    *,
    json_body: MergeOperation,
    expected_hash: str,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["expectedHash"] = expected_hash

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v1/trees/branch/{branchName}/merge".format(
            branchName=branch_name,
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
    branch_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: MergeOperation,
    expected_hash: str,
) -> Response[Any]:
    """Merge commits from 'mergeRef' onto 'branchName'.

     Merge items from an existing hash in 'mergeRef' into the requested branch. The merge is always a
    rebase + fast-forward merge and is only completed if the rebase is conflict free. The set of commits
    added to the branch will be all of those until we arrive at a common ancestor. Depending on the
    underlying implementation, the number of commits allowed as part of this operation may be limited.

    Args:
        branch_name (str):
        expected_hash (str):
        json_body (MergeOperation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        branch_name=branch_name,
        json_body=json_body,
        expected_hash=expected_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    branch_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: MergeOperation,
    expected_hash: str,
) -> Response[Any]:
    """Merge commits from 'mergeRef' onto 'branchName'.

     Merge items from an existing hash in 'mergeRef' into the requested branch. The merge is always a
    rebase + fast-forward merge and is only completed if the rebase is conflict free. The set of commits
    added to the branch will be all of those until we arrive at a common ancestor. Depending on the
    underlying implementation, the number of commits allowed as part of this operation may be limited.

    Args:
        branch_name (str):
        expected_hash (str):
        json_body (MergeOperation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        branch_name=branch_name,
        json_body=json_body,
        expected_hash=expected_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
