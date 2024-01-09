from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_key import ContentKey
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: Any,
    *,
    content: Union[Unset, None, bool] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, List["ContentKey"]] = UNSET,
    max_key: Union[Unset, None, "ContentKey"] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    min_key: Union[Unset, None, "ContentKey"] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    prefix_key: Union[Unset, None, "ContentKey"] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["content"] = content

    params["filter"] = filter_

    json_key: Union[Unset, None, List[Dict[str, Any]]] = UNSET
    if not isinstance(key, Unset):
        if key is None:
            json_key = None
        else:
            json_key = []
            for key_item_data in key:
                key_item = key_item_data.to_dict()

                json_key.append(key_item)

    params["key"] = json_key

    json_max_key: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(max_key, Unset):
        json_max_key = max_key.to_dict() if max_key else None

    if not isinstance(json_max_key, Unset) and json_max_key is not None:
        params.update(json_max_key)

    params["max-records"] = max_records

    json_min_key: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(min_key, Unset):
        json_min_key = min_key.to_dict() if min_key else None

    if not isinstance(json_min_key, Unset) and json_min_key is not None:
        params.update(json_min_key)

    params["page-token"] = page_token

    json_prefix_key: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(prefix_key, Unset):
        json_prefix_key = prefix_key.to_dict() if prefix_key else None

    if not isinstance(json_prefix_key, Unset) and json_prefix_key is not None:
        params.update(json_prefix_key)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v2/trees/{ref}/entries".format(
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
    content: Union[Unset, None, bool] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, List["ContentKey"]] = UNSET,
    max_key: Union[Unset, None, "ContentKey"] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    min_key: Union[Unset, None, "ContentKey"] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    prefix_key: Union[Unset, None, "ContentKey"] = UNSET,
) -> Response[Any]:
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
    available data in one page.

    Different pages may have different numbers of log records in them even if they come from another
    call to this method with the same parameters. Also, pages are not guaranteed to be filled to contain
    exactly 'maxRecords' even if the total amount of available data allows that. Pages may contain more
    of less entries at server's discretion.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    Args:
        ref (Any):
        content (Union[Unset, None, bool]):
        filter_ (Union[Unset, None, str]):
        key (Union[Unset, None, List['ContentKey']]):
        max_key (Union[Unset, None, ContentKey]):
        max_records (Union[Unset, None, int]):
        min_key (Union[Unset, None, ContentKey]):
        page_token (Union[Unset, None, str]):
        prefix_key (Union[Unset, None, ContentKey]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        content=content,
        filter_=filter_,
        key=key,
        max_key=max_key,
        max_records=max_records,
        min_key=min_key,
        page_token=page_token,
        prefix_key=prefix_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ref: Any,
    *,
    client: Union[AuthenticatedClient, Client],
    content: Union[Unset, None, bool] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    key: Union[Unset, None, List["ContentKey"]] = UNSET,
    max_key: Union[Unset, None, "ContentKey"] = UNSET,
    max_records: Union[Unset, None, int] = UNSET,
    min_key: Union[Unset, None, "ContentKey"] = UNSET,
    page_token: Union[Unset, None, str] = UNSET,
    prefix_key: Union[Unset, None, "ContentKey"] = UNSET,
) -> Response[Any]:
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
    available data in one page.

    Different pages may have different numbers of log records in them even if they come from another
    call to this method with the same parameters. Also, pages are not guaranteed to be filled to contain
    exactly 'maxRecords' even if the total amount of available data allows that. Pages may contain more
    of less entries at server's discretion.

    The 'filter' parameter allows for advanced filtering capabilities using the Common Expression
    Language (CEL).
    An intro to CEL can be found at https://github.com/google/cel-spec/blob/master/doc/intro.md.

    Args:
        ref (Any):
        content (Union[Unset, None, bool]):
        filter_ (Union[Unset, None, str]):
        key (Union[Unset, None, List['ContentKey']]):
        max_key (Union[Unset, None, ContentKey]):
        max_records (Union[Unset, None, int]):
        min_key (Union[Unset, None, ContentKey]):
        page_token (Union[Unset, None, str]):
        prefix_key (Union[Unset, None, ContentKey]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        content=content,
        filter_=filter_,
        key=key,
        max_key=max_key,
        max_records=max_records,
        min_key=min_key,
        page_token=page_token,
        prefix_key=prefix_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
