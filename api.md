# HealthServices

Types:

```python
from disqus-admin-panel.types import HealthServiceListResponse
```

Methods:

- <code title="get /">client.health_services.<a href="./src/disqus-admin-panel/resources/health_services/health_services.py">list</a>() -> <a href="./src/disqus-admin-panel/types/health_service_list_response.py">object</a></code>

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

## Moderator

Types:

```python
from disqus-admin-panel.types.admin_services import ModeratorUpdateResponse, ModeratorListResponse, ModeratorAddResponse
```

Methods:

- <code title="put /moderator/update">client.admin_services.moderator.<a href="./src/disqus-admin-panel/resources/admin_services/moderator.py">update</a>(\*\*<a href="src/disqus-admin-panel/types/admin_services/moderator_update_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/admin_services/moderator_update_response.py">object</a></code>
- <code title="get /moderator/list">client.admin_services.moderator.<a href="./src/disqus-admin-panel/resources/admin_services/moderator.py">list</a>() -> <a href="./src/disqus-admin-panel/types/admin_services/moderator_list_response.py">object</a></code>
- <code title="post /moderator/add">client.admin_services.moderator.<a href="./src/disqus-admin-panel/resources/admin_services/moderator.py">add</a>(\*\*<a href="src/disqus-admin-panel/types/admin_services/moderator_add_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/admin_services/moderator_add_response.py">object</a></code>

# UserServices

## User

Types:

```python
from disqus-admin-panel.types.user_services import UserListResponse
```

Methods:

- <code title="get /user/list">client.user_services.user.<a href="./src/disqus-admin-panel/resources/user_services/user/user.py">list</a>(\*\*<a href="src/disqus-admin-panel/types/user_services/user_list_params.py">params</a>) -> <a href="./src/disqus-admin-panel/types/user_services/user_list_response.py">object</a></code>

### ActionCounts

Types:

```python
from disqus-admin-panel.types.user_services.user import ActionCountRetrieveResponse
```

Methods:

- <code title="get /user/action_counts">client.user_services.user.action_counts.<a href="./src/disqus-admin-panel/resources/user_services/user/action_counts.py">retrieve</a>() -> <a href="./src/disqus-admin-panel/types/user_services/user/action_count_retrieve_response.py">object</a></code>

### ActionHistory

Types:

```python
from disqus-admin-panel.types.user_services.user import ActionHistoryRetrieveResponse
```

Methods:

- <code title="get /user/action_history">client.user_services.user.action_history.<a href="./src/disqus-admin-panel/resources/user_services/user/action_history.py">retrieve</a>() -> <a href="./src/disqus-admin-panel/types/user_services/user/action_history_retrieve_response.py">object</a></code>
