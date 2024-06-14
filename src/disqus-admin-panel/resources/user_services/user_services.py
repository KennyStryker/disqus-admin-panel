# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .user.user import UserResource, AsyncUserResource

from ..._compat import cached_property

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
from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)

__all__ = ["UserServicesResource", "AsyncUserServicesResource"]


class UserServicesResource(SyncAPIResource):
    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserServicesResourceWithRawResponse:
        return UserServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserServicesResourceWithStreamingResponse:
        return UserServicesResourceWithStreamingResponse(self)


class AsyncUserServicesResource(AsyncAPIResource):
    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserServicesResourceWithRawResponse:
        return AsyncUserServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserServicesResourceWithStreamingResponse:
        return AsyncUserServicesResourceWithStreamingResponse(self)


class UserServicesResourceWithRawResponse:
    def __init__(self, user_services: UserServicesResource) -> None:
        self._user_services = user_services

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._user_services.user)


class AsyncUserServicesResourceWithRawResponse:
    def __init__(self, user_services: AsyncUserServicesResource) -> None:
        self._user_services = user_services

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._user_services.user)


class UserServicesResourceWithStreamingResponse:
    def __init__(self, user_services: UserServicesResource) -> None:
        self._user_services = user_services

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._user_services.user)


class AsyncUserServicesResourceWithStreamingResponse:
    def __init__(self, user_services: AsyncUserServicesResource) -> None:
        self._user_services = user_services

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._user_services.user)
