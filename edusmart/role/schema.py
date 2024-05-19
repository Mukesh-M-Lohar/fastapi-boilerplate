from uuid import UUID

from pydantic import Field

from core.db.mixins.base_mixin import StatusMixin, TimestampMixin
from edusmart.schema.base import ModifyBy


class RoleBase(StatusMixin):
    name: str = Field(min_length=10)
    display_name: str = Field(min_length=15)
    description: str = Field(min_length=15)

    class config:
        orm_mode = True


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase, ModifyBy):
    pass


class RoleResponses(RoleBase, TimestampMixin):
    id: UUID
