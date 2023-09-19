"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import common.healthcheck.v1alpha.healthcheck_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _View:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ViewEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_View.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    VIEW_UNSPECIFIED: _View.ValueType  # 0
    """View: UNSPECIFIED, equivalent to BASIC."""
    VIEW_BASIC: _View.ValueType  # 1
    """View: BASIC"""
    VIEW_FULL: _View.ValueType  # 2
    """View: FULL"""

class View(_View, metaclass=_ViewEnumTypeWrapper):
    """View represents a view of any resource. The resource view is implemented by
    adding a parameter to the method request which allows the client to specify
    which view of the resource it wants to receive in the response.
    """

VIEW_UNSPECIFIED: View.ValueType  # 0
"""View: UNSPECIFIED, equivalent to BASIC."""
VIEW_BASIC: View.ValueType  # 1
"""View: BASIC"""
VIEW_FULL: View.ValueType  # 2
"""View: FULL"""
global___View = View

class _OwnerType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _OwnerTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OwnerType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OWNER_TYPE_UNSPECIFIED: _OwnerType.ValueType  # 0
    """OwnerType: UNSPECIFIED"""
    OWNER_TYPE_USER: _OwnerType.ValueType  # 1
    """OwnerType: USER"""
    OWNER_TYPE_ORGANIZATION: _OwnerType.ValueType  # 2
    """OwnerType: ORGANIZATION"""

class OwnerType(_OwnerType, metaclass=_OwnerTypeEnumTypeWrapper):
    """OwnerType enumerates the owner type of any resource"""

OWNER_TYPE_UNSPECIFIED: OwnerType.ValueType  # 0
"""OwnerType: UNSPECIFIED"""
OWNER_TYPE_USER: OwnerType.ValueType  # 1
"""OwnerType: USER"""
OWNER_TYPE_ORGANIZATION: OwnerType.ValueType  # 2
"""OwnerType: ORGANIZATION"""
global___OwnerType = OwnerType

