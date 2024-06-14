# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ModeratorUpdateParams"]


class ModeratorUpdateParams(TypedDict, total=False):
    is_active: Required[bool]

    is_admin: Required[bool]

    username: Required[str]
