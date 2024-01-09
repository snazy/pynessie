from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    from_ref_with_hash: str,
    to_ref_with_hash: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v1/diffs/{fromRefWithHash}...{toRefWithHash}".format(
            fromRefWithHash=from_ref_with_hash,
            toRefWithHash=to_ref_with_hash,
        ),
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
    from_ref_with_hash: str,
    to_ref_with_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    r"""Get a diff for two given references

     The URL pattern is basically 'from' and 'to' separated by '...' (three dots). 'from' and 'to' must
    start with a reference name, optionally followed by hash on that reference, the hash prefixed with
    the'*' character.

    Examples:
      diffs/main...myBranch
      diffs/main...myBranch\*1234567890123456
      diffs/main\*1234567890123456...myBranch
      diffs/main\*1234567890123456...myBranch\*1234567890123456

    Args:
        from_ref_with_hash (str):
        to_ref_with_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        from_ref_with_hash=from_ref_with_hash,
        to_ref_with_hash=to_ref_with_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    from_ref_with_hash: str,
    to_ref_with_hash: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    r"""Get a diff for two given references

     The URL pattern is basically 'from' and 'to' separated by '...' (three dots). 'from' and 'to' must
    start with a reference name, optionally followed by hash on that reference, the hash prefixed with
    the'*' character.

    Examples:
      diffs/main...myBranch
      diffs/main...myBranch\*1234567890123456
      diffs/main\*1234567890123456...myBranch
      diffs/main\*1234567890123456...myBranch\*1234567890123456

    Args:
        from_ref_with_hash (str):
        to_ref_with_hash (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        from_ref_with_hash=from_ref_with_hash,
        to_ref_with_hash=to_ref_with_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
