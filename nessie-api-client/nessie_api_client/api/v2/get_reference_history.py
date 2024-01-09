from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: str,
    *,
    scan_commits: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["scan-commits"] = scan_commits

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v2/trees/{ref}/recent-changes".format(
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
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scan_commits: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    r"""Fetch recent pointer changes of a reference

     Retrieve the recorded recent history of a reference.

    A reference's history is a size and time limited record of changes of the reference's current
    pointer, aka HEAD. The size and time limits are configured in the Nessie server configuration.

    This function is only useful for deployments using replicating multi-zone/region database setups. If
    the \"primary write target\" fails and cannot be recovered, replicas might not have all written
    records (data loss scenario). This function helps identifying whether the commits of a reference
    that were written within the configured \"replication lag\" are present and consistent. A reference
    might then be deleted or re-assigned to a consistent commit.

    Args:
        ref (str):
        scan_commits (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        scan_commits=scan_commits,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    scan_commits: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    r"""Fetch recent pointer changes of a reference

     Retrieve the recorded recent history of a reference.

    A reference's history is a size and time limited record of changes of the reference's current
    pointer, aka HEAD. The size and time limits are configured in the Nessie server configuration.

    This function is only useful for deployments using replicating multi-zone/region database setups. If
    the \"primary write target\" fails and cannot be recovered, replicas might not have all written
    records (data loss scenario). This function helps identifying whether the commits of a reference
    that were written within the configured \"replication lag\" are present and consistent. A reference
    might then be deleted or re-assigned to a consistent commit.

    Args:
        ref (str):
        scan_commits (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        scan_commits=scan_commits,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
