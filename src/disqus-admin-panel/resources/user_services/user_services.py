# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .users import UsersResource, AsyncUsersResource

from ..._compat import cached_property

from ..._utils import maybe_transform, async_maybe_transform

from typing import Union

from datetime import datetime

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
from ...types import user_service_get_comment_info_params
from ...types import user_service_restrict_access_params
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)

__all__ = ["UserServicesResource", "AsyncUserServicesResource"]


class UserServicesResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserServicesResourceWithRawResponse:
        return UserServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserServicesResourceWithStreamingResponse:
        return UserServicesResourceWithStreamingResponse(self)

    def get_comment_info(
        self,
        *,
        comment_id_or_url: str,
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
            "/user/get_comment_info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"comment_id_or_url": comment_id_or_url},
                    user_service_get_comment_info_params.UserServiceGetCommentInfoParams,
                ),
            ),
            cast_to=object,
        )

    def restrict_access(
        self,
        *,
        comment: str,
        comment_date: Union[str, datetime],
        comment_id: int,
        delete_all_comments: bool,
        display_name: str,
        duration: int,
        editable_until: Union[str, datetime],
        forum: str,
        is_permanent: bool,
        reason: str,
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
            "/user/restrict_access",
            body=maybe_transform(
                {
                    "comment": comment,
                    "comment_date": comment_date,
                    "comment_id": comment_id,
                    "delete_all_comments": delete_all_comments,
                    "display_name": display_name,
                    "duration": duration,
                    "editable_until": editable_until,
                    "forum": forum,
                    "is_permanent": is_permanent,
                    "reason": reason,
                    "username": username,
                },
                user_service_restrict_access_params.UserServiceRestrictAccessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncUserServicesResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserServicesResourceWithRawResponse:
        return AsyncUserServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserServicesResourceWithStreamingResponse:
        return AsyncUserServicesResourceWithStreamingResponse(self)

    async def get_comment_info(
        self,
        *,
        comment_id_or_url: str,
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
            "/user/get_comment_info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"comment_id_or_url": comment_id_or_url},
                    user_service_get_comment_info_params.UserServiceGetCommentInfoParams,
                ),
            ),
            cast_to=object,
        )

    async def restrict_access(
        self,
        *,
        comment: str,
        comment_date: Union[str, datetime],
        comment_id: int,
        delete_all_comments: bool,
        display_name: str,
        duration: int,
        editable_until: Union[str, datetime],
        forum: str,
        is_permanent: bool,
        reason: str,
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
            "/user/restrict_access",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "comment_date": comment_date,
                    "comment_id": comment_id,
                    "delete_all_comments": delete_all_comments,
                    "display_name": display_name,
                    "duration": duration,
                    "editable_until": editable_until,
                    "forum": forum,
                    "is_permanent": is_permanent,
                    "reason": reason,
                    "username": username,
                },
                user_service_restrict_access_params.UserServiceRestrictAccessParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class UserServicesResourceWithRawResponse:
    def __init__(self, user_services: UserServicesResource) -> None:
        self._user_services = user_services

        self.get_comment_info = to_raw_response_wrapper(
            user_services.get_comment_info,
        )
        self.restrict_access = to_raw_response_wrapper(
            user_services.restrict_access,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._user_services.users)


class AsyncUserServicesResourceWithRawResponse:
    def __init__(self, user_services: AsyncUserServicesResource) -> None:
        self._user_services = user_services

        self.get_comment_info = async_to_raw_response_wrapper(
            user_services.get_comment_info,
        )
        self.restrict_access = async_to_raw_response_wrapper(
            user_services.restrict_access,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._user_services.users)


class UserServicesResourceWithStreamingResponse:
    def __init__(self, user_services: UserServicesResource) -> None:
        self._user_services = user_services

        self.get_comment_info = to_streamed_response_wrapper(
            user_services.get_comment_info,
        )
        self.restrict_access = to_streamed_response_wrapper(
            user_services.restrict_access,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._user_services.users)


class AsyncUserServicesResourceWithStreamingResponse:
    def __init__(self, user_services: AsyncUserServicesResource) -> None:
        self._user_services = user_services

        self.get_comment_info = async_to_streamed_response_wrapper(
            user_services.get_comment_info,
        )
        self.restrict_access = async_to_streamed_response_wrapper(
            user_services.restrict_access,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._user_services.users)
