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
from disqus-admin-panel.types.auth_services import access_token_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestAccessToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: DisqusAdminPanel) -> None:
        access_token = client.auth_services.access_token.create(
            password="string",
            username="string",
        )
        assert_matches_type(object, access_token, path=['response'])

    @parametrize
    def test_method_create_with_all_params(self, client: DisqusAdminPanel) -> None:
        access_token = client.auth_services.access_token.create(
            password="string",
            username="string",
            client_id="string",
            client_secret="string",
            grant_type="string",
            scope="string",
        )
        assert_matches_type(object, access_token, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: DisqusAdminPanel) -> None:

        response = client.auth_services.access_token.with_raw_response.create(
            password="string",
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_token = response.parse()
        assert_matches_type(object, access_token, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: DisqusAdminPanel) -> None:
        with client.auth_services.access_token.with_streaming_response.create(
            password="string",
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_token = response.parse()
            assert_matches_type(object, access_token, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncAccessToken:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncDisqusAdminPanel) -> None:
        access_token = await async_client.auth_services.access_token.create(
            password="string",
            username="string",
        )
        assert_matches_type(object, access_token, path=['response'])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDisqusAdminPanel) -> None:
        access_token = await async_client.auth_services.access_token.create(
            password="string",
            username="string",
            client_id="string",
            client_secret="string",
            grant_type="string",
            scope="string",
        )
        assert_matches_type(object, access_token, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.auth_services.access_token.with_raw_response.create(
            password="string",
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        access_token = await response.parse()
        assert_matches_type(object, access_token, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.auth_services.access_token.with_streaming_response.create(
            password="string",
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            access_token = await response.parse()
            assert_matches_type(object, access_token, path=['response'])

        assert cast(Any, response.is_closed) is True