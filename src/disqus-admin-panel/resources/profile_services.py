# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from .._utils import maybe_transform, async_maybe_transform

from .._types import FileTypes

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import profile_service_change_password_params
from ..types import profile_service_change_profile_picture_params

__all__ = ["ProfileServicesResource", "AsyncProfileServicesResource"]


class ProfileServicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfileServicesResourceWithRawResponse:
        return ProfileServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfileServicesResourceWithStreamingResponse:
        return ProfileServicesResourceWithStreamingResponse(self)

    def change_password(
        self,
        *,
        current_password: str,
        new_password: str,
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
            "/profile/change_password",
            body=maybe_transform(
                {
                    "current_password": current_password,
                    "new_password": new_password,
                },
                profile_service_change_password_params.ProfileServiceChangePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def change_profile_picture(
        self,
        *,
        file: FileTypes,
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
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            "/profile/change_profile_picture",
            body=maybe_transform(
                body, profile_service_change_profile_picture_params.ProfileServiceChangeProfilePictureParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncProfileServicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfileServicesResourceWithRawResponse:
        return AsyncProfileServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfileServicesResourceWithStreamingResponse:
        return AsyncProfileServicesResourceWithStreamingResponse(self)

    async def change_password(
        self,
        *,
        current_password: str,
        new_password: str,
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
            "/profile/change_password",
            body=await async_maybe_transform(
                {
                    "current_password": current_password,
                    "new_password": new_password,
                },
                profile_service_change_password_params.ProfileServiceChangePasswordParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def change_profile_picture(
        self,
        *,
        file: FileTypes,
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
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            "/profile/change_profile_picture",
            body=await async_maybe_transform(
                body, profile_service_change_profile_picture_params.ProfileServiceChangeProfilePictureParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ProfileServicesResourceWithRawResponse:
    def __init__(self, profile_services: ProfileServicesResource) -> None:
        self._profile_services = profile_services

        self.change_password = to_raw_response_wrapper(
            profile_services.change_password,
        )
        self.change_profile_picture = to_raw_response_wrapper(
            profile_services.change_profile_picture,
        )


class AsyncProfileServicesResourceWithRawResponse:
    def __init__(self, profile_services: AsyncProfileServicesResource) -> None:
        self._profile_services = profile_services

        self.change_password = async_to_raw_response_wrapper(
            profile_services.change_password,
        )
        self.change_profile_picture = async_to_raw_response_wrapper(
            profile_services.change_profile_picture,
        )


class ProfileServicesResourceWithStreamingResponse:
    def __init__(self, profile_services: ProfileServicesResource) -> None:
        self._profile_services = profile_services

        self.change_password = to_streamed_response_wrapper(
            profile_services.change_password,
        )
        self.change_profile_picture = to_streamed_response_wrapper(
            profile_services.change_profile_picture,
        )


class AsyncProfileServicesResourceWithStreamingResponse:
    def __init__(self, profile_services: AsyncProfileServicesResource) -> None:
        self._profile_services = profile_services

        self.change_password = async_to_streamed_response_wrapper(
            profile_services.change_password,
        )
        self.change_profile_picture = async_to_streamed_response_wrapper(
            profile_services.change_profile_picture,
        )
