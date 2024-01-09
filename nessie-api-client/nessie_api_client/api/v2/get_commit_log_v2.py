from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_option import FetchOption
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: Any,
    *,
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    limit_hash: Union[Unset, None, str] = UNSET,
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

    params["limit-hash"] = limit_hash

    params["max-records"] = max_records

    params["page-token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v2/trees/{ref}/history".format(
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
    ref: Any,
    *,
    client: Union[AuthenticatedClient, Client],
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    limit_hash: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    r"""Get commit log for a particular reference

     Retrieve the commit log for a reference, potentially truncated by the backend.

    The backend may respect the given 'max-entries' records hint, or may return more or less entries.
    Backends may also cap the returned entries at a hard-coded limit

    To implement paging, check 'hasMore' in the response and, if 'true', pass the value returned as
    'token' in the next invocation as the 'pageToken' parameter.

    The content and meaning of the returned 'token' is \"private\" to the implementation,treat is as an
    opaque value.

    It is wrong to assume that invoking this method with a very high 'maxRecords' value will return all
    available data in one page.

    Different pages may have different numbers of log records in them even if they come from another
    call to this method with the same parameters. Also, pages are not guaranteed to be filled to contain
    exactly 'maxRecords' even if the total amount of available data allows that. Pages may contain more
    of less entries at server's discretion.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    The fetching of the log starts from the HEAD of the given ref (or a more specific commit, if
    provided as part of the 'ref' path element) and proceeds until the 'root' commit or the 'limit-hash'
    commit are encountered.

    Args:
        ref (Any):
        fetch (Union[Unset, None, FetchOption]):
        filter_ (Union[Unset, None, str]):
        limit_hash (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        fetch=fetch,
        filter_=filter_,
        limit_hash=limit_hash,
        max_records=max_records,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ref: Any,
    *,
    client: Union[AuthenticatedClient, Client],
    fetch: Union[Unset, None, FetchOption] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    limit_hash: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    r"""Get commit log for a particular reference

     Retrieve the commit log for a reference, potentially truncated by the backend.

    The backend may respect the given 'max-entries' records hint, or may return more or less entries.
    Backends may also cap the returned entries at a hard-coded limit

    To implement paging, check 'hasMore' in the response and, if 'true', pass the value returned as
    'token' in the next invocation as the 'pageToken' parameter.

    The content and meaning of the returned 'token' is \"private\" to the implementation,treat is as an
    opaque value.

    It is wrong to assume that invoking this method with a very high 'maxRecords' value will return all
    available data in one page.

    Different pages may have different numbers of log records in them even if they come from another
    call to this method with the same parameters. Also, pages are not guaranteed to be filled to contain
    exactly 'maxRecords' even if the total amount of available data allows that. Pages may contain more
    of less entries at server's discretion.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    The fetching of the log starts from the HEAD of the given ref (or a more specific commit, if
    provided as part of the 'ref' path element) and proceeds until the 'root' commit or the 'limit-hash'
    commit are encountered.

    Args:
        ref (Any):
        fetch (Union[Unset, None, FetchOption]):
        filter_ (Union[Unset, None, str]):
        limit_hash (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        fetch=fetch,
        filter_=filter_,
        limit_hash=limit_hash,
        max_records=max_records,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
