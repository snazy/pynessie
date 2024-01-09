from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entries_response_v1 import EntriesResponseV1
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: str,
    *,
    filter_: Union[Unset, None, str] = UNSET,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    namespace_depth: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["filter"] = filter_

    params["hashOnRef"] = hash_on_ref

    params["maxRecords"] = max_records

    params["namespaceDepth"] = namespace_depth

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v1/trees/tree/{ref}/entries".format(
            ref=ref,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EntriesResponseV1]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EntriesResponseV1.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, EntriesResponseV1]]:
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
    filter_: Union[Unset, None, str] = UNSET,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    namespace_depth: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, EntriesResponseV1]]:
    r"""Fetch all entries for a given reference

     Retrieves objects for a ref, potentially truncated by the backend.

    Retrieves up to 'maxRecords' entries for the given named reference (tag or branch) or the given
    hash. The backend may respect the given 'max' records hint, but return less or more entries.
    Backends may also cap the returned entries at a hard-coded limit, the default REST server
    implementation has such a hard-coded limit.

    To implement paging, check 'hasMore' in the response and, if 'true', pass the value returned as
    'token' in the next invocation as the 'pageToken' parameter.

    The content and meaning of the returned 'token' is \"private\" to the implementation,treat is as an
    opaque value.

    It is wrong to assume that invoking this method with a very high 'maxRecords' value will return all
    commit log entries.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    The 'namespaceDepth' parameter returns only the ContentKey components up to the depth of
    'namespaceDepth'.
    For example they key 'a.b.c.d' with a depth of 3 will return 'a.b.c'. The operation is guaranteed to
    not return
    duplicates and therefore will never page.

    Args:
        ref (str):
        filter_ (Union[Unset, None, str]):
        hash_on_ref (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        namespace_depth (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EntriesResponseV1]]
    """

    kwargs = _get_kwargs(
        ref=ref,
        filter_=filter_,
        hash_on_ref=hash_on_ref,
        max_records=max_records,
        namespace_depth=namespace_depth,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, None, str] = UNSET,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    namespace_depth: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, EntriesResponseV1]]:
    r"""Fetch all entries for a given reference

     Retrieves objects for a ref, potentially truncated by the backend.

    Retrieves up to 'maxRecords' entries for the given named reference (tag or branch) or the given
    hash. The backend may respect the given 'max' records hint, but return less or more entries.
    Backends may also cap the returned entries at a hard-coded limit, the default REST server
    implementation has such a hard-coded limit.

    To implement paging, check 'hasMore' in the response and, if 'true', pass the value returned as
    'token' in the next invocation as the 'pageToken' parameter.

    The content and meaning of the returned 'token' is \"private\" to the implementation,treat is as an
    opaque value.

    It is wrong to assume that invoking this method with a very high 'maxRecords' value will return all
    commit log entries.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    The 'namespaceDepth' parameter returns only the ContentKey components up to the depth of
    'namespaceDepth'.
    For example they key 'a.b.c.d' with a depth of 3 will return 'a.b.c'. The operation is guaranteed to
    not return
    duplicates and therefore will never page.

    Args:
        ref (str):
        filter_ (Union[Unset, None, str]):
        hash_on_ref (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        namespace_depth (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EntriesResponseV1]
    """

    return sync_detailed(
        ref=ref,
        client=client,
        filter_=filter_,
        hash_on_ref=hash_on_ref,
        max_records=max_records,
        namespace_depth=namespace_depth,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, None, str] = UNSET,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    namespace_depth: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, EntriesResponseV1]]:
    r"""Fetch all entries for a given reference

     Retrieves objects for a ref, potentially truncated by the backend.

    Retrieves up to 'maxRecords' entries for the given named reference (tag or branch) or the given
    hash. The backend may respect the given 'max' records hint, but return less or more entries.
    Backends may also cap the returned entries at a hard-coded limit, the default REST server
    implementation has such a hard-coded limit.

    To implement paging, check 'hasMore' in the response and, if 'true', pass the value returned as
    'token' in the next invocation as the 'pageToken' parameter.

    The content and meaning of the returned 'token' is \"private\" to the implementation,treat is as an
    opaque value.

    It is wrong to assume that invoking this method with a very high 'maxRecords' value will return all
    commit log entries.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    The 'namespaceDepth' parameter returns only the ContentKey components up to the depth of
    'namespaceDepth'.
    For example they key 'a.b.c.d' with a depth of 3 will return 'a.b.c'. The operation is guaranteed to
    not return
    duplicates and therefore will never page.

    Args:
        ref (str):
        filter_ (Union[Unset, None, str]):
        hash_on_ref (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        namespace_depth (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EntriesResponseV1]]
    """

    kwargs = _get_kwargs(
        ref=ref,
        filter_=filter_,
        hash_on_ref=hash_on_ref,
        max_records=max_records,
        namespace_depth=namespace_depth,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ref: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_: Union[Unset, None, str] = UNSET,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    namespace_depth: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, EntriesResponseV1]]:
    r"""Fetch all entries for a given reference

     Retrieves objects for a ref, potentially truncated by the backend.

    Retrieves up to 'maxRecords' entries for the given named reference (tag or branch) or the given
    hash. The backend may respect the given 'max' records hint, but return less or more entries.
    Backends may also cap the returned entries at a hard-coded limit, the default REST server
    implementation has such a hard-coded limit.

    To implement paging, check 'hasMore' in the response and, if 'true', pass the value returned as
    'token' in the next invocation as the 'pageToken' parameter.

    The content and meaning of the returned 'token' is \"private\" to the implementation,treat is as an
    opaque value.

    It is wrong to assume that invoking this method with a very high 'maxRecords' value will return all
    commit log entries.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    The 'namespaceDepth' parameter returns only the ContentKey components up to the depth of
    'namespaceDepth'.
    For example they key 'a.b.c.d' with a depth of 3 will return 'a.b.c'. The operation is guaranteed to
    not return
    duplicates and therefore will never page.

    Args:
        ref (str):
        filter_ (Union[Unset, None, str]):
        hash_on_ref (Union[Unset, None, str]):
        max_records (Union[Unset, None, int]):
        namespace_depth (Union[Unset, None, int]):
        page_token (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EntriesResponseV1]
    """

    return (
        await asyncio_detailed(
            ref=ref,
            client=client,
            filter_=filter_,
            hash_on_ref=hash_on_ref,
            max_records=max_records,
            namespace_depth=namespace_depth,
            page_token=page_token,
        )
    ).parsed
