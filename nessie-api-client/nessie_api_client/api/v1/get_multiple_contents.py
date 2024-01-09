from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_multiple_contents_request import GetMultipleContentsRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: GetMultipleContentsRequest,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    ref: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["hashOnRef"] = hash_on_ref

    params["ref"] = ref

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/v1/contents",
        "json": json_json_body,
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
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: GetMultipleContentsRequest,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    ref: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get multiple objects' content.

     Similar to 'getContent', but takes multiple 'ContentKey's and returns the content-values for the one
    or more content-keys in a named-reference (a branch or tag).

    If the table-metadata is tracked globally (Iceberg), Nessie returns a 'Content' object, that
    contains the most up-to-date part for the globally tracked part (Iceberg: table-metadata) plus the
    per-Nessie-reference/hash specific part (Iceberg: snapshot-ID,schema-ID, partition-spec-ID, default-
    sort-order-ID).

    Args:
        hash_on_ref (Union[Unset, None, str]):
        ref (Union[Unset, None, str]):
        json_body (GetMultipleContentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        hash_on_ref=hash_on_ref,
        ref=ref,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: GetMultipleContentsRequest,
    hash_on_ref: Union[Unset, None, str] = UNSET,
    ref: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get multiple objects' content.

     Similar to 'getContent', but takes multiple 'ContentKey's and returns the content-values for the one
    or more content-keys in a named-reference (a branch or tag).

    If the table-metadata is tracked globally (Iceberg), Nessie returns a 'Content' object, that
    contains the most up-to-date part for the globally tracked part (Iceberg: table-metadata) plus the
    per-Nessie-reference/hash specific part (Iceberg: snapshot-ID,schema-ID, partition-spec-ID, default-
    sort-order-ID).

    Args:
        hash_on_ref (Union[Unset, None, str]):
        ref (Union[Unset, None, str]):
        json_body (GetMultipleContentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        hash_on_ref=hash_on_ref,
        ref=ref,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