@typing_extensions.final
class LivenessRequest(google.protobuf.message.Message):
    """LivenessRequest represents a request to check a service liveness status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_CHECK_REQUEST_FIELD_NUMBER: builtins.int
    @property
    def health_check_request(self) -> common.healthcheck.v1alpha.healthcheck_pb2.HealthCheckRequest:
        """HealthCheckRequest message"""
    def __init__(
        self,
        *,
        health_check_request: common.healthcheck.v1alpha.healthcheck_pb2.HealthCheckRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_health_check_request", b"_health_check_request", "health_check_request", b"health_check_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_health_check_request", b"_health_check_request", "health_check_request", b"health_check_request"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_health_check_request", b"_health_check_request"]) -> typing_extensions.Literal["health_check_request"] | None: ...

global___LivenessRequest = LivenessRequest

@typing_extensions.final
class LivenessResponse(google.protobuf.message.Message):
    """LivenessResponse represents a response for a service liveness status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_CHECK_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def health_check_response(self) -> common.healthcheck.v1alpha.healthcheck_pb2.HealthCheckResponse:
        """HealthCheckResponse message"""
    def __init__(
        self,
        *,
        health_check_response: common.healthcheck.v1alpha.healthcheck_pb2.HealthCheckResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["health_check_response", b"health_check_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["health_check_response", b"health_check_response"]) -> None: ...

global___LivenessResponse = LivenessResponse

@typing_extensions.final
class ReadinessRequest(google.protobuf.message.Message):
    """ReadinessRequest represents a request to check a service readiness status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_CHECK_REQUEST_FIELD_NUMBER: builtins.int
    @property
    def health_check_request(self) -> common.healthcheck.v1alpha.healthcheck_pb2.HealthCheckRequest:
        """HealthCheckRequest message"""
    def __init__(
        self,
        *,
        health_check_request: common.healthcheck.v1alpha.healthcheck_pb2.HealthCheckRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_health_check_request", b"_health_check_request", "health_check_request", b"health_check_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_health_check_request", b"_health_check_request", "health_check_request", b"health_check_request"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_health_check_request", b"_health_check_request"]) -> typing_extensions.Literal["health_check_request"] | None: ...

global___ReadinessRequest = ReadinessRequest

@typing_extensions.final
class ReadinessResponse(google.protobuf.message.Message):
    """ReadinessResponse represents a response for a service readiness status"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEALTH_CHECK_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def health_check_response(self) -> common.healthcheck.v1alpha.healthcheck_pb2.HealthCheckResponse:
        """HealthCheckResponse message"""
    def __init__(
        self,
        *,
        health_check_response: common.healthcheck.v1alpha.healthcheck_pb2.HealthCheckResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["health_check_response", b"health_check_response"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["health_check_response", b"health_check_response"]) -> None: ...

global___ReadinessResponse = ReadinessResponse

@typing_extensions.final
class User(google.protobuf.message.Message):
    """User represents the content of a user"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    FIRST_NAME_FIELD_NUMBER: builtins.int
    LAST_NAME_FIELD_NUMBER: builtins.int
    ORG_NAME_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    NEWSLETTER_SUBSCRIPTION_FIELD_NUMBER: builtins.int
    COOKIE_TOKEN_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Resource name. It must have the format of "users/*".
    For example: "users/local-user".
    """
    uid: builtins.str
    """User ID in UUIDv4. This field is optionally set by users
    (optional on resource creation, server-generated if unset).
    """
    id: builtins.str
    """Resource ID (the last segment of the resource name), also the user
    username. This conforms to RFC-1034, which restricts to letters, numbers,
    and hyphen, with the first character a letter, the last a letter or a
    number, and a 63 character maximum.
    Note that the ID can be updated.
    """
    type: global___OwnerType.ValueType
    """Owner type: fixed to `OWNER_TYPE_USER`"""
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """User creation time"""
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """User update time"""
    email: builtins.str
    """User email"""
    customer_id: builtins.str
    """Stripe customer ID. This field is used in Instill Cloud."""
    first_name: builtins.str
    """User first name"""
    last_name: builtins.str
    """User last name"""
    org_name: builtins.str
    """User company or institution name"""
    role: builtins.str
    """User role. Allowed roles:
     - "manager"
     - "ai-researcher"
     - "ai-engineer"
     - "data-engineer",
     - "data-scientist",
     - "analytics-engineer"
     - "hobbyist"
    """
    newsletter_subscription: builtins.bool
    """User newsletter subscription"""
    cookie_token: builtins.str
    """User console cookie token"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        uid: builtins.str | None = ...,
        id: builtins.str = ...,
        type: global___OwnerType.ValueType = ...,
        create_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        update_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        email: builtins.str = ...,
        customer_id: builtins.str = ...,
        first_name: builtins.str | None = ...,
        last_name: builtins.str | None = ...,
        org_name: builtins.str | None = ...,
        role: builtins.str | None = ...,
        newsletter_subscription: builtins.bool = ...,
        cookie_token: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_cookie_token", b"_cookie_token", "_first_name", b"_first_name", "_last_name", b"_last_name", "_org_name", b"_org_name", "_role", b"_role", "_uid", b"_uid", "cookie_token", b"cookie_token", "create_time", b"create_time", "first_name", b"first_name", "last_name", b"last_name", "org_name", b"org_name", "role", b"role", "uid", b"uid", "update_time", b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_cookie_token", b"_cookie_token", "_first_name", b"_first_name", "_last_name", b"_last_name", "_org_name", b"_org_name", "_role", b"_role", "_uid", b"_uid", "cookie_token", b"cookie_token", "create_time", b"create_time", "customer_id", b"customer_id", "email", b"email", "first_name", b"first_name", "id", b"id", "last_name", b"last_name", "name", b"name", "newsletter_subscription", b"newsletter_subscription", "org_name", b"org_name", "role", b"role", "type", b"type", "uid", b"uid", "update_time", b"update_time"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_cookie_token", b"_cookie_token"]) -> typing_extensions.Literal["cookie_token"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_first_name", b"_first_name"]) -> typing_extensions.Literal["first_name"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_last_name", b"_last_name"]) -> typing_extensions.Literal["last_name"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_org_name", b"_org_name"]) -> typing_extensions.Literal["org_name"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_role", b"_role"]) -> typing_extensions.Literal["role"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_uid", b"_uid"]) -> typing_extensions.Literal["uid"] | None: ...

global___User = User

@typing_extensions.final
class ListUsersAdminRequest(google.protobuf.message.Message):
    """ListUsersAdminRequest represents a request to list all users by admin"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """Page size: the maximum number of resources to return. The service may
    return fewer than this value. If unspecified, at most 10 users will be
    returned. The maximum value is 100; values above 100 will be coereced to
    100.
    """
    page_token: builtins.str
    """Page token"""
    view: global___View.ValueType
    """View view (default is VIEW_BASIC)"""
    filter: builtins.str
    """Filter expression to list users"""
    def __init__(
        self,
        *,
        page_size: builtins.int | None = ...,
        page_token: builtins.str | None = ...,
        view: global___View.ValueType | None = ...,
        filter: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_filter", b"_filter", "_page_size", b"_page_size", "_page_token", b"_page_token", "_view", b"_view", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token", "view", b"view"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_filter", b"_filter", "_page_size", b"_page_size", "_page_token", b"_page_token", "_view", b"_view", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token", "view", b"view"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_filter", b"_filter"]) -> typing_extensions.Literal["filter"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_page_size", b"_page_size"]) -> typing_extensions.Literal["page_size"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_page_token", b"_page_token"]) -> typing_extensions.Literal["page_token"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_view", b"_view"]) -> typing_extensions.Literal["view"] | None: ...

global___ListUsersAdminRequest = ListUsersAdminRequest

@typing_extensions.final
class ListUsersAdminResponse(google.protobuf.message.Message):
    """ListUsersAdminResponse represents a response for a list of users"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USERS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___User]:
        """A list of users"""
    next_page_token: builtins.str
    """Next page token"""
    total_size: builtins.int
    """Total count of users"""
    def __init__(
        self,
        *,
        users: collections.abc.Iterable[global___User] | None = ...,
        next_page_token: builtins.str = ...,
        total_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "total_size", b"total_size", "users", b"users"]) -> None: ...

global___ListUsersAdminResponse = ListUsersAdminResponse

@typing_extensions.final
class CreateUserAdminRequest(google.protobuf.message.Message):
    """CreateUserAdminRequest represents a request to create a user by admin"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """The user to be created

        The user's `name` field is used to identify the user to create.
        Format: users/{user}
        """
    def __init__(
        self,
        *,
        user: global___User | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user", b"user"]) -> None: ...

global___CreateUserAdminRequest = CreateUserAdminRequest

@typing_extensions.final
class CreateUserAdminResponse(google.protobuf.message.Message):
    """CreateUserAdminResponse represents a response for a user response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """A user resource"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user", b"user"]) -> None: ...

global___CreateUserAdminResponse = CreateUserAdminResponse

@typing_extensions.final
class GetUserAdminRequest(google.protobuf.message.Message):
    """GetUserAdminRequest represents a request to query a user by admin"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Resource name of a user. For example:
    "users/local-user"
    """
    view: global___View.ValueType
    """View view (default is VIEW_BASIC)"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        view: global___View.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_view", b"_view", "view", b"view"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_view", b"_view", "name", b"name", "view", b"view"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_view", b"_view"]) -> typing_extensions.Literal["view"] | None: ...

