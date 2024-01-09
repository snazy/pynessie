from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_option import FetchOption
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: str,
    *,
    end_hash: Union[Unset, None, str] = UNSET,
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    start_hash: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["endHash"] = end_hash

    json_fetch: Union[Unset, None, str] = UNSET
    if not isinstance(fetch, Unset):
        json_fetch = fetch.value if fetch else None

    params["fetch"] = json_fetch

    params["filter"] = filter_

    params["maxRecords"] = max_records

    params["pageToken"] = page_token

    params["startHash"] = start_hash

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/trees/tree/{ref}/log".format(
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
    end_hash: Union[Unset, None, str] = UNSET,
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    start_hash: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    r"""Get commit log for a reference

     Retrieve the commit log for a ref, potentially truncated by the backend.

    Retrieves up to 'maxRecords' commit-log-entries starting at the HEAD of the given named reference
    (tag or branch) or the given hash. The backend may respect the given 'max' records hint, but return
    less or more entries. Backends may also cap the returned entries at a hard-coded limit, the default
    REST server implementation has such a hard-coded limit.

    To implement paging, check 'hasMore' in the response and, if 'true', pass the value returned as
    'token' in the next invocation as the 'pageToken' parameter.

    The content and meaning of the returned 'token' is \"private\" to the implementation,treat is as an
    opaque value.

    It is wrong to assume that invoking this method with a very high 'maxRecords' value will return all
    commit log entries.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    Args:
        ref (str):
        end_hash (Union[Unset, None, str]):
        fetch (Union[Unset, None, FetchOption]):
        filter_ (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        start_hash (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        end_hash=end_hash,
        fetch=fetch,
        filter_=filter_,
        max_records=max_records,
        page_token=page_token,
        start_hash=start_hash,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    end_hash: Union[Unset, None, str] = UNSET,
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    start_hash: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    r"""Get commit log for a reference

     Retrieve the commit log for a ref, potentially truncated by the backend.

    Retrieves up to 'maxRecords' commit-log-entries starting at the HEAD of the given named reference
    (tag or branch) or the given hash. The backend may respect the given 'max' records hint, but return
    less or more entries. Backends may also cap the returned entries at a hard-coded limit, the default
    REST server implementation has such a hard-coded limit.

    To implement paging, check 'hasMore' in the response and, if 'true', pass the value returned as
    'token' in the next invocation as the 'pageToken' parameter.

    The content and meaning of the returned 'token' is \"private\" to the implementation,treat is as an
    opaque value.

    It is wrong to assume that invoking this method with a very high 'maxRecords' value will return all
    commit log entries.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    Args:
        ref (str):
        end_hash (Union[Unset, None, str]):
        fetch (Union[Unset, None, FetchOption]):
        filter_ (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):
        start_hash (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        end_hash=end_hash,
        fetch=fetch,
        filter_=filter_,
        max_records=max_records,
        page_token=page_token,
        start_hash=start_hash,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
