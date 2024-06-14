# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .moderators import ModeratorsResource, AsyncModeratorsResource

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
from .moderators import (
    ModeratorsResource,
    AsyncModeratorsResource,
    ModeratorsResourceWithRawResponse,
    AsyncModeratorsResourceWithRawResponse,
    ModeratorsResourceWithStreamingResponse,
    AsyncModeratorsResourceWithStreamingResponse,
)

__all__ = ["AdminServicesResource", "AsyncAdminServicesResource"]


class AdminServicesResource(SyncAPIResource):
    @cached_property
    def moderators(self) -> ModeratorsResource:
        return ModeratorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminServicesResourceWithRawResponse:
        return AdminServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminServicesResourceWithStreamingResponse:
        return AdminServicesResourceWithStreamingResponse(self)


class AsyncAdminServicesResource(AsyncAPIResource):
    @cached_property
    def moderators(self) -> AsyncModeratorsResource:
        return AsyncModeratorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminServicesResourceWithRawResponse:
        return AsyncAdminServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminServicesResourceWithStreamingResponse:
        return AsyncAdminServicesResourceWithStreamingResponse(self)


class AdminServicesResourceWithRawResponse:
    def __init__(self, admin_services: AdminServicesResource) -> None:
        self._admin_services = admin_services

    @cached_property
    def moderators(self) -> ModeratorsResourceWithRawResponse:
        return ModeratorsResourceWithRawResponse(self._admin_services.moderators)


class AsyncAdminServicesResourceWithRawResponse:
    def __init__(self, admin_services: AsyncAdminServicesResource) -> None:
        self._admin_services = admin_services

    @cached_property
    def moderators(self) -> AsyncModeratorsResourceWithRawResponse:
        return AsyncModeratorsResourceWithRawResponse(self._admin_services.moderators)


class AdminServicesResourceWithStreamingResponse:
    def __init__(self, admin_services: AdminServicesResource) -> None:
        self._admin_services = admin_services

    @cached_property
    def moderators(self) -> ModeratorsResourceWithStreamingResponse:
        return ModeratorsResourceWithStreamingResponse(self._admin_services.moderators)


class AsyncAdminServicesResourceWithStreamingResponse:
    def __init__(self, admin_services: AsyncAdminServicesResource) -> None:
        self._admin_services = admin_services

    @cached_property
    def moderators(self) -> AsyncModeratorsResourceWithStreamingResponse:
        return AsyncModeratorsResourceWithStreamingResponse(self._admin_services.moderators)