global___GetUserAdminRequest = GetUserAdminRequest

@typing_extensions.final
class GetUserAdminResponse(google.protobuf.message.Message):
    """GetUserAdminResponse represents a response for a user resource"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """A user resource"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user", b"user"]) -> None: ...

global___GetUserAdminResponse = GetUserAdminResponse

@typing_extensions.final
class UpdateUserAdminRequest(google.protobuf.message.Message):
    """UpdateUserAdminRequest represents a request to update a user by admin"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """The user to update

        The user's `name` field is used to identify the user to update.
        Format: users/{user}
        """
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Update mask for a user resource"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask", "user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask", "user", b"user"]) -> None: ...

global___UpdateUserAdminRequest = UpdateUserAdminRequest

@typing_extensions.final
class UpdateUserAdminResponse(google.protobuf.message.Message):
    """UpdateUserAdminResponse represents a response for a user resource"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """A user resource"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user", b"user"]) -> None: ...

global___UpdateUserAdminResponse = UpdateUserAdminResponse

@typing_extensions.final
class DeleteUserAdminRequest(google.protobuf.message.Message):
    """DeleteUserAdminRequest represents a request to delete a user by admin"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The resource name of the user to be deleted,
    for example: "users/local-user"
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___DeleteUserAdminRequest = DeleteUserAdminRequest

@typing_extensions.final
class DeleteUserAdminResponse(google.protobuf.message.Message):
    """DeleteUserAdminResponse represents an empty response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteUserAdminResponse = DeleteUserAdminResponse

