from core.db.mixins.base_mixin import StatusMixin, TimestampMixin, UUIDMixin
from core.db.session import Base
from edusmart.user.schema import UserBaseModel


class User(Base, UserBaseModel, StatusMixin, TimestampMixin, UUIDMixin):
    __tablename__ = "user"
