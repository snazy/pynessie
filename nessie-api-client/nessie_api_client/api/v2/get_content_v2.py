from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_key import ContentKey
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ref: Any,
    key: "ContentKey",
    *,
    with_doc: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["with-doc"] = with_doc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/v2/trees/{ref}/contents/{key}".format(
            ref=ref,
            key=key,
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
    key: "ContentKey",
    *,
    client: Union[AuthenticatedClient, Client],
    with_doc: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """Get the content object associated with a key.

     This operation returns the content value for a content key at a particular point in history as
    defined by the 'ref' parameter.

    Args:
        ref (Any):
        key (ContentKey):
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
    key: "ContentKey",
    *,
    client: Union[AuthenticatedClient, Client],
    with_doc: Union[Unset, None, bool] = UNSET,
) -> Response[Any]:
    """Get the content object associated with a key.

     This operation returns the content value for a content key at a particular point in history as
    defined by the 'ref' parameter.

    Args:
        ref (Any):
        key (ContentKey):
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
