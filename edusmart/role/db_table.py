from core.db.mixins.base_mixin import TimestampMixin, UUIDMixin
from core.db.session import Base
from edusmart.role.schema import RoleBase


class Role(Base, RoleBase, TimestampMixin, UUIDMixin):
    __tablename__ = "role"
