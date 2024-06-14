# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .action_counts import ActionCountsResource, AsyncActionCountsResource

from ...._compat import cached_property

from .action_history import ActionHistoryResource, AsyncActionHistoryResource

from ...._utils import maybe_transform, async_maybe_transform

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.user_services import user_list_params
from .action_counts import (
    ActionCountsResource,
    AsyncActionCountsResource,
    ActionCountsResourceWithRawResponse,
    AsyncActionCountsResourceWithRawResponse,
    ActionCountsResourceWithStreamingResponse,
    AsyncActionCountsResourceWithStreamingResponse,
)
from .action_history import (
    ActionHistoryResource,
    AsyncActionHistoryResource,
    ActionHistoryResourceWithRawResponse,
    AsyncActionHistoryResourceWithRawResponse,
    ActionHistoryResourceWithStreamingResponse,
    AsyncActionHistoryResourceWithStreamingResponse,
)

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def action_counts(self) -> ActionCountsResource:
        return ActionCountsResource(self._client)

    @cached_property
    def action_history(self) -> ActionHistoryResource:
        return ActionHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        username: str,
        page_size: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
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
        return self._get(
            "/user/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "username": username,
                        "page_size": page_size,
                        "skip": skip,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=object,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def action_counts(self) -> AsyncActionCountsResource:
        return AsyncActionCountsResource(self._client)

    @cached_property
    def action_history(self) -> AsyncActionHistoryResource:
        return AsyncActionHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        username: str,
        page_size: int | NotGiven = NOT_GIVEN,
        skip: int | NotGiven = NOT_GIVEN,
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
        return await self._get(
            "/user/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "username": username,
                        "page_size": page_size,
                        "skip": skip,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=object,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.list = to_raw_response_wrapper(
            user.list,
        )

    @cached_property
    def action_counts(self) -> ActionCountsResourceWithRawResponse:
        return ActionCountsResourceWithRawResponse(self._user.action_counts)

    @cached_property
    def action_history(self) -> ActionHistoryResourceWithRawResponse:
        return ActionHistoryResourceWithRawResponse(self._user.action_history)


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.list = async_to_raw_response_wrapper(
            user.list,
        )

    @cached_property
    def action_counts(self) -> AsyncActionCountsResourceWithRawResponse:
        return AsyncActionCountsResourceWithRawResponse(self._user.action_counts)

    @cached_property
    def action_history(self) -> AsyncActionHistoryResourceWithRawResponse:
        return AsyncActionHistoryResourceWithRawResponse(self._user.action_history)


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.list = to_streamed_response_wrapper(
            user.list,
        )

    @cached_property
    def action_counts(self) -> ActionCountsResourceWithStreamingResponse:
        return ActionCountsResourceWithStreamingResponse(self._user.action_counts)

    @cached_property
    def action_history(self) -> ActionHistoryResourceWithStreamingResponse:
        return ActionHistoryResourceWithStreamingResponse(self._user.action_history)


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.list = async_to_streamed_response_wrapper(
            user.list,
        )

    @cached_property
    def action_counts(self) -> AsyncActionCountsResourceWithStreamingResponse:
        return AsyncActionCountsResourceWithStreamingResponse(self._user.action_counts)

    @cached_property
    def action_history(self) -> AsyncActionHistoryResourceWithStreamingResponse:
        return AsyncActionHistoryResourceWithStreamingResponse(self._user.action_history)