@typing_extensions.final
class LookUpUserAdminRequest(google.protobuf.message.Message):
    """LookUpUserAdminRequest represents a request to query a user via permalink by
    admin
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PERMALINK_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    permalink: builtins.str
    """Permalink of a user. For example:
    "users/{uid}"
    """
    view: global___View.ValueType
    """View view (default is VIEW_BASIC)"""
    def __init__(
        self,
        *,
        permalink: builtins.str = ...,
        view: global___View.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_view", b"_view", "view", b"view"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_view", b"_view", "permalink", b"permalink", "view", b"view"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_view", b"_view"]) -> typing_extensions.Literal["view"] | None: ...

global___LookUpUserAdminRequest = LookUpUserAdminRequest

@typing_extensions.final
class LookUpUserAdminResponse(google.protobuf.message.Message):
    """LookUpUserAdminResponse represents a response for a user resource by admin"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """A user resource"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user", b"user"]) -> None: ...

global___LookUpUserAdminResponse = LookUpUserAdminResponse

@typing_extensions.final
class QueryAuthenticatedUserRequest(google.protobuf.message.Message):
    """QueryAuthenticatedUserRequest represents a request to
    query the authenticated user
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryAuthenticatedUserRequest = QueryAuthenticatedUserRequest

@typing_extensions.final
class QueryAuthenticatedUserResponse(google.protobuf.message.Message):
    """QueryAuthenticatedUserResponse represents a response for
    the authenticated user resource
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """A user resource"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user", b"user"]) -> None: ...

global___QueryAuthenticatedUserResponse = QueryAuthenticatedUserResponse

@typing_extensions.final
class PatchAuthenticatedUserRequest(google.protobuf.message.Message):
    """PatchAuthenticatedUserRequest represents a request to
    update the authenticated user
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """The user to update"""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Update mask for a user resource"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask", "user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["update_mask", b"update_mask", "user", b"user"]) -> None: ...

global___PatchAuthenticatedUserRequest = PatchAuthenticatedUserRequest

@typing_extensions.final
class PatchAuthenticatedUserResponse(google.protobuf.message.Message):
    """PatchAuthenticatedUserResponse represents a response for
    the authenticated user resource
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    @property
    def user(self) -> global___User:
        """A user resource"""
    def __init__(
        self,
        *,
        user: global___User | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["user", b"user"]) -> None: ...

global___PatchAuthenticatedUserResponse = PatchAuthenticatedUserResponse

@typing_extensions.final
class ExistUsernameRequest(google.protobuf.message.Message):
    """ExistUsernameRequest represents a request to verify if
    a username has been occupied
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The resource name of the user to check,
    for example: "users/local-user"
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___ExistUsernameRequest = ExistUsernameRequest

