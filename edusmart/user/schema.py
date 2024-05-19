from datetime import datetime
from uuid import UUID

from pydantic import Field

from core.db.mixins.base_mixin import StatusMixin, TimestampMixin
from edusmart.schema.base import Common, ModifyBy


class UserBaseModel(Common, ModifyBy):
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    date_of_birth: datetime
    user_name: str = Field(min_length=10)
    school_name: str
    portfolio: dict
    cover_pic_path: str
    role_id: UUID
    organzation_id: UUID
    status: int

    class config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserCreate(UserBaseModel):
    pass


class UserUpdate(UserBaseModel):
    pass


class UserResponses(UserBaseModel, StatusMixin, TimestampMixin):
    id: str
