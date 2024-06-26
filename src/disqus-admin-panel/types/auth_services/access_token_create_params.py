# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["AccessTokenCreateParams"]


class AccessTokenCreateParams(TypedDict, total=False):
    password: Required[str]

    username: Required[str]

    client_id: Optional[str]

    client_secret: Optional[str]

    grant_type: Optional[str]

    scope: str
