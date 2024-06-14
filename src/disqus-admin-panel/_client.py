# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

import os

from ._streaming import AsyncStream as AsyncStream, Stream as Stream

from ._exceptions import DisqusAdminPanelError, APIStatusError

from typing_extensions import override, Self

from typing import Any

from ._utils import get_async_library

from . import _exceptions

import os
import asyncio
import warnings
from typing import Optional, Union, Dict, Any, Mapping, overload, cast
from typing_extensions import Literal

import httpx

from ._version import __version__
from ._qs import Querystring
from .types import shared_params
from ._utils import (
    extract_files,
    maybe_transform,
    required_args,
    deepcopy_minimal,
    maybe_coerce_integer,
    maybe_coerce_float,
    maybe_coerce_boolean,
    is_given,
)
from ._types import (
    Omit,
    NotGiven,
    Timeout,
    Transport,
    ProxiesTypes,
    RequestOptions,
    Headers,
    NoneType,
    Query,
    Body,
    NOT_GIVEN,
)
from ._base_client import (
    DEFAULT_CONNECTION_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    ResponseT,
    SyncHttpxClientWrapper,
    AsyncHttpxClientWrapper,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from . import resources

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "DisqusAdminPanel",
    "AsyncDisqusAdminPanel",
    "Client",
    "AsyncClient",
]


class DisqusAdminPanel(SyncAPIClient):
    health_services: resources.HealthServicesResource
    auth_services: resources.AuthServicesResource
    admin_services: resources.AdminServicesResource
    user_services: resources.UserServicesResource
    profile_services: resources.ProfileServicesResource
    with_raw_response: DisqusAdminPanelWithRawResponse
    with_streaming_response: DisqusAdminPanelWithStreamedResponse

    # client options
    access_token: str

    def __init__(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous disqus-admin-panel client instance.

        This automatically infers the `access_token` argument from the `DISQUS_ADMIN_PANEL_ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("DISQUS_ADMIN_PANEL_ACCESS_TOKEN")
        if access_token is None:
            raise DisqusAdminPanelError(
                "The access_token client option must be set either by passing access_token to the client or by setting the DISQUS_ADMIN_PANEL_ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("DISQUS_ADMIN_PANEL_BASE_URL")
        if base_url is None:
            base_url = f"https://localhost:8080/test-api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.health_services = resources.HealthServicesResource(self)
        self.auth_services = resources.AuthServicesResource(self)
        self.admin_services = resources.AdminServicesResource(self)
        self.user_services = resources.UserServicesResource(self)
        self.profile_services = resources.ProfileServicesResource(self)
        self.with_raw_response = DisqusAdminPanelWithRawResponse(self)
        self.with_streaming_response = DisqusAdminPanelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncDisqusAdminPanel(AsyncAPIClient):
    health_services: resources.AsyncHealthServicesResource
    auth_services: resources.AsyncAuthServicesResource
    admin_services: resources.AsyncAdminServicesResource
    user_services: resources.AsyncUserServicesResource
    profile_services: resources.AsyncProfileServicesResource
    with_raw_response: AsyncDisqusAdminPanelWithRawResponse
    with_streaming_response: AsyncDisqusAdminPanelWithStreamedResponse

    # client options
    access_token: str

    def __init__(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async disqus-admin-panel client instance.

        This automatically infers the `access_token` argument from the `DISQUS_ADMIN_PANEL_ACCESS_TOKEN` environment variable if it is not provided.
        """
        if access_token is None:
            access_token = os.environ.get("DISQUS_ADMIN_PANEL_ACCESS_TOKEN")
        if access_token is None:
            raise DisqusAdminPanelError(
                "The access_token client option must be set either by passing access_token to the client or by setting the DISQUS_ADMIN_PANEL_ACCESS_TOKEN environment variable"
            )
        self.access_token = access_token

        if base_url is None:
            base_url = os.environ.get("DISQUS_ADMIN_PANEL_BASE_URL")
        if base_url is None:
            base_url = f"https://localhost:8080/test-api"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.health_services = resources.AsyncHealthServicesResource(self)
        self.auth_services = resources.AsyncAuthServicesResource(self)
        self.admin_services = resources.AsyncAdminServicesResource(self)
        self.user_services = resources.AsyncUserServicesResource(self)
        self.profile_services = resources.AsyncProfileServicesResource(self)
        self.with_raw_response = AsyncDisqusAdminPanelWithRawResponse(self)
        self.with_streaming_response = AsyncDisqusAdminPanelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class DisqusAdminPanelWithRawResponse:
    def __init__(self, client: DisqusAdminPanel) -> None:
        self.health_services = resources.HealthServicesResourceWithRawResponse(client.health_services)
        self.auth_services = resources.AuthServicesResourceWithRawResponse(client.auth_services)
        self.admin_services = resources.AdminServicesResourceWithRawResponse(client.admin_services)
        self.user_services = resources.UserServicesResourceWithRawResponse(client.user_services)
        self.profile_services = resources.ProfileServicesResourceWithRawResponse(client.profile_services)


class AsyncDisqusAdminPanelWithRawResponse:
    def __init__(self, client: AsyncDisqusAdminPanel) -> None:
        self.health_services = resources.AsyncHealthServicesResourceWithRawResponse(client.health_services)
        self.auth_services = resources.AsyncAuthServicesResourceWithRawResponse(client.auth_services)
        self.admin_services = resources.AsyncAdminServicesResourceWithRawResponse(client.admin_services)
        self.user_services = resources.AsyncUserServicesResourceWithRawResponse(client.user_services)
        self.profile_services = resources.AsyncProfileServicesResourceWithRawResponse(client.profile_services)


class DisqusAdminPanelWithStreamedResponse:
    def __init__(self, client: DisqusAdminPanel) -> None:
        self.health_services = resources.HealthServicesResourceWithStreamingResponse(client.health_services)
        self.auth_services = resources.AuthServicesResourceWithStreamingResponse(client.auth_services)
        self.admin_services = resources.AdminServicesResourceWithStreamingResponse(client.admin_services)
        self.user_services = resources.UserServicesResourceWithStreamingResponse(client.user_services)
        self.profile_services = resources.ProfileServicesResourceWithStreamingResponse(client.profile_services)


class AsyncDisqusAdminPanelWithStreamedResponse:
    def __init__(self, client: AsyncDisqusAdminPanel) -> None:
        self.health_services = resources.AsyncHealthServicesResourceWithStreamingResponse(client.health_services)
        self.auth_services = resources.AsyncAuthServicesResourceWithStreamingResponse(client.auth_services)
        self.admin_services = resources.AsyncAdminServicesResourceWithStreamingResponse(client.admin_services)
        self.user_services = resources.AsyncUserServicesResourceWithStreamingResponse(client.user_services)
        self.profile_services = resources.AsyncProfileServicesResourceWithStreamingResponse(client.profile_services)


Client = DisqusAdminPanel

AsyncClient = AsyncDisqusAdminPanel