@typing_extensions.final
class ExistUsernameResponse(google.protobuf.message.Message):
    """ExistUsernameResponse represents a response about whether
    the queried username has been occupied
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXISTS_FIELD_NUMBER: builtins.int
    exists: builtins.bool
    """A boolean value indicating whether the username has been occupied"""
    def __init__(
        self,
        *,
        exists: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exists", b"exists"]) -> None: ...

global___ExistUsernameResponse = ExistUsernameResponse

@typing_extensions.final
class ApiToken(google.protobuf.message.Message):
    """ApiToken represents the content of a API token"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _State:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StateEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ApiToken._State.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATE_UNSPECIFIED: ApiToken._State.ValueType  # 0
        """State: UNSPECIFIED"""
        STATE_INACTIVE: ApiToken._State.ValueType  # 1
        """State: INACTIVE"""
        STATE_ACTIVE: ApiToken._State.ValueType  # 2
        """State: ACTIVE"""
        STATE_EXPIRED: ApiToken._State.ValueType  # 3
        """State: EXPIRED"""

    class State(_State, metaclass=_StateEnumTypeWrapper):
        """State enumerates the state of an API token"""

    STATE_UNSPECIFIED: ApiToken.State.ValueType  # 0
    """State: UNSPECIFIED"""
    STATE_INACTIVE: ApiToken.State.ValueType  # 1
    """State: INACTIVE"""
    STATE_ACTIVE: ApiToken.State.ValueType  # 2
    """State: ACTIVE"""
    STATE_EXPIRED: ApiToken.State.ValueType  # 3
    """State: EXPIRED"""

    NAME_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    ACCESS_TOKEN_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    TOKEN_TYPE_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    EXPIRE_TIME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """API token resource name. It must have the format of "tokens/*" """
    uid: builtins.str
    """API token UUID"""
    id: builtins.str
    """API token resource ID (the last segment of the resource name) used to
    construct the resource name. This conforms to RFC-1034, which restricts to
    letters, numbers, and hyphen, with the first character a letter, the last a
    letter or a number, and a 63 character maximum.
    Use this field to define where it's being used.
    """
    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """API token creation time"""
    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """API token update time"""
    access_token: builtins.str
    """An opaque access token representing the API token string.
    To validate the token, the recipient of the token needs to call the server
    that issued the token.
    """
    state: global___ApiToken.State.ValueType
    """API token state"""
    token_type: builtins.str
    """API token type, value is fixed to "Bearer" """
    ttl: builtins.int
    """Input only. The TTL in seconds for this resource."""
    @property
    def expire_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """API token expire time"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        uid: builtins.str = ...,
        id: builtins.str = ...,
        create_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        update_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        access_token: builtins.str = ...,
        state: global___ApiToken.State.ValueType = ...,
        token_type: builtins.str = ...,
        ttl: builtins.int = ...,
        expire_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["create_time", b"create_time", "expiration", b"expiration", "expire_time", b"expire_time", "ttl", b"ttl", "update_time", b"update_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_token", b"access_token", "create_time", b"create_time", "expiration", b"expiration", "expire_time", b"expire_time", "id", b"id", "name", b"name", "state", b"state", "token_type", b"token_type", "ttl", b"ttl", "uid", b"uid", "update_time", b"update_time"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["expiration", b"expiration"]) -> typing_extensions.Literal["ttl", "expire_time"] | None: ...

global___ApiToken = ApiToken

@typing_extensions.final
class CreateTokenRequest(google.protobuf.message.Message):
    """CreateTokenRequest represents a request to create a API token"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    @property
    def token(self) -> global___ApiToken:
        """A token resource to create"""
    def __init__(
        self,
        *,
        token: global___ApiToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token", b"token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token", b"token"]) -> None: ...

global___CreateTokenRequest = CreateTokenRequest

@typing_extensions.final
class CreateTokenResponse(google.protobuf.message.Message):
    """CreateTokenResponse represents a response for a API token resource"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    @property
    def token(self) -> global___ApiToken:
        """The created API token resource"""
    def __init__(
        self,
        *,
        token: global___ApiToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token", b"token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token", b"token"]) -> None: ...

global___CreateTokenResponse = CreateTokenResponse

@typing_extensions.final
class ListTokensRequest(google.protobuf.message.Message):
    """ListTokensRequest represents a request to list tokens"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    page_size: builtins.int
    """The maximum number of API tokens to return. The service may return fewer
    than this value. If unspecified, at most 10 API tokens will be returned.
    The maximum value is 100; values above 100 will be coerced to 100.
    """
    page_token: builtins.str
    """Page token"""
    def __init__(
        self,
        *,
        page_size: builtins.int | None = ...,
        page_token: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_page_size", b"_page_size", "_page_token", b"_page_token", "page_size", b"page_size", "page_token", b"page_token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_page_size", b"_page_size", "_page_token", b"_page_token", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_page_size", b"_page_size"]) -> typing_extensions.Literal["page_size"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_page_token", b"_page_token"]) -> typing_extensions.Literal["page_token"] | None: ...

global___ListTokensRequest = ListTokensRequest

@typing_extensions.final
class ListTokensResponse(google.protobuf.message.Message):
    """ListTokensResponse represents a response for a list of API tokens"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKENS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    TOTAL_SIZE_FIELD_NUMBER: builtins.int
    @property
    def tokens(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ApiToken]:
        """A list of API tokens resources"""
    next_page_token: builtins.str
    """Next page token"""
    total_size: builtins.int
    """Total count of API tokens resources"""
    def __init__(
        self,
        *,
        tokens: collections.abc.Iterable[global___ApiToken] | None = ...,
        next_page_token: builtins.str = ...,
        total_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["next_page_token", b"next_page_token", "tokens", b"tokens", "total_size", b"total_size"]) -> None: ...

global___ListTokensResponse = ListTokensResponse

@typing_extensions.final
class GetTokenRequest(google.protobuf.message.Message):
    """GetTokenRequest represents a request to query an API token"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """API tokens resource name. It must have the format of "tokens/*" """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___GetTokenRequest = GetTokenRequest

@typing_extensions.final
class GetTokenResponse(google.protobuf.message.Message):
    """GetTokenResponse represents a response for an API token resource"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    @property
    def token(self) -> global___ApiToken:
        """An API token resource"""
    def __init__(
        self,
        *,
        token: global___ApiToken | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["token", b"token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["token", b"token"]) -> None: ...

global___GetTokenResponse = GetTokenResponse

@typing_extensions.final
class DeleteTokenRequest(google.protobuf.message.Message):
    """DeleteTokenRequest represents a request to delete an API token resource"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """API token resource name. It must have the format of "tokens/*" """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___DeleteTokenRequest = DeleteTokenRequest

@typing_extensions.final
class DeleteTokenResponse(google.protobuf.message.Message):
    """DeleteTokenResponse represents an empty response"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteTokenResponse = DeleteTokenResponse

@typing_extensions.final
class ValidateTokenRequest(google.protobuf.message.Message):
    """Request for validating the token"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ValidateTokenRequest = ValidateTokenRequest

@typing_extensions.final
class ValidateTokenResponse(google.protobuf.message.Message):
    """Response for validating the token"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_UID_FIELD_NUMBER: builtins.int
    user_uid: builtins.str
    """user_uid"""
    def __init__(
        self,
        *,
        user_uid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["user_uid", b"user_uid"]) -> None: ...

global___ValidateTokenResponse = ValidateTokenResponse
