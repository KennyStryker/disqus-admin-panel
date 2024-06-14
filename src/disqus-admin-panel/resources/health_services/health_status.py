# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

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

__all__ = ["HealthStatusResource", "AsyncHealthStatusResource"]


class HealthStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthStatusResourceWithRawResponse:
        return HealthStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthStatusResourceWithStreamingResponse:
        return HealthStatusResourceWithStreamingResponse(self)

    def retrieve(
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
            "/health_status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncHealthStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthStatusResourceWithRawResponse:
        return AsyncHealthStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthStatusResourceWithStreamingResponse:
        return AsyncHealthStatusResourceWithStreamingResponse(self)

    async def retrieve(
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
            "/health_status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class HealthStatusResourceWithRawResponse:
    def __init__(self, health_status: HealthStatusResource) -> None:
        self._health_status = health_status

        self.retrieve = to_raw_response_wrapper(
            health_status.retrieve,
        )


class AsyncHealthStatusResourceWithRawResponse:
    def __init__(self, health_status: AsyncHealthStatusResource) -> None:
        self._health_status = health_status

        self.retrieve = async_to_raw_response_wrapper(
            health_status.retrieve,
        )


class HealthStatusResourceWithStreamingResponse:
    def __init__(self, health_status: HealthStatusResource) -> None:
        self._health_status = health_status

        self.retrieve = to_streamed_response_wrapper(
            health_status.retrieve,
        )


class AsyncHealthStatusResourceWithStreamingResponse:
    def __init__(self, health_status: AsyncHealthStatusResource) -> None:
        self._health_status = health_status

        self.retrieve = async_to_streamed_response_wrapper(
            health_status.retrieve,
        )
