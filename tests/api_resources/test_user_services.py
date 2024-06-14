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
from disqus-admin-panel.types import user_service_get_comment_info_params
from disqus-admin-panel.types import user_service_restrict_access_params
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime
from disqus-admin-panel._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestUserServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_get_comment_info(self, client: DisqusAdminPanel) -> None:
        user_service = client.user_services.get_comment_info(
            comment_id_or_url="string",
        )
        assert_matches_type(object, user_service, path=['response'])

    @parametrize
    def test_raw_response_get_comment_info(self, client: DisqusAdminPanel) -> None:

        response = client.user_services.with_raw_response.get_comment_info(
            comment_id_or_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user_service = response.parse()
        assert_matches_type(object, user_service, path=['response'])

    @parametrize
    def test_streaming_response_get_comment_info(self, client: DisqusAdminPanel) -> None:
        with client.user_services.with_streaming_response.get_comment_info(
            comment_id_or_url="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user_service = response.parse()
            assert_matches_type(object, user_service, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_restrict_access(self, client: DisqusAdminPanel) -> None:
        user_service = client.user_services.restrict_access(
            comment="string",
            comment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comment_id=0,
            delete_all_comments=True,
            display_name="string",
            duration=0,
            editable_until=parse_datetime("2019-12-27T18:11:19.117Z"),
            forum="string",
            is_permanent=True,
            reason="string",
            username="string",
        )
        assert_matches_type(object, user_service, path=['response'])

    @parametrize
    def test_raw_response_restrict_access(self, client: DisqusAdminPanel) -> None:

        response = client.user_services.with_raw_response.restrict_access(
            comment="string",
            comment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comment_id=0,
            delete_all_comments=True,
            display_name="string",
            duration=0,
            editable_until=parse_datetime("2019-12-27T18:11:19.117Z"),
            forum="string",
            is_permanent=True,
            reason="string",
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user_service = response.parse()
        assert_matches_type(object, user_service, path=['response'])

    @parametrize
    def test_streaming_response_restrict_access(self, client: DisqusAdminPanel) -> None:
        with client.user_services.with_streaming_response.restrict_access(
            comment="string",
            comment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comment_id=0,
            delete_all_comments=True,
            display_name="string",
            duration=0,
            editable_until=parse_datetime("2019-12-27T18:11:19.117Z"),
            forum="string",
            is_permanent=True,
            reason="string",
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user_service = response.parse()
            assert_matches_type(object, user_service, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncUserServices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_get_comment_info(self, async_client: AsyncDisqusAdminPanel) -> None:
        user_service = await async_client.user_services.get_comment_info(
            comment_id_or_url="string",
        )
        assert_matches_type(object, user_service, path=['response'])

    @parametrize
    async def test_raw_response_get_comment_info(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.user_services.with_raw_response.get_comment_info(
            comment_id_or_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user_service = await response.parse()
        assert_matches_type(object, user_service, path=['response'])

    @parametrize
    async def test_streaming_response_get_comment_info(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.user_services.with_streaming_response.get_comment_info(
            comment_id_or_url="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user_service = await response.parse()
            assert_matches_type(object, user_service, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_restrict_access(self, async_client: AsyncDisqusAdminPanel) -> None:
        user_service = await async_client.user_services.restrict_access(
            comment="string",
            comment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comment_id=0,
            delete_all_comments=True,
            display_name="string",
            duration=0,
            editable_until=parse_datetime("2019-12-27T18:11:19.117Z"),
            forum="string",
            is_permanent=True,
            reason="string",
            username="string",
        )
        assert_matches_type(object, user_service, path=['response'])

    @parametrize
    async def test_raw_response_restrict_access(self, async_client: AsyncDisqusAdminPanel) -> None:

        response = await async_client.user_services.with_raw_response.restrict_access(
            comment="string",
            comment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comment_id=0,
            delete_all_comments=True,
            display_name="string",
            duration=0,
            editable_until=parse_datetime("2019-12-27T18:11:19.117Z"),
            forum="string",
            is_permanent=True,
            reason="string",
            username="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        user_service = await response.parse()
        assert_matches_type(object, user_service, path=['response'])

    @parametrize
    async def test_streaming_response_restrict_access(self, async_client: AsyncDisqusAdminPanel) -> None:
        async with async_client.user_services.with_streaming_response.restrict_access(
            comment="string",
            comment_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            comment_id=0,
            delete_all_comments=True,
            display_name="string",
            duration=0,
            editable_until=parse_datetime("2019-12-27T18:11:19.117Z"),
            forum="string",
            is_permanent=True,
            reason="string",
            username="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            user_service = await response.parse()
            assert_matches_type(object, user_service, path=['response'])

        assert cast(Any, response.is_closed) is True