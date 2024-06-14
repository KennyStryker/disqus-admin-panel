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
from disqus-admin-panel.types.admin_services import moderator_update_params
from disqus-admin-panel.types.admin_services import moderator_add_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestModerators:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_update(self, client: DisqusAdminPanel) -> None:
        moderator = client.admin_services.moderators.update(
            is_active=True,
            is_admin=True,
            username="string",
        )
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: DisqusAdminPanel) -> None:

        response = client.admin_services.moderators.with_raw_response.update(
            is_active=True,
            is_admin=True,
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        moderator = response.parse()
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: DisqusAdminPanel) -> None:
        with client.admin_services.moderators.with_streaming_response.update(
            is_active=True,
            is_admin=True,
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            moderator = response.parse()
            assert_matches_type(object, moderator, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: DisqusAdminPanel) -> None:
        moderator = client.admin_services.moderators.list()
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: DisqusAdminPanel) -> None:

        response = client.admin_services.moderators.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        moderator = response.parse()
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: DisqusAdminPanel) -> None:
        with client.admin_services.moderators.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            moderator = response.parse()
            assert_matches_type(object, moderator, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add(self, client: DisqusAdminPanel) -> None:
        moderator = client.admin_services.moderators.add(
            password="string",
            username="string",
        )
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    def test_raw_response_add(self, client: DisqusAdminPanel) -> None:

        response = client.admin_services.moderators.with_raw_response.add(
            password="string",
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        moderator = response.parse()
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    def test_streaming_response_add(self, client: DisqusAdminPanel) -> None:
        with client.admin_services.moderators.with_streaming_response.add(
            password="string",
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            moderator = response.parse()
            assert_matches_type(object, moderator, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncModerators:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_update(self, async_client: AsyncDisqusAdminPanel) -> None:
        moderator = await async_client.admin_services.moderators.update(
            is_active=True,
            is_admin=True,
            username="string",
        )
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.admin_services.moderators.with_raw_response.update(
            is_active=True,
            is_admin=True,
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        moderator = await response.parse()
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.admin_services.moderators.with_streaming_response.update(
            is_active=True,
            is_admin=True,
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            moderator = await response.parse()
            assert_matches_type(object, moderator, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncDisqusAdminPanel) -> None:
        moderator = await async_client.admin_services.moderators.list()
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.admin_services.moderators.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        moderator = await response.parse()
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.admin_services.moderators.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            moderator = await response.parse()
            assert_matches_type(object, moderator, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add(self, async_client: AsyncDisqusAdminPanel) -> None:
        moderator = await async_client.admin_services.moderators.add(
            password="string",
            username="string",
        )
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.admin_services.moderators.with_raw_response.add(
            password="string",
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        moderator = await response.parse()
        assert_matches_type(object, moderator, path=['response'])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.admin_services.moderators.with_streaming_response.add(
            password="string",
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            moderator = await response.parse()
            assert_matches_type(object, moderator, path=['response'])

        assert cast(Any, response.is_closed) is True