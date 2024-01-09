from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: Any,
    *,
    key: Union[Unset, None, List[str]] = UNSET,
    with_doc: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_key: Union[Unset, None, List[str]] = UNSET
    if not isinstance(key, Unset):
        if key is None:
            json_key = None
        else:
            json_key = key

    params["key"] = json_key

    params["with-doc"] = with_doc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v2/trees/{ref}/contents".format(
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
    key: Union[Unset, None, List[str]] = UNSET,
    with_doc: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """Get multiple content objects.

     Similar to 'GET /trees/{ref}/content/{key}', but takes multiple 'key' query parameters and returns
    zero or more content values in the same JSON structure as the 'POST /trees/{ref}/content' endpoint.

    This is a convenience method for fetching a small number of content objects. It is mostly intended
    for human use. For automated use cases or when the number of keys is large the 'POST
    /trees/{ref}/content' method is preferred.

    Args:
        ref (Any):
        key (Union[Unset, None, List[str]]):
        with_doc (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        key=key,
        with_doc=with_doc,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    ref: Any,
    *,
    client: Union[AuthenticatedClient, Client],
    key: Union[Unset, None, List[str]] = UNSET,
    with_doc: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """Get multiple content objects.

     Similar to 'GET /trees/{ref}/content/{key}', but takes multiple 'key' query parameters and returns
    zero or more content values in the same JSON structure as the 'POST /trees/{ref}/content' endpoint.

    This is a convenience method for fetching a small number of content objects. It is mostly intended
    for human use. For automated use cases or when the number of keys is large the 'POST
    /trees/{ref}/content' method is preferred.

    Args:
        ref (Any):
        key (Union[Unset, None, List[str]]):
        with_doc (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ref=ref,
        key=key,
        with_doc=with_doc,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
