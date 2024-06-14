# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.auth_services import access_token_create_params

__all__ = ["AccessTokenResource", "AsyncAccessTokenResource"]


class AccessTokenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessTokenResourceWithRawResponse:
        return AccessTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessTokenResourceWithStreamingResponse:
        return AccessTokenResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        password: str,
        username: str,
        client_id: Optional[str] | NotGiven = NOT_GIVEN,
        client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        grant_type: Optional[str] | NotGiven = NOT_GIVEN,
        scope: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Endpoint to check the health status of the server.

        Raises: JSON Response: Error 503 if server is not alive.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/login/access-token",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "scope": scope,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAccessTokenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessTokenResourceWithRawResponse:
        return AsyncAccessTokenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessTokenResourceWithStreamingResponse:
        return AsyncAccessTokenResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        password: str,
        username: str,
        client_id: Optional[str] | NotGiven = NOT_GIVEN,
        client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        grant_type: Optional[str] | NotGiven = NOT_GIVEN,
        scope: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Endpoint to check the health status of the server.

        Raises: JSON Response: Error 503 if server is not alive.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/login/access-token",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "username": username,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "scope": scope,
                },
                access_token_create_params.AccessTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AccessTokenResourceWithRawResponse:
    def __init__(self, access_token: AccessTokenResource) -> None:
        self._access_token = access_token

        self.create = to_raw_response_wrapper(
            access_token.create,
        )


class AsyncAccessTokenResourceWithRawResponse:
    def __init__(self, access_token: AsyncAccessTokenResource) -> None:
        self._access_token = access_token

        self.create = async_to_raw_response_wrapper(
            access_token.create,
        )


class AccessTokenResourceWithStreamingResponse:
    def __init__(self, access_token: AccessTokenResource) -> None:
        self._access_token = access_token

        self.create = to_streamed_response_wrapper(
            access_token.create,
        )


class AsyncAccessTokenResourceWithStreamingResponse:
    def __init__(self, access_token: AsyncAccessTokenResource) -> None:
        self._access_token = access_token

        self.create = async_to_streamed_response_wrapper(
            access_token.create,
        )
