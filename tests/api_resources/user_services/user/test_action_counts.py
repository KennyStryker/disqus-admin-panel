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

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestActionCounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_retrieve(self, client: DisqusAdminPanel) -> None:
        action_count = client.user_services.user.action_counts.retrieve()
        assert_matches_type(object, action_count, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: DisqusAdminPanel) -> None:

        response = client.user_services.user.action_counts.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action_count = response.parse()
        assert_matches_type(object, action_count, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: DisqusAdminPanel) -> None:
        with client.user_services.user.action_counts.with_streaming_response.retrieve() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action_count = response.parse()
            assert_matches_type(object, action_count, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncActionCounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDisqusAdminPanel) -> None:
        action_count = await async_client.user_services.user.action_counts.retrieve()
        assert_matches_type(object, action_count, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.user_services.user.action_counts.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        action_count = await response.parse()
        assert_matches_type(object, action_count, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.user_services.user.action_counts.with_streaming_response.retrieve() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            action_count = await response.parse()
            assert_matches_type(object, action_count, path=['response'])

        assert cast(Any, response.is_closed) is True