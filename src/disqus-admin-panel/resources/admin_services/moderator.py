# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ..._utils import maybe_transform, async_maybe_transform

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
from ...types.admin_services import moderator_update_params
from ...types.admin_services import moderator_add_params

__all__ = ["ModeratorResource", "AsyncModeratorResource"]


class ModeratorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModeratorResourceWithRawResponse:
        return ModeratorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModeratorResourceWithStreamingResponse:
        return ModeratorResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        is_active: bool,
        is_admin: bool,
        username: str,
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
        return self._put(
            "/moderator/update",
            body=maybe_transform(
                {
                    "is_active": is_active,
                    "is_admin": is_admin,
                    "username": username,
                },
                moderator_update_params.ModeratorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
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
        """
        return self._get(
            "/moderator/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def add(
        self,
        *,
        password: str,
        username: str,
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
            "/moderator/add",
            body=maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                moderator_add_params.ModeratorAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncModeratorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModeratorResourceWithRawResponse:
        return AsyncModeratorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModeratorResourceWithStreamingResponse:
        return AsyncModeratorResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        is_active: bool,
        is_admin: bool,
        username: str,
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
        return await self._put(
            "/moderator/update",
            body=await async_maybe_transform(
                {
                    "is_active": is_active,
                    "is_admin": is_admin,
                    "username": username,
                },
                moderator_update_params.ModeratorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
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
        """
        return await self._get(
            "/moderator/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def add(
        self,
        *,
        password: str,
        username: str,
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
            "/moderator/add",
            body=await async_maybe_transform(
                {
                    "password": password,
                    "username": username,
                },
                moderator_add_params.ModeratorAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ModeratorResourceWithRawResponse:
    def __init__(self, moderator: ModeratorResource) -> None:
        self._moderator = moderator

        self.update = to_raw_response_wrapper(
            moderator.update,
        )
        self.list = to_raw_response_wrapper(
            moderator.list,
        )
        self.add = to_raw_response_wrapper(
            moderator.add,
        )


class AsyncModeratorResourceWithRawResponse:
    def __init__(self, moderator: AsyncModeratorResource) -> None:
        self._moderator = moderator

        self.update = async_to_raw_response_wrapper(
            moderator.update,
        )
        self.list = async_to_raw_response_wrapper(
            moderator.list,
        )
        self.add = async_to_raw_response_wrapper(
            moderator.add,
        )


class ModeratorResourceWithStreamingResponse:
    def __init__(self, moderator: ModeratorResource) -> None:
        self._moderator = moderator

        self.update = to_streamed_response_wrapper(
            moderator.update,
        )
        self.list = to_streamed_response_wrapper(
            moderator.list,
        )
        self.add = to_streamed_response_wrapper(
            moderator.add,
        )


class AsyncModeratorResourceWithStreamingResponse:
    def __init__(self, moderator: AsyncModeratorResource) -> None:
        self._moderator = moderator

        self.update = async_to_streamed_response_wrapper(
            moderator.update,
        )
        self.list = async_to_streamed_response_wrapper(
            moderator.list,
        )
        self.add = async_to_streamed_response_wrapper(
            moderator.add,
        )
