# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .access_token import AccessTokenResource, AsyncAccessTokenResource

from ..._compat import cached_property

from .current_moderator import CurrentModeratorResource, AsyncCurrentModeratorResource

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
from .access_token import (
    AccessTokenResource,
    AsyncAccessTokenResource,
    AccessTokenResourceWithRawResponse,
    AsyncAccessTokenResourceWithRawResponse,
    AccessTokenResourceWithStreamingResponse,
    AsyncAccessTokenResourceWithStreamingResponse,
)
from .current_moderator import (
    CurrentModeratorResource,
    AsyncCurrentModeratorResource,
    CurrentModeratorResourceWithRawResponse,
    AsyncCurrentModeratorResourceWithRawResponse,
    CurrentModeratorResourceWithStreamingResponse,
    AsyncCurrentModeratorResourceWithStreamingResponse,
)

__all__ = ["AuthServicesResource", "AsyncAuthServicesResource"]


class AuthServicesResource(SyncAPIResource):
    @cached_property
    def access_token(self) -> AccessTokenResource:
        return AccessTokenResource(self._client)

    @cached_property
    def current_moderator(self) -> CurrentModeratorResource:
        return CurrentModeratorResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthServicesResourceWithRawResponse:
        return AuthServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthServicesResourceWithStreamingResponse:
        return AuthServicesResourceWithStreamingResponse(self)


class AsyncAuthServicesResource(AsyncAPIResource):
    @cached_property
    def access_token(self) -> AsyncAccessTokenResource:
        return AsyncAccessTokenResource(self._client)

    @cached_property
    def current_moderator(self) -> AsyncCurrentModeratorResource:
        return AsyncCurrentModeratorResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthServicesResourceWithRawResponse:
        return AsyncAuthServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthServicesResourceWithStreamingResponse:
        return AsyncAuthServicesResourceWithStreamingResponse(self)


class AuthServicesResourceWithRawResponse:
    def __init__(self, auth_services: AuthServicesResource) -> None:
        self._auth_services = auth_services

    @cached_property
    def access_token(self) -> AccessTokenResourceWithRawResponse:
        return AccessTokenResourceWithRawResponse(self._auth_services.access_token)

    @cached_property
    def current_moderator(self) -> CurrentModeratorResourceWithRawResponse:
        return CurrentModeratorResourceWithRawResponse(self._auth_services.current_moderator)


class AsyncAuthServicesResourceWithRawResponse:
    def __init__(self, auth_services: AsyncAuthServicesResource) -> None:
        self._auth_services = auth_services

    @cached_property
    def access_token(self) -> AsyncAccessTokenResourceWithRawResponse:
        return AsyncAccessTokenResourceWithRawResponse(self._auth_services.access_token)

    @cached_property
    def current_moderator(self) -> AsyncCurrentModeratorResourceWithRawResponse:
        return AsyncCurrentModeratorResourceWithRawResponse(self._auth_services.current_moderator)


class AuthServicesResourceWithStreamingResponse:
    def __init__(self, auth_services: AuthServicesResource) -> None:
        self._auth_services = auth_services

    @cached_property
    def access_token(self) -> AccessTokenResourceWithStreamingResponse:
        return AccessTokenResourceWithStreamingResponse(self._auth_services.access_token)

    @cached_property
    def current_moderator(self) -> CurrentModeratorResourceWithStreamingResponse:
        return CurrentModeratorResourceWithStreamingResponse(self._auth_services.current_moderator)


class AsyncAuthServicesResourceWithStreamingResponse:
    def __init__(self, auth_services: AsyncAuthServicesResource) -> None:
        self._auth_services = auth_services

    @cached_property
    def access_token(self) -> AsyncAccessTokenResourceWithStreamingResponse:
        return AsyncAccessTokenResourceWithStreamingResponse(self._auth_services.access_token)

    @cached_property
    def current_moderator(self) -> AsyncCurrentModeratorResourceWithStreamingResponse:
        return AsyncCurrentModeratorResourceWithStreamingResponse(self._auth_services.current_moderator)
