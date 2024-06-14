# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .health_status import HealthStatusResource, AsyncHealthStatusResource

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
from .health_status import (
    HealthStatusResource,
    AsyncHealthStatusResource,
    HealthStatusResourceWithRawResponse,
    AsyncHealthStatusResourceWithRawResponse,
    HealthStatusResourceWithStreamingResponse,
    AsyncHealthStatusResourceWithStreamingResponse,
)

__all__ = ["HealthServicesResource", "AsyncHealthServicesResource"]


class HealthServicesResource(SyncAPIResource):
    @cached_property
    def health_status(self) -> HealthStatusResource:
        return HealthStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> HealthServicesResourceWithRawResponse:
        return HealthServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthServicesResourceWithStreamingResponse:
        return HealthServicesResourceWithStreamingResponse(self)

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
        """Redirect Docs"""
        return self._get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncHealthServicesResource(AsyncAPIResource):
    @cached_property
    def health_status(self) -> AsyncHealthStatusResource:
        return AsyncHealthStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHealthServicesResourceWithRawResponse:
        return AsyncHealthServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthServicesResourceWithStreamingResponse:
        return AsyncHealthServicesResourceWithStreamingResponse(self)

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
        """Redirect Docs"""
        return await self._get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class HealthServicesResourceWithRawResponse:
    def __init__(self, health_services: HealthServicesResource) -> None:
        self._health_services = health_services

        self.retrieve = to_raw_response_wrapper(
            health_services.retrieve,
        )

    @cached_property
    def health_status(self) -> HealthStatusResourceWithRawResponse:
        return HealthStatusResourceWithRawResponse(self._health_services.health_status)


class AsyncHealthServicesResourceWithRawResponse:
    def __init__(self, health_services: AsyncHealthServicesResource) -> None:
        self._health_services = health_services

        self.retrieve = async_to_raw_response_wrapper(
            health_services.retrieve,
        )

    @cached_property
    def health_status(self) -> AsyncHealthStatusResourceWithRawResponse:
        return AsyncHealthStatusResourceWithRawResponse(self._health_services.health_status)


class HealthServicesResourceWithStreamingResponse:
    def __init__(self, health_services: HealthServicesResource) -> None:
        self._health_services = health_services

        self.retrieve = to_streamed_response_wrapper(
            health_services.retrieve,
        )

    @cached_property
    def health_status(self) -> HealthStatusResourceWithStreamingResponse:
        return HealthStatusResourceWithStreamingResponse(self._health_services.health_status)


class AsyncHealthServicesResourceWithStreamingResponse:
    def __init__(self, health_services: AsyncHealthServicesResource) -> None:
        self._health_services = health_services

        self.retrieve = async_to_streamed_response_wrapper(
            health_services.retrieve,
        )

    @cached_property
    def health_status(self) -> AsyncHealthStatusResourceWithStreamingResponse:
        return AsyncHealthStatusResourceWithStreamingResponse(self._health_services.health_status)
