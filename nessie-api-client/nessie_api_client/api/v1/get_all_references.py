from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_option import FetchOption
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_fetch: Union[Unset, None, str] = UNSET
    if not isinstance(fetch, Unset):
        json_fetch = fetch.value if fetch else None

    params["fetch"] = json_fetch

    params["filter"] = filter_

    params["maxRecords"] = max_records

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/trees",
        "params": params,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.UNAUTHORIZED:
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
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get all references

    Args:
        fetch (Union[Unset, None, FetchOption]):
        filter_ (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fetch=fetch,
        filter_=filter_,
        max_records=max_records,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get all references

    Args:
        fetch (Union[Unset, None, FetchOption]):
        filter_ (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        fetch=fetch,
        filter_=filter_,
        max_records=max_records,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
