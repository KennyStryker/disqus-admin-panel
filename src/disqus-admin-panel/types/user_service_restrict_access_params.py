# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Union

from datetime import datetime

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["UserServiceRestrictAccessParams"]


class UserServiceRestrictAccessParams(TypedDict, total=False):
    comment: Required[str]

    comment_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    comment_id: Required[int]

    delete_all_comments: Required[bool]

    display_name: Required[str]

    duration: Required[int]

    editable_until: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    forum: Required[str]

    is_permanent: Required[bool]

    reason: Required[str]

    username: Required[str]
