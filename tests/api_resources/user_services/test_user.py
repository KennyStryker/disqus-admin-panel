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
from disqus-admin-panel.types.user_services import user_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_list(self, client: DisqusAdminPanel) -> None:
        user = client.user_services.user.list(
            username="string",
        )
        assert_matches_type(object, user, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: DisqusAdminPanel) -> None:
        user = client.user_services.user.list(
            username="string",
            page_size=0,
            skip=0,
        )
        assert_matches_type(object, user, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: DisqusAdminPanel) -> None:

        response = client.user_services.user.with_raw_response.list(
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = response.parse()
        assert_matches_type(object, user, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: DisqusAdminPanel) -> None:
        with client.user_services.user.with_streaming_response.list(
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = response.parse()
            assert_matches_type(object, user, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_list(self, async_client: AsyncDisqusAdminPanel) -> None:
        user = await async_client.user_services.user.list(
            username="string",
        )
        assert_matches_type(object, user, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDisqusAdminPanel) -> None:
        user = await async_client.user_services.user.list(
            username="string",
            page_size=0,
            skip=0,
        )
        assert_matches_type(object, user, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.user_services.user.with_raw_response.list(
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user = await response.parse()
        assert_matches_type(object, user, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.user_services.user.with_streaming_response.list(
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user = await response.parse()
            assert_matches_type(object, user, path=['response'])

        assert cast(Any, response.is_closed) is True