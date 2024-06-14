# HealthServices

Types:

```python
from disqus-admin-panel.types import HealthServiceRetrieveResponse
```

Methods:

- <code title="get /">client.health_services.<a href="./src/disqus-admin-panel/resources/health_services/health_services.py">retrieve</a>() -> <a href="./src/disqus-admin-panel/types/health_service_retrieve_response.py">object</a></code>

## HealthStatus

Types:

```python
from disqus-admin-panel.types.health_services import HealthStatusRetrieveResponse
```

Methods:

- <code title="get /health_status">client.health_services.health_status.<a href="./src/disqus-admin-panel/resources/health_services/health_status.py">retrieve</a>() -> <a href="./src/disqus-admin-panel/types/health_services/health_status_retrieve_response.py">object</a></code>

# AuthServices

## AccessToken

Types:

```python
from disqus-admin-panel.types.auth_services import AccessTokenCreateResponse
```

Methods:

- <code title="post /login/access-token">client.auth_services.access_token.<a href="./src/disqus-admin-panel/resources/auth_services/access_token.py">create</a>(\*\*<a href="src/disqus-admin-panel/types/auth_services/access_token_create_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/auth_services/access_token_create_response.py">object</a></code>

## CurrentModerator

Types:

```python
from disqus-admin-panel.types.auth_services import CurrentModeratorRetrieveResponse
```

Methods:

- <code title="get /get_current_moderator">client.auth_services.current_moderator.<a href="./src/disqus-admin-panel/resources/auth_services/current_moderator.py">retrieve</a>() -> <a href="./src/disqus-admin-panel/types/auth_services/current_moderator_retrieve_response.py">object</a></code>

# AdminServices

## Moderators

Types:

```python
from disqus-admin-panel.types.admin_services import ModeratorUpdateResponse, ModeratorListResponse, ModeratorAddResponse
```

Methods:

- <code title="put /moderator/update">client.admin_services.moderators.<a href="./src/disqus-admin-panel/resources/admin_services/moderators.py">update</a>(\*\*<a href="src/disqus-admin-panel/types/admin_services/moderator_update_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/admin_services/moderator_update_response.py">object</a></code>
- <code title="get /moderator/list">client.admin_services.moderators.<a href="./src/disqus-admin-panel/resources/admin_services/moderators.py">list</a>() -> <a href="./src/disqus-admin-panel/types/admin_services/moderator_list_response.py">object</a></code>
- <code title="post /moderator/add">client.admin_services.moderators.<a href="./src/disqus-admin-panel/resources/admin_services/moderators.py">add</a>(\*\*<a href="src/disqus-admin-panel/types/admin_services/moderator_add_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/admin_services/moderator_add_response.py">object</a></code>

# UserServices

Types:

```python
from disqus-admin-panel.types import UserServiceGetCommentInfoResponse, UserServiceRestrictAccessResponse
```

Methods:

- <code title="get /user/get_comment_info">client.user_services.<a href="./src/disqus-admin-panel/resources/user_services/user_services.py">get_comment_info</a>(\*\*<a href="src/disqus-admin-panel/types/user_service_get_comment_info_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/user_service_get_comment_info_response.py">object</a></code>
- <code title="post /user/restrict_access">client.user_services.<a href="./src/disqus-admin-panel/resources/user_services/user_services.py">restrict_access</a>(\*\*<a href="src/disqus-admin-panel/types/user_service_restrict_access_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/user_service_restrict_access_response.py">object</a></code>

## Users

Types:

```python
from disqus-admin-panel.types.user_services import UserListResponse, UserActionCountsResponse, UserActionHistoryResponse
```

Methods:

- <code title="get /user/list">client.user_services.users.<a href="./src/disqus-admin-panel/resources/user_services/users.py">list</a>(\*\*<a href="src/disqus-admin-panel/types/user_services/user_list_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/user_services/user_list_response.py">object</a></code>
- <code title="get /user/action_counts">client.user_services.users.<a href="./src/disqus-admin-panel/resources/user_services/users.py">action_counts</a>() -> <a href="./src/disqus-admin-panel/types/user_services/user_action_counts_response.py">object</a></code>
- <code title="get /user/action_history">client.user_services.users.<a href="./src/disqus-admin-panel/resources/user_services/users.py">action_history</a>() -> <a href="./src/disqus-admin-panel/types/user_services/user_action_history_response.py">object</a></code>

# ProfileServices

Types:

```python
from disqus-admin-panel.types import ProfileServiceChangePasswordResponse, ProfileServiceChangeProfilePictureResponse
```

Methods:

- <code title="put /profile/change_password">client.profile_services.<a href="./src/disqus-admin-panel/resources/profile_services.py">change_password</a>(\*\*<a href="src/disqus-admin-panel/types/profile_service_change_password_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/profile_service_change_password_response.py">object</a></code>
- <code title="put /profile/change_profile_picture">client.profile_services.<a href="./src/disqus-admin-panel/resources/profile_services.py">change_profile_picture</a>(\*\*<a href="src/disqus-admin-panel/types/profile_service_change_profile_picture_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/profile_service_change_profile_picture_response.py">object</a></code>
