# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from disqus-admin-panel import DisqusAdminPanel, AsyncDisqusAdminPanel

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from disqus-admin-panel import DisqusAdminPanel, AsyncDisqusAdminPanel
from tests.utils import assert_matches_type
from disqus-admin-panel.types import profile_service_change_password_params
from disqus-admin-panel.types import profile_service_change_profile_picture_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestProfileServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_change_password(self, client: DisqusAdminPanel) -> None:
        profile_service = client.profile_services.change_password(
            current_password="string",
            new_password="string",
        )
        assert_matches_type(object, profile_service, path=['response'])

    @parametrize
    def test_raw_response_change_password(self, client: DisqusAdminPanel) -> None:

        response = client.profile_services.with_raw_response.change_password(
            current_password="string",
            new_password="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        profile_service = response.parse()
        assert_matches_type(object, profile_service, path=['response'])

    @parametrize
    def test_streaming_response_change_password(self, client: DisqusAdminPanel) -> None:
        with client.profile_services.with_streaming_response.change_password(
            current_password="string",
            new_password="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            profile_service = response.parse()
            assert_matches_type(object, profile_service, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_change_profile_picture(self, client: DisqusAdminPanel) -> None:
        profile_service = client.profile_services.change_profile_picture(
            file=b'raw file contents',
        )
        assert_matches_type(object, profile_service, path=['response'])

    @parametrize
    def test_raw_response_change_profile_picture(self, client: DisqusAdminPanel) -> None:

        response = client.profile_services.with_raw_response.change_profile_picture(
            file=b'raw file contents',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        profile_service = response.parse()
        assert_matches_type(object, profile_service, path=['response'])

    @parametrize
    def test_streaming_response_change_profile_picture(self, client: DisqusAdminPanel) -> None:
        with client.profile_services.with_streaming_response.change_profile_picture(
            file=b'raw file contents',
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            profile_service = response.parse()
            assert_matches_type(object, profile_service, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncProfileServices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_change_password(self, async_client: AsyncDisqusAdminPanel) -> None:
        profile_service = await async_client.profile_services.change_password(
            current_password="string",
            new_password="string",
        )
        assert_matches_type(object, profile_service, path=['response'])

    @parametrize
    async def test_raw_response_change_password(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.profile_services.with_raw_response.change_password(
            current_password="string",
            new_password="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        profile_service = await response.parse()
        assert_matches_type(object, profile_service, path=['response'])

    @parametrize
    async def test_streaming_response_change_password(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.profile_services.with_streaming_response.change_password(
            current_password="string",
            new_password="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            profile_service = await response.parse()
            assert_matches_type(object, profile_service, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_change_profile_picture(self, async_client: AsyncDisqusAdminPanel) -> None:
        profile_service = await async_client.profile_services.change_profile_picture(
            file=b'raw file contents',
        )
        assert_matches_type(object, profile_service, path=['response'])

    @parametrize
    async def test_raw_response_change_profile_picture(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.profile_services.with_raw_response.change_profile_picture(
            file=b'raw file contents',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        profile_service = await response.parse()
        assert_matches_type(object, profile_service, path=['response'])

    @parametrize
    async def test_streaming_response_change_profile_picture(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.profile_services.with_streaming_response.change_profile_picture(
            file=b'raw file contents',
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            profile_service = await response.parse()
            assert_matches_type(object, profile_service, path=['response'])

        assert cast(Any, response.is_closed) is True