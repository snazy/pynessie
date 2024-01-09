from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operations import Operations
from ...types import Response


def _get_kwargs(
    branch: Any,
    *,
    json_body: Operations,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v2/trees/{branch}/history/commit".format(
            branch=branch,
        ),
        "json": json_json_body,
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
    branch: Any,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Operations,
) -> Response[Any]:
    """Commit one or more operations against the given 'branch'.

     The state of contents specified by the 'branch' reference will be used for detecting conflicts with
    the operation being committed.

    The hash in the successful response will be the hash of the commit that contains the requested
    operations, whose immediate parent commit will be the current HEAD of the specified branch.

    Args:
        branch (Any):
        json_body (Operations):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        branch=branch,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    branch: Any,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Operations,
) -> Response[Any]:
    """Commit one or more operations against the given 'branch'.

     The state of contents specified by the 'branch' reference will be used for detecting conflicts with
    the operation being committed.

    The hash in the successful response will be the hash of the commit that contains the requested
    operations, whose immediate parent commit will be the current HEAD of the specified branch.

    Args:
        branch (Any):
        json_body (Operations):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        branch=branch,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
